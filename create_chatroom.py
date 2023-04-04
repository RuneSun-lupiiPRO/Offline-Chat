import csv
import os

# Function to create a new chatroom
def create_chatroom():
    chatroom_name = input("Enter the name of the new chatroom: ")
    chatroom_file_name = chatroom_name.lower().replace(" ", "_") + ".csv"
    with open(chatroom_file_name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["username", "message"])
    print("Chatroom created successfully!\n")

# Function to join an existing chatroom
def join_chatroom():
    chatroom_name = input("Enter the name of the chatroom: ")
    chatroom_file_name = chatroom_name.lower().replace(" ", "_") + ".csv"
    if not os.path.isfile(chatroom_file_name):
        print("Chatroom does not exist. Please try again.\n")
        return
    username = input("Enter your username: ")
    print(f"\nWelcome to {chatroom_name}, {username}!\n")
    with open(chatroom_file_name, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(f"{row[0]}: {row[1]}")
    print("\nType /exit to leave the chatroom.\n")
    while True:
        message = input("Enter your message: ")
        if message == "/exit":
            break
        with open(chatroom_file_name, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([username, message])
        print("Message sent successfully!\n")

# Function to display the main menu
def show_menu():
    while True:
        print("1. Create a new chatroom")
        print("2. Join an existing chatroom")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            create_chatroom()
        elif choice == "2":
            join_chatroom()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Display the main menu
show_menu()
