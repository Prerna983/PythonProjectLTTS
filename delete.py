# Function to delete a record containing the roll number of the student

import csv


def delete(roll):
    found = False
    database = 'student.csv'
    data = []

    # Checking if the entered roll number is present or not
    with open(database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        count = 0
        for row in reader:
            if len(row) > 0:
                if roll != row[5]:
                    data.append(row)
                    count += 1
                else:
                    found = True

    if found is True:
        with open(database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(data)
        print("\n------------------Successfully Removed------------------")
        print("\n---------Hope you had a great time in the college-------\n")
        f.close()
        return 1

    else:
        print("\n-----------------No such roll no. found-----------------")
        return 0
