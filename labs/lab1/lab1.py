def monthly_interest():
    net_balance= eval(input("What is your previous balance?"))
    days_billing_cycle= eval(input("What is the number of days in billing cycle for the month?"))
    balance= net_balance * days_billing_cycle

    payment_recieved= eval(input("Payment recieved amount:" ))
    day_of_payment= eval(input("What day of the billing cycle did you receive payment?"))
    days_before_end_cycle= days_billing_cycle - day_of_payment
    net_payment_recieved= payment_recieved * days_before_end_cycle

    amount= balance - net_payment_recieved
    average_daily_balance= amount / days_billing_cycle

    annual_interest_rate= eval(input("What is your annual interest rate?"))
    charge= annual_interest_rate / 12
    charge1= charge/ 100
    monthly_interest_charge= round(average_daily_balance * charge1, 2)
    print("Your monthly interest charge is:", monthly_interest_charge)


monthly_interest()