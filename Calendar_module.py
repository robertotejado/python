print("Calendar Module")

import calendar

dic=calendar.TextCalendar(calendar.MONDAY)
print(dic.prmonth(2020,12))

##############################################
#birthday=calendar.TextCalendar(calendar.MONDAY)
#print(birthday.prmonth(1977,4))

#leaps=calendar.leapdays(1977,2020)
#print(leaps)
#############################################

#import calendar
#print(">>>>>>>>>>Leap Year Calculator<<<<<<<<<<\n")
#y1=int(input("Enter the first year: "))
#y2=int(input("Enter the second year: "))
#leaps=calendar.leapdays(y1, y2)
#print("Number of Leap years between", y1, "and",y2, "is:", leaps )

############################################

import locale
locale.setlocale(locale.LC_ALL, ("es_ES", "UTF-8"))

import calendar
for name in calendar.month_name:
    print(name)

import calendar
for name in calendar.day_name:
    print(name)

#################################################
import locale
locale.setlocale(locale.LC_ALL, ("es_ES", "UTF-8"))
from datetime import datetime
fecha= datetime.now()
print("Fecha y hora actual")
print(fecha.strftime("%H:%M %d/%b/%Y"))

##################################

import calendar
cal=open("./cal.html","w")
c=calendar.HTMLCalendar(calendar.MONDAY)
cal.write(c.formatmonth(2020,12))
cal.close()

######################################


import calendar

year=int(input("Enter the year to display as a webpage: "))
cal=open("./cal2.html","w")
cal.write(calendar.HTMLCalendar(calendar.MONDAY).formatyear(year))
cal.close()
