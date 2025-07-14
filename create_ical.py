import pytz
from datetime import datetime, date, timedelta
from icalendar import Calendar, Event, vText, Timezone, TimezoneStandard
import db
from os import path

def date_tuple(date : str, delimiter = '/'):
    """
    Returns a tuple of integers, (YYYY, MM, DD)\n
    Assumes millenium is 2000
    """
    date = date.split(delimiter)[::-1]
    return (2000+int(date[0]), int(date[1]), int(date[2]))


def find_nearest_weekday(date : date, weekday : str):
    """
    Find the nearest weekday to a given date. Searches forward only.

    :params:
        date (datetime.date): The date to find the nearest weekday for.\n
        weekday (str): The weekday to find (e.g. 'MO', 'TU', etc.).

    :returns:
        datetime.date: The nearest weekday to the given date.
    """
    weekday_map = {
        'MO': 0,
        'TU': 1,
        'WE': 2,
        'TH': 3,
        'FR': 4,
        'SA': 5,
        'SU': 6
    }

    target_weekday = weekday_map[weekday.upper()]
    current_weekday = date.weekday()

    if target_weekday == current_weekday:
        return date

    # Move to the next week until we find the target weekday
    while True:
        date += timedelta(days=1)
        if date.weekday() == target_weekday:
            return date

def form_holidays(h : list[tuple[str]]):
    hols : list[date] = []
    for i in h:
        s_date = date_tuple(i[1])
        s_date = date(s_date[0], s_date[1], s_date[2])

        for j in range(i[-1]):
            hols.append(s_date + timedelta(days=j))
    return hols
# a=find_nearest_weekday(date(2025,7,28), 'SU')
# print(datetime(a.year, a.month, a.day, tzinfo=pytz.timezone("Asia/Kolkata")))
# def datetime_2_icaldatetime(date : tuple, time = None):
#     """
#     Tuple must be (YYYY, MM, DD). Defaults to EOD time i.e, 23:59:59
#     Returns ical format string
#     """
#     s=''
#     for i in date:
#         if i//10 == 0:
#             s+='0'
#         s+=str(i)
#     s+='T'
#     if time is not None:
#         for j in time:
#             s+=str(j)
#     else:
#         s+='000000'
#     s+='Z'
#     return s


'''
Creating Calendar
!!!IMPORTANT 
When inputting properties based on text, no spaces are allowed before and after semicolons
!!!
Colours are not supported in Google Calendar :_(
To add colours in Google Calendar have to use OAuth2 credentials and use Google API client
'''

class MyCalendar(str):
    """
    Creates an icalendar.Calendar object (self.cal) and adds events to it.
    There are three events for triweekly, two events for biweekly, and one event for a weekly courses.
    Calendar is written to .ics file saved in ./cal.ics
    :returns: A str of the calendar data
    """
    def __init__(self):
        super().__init__()

        self.init_vars()
        self.init_data()
        self.create_calendar()
        self.write_to_file()
        
    def __str__(self):
        return self.cal.to_ical().decode('utf-8')

    def init_vars(self):
        self.slot_day_map = {"A":("MO,WE,TH",3),
                "B":("MO,WE,TH",3),
                "C":("MO,WE,TH",3),
                "D":("MO,TU,FR",3),
                "E":("TU,TH,FR",3),
                "F":("TU,WE,FR",3),
                "G":("TU,WE,FR",3),
                "P":("MO,TH",2),
                "Q":("MO,TH",2),
                "R":("TU,FR",2),
                "S":("TU,FR",2),
                "FN1":("MO",1),
                "FN2":("TU",1),
                "FN3":("WE",1),
                "FN4":("TH",1),
                "FN5":("FR",1),
                "AN1":("MO",1),
                "AN2":("TU",1),
                "AN3":("WE",1),
                "AN4":("TH",1),
                "AN5":("FR",1),
                }
        self.slot_timings = {"A":[((9,0,0), (9,55,0)),((11,0,0), (11,55,0)), ((10,0,0), (10,55,0))],
                        "B":[((10,0,0), (10,55,0)),((9,0,0), (9,55,0)), ((11,0,0), (11,55,0))],
                        "C":[((11,0,0), (11,55,0)),((10,0,0), (10,55,0)), ((9,0,0), (9,55,0))],
                        "D":[((12,0,0), (12,55,0)), ((9,0,0), (9,55,0)), ((11,0,0), (11,55,0))],
                        "E":[((10,0,0), (10,55,0)), ((12,0,0), (12,55,0)), ((9,0,0), (9,55,0))],
                        "F":[((11,0,0), (11,55,0)), ((14,30,0), (15,55,0)), ((10,0,0), (10,55,0))],
                        "G":[((12,0,0), (12,55,0)), ((12,0,0), (12,55,0)), ((12,0,0), (12,55,0))],
                        "P":[((14,30,0), (15,55,0)), ((16,0,0), (17,25,0))],
                        "Q":[((16,0,0), (17,25,0)), ((14,30,0), (15,55,0))],
                        "R":[((14,30,0), (15,55,0)), ((16,0,0), (17,25,0))],
                        "S":[((16,0,0), (17,25,0)), ((14,30,0), (15,55,0))],
                        "FN1":[((9,0,0), (11,55,0))],
                        "FN2":[((9,0,0), (11,55,0))],
                        "FN3":[((9,0,0), (11,55,0))],
                        "FN4":[((9,0,0), (11,55,0))],
                        "FN5":[((9,0,0), (11,55,0))],
                        "AN1":[((14,30,0), (17,25,0))],
                        "AN2":[((14,30,0), (17,25,0))],
                        "AN3":[((14,30,0), (17,25,0))],
                        "AN4":[((14,30,0), (17,25,0))],
                        "AN5":[((14,30,0), (17,25,0))],
                        }

        self.colours = ["red", "purple", "green", "yellow", "blue", "aqua", "maroon", "fuchsia", "lime", "olive", "orange", "navy", "teal", "black", "silver", "gray", "palegreen", "aquamarine"]
        self.remaining_colours = self.colours.copy()
    
    def init_data(self):
        db.initialize_db()
        res = db.get_courses_info_for_cal()
        self.updated_hols = form_holidays(db.get_all_holidays_info())
        # print(db.get_all_holidays_info())
        # print(updated_hols)
        self.updated_info = []
        for course in res:
            s_start = course[-2]
            s_end = course[-1]
            start_date = db.get_segment_info(s_start)[0][-2]
            end_date = db.get_segment_info(s_end)[0][-1]
            start_date = date_tuple(start_date)
            end_date = date_tuple(end_date)
            temp = [*course[:-2], start_date, end_date]
            self.updated_info.append(temp)
        # print(self.updated_info)
    
    def create_calendar(self):
        self.tz = pytz.timezone("Asia/Kolkata")
        self.event_count = 0 # to make a unique id for each event

        self.cal = Calendar()
        self.cal.add('version', "2.0")
        self.cal.add('prodid', "IITH Timetable")

        vtz = Timezone()
        vtz['tzid'] = self.tz
        s_tz = TimezoneStandard()
        s_tz['dtstart'] = datetime.now(self.tz).astimezone(pytz.utc).strftime("%Y%m%dT%H%M%SZ")
        s_tz['tzoffsetto'] = '+0553'
        s_tz["tzoffsetfrom"] = '+0553'
        vtz.add_component(s_tz)
        self.cal.add_component(vtz)

        for i in self.updated_info:
            if len(self.remaining_colours) < 1:
                self.remaining_colours = self.colours.copy()
            # chosen = self.remaining_colours.pop(randrange(len(self.remaining_colours)))
            chosen = self.remaining_colours.pop(0)
            # checking if event is only once a week
            if self.slot_day_map[i[1]][-1] == 1:
                timing = self.slot_timings[i[1]][0]
                # make event start on its respective day instead of beginning of segment
                date_start = find_nearest_weekday(date(i[-2][0], i[-2][1], i[-2][2]), self.slot_day_map[i[1]][0][:2])
                until = self.tz.localize(datetime(i[-1][0], i[-1][1], i[-1][2], timing[1][0], timing[1][1])).astimezone(pytz.utc)
                bydays = vText(self.slot_day_map[i[1]][0])
                exdates = []
                for j in self.updated_hols:
                    exdates.append(self.tz.localize(datetime(j.year, j.month, j.day, timing[0][0], timing[0][1], timing[0][2])))

                event = Event()
                event.add('uid', 'event'+str(self.event_count))
                event.add('dtstamp', datetime.now(self.tz))
                event.add('dtstart', datetime(date_start.year, date_start.month, date_start.day, timing[0][0], timing[0][1], timing[0][2],tzinfo=self.tz))
                event.add('dtend', datetime(date_start.year, date_start.month, date_start.day, timing[1][0], timing[1][1], timing[1][2],tzinfo=self.tz))
                event.add('rrule', f"FREQ=WEEKLY;UNTIL={until.strftime("%Y%m%dT%H%M%SZ")};BYDAY={bydays}") # space after semicolons not allowed
                event.add('exdate', exdates)
                event['location'] = vText(i[2])
                event['summary'] = vText(i[0])
                self.event_count+=1
                event.color = chosen
                self.cal.add_component(event)
            # twice a week event
            elif self.slot_day_map[i[1]][-1] == 2:
                bydays = vText(self.slot_day_map[i[1]][0])

                day0 = bydays[:2]
                timing0 = self.slot_timings[i[1]][0]
                date_start0 = find_nearest_weekday(date(i[-2][0], i[-2][1], i[-2][2]), day0)
                # until time is 23:59 coz keeping different until for different days (day0, day1, ...) is cumbersome
                until = self.tz.localize(datetime(i[-1][0], i[-1][1], i[-1][2], 23, 59)).astimezone(pytz.utc)
                exdates = []
                for j in self.updated_hols:
                    exdates.append(self.tz.localize(datetime(j.year, j.month, j.day, timing0[0][0], timing0[0][1], timing0[0][2])))

                event0 = Event()
                event0.add('uid', 'event'+str(self.event_count))
                event0.add('dtstamp', datetime.now(self.tz))
                event0.add('dtstart', datetime(date_start0.year, date_start0.month, date_start0.day, timing0[0][0], timing0[0][1], timing0[0][2],tzinfo=self.tz))
                event0.add('dtend', datetime(date_start0.year, date_start0.month, date_start0.day, timing0[1][0], timing0[1][1], timing0[1][2],tzinfo=self.tz))
                event0.add('rrule', f"FREQ=WEEKLY;UNTIL={until.strftime("%Y%m%dT%H%M%SZ")};BYDAY={day0}")
                event0.add('exdate', exdates)
                event0['location'] = vText(i[2])
                event0['summary'] = vText(i[0])
                self.event_count+=1
                event0.color = chosen
                self.cal.add_component(event0)

                day1 = bydays[3:]
                timing1 = self.slot_timings[i[1]][1]
                exdates = []
                for j in self.updated_hols:
                    exdates.append(self.tz.localize(datetime(j.year, j.month, j.day, timing1[0][0], timing1[0][1], timing1[0][2])))
                date_start1 = find_nearest_weekday(date(i[-2][0], i[-2][1], i[-2][2]), day1)
                event1 = Event()
                event1.add('uid', 'event'+str(self.event_count))
                event1.add('dtstamp', datetime.now(self.tz))
                event1.add('dtstart', datetime(date_start1.year, date_start1.month, date_start1.day, timing1[0][0], timing1[0][1], timing1[0][2],tzinfo=self.tz))
                event1.add('dtend', datetime(date_start1.year, date_start1.month, date_start1.day, timing1[1][0], timing1[1][1], timing1[1][2],tzinfo=self.tz))
                event1.add('rrule', f"FREQ=WEEKLY;UNTIL={until.strftime("%Y%m%dT%H%M%SZ")};BYDAY={day1}")
                event1.add('exdate', exdates)
                event1['location'] = vText(i[2])
                event1['summary'] = vText(i[0])
                self.event_count+=1
                event1.color = chosen
                self.cal.add_component(event1)
            # thrice a week event
            else:
                bydays = vText(self.slot_day_map[i[1]][0])

                day0 = bydays[:2]
                timing0 = self.slot_timings[i[1]][0]
                exdates = []
                for j in self.updated_hols:
                    exdates.append(self.tz.localize(datetime(j.year, j.month, j.day, timing0[0][0], timing0[0][1], timing0[0][2])))
                date_start0 = find_nearest_weekday(date(i[-2][0], i[-2][1], i[-2][2]), day0)
                # until time is 23:59 coz keeping different until for different days (day0, day1, ...) is cumbersome
                # would require to find weekday in negative direction
                until = self.tz.localize(datetime(i[-1][0], i[-1][1], i[-1][2], 23, 59)).astimezone(pytz.utc)

                event0 = Event()
                event0.add('uid', 'event'+str(self.event_count))
                event0.add('dtstamp', datetime.now(self.tz))
                event0.add('dtstart', datetime(date_start0.year, date_start0.month, date_start0.day, timing0[0][0], timing0[0][1], timing0[0][2],tzinfo=self.tz))
                event0.add('dtend', datetime(date_start0.year, date_start0.month, date_start0.day, timing0[1][0], timing0[1][1], timing0[1][2],tzinfo=self.tz))
                event0.add('rrule', f"FREQ=WEEKLY;UNTIL={until.strftime("%Y%m%dT%H%M%SZ")};BYDAY={day0}")
                event0.add('exdate', exdates)
                event0['location'] = vText(i[2])
                event0['summary'] = vText(i[0])
                self.event_count+=1
                event0.color = chosen
                self.cal.add_component(event0)

                day1 = bydays[3:5]
                timing1 = self.slot_timings[i[1]][1]
                exdates = []
                for j in self.updated_hols:
                    exdates.append(self.tz.localize(datetime(j.year, j.month, j.day, timing1[0][0], timing1[0][1], timing1[0][2])))
                date_start1 = find_nearest_weekday(date(i[-2][0], i[-2][1], i[-2][2]), day1)

                event1 = Event()
                event1.add('uid', 'event'+str(self.event_count))
                event1.add('dtstamp', datetime.now(self.tz))
                event1.add('dtstart', datetime(date_start1.year, date_start1.month, date_start1.day, timing1[0][0], timing1[0][1], timing1[0][2],tzinfo=self.tz))
                event1.add('dtend', datetime(date_start1.year, date_start1.month, date_start1.day, timing1[1][0], timing1[1][1], timing1[1][2],tzinfo=self.tz))
                event1.add('rrule', f"FREQ=WEEKLY;UNTIL={until.strftime("%Y%m%dT%H%M%SZ")};BYDAY={day1}")
                event1.add('exdate', exdates)
                event1['location'] = vText(i[2])
                event1['summary'] = vText(i[0])
                self.event_count+=1
                event1.color = chosen
                self.cal.add_component(event1)

                day2 = bydays[6:]
                timing2 = self.slot_timings[i[1]][2]
                exdates = []
                for j in self.updated_hols:
                    exdates.append(self.tz.localize(datetime(j.year, j.month, j.day, timing2[0][0], timing2[0][1], timing2[0][2])))
                date_start2 = find_nearest_weekday(date(i[-2][0], i[-2][1], i[-2][2]), day2)

                event2 = Event()
                event2.add('uid', 'event'+str(self.event_count))
                event2.add('dtstamp', datetime.now(self.tz))
                event2.add('dtstart', datetime(date_start2.year, date_start2.month, date_start2.day, timing2[0][0], timing2[0][1], timing2[0][2],tzinfo=self.tz))
                event2.add('dtend', datetime(date_start2.year, date_start2.month, date_start2.day, timing2[1][0], timing2[1][1], timing2[1][2],tzinfo=self.tz))
                event2.add('rrule', f"FREQ=WEEKLY;UNTIL={until.strftime("%Y%m%dT%H%M%SZ")};BYDAY={day2}")
                event2.add('exdate', exdates)
                event2['location'] = vText(i[2])
                event2['summary'] = vText(i[0])
                self.event_count+=1
                event2.color = chosen
                self.cal.add_component(event2)

        # print('\n\n\n')
        # print(cal.to_ical().decode('utf-8'))
    
    def write_to_file(self):
        with open('cal.ics', 'wb') as f:
            f.write(self.cal.to_ical())
        print("Calendar was created successfully, find path below", path.abspath("cal.ics"), sep='\n')