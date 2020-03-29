import os
from django.conf import settings
import requests
from background_task import background
# Configure settings for project
# Need to run this before calling models from application!

# import django
import datetime
from .models import Stats

#class UpdateData:

     #def __init__(self, date):
         #self.date = date

@background(schedule=120)
def get_the_data():

            url = "https://covidtracking.com//api/states/daily?state=NC&date=20200325"
            request = requests.get(url)
            print(request.json())
            d = request.json()
            #total = d['total']
            #print(total)
            i = 0

            for each in d:
                date = str(d[i]['date'])
                date =datetime.datetime.strptime(date, '%Y%m%d')
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
                    date = date,
                    state = state,
                    positive= positive,
                    positiveIncrease = positiveIncrease,
                    totalTestResultsIncrease = totalTestResultsIncrease,
                    total = total,
                    )
                i += 1

            return request.json
