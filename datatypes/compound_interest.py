"""
Compound Interest = Amount - Principal
P = Principal amount
R = Rate of interest
T = Time
Amount = P(1+R/100) ** T
"""

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time of interest: "))

amount1 = principal * (1+rate/100) ** time
amount2 = principal * pow((1+rate/100), time)

print(f"The amount is {round(amount1,5)}")
print(f"The amount is {round(amount2,5)}")

print(f"The compound interest is {round(amount2 - principal,5)}")