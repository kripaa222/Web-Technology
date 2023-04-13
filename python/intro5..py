n=int(input("Enter a positive integer: "))

if n<=0:
    print("Invalid input! Please enter a positive integer.")
else:
    print(f"Multiplication table of (n):")
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")

