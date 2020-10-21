from apscheduler.schedulers.blocking import BlockingScheduler
from personal_assistant import *
import datetime

# scheduler = BlockingScheduler()
# scheduler.add_job(morning_events, 'interval', hours= 24, id='my_job_id')
# print(datetime.datetime.now())
from time import ctime
scheduler = BlockingScheduler()
# scheduler.add_job(morning_events, 'interval', seconds=40, id='my_job_id')
# print(datetime.datetime.now())
@scheduler.scheduled_job('cron', hour=9,minute = 30)
def timed_job_one():
    morning_events()
    print(ctime())

scheduler.start()