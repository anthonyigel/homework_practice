"""
1.A. User Input: Write a function get_list_of_words(): Use a while loop to continually ask the user to input
      a word, until they type "quit", Once they type a word in, add it to a list. Once they quit the loop,
      return the list (Please do not print, but return the list).
  B. Write another function print_sorted(in_list): that will use a for loop to print all items within the list in
     a reversed order. The print should separate the words using a comma and at the end put out a new line.
     
  Test against the words: USA, ISA, FSB, Miami, ISA, Python, quit
  
  C. Modify the get_list_of_words to get_list_of_numbers()
"""

#-------------------------------------
# Create an empty list to initialize the variable 
tst_list = []

def get_list_of_words():
    
    # Determine if tst_list is already created, if not then create it.
    if 'tst_list' not in locals():
        tst_list = []
    user_input = ''
    while user_input != 'quit':
        user_input = str(input('Please enter a word or enter "quit": '))
        if user_input != 'quit':
            tst_list.append(user_input)
        else:
            return tst_list

# Assign the returned output to name in_list
in_list = get_list_of_words()
in_list

#-------------------------------------
def print_sorted(in_ls):
    
    # Reverse the order of the alphabetically sorted listed
    reverse_ls = sorted(in_ls, reverse=True)
    
    # Establish sentence as a string variable
    sentence = ''
    
    # Determine the length of the list and define the index of the last variable
    last_element = len(reverse_ls) - 1
    
    # Iterate through the list and add a comma
    for i in reverse_ls:
        if i == reverse_ls[last_element]:
            i = i + '\n'
        else:
            i = i + ','

        sentence = sentence + i 
    print(sentence)

print_sorted(in_list)

#-------------------------------------
# Create an empty list to initialize the variable 
tst_num_list = []

def get_list_of_numbers():
    
    # Determine if tst_list is already created, if not then create it.
    if 'tst_num_list' not in locals():
        tst_num_list = []
    user_input = ''
    while user_input != 'quit':
        user_input = str(input('Please enter a number or enter "quit": '))
        if user_input != 'quit':
            user_input = float(user_input)
            tst_num_list.append(user_input)
        else:
            return tst_num_list
          
          
#------------------------------------------------------------------------------------------------------------------------------
"""
2. Find the mode of the numbers in the list.
   (Some Hints and breakdown below) - https://www.wikihow.com/Find-the-Mode-of-a-Set-of-Numbers
   Hints: This is one approach - other equally valid methods exist, "breakdowns may differ"
       1. First setify - get another list without duplicates
       2. Create a histogram list with the count of all the entries
       3. Find the index corresponding to the maximum value in the histogram list
       4. Report the corrresponding entry in the setify lilst for (Option A)
       5. If there is more than one max value, the report all (Option B)
       6. If all entries have the same count, then no more (Option C)
  Option A: Test against this set of value that you enter one at a time [18, 21, 11, 21, 15, 19, 17, 21, 17]
  Option B: Test and make sure it works against these value also [18, 21, 17, 11 ,21, 15, 19, 17, 21, 17]
  Option C: Test and make sure it works against these value also: [18, 21, 17, 11 ,15, 19]
"""
option_a_numbers = [18, 21, 11, 21, 15, 19, 17, 21, 17]
option_b_numbers = [18, 21, 17, 11 ,21, 15, 19, 17, 21, 17]
option_c_numbers = [18, 21, 17, 11, 15, 19]

def get_mode_value(ls_of_numbers):
    
    # Sort the original list of numbers
    ls_of_numbers = sorted(ls_of_numbers)
    
    # Define variable 
    no_dup_ls_of_numbers = []
    
    # Loop through original list to remove duplicates
    for i in ls_of_numbers: 
        if i not in no_dup_ls_of_numbers: 
            no_dup_ls_of_numbers.append(i) 
    
    # Sort the non-duplicative list of numbers
    no_dup_ls_of_numbers = sorted(no_dup_ls_of_numbers)
    
    
    # Creating an empty dictionary to add frequency counts to no duplicated numbers
    freq = {} 
    for i in ls_of_numbers:
        freq[i] = freq.get(i, 0) + 1
    
    
    temp_mode = [k for k, v in dic.items() if v == max(list(dic.values()))] 
        
        
    if len(temp_mode) == n: 
        get_mode = "No mode found"
    else: 
        get_mode = "Mode is / are: " + ', '.join(map(str, temp_mode)) 

    print(get_mode) 
    return freq


dic = get_mode_value(option_a_numbers)
