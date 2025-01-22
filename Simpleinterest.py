x=int(input("Enter the principal:"))
y=int(input("Enter the rate:"))
z=int(input("Enter the time:"))
def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

print(f"Simple Interest (P={x},R={y}%,T={z}years):", simple_interest(x,y,z))