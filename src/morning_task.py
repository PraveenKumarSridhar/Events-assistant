from apscheduler.schedulers.blocking import BlockingScheduler
from personal_assistant import *
import datetime

scheduler = BlockingScheduler()
scheduler.add_job(morning_events, 'interval', hours= 24, id='my_job_id')
print(datetime.datetime.now())
scheduler.start()