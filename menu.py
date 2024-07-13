from service import login_check, register_user
from prints import print_info, print_success


def menu():
    while True:
        print_info("Welcome to Menu")
        print_info("1. Login")
        print_info("2. Register")
        print_info("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            login_check()

        elif choice == "2":
            register_user()

        elif choice == "3":
            print_success("Thank you😊👌")
            break


if __name__ == "__main__":
    menu()
