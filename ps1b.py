portion_down_payment = 0.25
current_savings = 0
r = 0.04
n = 0

total_cost = float(input('What is the cost of your dream house ...'))
annual_salary = float(input('What is your starting annual salary ...'))
percentage_saved = float(input('Enter the percent of your salary to save, as a decimal...'))
semi_annual_raise = float(input('Enter the semi-annual raise, as a decimal...'))

monthly_salary = annual_salary/12
portion_saved = percentage_saved * monthly_salary

while current_savings < portion_down_payment * total_cost:
    if n !=1 and n%6 ==1:
        annual_salary = annual_salary * (1 + semi_annual_raise)
        monthly_salary = annual_salary/12
        portion_saved = percentage_saved * monthly_salary
    current_savings = current_savings * (1 + r/12) + portion_saved
    n = n + 1
print(n)
print(current_savings)