import camelot
from pypdf import PdfReader

def normalize_str(s : str):
    n_s = ""
    for char in s:
        if char not in {'\n', '\t'}:
            n_s += char
    return n_s

def to_camel_case(s : str):
    return s[0].upper() + s[1:]

def int_2_str(n : int):
    """
    Returns string of given integer. 9 is returned as 09
    """
    if (n//10 == 0):
        return '0' + str(n)
    else:
        return str(n)

def month_2_int(month):
    month = month.lower().strip()
    match month:
        case 'jan':
            return '01'
        case 'feb':
            return '02'
        case 'mar':
            return '03'
        case 'apr':
            return '04'
        case 'may':
            return '05'
        case 'jun':
            return '06'
        case 'jul':
            return '07'
        case 'aug':
            return '08'
        case 'sep':
            return '09'
        case 'oct':
            return '10'
        case 'nov':
            return '11'
        case 'dec':
            return '12'

def get_next_date_str(s : str, leap : bool = False):
    """
    s should be of the form dd mon. Eg: '09 Jun' returns '10 Jun'
    """
    months_list = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
    day, month = s.split(' ')
    month = month.lower().strip()
    if day == '31' and month in ["jan", "mar", "may", "jul", "aug", "oct", "dec"]:
        next_day = '01'
        month = months_list[months_list.index(month) + 1]
    elif day == '30' and month in ["apr", "jun", "sep", "nov"]:
        next_day = '01'
        month = months_list[months_list.index(month) + 1]
    elif day =='29' and month == "feb" and leap == True:
        next_day = '01'
        month = months_list[months_list.index(month) + 1]
    elif day == '28' and month == "feb" and leap == False:
        next_day = '01'
        month = months_list[months_list.index(month) + 1]
    else:
        next_day = int_2_str(int(day) + 1)
    return next_day + ' ' + to_camel_case(month)

def find_start_date(row):
    for item in row:
        if item in {row.Index, row._1}:
            continue
        if item.replace(' ', '').isalnum():
            return item
        
def find_end_date(row):
    before = [None, None]
    end_char = ''
    for item, index in zip(row,range(0,10)):
        if index in [0, 1]:
            if index == 1 and normalize_str(item).lower().strip() == "semester break":
                end_char = '*'
            before[0] = before[1]
            before[1] = item
            continue
        if item == '':
            if normalize_str(before[1]).replace(' ', '').isalpha() == False:
                # this means its a date 
                return normalize_str(before[1]) + end_char
            else:
                # before is a string like Dussehra
                # try to get date of holiday from previous to previous
                return get_next_date_str(before[0]) + end_char
        before[0] = before[1]
        before[1] = item

def find_no_w_days(row):
    if '13' in normalize_str(row._8):
        return '13'
    elif '12' in normalize_str(row._8):
        return '12'
    else:
        return normalize_str(row._8)


class TT_Pdf:
    def __init__(self, file_path):
        tb = camelot.read_pdf(filepath=file_path, pages='1,2', flavor='lattice')

        self.s_dates = []
        self.e_dates = []
        self.no_working_days = []
        prev = None
        for i in tb[1].df.itertuples():
            # print(prev)
            if i.Index == 0:
                prev = i
                continue
            if i._1 != '':
                self.s_dates.append(find_start_date(i))
                self.e_dates.append(find_end_date(prev))
                self.no_working_days.append(find_no_w_days(i))
            prev = i
        self.e_dates = self.e_dates[1:]

        self.sem_break_seg = self.no_working_days.index('')

        self.d_dates = {}
        flag = 0
        for start, end, n in zip(self.s_dates, self.e_dates, range(len(self.no_working_days))):
            if n != self.sem_break_seg and n!= self.sem_break_seg+1:
                if flag == 0:
                    self.d_dates[str(n+1)] = [start, end]
                else:
                    # means self.sem_break_seg has been completed
                    self.d_dates[str(self.sem_break_seg+flag)] = [start, end]
                    flag += 1
            elif n==self.sem_break_seg:
                self.d_dates['Sem_Break'] = [start, end[:-1]]
            else:
                self.d_dates[str(self.sem_break_seg)] = [self.d_dates.get(str(self.sem_break_seg))[0], end]
                flag = 1

        page_1 = PdfReader(stream=file_path).pages[0]
        text = page_1.extract_text()
        for line in text.split('\n'):
            if line != '':
                req_line = line
                break
        req_line = req_line.replace('(', '')
        req_line = req_line[:-2]
        self.year = int_2_str(int(req_line.split(' ')[-1])%100)

        self.convert_to_date()
        print(self.d_dates)
    
    def convert_to_date(self):
        for key, dates in self.d_dates.items():
            s_date, s_month = dates[0].split(' ')
            s_month = month_2_int(s_month)
            s = s_date + '/' + s_month + '/' + self.year
            e_date, e_month = dates[1].split(' ')
            e_month = month_2_int(e_month)
            e = e_date + '/' + e_month + '/' + self.year
            
            self.d_dates[key] = [s, e]
