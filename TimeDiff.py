#Needed to work
import datetime
from datetime import datetime
from datetime import timedelta

#Time differences are calculated from here
TriggerTime = raw_input("Please enter the initial trigger date in the format 'yyyy/mm/dd hh:mm:ss.ss': ")

ObsTime = raw_input("Please enter the observation time in the format 'yyyy/mm/dd hh:mm:ss.ss': ")

FMT = '%Y/%m/%d %H:%M:%S.%f'

TimeDiff = datetime.strptime(ObsTime, FMT) - datetime.strptime(TriggerTime, FMT)

print("Time difference in seconds:")
print(TimeDiff.total_seconds())

TimeDiffDays=float(TimeDiff.total_seconds()/86400)

print("Time difference in days:")
print(TimeDiffDays)
