#Needed to work
import datetime
from datetime import datetime
from datetime import timedelta

#Times are inserted here
TriggerTime = raw_input("Please enter the initial trigger date in the format 'yyyy/mm/dd hh:mm:ss.ss': ")

FMT = '%Y/%m/%d %H:%M:%S.%f'

#Will add loop after here to make it quicker to calculate for multiple observations
while True:

	ObsTime = raw_input("Please enter the observation time in the format 'yyyy/mm/dd hh:mm:ss.ss': ")

	TimeDiff = datetime.strptime(ObsTime, FMT) - datetime.strptime(TriggerTime, FMT)

	print("Time difference in seconds:")
	print(TimeDiff.total_seconds())

	TimeDiffDays=float(TimeDiff.total_seconds()/86400)

	print("Time difference in days:")
	print(TimeDiffDays)

	Question = raw_input("Do you want to check another time (y/n)? ")
	if Question.strip() != "y":
		break
