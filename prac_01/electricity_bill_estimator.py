# print("Electricity bill estimator\n")
# cents_per_kWh = float(input("Enter cents per kWh: "))/100
# while cents_per_kWh < 0:
#    print("invalid value")
#    cents_per_kWh =  float(input("Enter cents per kWh: "))/100
#
# daily_use = float(input("Enter daily use in kWh: "))
# while daily_use < 0:
#    print("invalid value")
#    daily_use = float(input("Enter daily use in kWh: "))
#
# number_of_billing_days = int(input("Enter number of billing days: "))
# while number_of_billing_days < 0:
#    print("invalid choice")
#    number_of_billing_days = int(input("Enter number of billing days: "))
#
# estimated_bill = cents_per_kWh * daily_use * number_of_billing_days
# print("Estimated bill: ${:.2f}".format(estimated_bill))

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print("Electricity bill estimator 2.0\n")
tariff_number = int(input("which tariff? 11 or 31:"))
while tariff_number != 11 and tariff_number != 31:
    print("invalid tariff number")
    tariff_number = int(input("which tariff? 11 or 31:"))

if tariff_number == 11:
    cents_per_kWh = TARIFF_11
else:
    cents_per_kWh = TARIFF_31

daily_use = float(input("Enter daily use in kWh: "))
while daily_use < 0:
    print("invalid value")
    daily_use = float(input("Enter daily use in kWh: "))

number_of_billing_days = int(input("Enter number of billing days: "))
while number_of_billing_days < 0:
    print("invalid choice")
    number_of_billing_days = int(input("Enter number of billing days: "))

estimated_bill = cents_per_kWh * daily_use * number_of_billing_days
print("Estimated bill: ${:.2f}".format(estimated_bill))
