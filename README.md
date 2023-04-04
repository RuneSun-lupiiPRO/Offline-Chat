# Offline Chat

This project aims to create an offline chat application that can be used when there is no internet connection available. The application is built in Python and utilizes CSV files to store and retrieve chat logs.

## Installation

1. Clone this repository to your local machine
2. Install the required Python libraries by running `pip install -r requirements.txt`
3. Run the application by running `python offlinechat.py`

## Usage

The application will prompt you to enter a username and choose a chatroom.
Once you have entered the chatroom, you can start chatting with other users in real-time.
To exit the chatroom, simply type `/exit` and you will be returned to the main menu.

## File Structure

- `offlinechat.py`: The main Python file containing the application code
- `new_chat_log.csv`: The CSV file that stores the chat logs
- `README.md`: This file that provides information about the project

## Contrib
what do I do with the following information "The above code defines three functions: create_chatroom(), join_chatroom(), and show_menu().

The create_chatroom() function prompts the user to enter the name of a new chatroom and creates a new CSV file with that name to store the chat logs.

The join_chatroom() function prompts the user to enter the name of an existing chatroom and their username. It then reads the CSV file containing the chat logs for that chatroom and displays the logs to the user. It also prompts the user to enter messages to send to the chatroom and writes those messages to the CSV file.

The show_menu() function displays the main menu to the user and prompts them to choose an option: create a new chatroom, join an existing chatroom, or exit the application. It calls the appropriate function based on the user's choice.

Finally, the show_menu() function is called at the end of the code to display the main menu and start the application."

The information you provided explains the purpose of the three functions defined in the code and how they work together to create an offline chat application. The create_chatroom() function creates a new chatroom, the join_chatroom() function allows users to join an existing chatroom and exchange messages with other users, and the show_menu() function displays the main menu and allows users to choose between creating a new chatroom, joining an existing chatroom, or exiting the application. The show_menu() function is called at the end of the code to start the application.

Offline Chat

This project aims to create an offline chat application that can be used when there is no internet connection available. The application is built in Python and utilizes CSV files to store and retrieve chat logs.
Installation

    Clone this repository to your local machine
    Install the required Python libraries by running pip install -r requirements.txt
    Run the application by running python offlinechat.py

Usage

    The application will prompt you to enter a username and choose a chatroom.
    Once you have entered the chatroom, you can start chatting with other users in real-time.
    To exit the chatroom, simply type /exit and you will be returned to the main menu.

File Structure

    offlinechat.py: The main Python file containing the application code
    new_chat_log.csv: The CSV file that stores the chat logs
    README.md: This file that provides information about the project

Contributing

If you would like to contribute to this project, please follow the steps below:

    Fork the repository
    Create a new branch for your changes
    Make your changes and test them
    Submit a pull request

License

This project is licensed under the MIT License - see the LICENSE file for details.
Contact

If you have any questions or comments about this project, please feel free to contact me at [lupii@pm.me].
