This code defines three functions: create_chatroom(), join_chatroom(), and show_menu(). The create_chatroom() function prompts the user to enter the name of a new chatroom and creates a new CSV file with that name to store the chat logs. The join_chatroom() function prompts the user to enter the name of an existing chatroom and their username. It then reads the CSV file containing the chat logs for that chatroom and displays the logs to the user. It also prompts the user to enter messages to send to the chatroom and writes those messages to the CSV file. The show_menu() function displays the main menu to the user and prompts them to choose an option: create a new chatroom, join an existing chatroom, or exit the application. It calls the appropriate function based on the user's choice. Finally, the show_menu() function is called at the end of the code to display the main menu and start the application.

To use this application, clone the repository to your local machine and run the command pip install -r requirements.txt to install the required Python libraries. Then, run the command python offlinechat.py to start the application. The application will prompt you to enter a username and choose a chatroom. Once you have entered the chatroom, you can start chatting with other users in real-time. To exit the chatroom, simply type /exit and you will be returned to the main menu.

The file structure of this project is:

    offlinechat.py: The main Python file containing the application code
    new_chat_log.csv: The CSV file that stores the chat logs
    README.md: This file that provides information about the project

If you would like to contribute to this project, please fork the repository, create a new branch for your changes, make your changes and test them, and then submit a pull request. This project is licensed
