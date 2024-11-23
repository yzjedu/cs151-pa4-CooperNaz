# Algorithm
- Determine how many headlines have a particular word in it, for a single file
- Write headlines containing a specific word to a new file.
  - User gets to choose the name of the word and the new file.
- Determine the average number of characters per headline
- Output the longest and shortest headline.
  - Length is determined by number of characters.
- Read in a new file to analyze.
  - If the user chooses this option, it overwrites the data you had been storing
  (e.g. old file is no longer stored in program after new file is read in)


Purpose: Check that the file name exists   
Name: verify_file  
Parameters: file name  
Return:   
Algorithm:   
1. While the file name does not exist
   1. Prompt the user to input another file name

Purpose: Determine how many headlines have a particular word in it   
Name: headlines_with_word  
Parameters: word  
Return: headline number  
Algorithm:   
1. Set headline number to 0
2. For each line
   1. If the word is in the line
      1. Add one to the headline number
3. Return the headline number

Purpose: Write headlines containing a specific word to a new file   
Name: write_headlines_with_word  
Parameters: word, output file  
Return:   
Algorithm:   
1. Create an empty list
2. For each line
   1. If the word is in the line
      1. Append the line to the list
3. If the list is not empty
   1. Open the output file with the intent to write
   2. Write the list to the output file
   3. Close the output file

Purpose: Determine the average number of characters per headline   
Name: average_character_number  
Parameters: file name  
Return: Average character number  
Algorithm:   
1. Set characters to 0
2. Open the file with the intent to read
3. Read the data from the file into a list
4. For each line in the list
   1. Add the length of the line to characters
5. Divide the characters by the length of the list
6. Return the average character number

Purpose: Output the longest and shortest headline   
Name: longest_and_shortest  
Parameters: file name  
Return:   
Algorithm:  
1. Set the longest and shortest to 0
2. Open the file with the intent to read
3. Read the data from the file into a list
4. For each line in the list
   1. If line is less than the shortest
      1. Set the shortest equal to the line
   2. If the line is greater than the longest
      1. Set the longest equal to the line
5. Return the longest and shortest

Purpose: Read in a new file to analyze   
Name: read_file  
Parameters: file name  
Return:   
Algorithm:   
1. Open the file with the intent to read
2. Read the data to a list
3. Output the list

Purpose: Prompt the user to choose an option from a list of actions  
Name: action_menu  
Parameters:   
Return:   
Algorithm:   
1. Set the sentinel to "no"
2. While the continue response is not "no"
   1. Prompt the user to choose between the five action options
   2. Call the function for the corresponding action
   3. Prompt the user to enter whether they want to choose another option or not

Purpose: Run the program   
Name: main  
Parameters: Name  
Return: Name  
Algorithm:   
1. Output a welcome message and an explanation of the program's purpose
2. Call the action_menu function