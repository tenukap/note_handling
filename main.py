import os

number = 0
Selection = [1, 2, 3]  # list of options for user to select
second_selection = []


# -------------------------------------------------------------------------------------------------
# encryption function
def my_securtiy(message):
    # declaring
    # message = NewNote
    shift = 1
    encrypted = " "
    length_text = len(message)
    # for text in message:
    # encrypted += chr(ord(text) + shift) % 26
    for text in message:
        if text.isupper():
            encrypted += chr((ord(text) + shift - 65) % 26 + 65)
        elif text.islower():
            encrypted += chr((ord(text) + shift - 97) % 26 + 97)
        else:
            encrypted += text

    print(f"this is the length of the message {length_text}")
    print("encryption is sucessfull")
    return encrypted


def decryption(message):
    shift = 1
    decrypted = " "

    print(message)
    for range in message:
        if range.isupper():
            decrypted += chr((ord(range) - shift - 65) % 26 + 65)
        elif range.islower():
            decrypted += chr((ord(range) - shift - 97) % 26 + 97)
        else:
            decrypted += range

    print(f"your message is \n{decrypted}")


# storing to new note library
def my_library(note_number, note_name):
    # storinng the counter
    file = open("library.txt", "a")
    file.write(f"{note_number} .) {note_name} \n")


# -------------------------------------------------------------------------------------------------

start = True
while start == True:
    no_of_notes = 0
    selector = 0
    print(
        "-----------------------------------------------------------------------------------"
    )
    print(
        "Welcome to Notes\n\n select below! \n\n 1.) New Note \n 2.) view Notes \n 3.) delete Note"
    )  # selection of options for user

    if not os.path.exists("library.txt"):
        count = open("library.txt", "wt")
        pass
    else:
        count = open("library.txt", "rt")
        no_of_notes = sum(1 for line in count)
        count_notes = int(no_of_notes)
        for i in range(no_of_notes):
            selector += 1
            second_selection.append(selector)

    # handling the no of files in a library

    userSelection = int(input("Please select an option: "))  # user input for selection
    if userSelection not in Selection:  # if user input is not in selection
        print("Invalid selection, please try again")  # error message
    elif userSelection == 1:
        Note_name = str(input("name of file: "))
        NewNote = str(input("Please enter your note: "))  # user input for new note
        Note_name = Note_name + ".txt"
        Encrypted_note = my_securtiy(message=NewNote)

        note = open("NewNote.txt", "wt")
        note.write(f"{Encrypted_note}\n")
        note.close()
        os.rename("NewNote.txt", Note_name)

        print(f"file is saved as {Note_name}.")
        no_of_notes = no_of_notes + 1
        my_library(note_name=Note_name, note_number=no_of_notes)

    elif userSelection == 2:
        choosing_saved_notes = []

        # printing the avaiable notes titile in the library
        output_stored_names = open("library.txt", "r")
        stored_titles = output_stored_names.read()
        print(stored_titles)
        number = 0
        choosing_saved_notes = []
        choosing_saved_notes.clear()  # list created
        for counter in range(
            count_notes
        ):  # count notes are the total sum of notes in the library.txt file

            number += 1
            choosing_saved_notes.append(number)

        # print(choosing_saved_notes) # appending the list and adding the number so we may select according to user choice
        print("-------------------------------------------")
        print(f"theres are the list numbers in the list {choosing_saved_notes}")
        print("-------------------------------------------")

        # user chooses what note to open
        user_choice = int(input("select the note you want to open \n"))
        selection = len(choosing_saved_notes)
        selection_inlists = 0

        if user_choice > count_notes:
            print("please select from the given note numbers only!")
        else:
            for selection_inlists in range(selection):
                # going in a  range of the total number of lines in library.txt
                if user_choice == int(choosing_saved_notes[selection_inlists]):
                    print(
                        f"you have chosen  {choosing_saved_notes[selection_inlists]}\n"
                    )

                    # going through the list to check which user choice is equal to the list
                    title_content = open("library.txt", "rt")
                    for line in title_content:
                        split_number = line.split()
                        split_title = line.split()
                        split_number = split_number[0]

                        split_number = int(
                            split_number
                        )  # selects only the number of the line
                        if split_number == user_choice:
                            title = split_title[2]
                            print(title)
                            output_text = open(title, "r")
                            user_output = output_text.read()
                            decryption(message=user_output)
                            # opening to edit is also the next step
                            # the next step would be to help delete all the selected files
                            # now we have gotten the output for instance for seleting 3 we get password. so
                            # next would be to open the fil eusing the split_title[] and decrpting
    elif userSelection == 3:

        choosing_saved_notes = []

        # printing the avaiable notes titile in the library
        output_stored_names = open("library.txt", "r")
        stored_titles = output_stored_names.read()
        print(stored_titles)
        number = 0
        choosing_saved_notes = []
        choosing_saved_notes.clear()  # list created
        for counter in range(
            count_notes
        ):  # count notes are the total sum of notes in the library.txt file

            number += 1
            choosing_saved_notes.append(number)
        print(f"the list of numbers in the library {choosing_saved_notes}")

        delete_choice = int(
            input("which file would u like to delete? \n")
        )  # example number 1 selected
        lencount = len(choosing_saved_notes)
        context = []  # list to store all the code for the appending of library
        for count in choosing_saved_notes:
            if delete_choice > lencount:
                print("pls select within the saved files\n")
            elif delete_choice == count:
                print(f"it matched {delete_choice}")
                content = open("library.txt", "rt")
                content = content.readlines()
                for line in content:
                    openline = line.split()
                    sum_delete = openline[2]
                    compare = int(openline[0])
                    if (
                        compare != delete_choice
                    ):  # output of openline is wrong check again next itme u open idle with a debug
                        print(f"KEEP {line}")
                        context.append(line)

                    else:
                        print(f"remove {line}")
                        os.remove(sum_delete)

                print(context)
                edit_library = open("library.txt", "wt")
                for edit in context:
                    edit_library.write(edit)

                edit_library.close()

                print(f"{openline} has been removed")
