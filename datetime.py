#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 14:19:54 2025

@author: ido
"""
# this line imports the libary named datetime
#the syntax is
#from<libary>import<function name>
from datetime import datetime

#current_month is the variable
#this code is about telling the month and the season
current_month=datetime.now().month
print(current_month)
if current_month==3 or current_month==4 or current_month==5:
    print('spring')
elif current_month==6 or current_month==7 or current_month==8:
    print('summer')
elif current_month==9 or current_month==10 or current_month==11:
    print('autumn')
else:
    print('winter')