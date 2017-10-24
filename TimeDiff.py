#Needed to work
import datetime
from datetime import datetime

#Time differences are calculated from here
TriggerTime = raw_input("Please enter the initial trigger date in the format 'yyyy/mm/dd hh:mm:ss': ")

ObsTime = raw_input("Please enter the observation time in the format 'yyyy/mm/dd hh:mm:ss': ")

FMT = '%Y/%m/%d %H:%M:%S'

TimeDiff = datetime.strptime(ObsTime, FMT) - datetime.strptime(TriggerTime, FMT)

print(TriggerTime)
print(ObsTime)
print(TimeDiff)
print("Brian")
