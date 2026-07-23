"""
Simple Interest = (P*R*T)/100
P = Principal amount
R = Rate of interest
T = Time
"""

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time of interest: "))

si = (principal * rate * time) / 100

print("Simple Interest: ", si)