#All needed to work
import datetime
from datetime import datetime
from datetime import timedelta

#Trigger time is given here
TriggerTime = raw_input("Please enter the initial trigger date in the format 'yyyy/mm/dd hh:mm:ss.ss': ")

FMT = '%Y/%m/%d %H:%M:%S.%f'

#Loops until the user doesn't enter y. Will ask for a new observation time to compare with the same trigger time.
while True:

	ObsTime = raw_input("Please enter the observation time in the format 'yyyy/mm/dd hh:mm:ss.ss': ")

	TimeDiff = datetime.strptime(ObsTime, FMT) - datetime.strptime(TriggerTime, FMT)

	#While not necessarily needed, it could be useful to have the time in seconds (SI unit) as well
	print("Time difference in seconds:")
	print(TimeDiff.total_seconds())

	TimeDiffDays=float(TimeDiff.total_seconds()/86400)

	print("Time difference in days:")
	print(TimeDiffDays)

	Question = raw_input("Do you want to check another time (y/n)? ")
	if Question.strip() != "y":
		break
