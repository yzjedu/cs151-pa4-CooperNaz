# Programmers:  Cooper Nazar
# Course:  CS151, Professor Yalew
# Due Date: November 21, 2024
# Programming Assignment:  PA 04
# Problem Statement: Create a program to analyze headlines from the Australian Broadcasting Company (ABC).
# Data In: File name
# Data Out: Data
# Input Files: txt
# Credits:

import os

# Purpose: Check that the file name exists
# Parameters: None
# Return: None
def verify_file():
    filename = input("What is the name of the file that you would like to open? ")
    while not os.path.isfile(filename):
        filename = input("What is the name of the file that you would like to open? ")
    return filename

# Purpose: Determine how many headlines have a particular word in it
# Parameters: None
# Return: None
def num_headlines_with_word():
    word = str(input("What word would you like to search for in the headlines? "))
    headline_count = 0
    file_name = verify_file()
    try:
        data_file = open(file_name, "r")
        file_data = data_file.read()
        data_file.close()
        for line in file_data:
            if word in line:
                headline_count += 1
        print("-" * 50)
        print(f"Number of headlines containing the word '{word}': {headline_count}")
        print("-" * 50)
    except:
        data_file.close()
        print("Error reading file.")

# Purpose: Write headlines containing a specific word to a new file
# Parameters:
# Return:
def write_headlines_with_word():
    word = input("What word would you like to search for in the headlines? ")
    headlines = []
    filename = verify_file()
    outfile = input("What is the name of the file that you would like to write the results to? ")
    try:
        data_file = open(filename, "r")
        file_data = data_file.read()
        data_file.close()
        for line in file_data:
            if word in line:
                headlines.append(line + "\n")
        out_data = open(outfile, "w")
        out_data.write(headlines)
        out_data.close()
        print(f"Data written to the file titled '{outfile}'")
    except:
        data_file.close()
        print("Error reading file.")

# Purpose: Determine the average number of characters per headline
# Parameters:
# Return:
def average_character_number():
    characters = 0
    filename = verify_file()
    try:
        data_file = open(filename, "r")
        file_data = data_file.readlines()
        for line in file_data:
            line_characters = len(line)
            characters += line_characters
        average_characters = int(characters / len(file_data))
        data_file.close()
    except:
        file_data.close()
        print("Error reading file.")
    print(f"Average characters in each headline: {average_characters}")

# Purpose: Output the longest and shortest headline
# Parameters: None
# Return: None
def longest_and_shortest():
    filename = verify_file()
    longest = 0
    shortest = 0
    try:
        data_file = open(filename, "r")
        file_data = data_file.read()
        data_file.close()
        for line in file_data:
            if len(line) < len(shortest):
                shortest = line
            if len(line) > len(longest):
                longest = line
    except:
        data_file.close()
        print("Error reading file.")
    print("-" * 50)
    print(f"Longest headline: {longest}")
    print(f"Shortest headline: {shortest}")
    print("-" * 50)

# Purpose: Read in a new file to analyze
# Parameters: None
# Return: None
def read_file():
    filename = verify_file()
    data_file = open(filename, "r")
    file_data = data_file.read()
    data_file.close()
    print("-" * 50)
    print(f"Data contained in the file titled {filename}: ")
    print(file_data)
    print("-" * 50)

# Purpose: Prompt the user to choose an action from the list of actions
# Parameters:
# Return:
def action_menu():
    SENTINEL = "no"
    continue_choice = "yes"
    choice = 0
    while continue_choice != SENTINEL:
        print("-" * 50)
        print("Which action would you like to take? \n")
        print("\t1. Determine how many headlines have a particular word in them \n")
        print("\t2. Determine which headlines have a particular word in them \n")
        print("\t3. Determine the average number of characters per headline \n")
        print("\t4. Determine the longest and shortest headlines \n")
        print("\t5. Read a file to analyze \n")
        print("-" * 50)
        choice = int(input("Please enter the number of your choice: "))
        if choice == 1:
            num_headlines_with_word()
        elif choice == 2:
            write_headlines_with_word()
        elif choice == 3:
            average_character_number()
        elif choice == 4:
            longest_and_shortest()
        elif choice == 5:
            read_file()
        else:
            print("Invalid choice.")
        continue_choice = input("Would you like to continue? Please enter yes or no: ")
        continue_choice = continue_choice.lower().strip()

# Purpose: Run the program
# Parameters: None
# Return: None
def main():
    print("-" * 50)
    print("This program is meant to analyze headlines from the Australian Broadcasting System from given files.")
    action_menu()
    print("\nThank you for using the program.")

main()