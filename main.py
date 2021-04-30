# Main function to run the project

from display import show
from add import add
from search import search
from delete import delete
from menu import displayMenu

field = ['name', 'age', 'branch', 'year', 'email', 'roll']
database = 'student.csv'

# To create and run the file for the first time
# with open(database, "a", encoding="utf-8") as f:
#     writer = csv.writer(f)
#     writer.writerow(field)
#
# f.close()

while True:
    displayMenu()

    choice = int(input("Enter your choice: "))
    if choice == 1:
        add()

    elif choice == 2:
        print("\n-------------------- Search Details --------------------")
        roll = input("Enter roll no. to search: ")
        search(roll)
        x = input("\nPress any key to continue.....")

    elif choice == 3:
        show()

    elif choice == 4:
        print("\n--------------------- Delete details --------------------")
        roll = input("Enter roll no. to delete: ")
        delete(roll)
        input("\n\nPress any key to continue.....")

    elif choice == 5:
        print("\n\t\t\t........Thank you..........")
        break

    else:
        print("You have entered a wrong input!! ")
        input("Press any key to continue.....")
