Year = int(input("Enter a year"))
if Year % 4 == 0 and (Year % 100 != 0 or (Year % 400 == 0)):
    print("This is a leap year")
else:
    print("This is NOT leap year")

