"""
WSGI config for coinTrade project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from apscheduler.schedulers.blocking import BlockingScheduler
from django.core.wsgi import get_wsgi_application
from django.views.decorators.csrf import csrf_exempt

from coinTrade.job.trade_job import run_trade

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "coinTrade.settings")

application = get_wsgi_application()


@csrf_exempt
def start_job_interval_():
    scheduler = BlockingScheduler()
    scheduler.add_job(run_trade, 'interval', seconds=30 , max_instances=1)
    scheduler.start()

start_job_interval_()