try:
    name = input("Enter your name: ")
    marks = int(input("Enter your mark (0-100): "))

    if marks < 0 or marks > 100:
        print("Invalid mark!")

    elif marks >= 90:
        print("Grade: A")

    elif marks >= 80:
        print("Grade: B")

    elif marks >= 70:
        print("Grade: C")

    elif marks >= 60:
        print("Grade: D")

    else:
        print("Grade: E")

except ValueError:
    print("Please enter numbers only.")