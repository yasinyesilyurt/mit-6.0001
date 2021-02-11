#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 11:43:12 2021

@author: yasinyesilyurt
"""

r = 0.04
total_cost = 1000000
portion_down_payment = 0.25
down_payment = total_cost * portion_down_payment
semi_annual_raise = 0.07
epsilon = 100
low = 0
high = 10000
annual_salary = float(input('Enter your starting annual salary ...'))
x = annual_salary
percentage_saved = high
bisection_steps = 0
possible = True

while True:
    annual_salary = x
    monthly_salary = annual_salary/12
    best_percentage_saved = percentage_saved / 10000
    portion_saved = best_percentage_saved * monthly_salary
    current_savings = 0
    n = 0
    steps = 0
    while n <= 36:
        current_savings = current_savings * (1 + r/12) + portion_saved
        n += 1
        if n !=1 and n%6 == 1:
            annual_salary = annual_salary * (1 + semi_annual_raise)
            monthly_salary = annual_salary/12
            portion_saved = best_percentage_saved * monthly_salary
    
    if abs(current_savings - down_payment) <= epsilon:
        break
    if current_savings > down_payment:
        high = percentage_saved
        bisection_steps += 1
    else:
        low = percentage_saved
        bisection_steps += 1    
    percentage_saved = (high+low)//2  
    if percentage_saved >= 10000:
        possible = False
        break
if possible:
    print('The best savings rate is', str(best_percentage_saved))
    print('Steps in bisection search:', str(bisection_steps))
else:
    print('It is not possible to pay the down payment in 3 years')