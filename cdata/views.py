from __future__ import print_function
from django.views.generic import TemplateView, DetailView, ListView, CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Count, Sum
from django.conf import settings
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import json
import time
from django.http import JsonResponse
import time
import requests
from viral.models import Stats
import datetime

#from viral.get_data import UpdateData


class HomeView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        #stats = UpdateData(all)
        #stats_published = stats.get_the_data()
        #print(stats_published)
        superset = []
        cdata = Stats.objects.filter(state="NC").order_by('date')

        for item in cdata:
            data_item = []
            d = datetime.datetime.strftime(item.date, '%Y%m%d')
            data_item.append(d)
            data_item.append(item.positive)

            print(d)
            print(item.positive)
            superset.append(data_item)
            print(superset)

        context['cdata'] = superset
        #[['Mushrooms', 3],['Onions', 1],['Olives', 1],['Zucchini', 1],['Pepperoni', 2]]

        return context
