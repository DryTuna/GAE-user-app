'''
Created on Apr 28, 2014

@author: Duy Tran
'''
from django.conf.urls.defaults import *
from codefellows.views import main_page, submit_data

urlpatterns = patterns('codefellows.views',
    (r'^sign/$', submit_data),
    (r'^$', main_page),
)