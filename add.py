# Function to add the details of the students

from Generate_Roll import new_roll
from Generate_Email import new_email
import csv


database = 'student.csv'
charr = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
         'V', 'W', 'X', 'Y', 'Z']


def add():
    print("\n--------------------------------------------------------")
    print("---------------------Add Information--------------------")
    print("--------------------------------------------------------\n")

    student_data = []

    # Entering and checking the name of the student
    while True:
        n = input("Enter your name: ")
        n = n.upper()
        for i in n:
            if i in charr:
                f = 1
            else:
                f = 0
                break
        if f == 1:
            student_data.append(n)
            break
        else:
            print("Please enter only alphabets\n")
            print("Try again.....")

    # Checking if the age entered is within the range 17 and 24 and if it is a digits
    while True:
        a = input("Enter your age: ")
        if a.isdigit():
            student_data.append(a)
            break
        elif int(a) < 17 or int(a) > 24:
            print("Please enter age between 17 and 24")
        else:
            print("Please enter valid age in digits\n")
            print("Try again.....")

    # Checking if the entered branch is cse, csse, csce, eee, etc
    while True:
        b = input("Enter your branch (CSE, CSSE, CSCE, EEE, ETC): ")
        b = b.upper()
        if b == 'CSE' or b == 'CSSE' or b == 'CS' or b == 'CSCE' or b == 'EEE' or b == 'ETC':
            student_data.append(b)
            break
        else:
            print("Please enter valid branch\n")
            print("Try again.....")

    # Checking if the joining year is between 2015 and 2020
    while True:
        yr = int(input("Enter year of join (2015-2020): "))
        if 2015 <= yr <= 2020:
            student_data.append(str(yr))
            break
        else:
            print("Please enter year in the provided range (2015-2020)\n")
            print("Try again.....")

    # Generating roll number and email id
    roll_no = str(new_roll(b, yr))
    mail = new_email(roll_no)

    student_data.append(mail)
    student_data.append(roll_no)

    with open(database, "a", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows([student_data])

    f.close()

    print("\n-----------------Data saved successfully----------------\n")

    print("Here is your Roll no. and email ID.")
    print("Please note and keep it safe.")

    print("\n\t     ROLL NUMBER : ", roll_no, " \t")
    print("\tEMAIL ID: ", mail, " \t")

    print("\n---------------------------------------------------------")
    print("        Thankyou for choosing this university....")
    print("           I hope you enjoy your stay here....   ")

    input("\nPress any key to continue.......")

    return
