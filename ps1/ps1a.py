#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 15:48:54 2021

@author: yasinyesilyurt
"""

portion_down_payment = 0.25
current_savings = 0
r = 0.04
n = 0

annual_salary = float(input('Enter your annual salary ...'))
percentage_saved = float(input('Enter the percent of your salary to save, as a decimal...'))
total_cost = float(input('Enter the cost of your dream house ...'))

monthly_salary = annual_salary/12
portion_saved = percentage_saved * monthly_salary

while current_savings < portion_down_payment * total_cost:
    current_savings = current_savings * (1 + r/12) + portion_saved
    n = n + 1
print('Number of months:',n)
