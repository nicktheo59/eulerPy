import time
from datetime import date
from datetime import timedelta

currentDate = date(1901,1,1)

oneDay = timedelta(days = 1)

sundays = 0

while currentDate != date(2000,12,31):
	if currentDate.weekday() == 6 and currentDate.day == 1:
		sundays += 1
	currentDate += oneDay

print sundays

