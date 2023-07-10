marks = int(input("Enter Marks of student"))
if 80 < marks < 100:
    print("You scored an A")
elif 60 < marks < 80:
    print("You scored an B")
elif 40 < marks < 60:
    print("You scored an C")
elif 20 < marks < 40:
    print("You scored an D")
elif 0 < marks < 20:
    print("You scored an E")
elif marks > 100 or marks < 0:
    print("Error number invalid")
