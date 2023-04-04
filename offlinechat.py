import csv

def create_chatroom():
    chatroom_name = input("Enter the name of the new chatroom: ")
    with open(chatroom_name + '.csv', mode='w', newline='') as chatroom_file:
        chatroom_writer = csv.writer(chatroom_file)
        chatroom_writer.writerow(['User', 'Message'])
    print("Chatroom created successfully.")

def join_chatroom():
    chatroom_name = input("Enter the name of the existing chatroom: ")
    username = input("Enter your username: ")
    with open(chatroom_name + '.csv', mode='r', newline='') as chatroom_file:
        chatroom_reader = csv.reader(chatroom_file)
        for row in chatroom_reader:
            print(row[0] + ': ' + row[1])
        while True:
            message = input("Enter your message (/exit to leave chatroom): ")
            if message == '/exit':
                break
            with open(chatroom_name + '.csv', mode='a', newline='') as chatroom_file:
                chatroom_writer = csv.writer(chatroom_file)
                chatroom_writer.writerow([username, message])

def show_menu():
    while True:
        print("1. Create a new chatroom")
        print("2. Join an existing chatroom")
        print("3. Exit the application")
        choice = input("Enter your choice: ")
        if choice == '1':
            create_chatroom()
        elif choice == '2':
            join_chatroom()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    print("Welcome to Offline Chat!")
    show_menu()
