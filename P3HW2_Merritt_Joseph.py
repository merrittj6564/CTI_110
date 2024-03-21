#Joseph Merritt
#19 March 2024
#P3HW2
#Salary

var = input("Enter employee's name: ")
hrs_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

    

print("--------------------------")
print("Employee name: ", var)

print(f"\n{'Hours Worked':<15}{'Pay Rate':<10}{'OverTime':<10}{'OverTime Pay':<15}{'RegHour Pay':<15} {'Gross Pay':<10}")
print("---------------------------------------------------------------------------")

if hrs_worked >= 41:
    reg_hrs = 40
    OT_hrs = hrs_worked - 40
else: #no overtime exists
    reg_hrs = hrs_worked
    OT_hrs = 0

OTpay_rate = pay_rate * 1.5
reg_pay = reg_hrs * pay_rate
OT_pay = OT_hrs * OTpay_rate
gross_pay = OT_pay + reg_pay

    

print(f'{hrs_worked:<15.2f} {pay_rate:<10.2f} {OT_hrs:<10.2f} {OT_pay:<15.2f}{reg_pay:<15.2f}{gross_pay:<15.2f}')
