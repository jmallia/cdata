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
from viral.models import States
from datetime import date
from datetime import datetime
from datetime import timedelta

def populate():

            states = ["AK","AL","AR","AZ","CA","CO","CT","DC","DE","FL","GA","GU","HI","IA","ID", "IL","IN","KS","KY","LA","MA","MD","ME","MH","MI","MN","MO","MS","MT","NC","ND","NE","NH","NJ","NM","NV","NY", "OH","OK","OR","PA","PR","PW","RI","SC","SD","TN","TX","UT","VA","VI","VT","WA","WI","WV","WY"]
            i = 0
            for each in states:
                States.objects.create(
                    state = states[i],
                                )
                i +=1



if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate()
    print('Populating Complete')
