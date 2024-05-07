print("------ Welcome to The Journaling App ------ 😀")
print("This App lets you create and manage simple notes")

username = input("Please enter your name: ")

print("Welcome to the The Journaling App " + username + "!")

print("""
------------------- Menu Options ---------------------------
1. Create Note
2. Edit Note
3. Delete Note
 """)

option = input("Please select an option: ")

option = int(option)

if option != 1 and option != 2 and option != 3:
    print("Invalid menu option")
    print("Please try again")
else:
    if option == 1:
        # create note
        note_name = input("Enter the note name: ")

        print("You are creating note " + note_name)

        with open(note_name, "w") as fileoject:
            pass
        print("Note created successfully! ✅")
    elif option == 3:
        import os
        note_to_be_deleted = input("Enter note to be deleted: ")

        if os.path.isfile(note_to_be_deleted):
            os.remove(note_to_be_deleted)
            print("Note " + note_to_be_deleted + " deleted successfully!")
        else:
            print("Invalid input. Note does not exist")
      


