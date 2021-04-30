# Function to search for a student details using roll number

import csv


def search(roll):

    database = 'student.csv'
    found = 0
    with open(database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0:
                if roll == row[5]:
                    found = 1
                    print("\n------------------ Student Found -----------------")
                    print("Roll Number: ", row[5])
                    print("Name: ", row[0])
                    print("Age: ", row[1])
                    print("Branch: ", row[2])
                    print("Year: ", row[3])
                    print("Email ID: ", row[4])

        else:
            print("\n----------------------Entry not found--------------------\n")

    f.close()
    return found
