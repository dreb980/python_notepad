notes = []
print("Welcome to the NotePad!")
print("You can create and save notes here.")
while True:
    choice = input("\n1. Create a new note \n2. View the most recently saved note \n3. Quit \n")
    if choice == "1":
        print("Okay!")
        print("Start typing!")
        new_note = input("")
        notes.append(new_note)
        print("Your new note is saved.")
    elif choice == "2":
        if len(notes) > 0:
            print(notes[-1])
        else:
            print("No notes to view.")
    elif choice == "3":
        print("Okay. Now exiting NotePad...")
        break
    else:
        print("Invalid choice. Please try again.")