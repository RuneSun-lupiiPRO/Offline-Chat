def send_message(chatroom_name, username, keywords):
    # Read the chat log from the CSV file
    with open(f"{chatroom_name}.csv", mode="r") as file:
        reader = csv.reader(file)
        chat_log = list(reader)

    # Prompt the user to enter messages
    while True:
        message = input(f"{username}: ")
        if message == "/exit":
            # Send the list of keywords back to the main chat
            if keywords:
                print("Keywords found:")
                print(keywords)
            break
        else:
            # Append the message to the chat log and write it to the CSV file
            chat_log.append([username, message])
            with open(f"{chatroom_name}.csv", mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(chat_log)

            # Check if the message contains the keyword
            if "keyword" in message:
                keywords.append(message)
