# Function to generate roll number based on branch and year

import random
import csv
database = 'student.csv'


def new_roll(branch, year):
    n_roll = year % 100

    # calculating roll number based on branch
    branch = branch.upper()
    if branch == 'CSE' or branch == 'CS':
        n_roll = n_roll * 100 + 25
    elif branch == 'EEE':
        n_roll = n_roll * 100 + 5
    elif branch == 'ETC':
        n_roll = n_roll * 100 + 7
    elif branch == 'CSSE':
        n_roll = n_roll * 100 + 28
    elif branch == 'CSCE':
        n_roll = n_roll * 100 + 29

    # Generating random number for last two digits
    x_roll = n_roll * 1000 + random.randint(1, 50)

    # Checking if the roll number already exists
    with open(database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0:
                if x_roll == row[5]:
                    # If it exists, new roll is generated
                    x_roll = n_roll * 1000 + random.randint(1, 50)
                    break

        # If not found unique, it is returned
        else:
            n_roll = x_roll

    f.close()
    return n_roll
