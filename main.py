import json

def create_note():
    title = input("Enter note title: ")
    content = input("Enter note content: ")
    return {"title": title, "content": content}

def save_notes(notes):
    with open("notes.json", "w") as f:
        json.dump(notes, f, indent=4)

def load_notes():
    try:
        with open("notes.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def view_notes(notes):
    for i, note in enumerate(notes):
        print(f"{i+1}. {note['title']}")

    choice = int(input("Enter the number of the note to view: ")) - 1
    print(notes[choice]['content'])

def search_notes(notes, query):
    results = [note for note in notes if query.lower() in note['title'].lower()]
    if results:
        view_notes(results)
    else:
        print("No notes found.")

def main():
    notes = load_notes()

    while True:
        print("\nNotepad Menu:")
        print("1. Create a new note")
        print("2. View all notes")
        print("3. Search notes")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            new_note = create_note()
            notes.append(new_note)
            save_notes(notes)
        elif choice == 2:
            view_notes(notes)
        elif choice == 3:
            query = input("Enter search query: ")
            search_notes(notes, query)
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
