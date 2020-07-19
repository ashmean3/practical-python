# mortgage.py
# Exercise 1.7 to 1.11

# Exercise 1.7
Principal= 500000.0
Rate= 0.05
Payment= 2684.11
Total_paid= 0.0

while Principal>0:
    Principal= Principal*(1+ Rate/12)- Payment
    Total_paid= Total_paid+ Payment

print('Total paid:', round(Total_paid, 2))

# Exercise 1.8

Principal= 500000.0
Rate= 0.05
Payment= 2684.11
Total_paid= 0.0
Months = 0

while Principal>0:
    
    Months= Months +1
    Principal= Principal*(1+ Rate/12)- Payment
    Total_paid= Total_paid+ Payment

    if Months <= 12:
        Principal = Principal - 1000
        Total_paid = Total_paid + 1000 

print('Updated Total paid:', round(Total_paid, 2))
print ('Total months:', Months)

# Exercise 1.9

Principal= 500000.0
Rate= 0.05
Payment= 2684.11
Total_paid= 0.0
Month = 0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000.0

while Principal > 0:
    
    Month= Month + 1
    Principal= Principal*(1+ Rate/12)- Payment
    Total_paid= Total_paid+ Payment

    if (Month >= extra_payment_start_month) and (Month <= extra_payment_end_month):
        Principal = Principal - extra_payment
        Total_paid = Total_paid + extra_payment

print('Modified Total paid:', round(Total_paid, 2))
print ('Total months:', Month)

# Exercise 1.10

Principal= 500000.0
Rate= 0.05
Payment= 2684.11
Total_paid= 0.0
Month = 0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000.0

while Principal > 0:
    
    Month= Month + 1
    Principal= Principal*(1+ Rate/12)- Payment
    Total_paid= Total_paid+ Payment

    if (Month >= extra_payment_start_month) and (Month <= extra_payment_end_month):
        Principal = Principal - extra_payment
        Total_paid = Total_paid + extra_payment

    print(Month, round(Total_paid,2), round(Principal, 2))

print('Modified Total paid:', round(Total_paid, 2))
print ('Total months:', Month)

# Exercise 1.11

Principal= 500000.0
Rate= 0.05
Payment= 2684.11
Total_paid= 0.0
Month = 0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000.0

while Principal > 0:
    
    Month= Month + 1
    Principal= Principal*(1+ Rate/12)- Payment
    Total_paid= Total_paid+ Payment

    if (Month >= extra_payment_start_month) and (Month <= extra_payment_end_month):
        Principal = Principal - extra_payment
        Total_paid = Total_paid + extra_payment

    if Principal < 0:
        Total_paid = Total_paid - Principal
        Principal = 0

    print(Month, round(Total_paid,2), round(Principal, 2))

print('Modified Total paid:', round(Total_paid, 2))
print ('Total months:', Month)
