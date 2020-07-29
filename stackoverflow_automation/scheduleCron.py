# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 12:51:59 2020

@author: jeevan
"""

from crontab import CronTab
my_cron = CronTab(tabfile='code_selenium.py')
job = my_cron.new(command='code_selenium.py')
job.minute.every(1)
 
my_cron.write()