portion_down_payment = 0.25
current_savings = 0
r = 0.04
n = 0

total_cost = float(input('What is the cost of your dream house ...'))
annual_salary = float(input('What is your annual salary ...'))
percentage_saved = float(input('Enter the percent of your salary to save, as a decimal...'))

monthly_salary = annual_salary/12
portion_saved = percentage_saved * monthly_salary

while current_savings < portion_down_payment * total_cost:
    current_savings = current_savings * (1 + r/12) + portion_saved
    n = n + 1
print(n)