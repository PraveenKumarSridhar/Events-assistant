from apscheduler.schedulers.blocking import BlockingScheduler
from personal_assistant import *
from global_variable import *
import datetime

# scheduler = BlockingScheduler()
# scheduler.add_job(morning_events, 'interval', hours= 24, id='my_job_id')
# print(datetime.datetime.now())
from time import ctime
scheduler = BlockingScheduler()
# scheduler.add_job(morning_events, 'interval', seconds=40, id='my_job_id')
# print(datetime.datetime.now())
alert_hr = int(ALERT_TIME.split(':')[0])
alert_min = int(ALERT_TIME.split(':')[-1])

@scheduler.scheduled_job('cron', hour=alert_hr ,minute = alert_min)
def timed_job_one():
    morning_events()
    print(ctime())

scheduler.start()