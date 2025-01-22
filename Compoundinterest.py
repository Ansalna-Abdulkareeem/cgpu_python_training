def compound_interest(principal, rate, time):
    return principal * ((1 + rate / 100) ** time) - principal
x=int(input("Enter the principal:"))
y=int(input("Enter the rate:"))
z=int(input("Enter the time:"))
print(f"Compound Interest(P={x},R={y}%,T={z}years):", compound_interest(x,y,z))