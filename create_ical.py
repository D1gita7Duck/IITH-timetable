import pytz
from datetime import datetime, date, timedelta
from icalendar import Calendar, Event, vText, vRecur, vDatetime, Timezone, TimezoneStandard
import db

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

slot_day_map = {"A":("MO,WE,TH",3),
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
slot_timings = {"A":[((9,0,0), (9,55,0)),((11,0,0), (11,55,0)), ((10,0,0), (10,55,0))],
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

db.initialize_db()
res = db.get_courses_info_for_cal()
updated_info = []
for course in res:
    s_start = course[-2]
    s_end = course[-1]
    start_date = db.get_segment_info(s_start)[0][-2]
    end_date = db.get_segment_info(s_end)[0][-1]
    start_date = date_tuple(start_date)
    end_date = date_tuple(end_date)
    temp = [*course[:-2], start_date, end_date]
    updated_info.append(temp)
# print(updated_info)

'''
Creating Calendar
!!!IMPORTANT 
When inputting properties based on text, no spaces are allowed before and after semicolons
!!!
'''
tz = pytz.timezone("Asia/Kolkata")
event_count = 0 # to make a unique id for each event

cal = Calendar()
cal.add('version', "2.0")
cal.add('prodid', "IITH Timetable")

vtz = Timezone()
vtz['tzid'] = tz
s_tz = TimezoneStandard()
s_tz['dtstart'] = datetime.now(tz).astimezone(pytz.utc).strftime("%Y%m%dT%H%M%SZ")
s_tz['tzoffsetto'] = '+0553'
s_tz["tzoffsetfrom"] = '+0553'
vtz.add_component(s_tz)
cal.add_component(vtz)

for i in updated_info:
    # checking if event is only once a week
    if slot_day_map[i[1]][-1] == 1:
        timing = slot_timings[i[1]][0]
        # make event start on its respective day instead of beginning of segment
        date_start = find_nearest_weekday(date(i[-2][0], i[-2][1], i[-2][2]), slot_day_map[i[1]][0][:2])
        until = tz.localize(datetime(i[-1][0], i[-1][1], i[-1][2], timing[1][0], timing[1][1])).astimezone(pytz.utc)
        bydays = vText(slot_day_map[i[1]][0])

        event = Event()
        event.add('uid', 'event'+str(event_count))
        event.add('dtstamp', datetime.now(tz))
        event.add('dtstart', datetime(date_start.year, date_start.month, date_start.day, timing[0][0], timing[0][1], timing[0][2],tzinfo=tz))
        event.add('dtend', datetime(date_start.year, date_start.month, date_start.day, timing[1][0], timing[1][1], timing[1][2],tzinfo=tz))
        event.add('rrule', f"FREQ=WEEKLY;UNTIL={until.strftime("%Y%m%dT%H%M%SZ")};BYDAY={bydays}") # space after semicolons not allowed
        event['location'] = vText(i[2])
        event['summary'] = vText(i[0])
        event_count+=1
        cal.add_component(event)
    # twice a week event
    elif slot_day_map[i[1]][-1] == 2:
        bydays = vText(slot_day_map[i[1]][0])

        day0 = bydays[:2]
        timing0 = slot_timings[i[1]][0]
        date_start0 = find_nearest_weekday(date(i[-2][0], i[-2][1], i[-2][2]), day0)
        # until time is 23:59 coz keeping different until for different days (day0, day1, ...) is cumbersome
        until = tz.localize(datetime(i[-1][0], i[-1][1], i[-1][2], 23, 59)).astimezone(pytz.utc)
        
        event0 = Event()
        event0.add('uid', 'event'+str(event_count))
        event0.add('dtstamp', datetime.now(tz))
        event0.add('dtstart', datetime(date_start0.year, date_start0.month, date_start0.day, timing0[0][0], timing0[0][1], timing0[0][2],tzinfo=tz))
        event0.add('dtend', datetime(date_start0.year, date_start0.month, date_start0.day, timing0[1][0], timing0[1][1], timing0[1][2],tzinfo=tz))
        event0.add('rrule', f"FREQ=WEEKLY;UNTIL={until.strftime("%Y%m%dT%H%M%SZ")};BYDAY={day0}")
        event0['location'] = vText(i[2])
        event0['summary'] = vText(i[0])
        event_count+=1
        cal.add_component(event0)

        day1 = bydays[3:]
        timing1 = slot_timings[i[1]][1]
        date_start1 = find_nearest_weekday(date(i[-2][0], i[-2][1], i[-2][2]), day1)
        event1 = Event()
        event1.add('uid', 'event'+str(event_count))
        event1.add('dtstamp', datetime.now(tz))
        event1.add('dtstart', datetime(date_start1.year, date_start1.month, date_start1.day, timing1[0][0], timing1[0][1], timing1[0][2],tzinfo=tz))
        event1.add('dtend', datetime(date_start1.year, date_start1.month, date_start1.day, timing1[1][0], timing1[1][1], timing1[1][2],tzinfo=tz))
        event1.add('rrule', f"FREQ=WEEKLY;UNTIL={until.strftime("%Y%m%dT%H%M%SZ")};BYDAY={day1}")
        event1['location'] = vText(i[2])
        event1['summary'] = vText(i[0])
        event_count+=1
        cal.add_component(event1)
    # thrice a week event
    else:
        bydays = vText(slot_day_map[i[1]][0])

        day0 = bydays[:2]
        timing0 = slot_timings[i[1]][0]
        date_start0 = find_nearest_weekday(date(i[-2][0], i[-2][1], i[-2][2]), day0)
        # until time is 23:59 coz keeping different until for different days (day0, day1, ...) is cumbersome
        # would require to find weekday in negative direction
        until = tz.localize(datetime(i[-1][0], i[-1][1], i[-1][2], 23, 59)).astimezone(pytz.utc)

        event0 = Event()
        event0.add('uid', 'event'+str(event_count))
        event0.add('dtstamp', datetime.now(tz))
        event0.add('dtstart', datetime(date_start0.year, date_start0.month, date_start0.day, timing0[0][0], timing0[0][1], timing0[0][2],tzinfo=tz))
        event0.add('dtend', datetime(date_start0.year, date_start0.month, date_start0.day, timing0[1][0], timing0[1][1], timing0[1][2],tzinfo=tz))
        event0.add('rrule', f"FREQ=WEEKLY;UNTIL={until.strftime("%Y%m%dT%H%M%SZ")};BYDAY={day0}")
        event0['location'] = vText(i[2])
        event0['summary'] = vText(i[0])
        event_count+=1
        cal.add_component(event0)

        day1 = bydays[3:5]
        timing1 = slot_timings[i[1]][1]
        date_start1 = find_nearest_weekday(date(i[-2][0], i[-2][1], i[-2][2]), day1)

        event1 = Event()
        event1.add('uid', 'event'+str(event_count))
        event1.add('dtstamp', datetime.now(tz))
        event1.add('dtstart', datetime(date_start1.year, date_start1.month, date_start1.day, timing1[0][0], timing1[0][1], timing1[0][2],tzinfo=tz))
        event1.add('dtend', datetime(date_start1.year, date_start1.month, date_start1.day, timing1[1][0], timing1[1][1], timing1[1][2],tzinfo=tz))
        event1.add('rrule', f"FREQ=WEEKLY;UNTIL={until.strftime("%Y%m%dT%H%M%SZ")};BYDAY={day1}")
        event1['location'] = vText(i[2])
        event1['summary'] = vText(i[0])
        event_count+=1
        cal.add_component(event1)

        day2 = bydays[6:]
        timing2 = slot_timings[i[1]][2]
        date_start2 = find_nearest_weekday(date(i[-2][0], i[-2][1], i[-2][2]), day2)

        event2 = Event()
        event2.add('uid', 'event'+str(event_count))
        event2.add('dtstamp', datetime.now(tz))
        event2.add('dtstart', datetime(date_start2.year, date_start2.month, date_start2.day, timing2[0][0], timing2[0][1], timing2[0][2],tzinfo=tz))
        event2.add('dtend', datetime(date_start2.year, date_start2.month, date_start2.day, timing2[1][0], timing2[1][1], timing2[1][2],tzinfo=tz))
        event2.add('rrule', f"FREQ=WEEKLY;UNTIL={until.strftime("%Y%m%dT%H%M%SZ")};BYDAY={day2}")
        event2['location'] = vText(i[2])
        event2['summary'] = vText(i[0])
        event_count+=1
        cal.add_component(event2)

print('\n\n\n')
print(cal.to_ical().decode('utf-8'))
with open('cal.ics', 'wb') as f:
    f.write(cal.to_ical())