import os
from django.conf import settings
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE','cdata.settings')

import django

# Import settings
django.setup()


import requests
import datetime
from viral.models import Stats
from datetime import date
from datetime import datetime
from datetime import timedelta

def populate():
            today = datetime.today()
            yesterday = today - timedelta(days=1)
            today_string = datetime.strftime(today, '%Y%m%d')
            print(today_string)
            url = "https://covidtracking.com//api/states/daily?date="+ today_string
            print(url)
            request = requests.get(url)
            print(request.json())
            d = request.json()
            #total = d['total']
            #print(total)
            i = 0

            for each in d:
                dte = str(d[i]['date'])
                dte =datetime.strptime(dte, '%Y%m%d')
                state = str(d[i]['state'])
                if d[i]['positive'] is None:
                    positive = 0
                else:
                    positive = int(d[i]['positive'])
                if d[i]['positiveIncrease'] is None:
                    positiveIncrease = 0
                else:
                    positiveIncrease = int(d[i]['positiveIncrease'])
                if d[i]['totalTestResultsIncrease'] is None:
                    totalTestResultsIncrease = 0
                else:
                    totalTestResultsIncrease = int(d[i]['totalTestResultsIncrease'])
                total = int(d[i]['total'])
                print(date)

                Stats.objects.create(
                    date = dte,
                    state = state,
                    positive= positive,
                    positiveIncrease = positiveIncrease,
                    totalTestResultsIncrease = totalTestResultsIncrease,
                    total = total,
                    )
                i += 1

            return request.json

if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate()
    print('Populating Complete')
