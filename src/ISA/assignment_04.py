#------------------------------------------------------------------------------------------------------------------------------
"""
Q1:

A) Given the following string variable stmt = 'In spring 2021, I took a python class in a hybrid environment'. Write a function create_dict_from_string that takes an argument of type string and based on the words in the string, creates a dictionary and returns that dictionary.

For example: When I pass the string stmt, the function should create and return the following dictionary:
{'in': 8, 'spring': 1, '2021,': 2, 'i': 3, 'took': 4, 'a': 9, 'python': 6, 'class': 7, 'hybrid': 10, 'environment': 11} Note that the later value of both ​in ​ and ​a ​ in the final result Points (3)

B) Write another function find_longest_word that identifies the longest word in the string using the dictionary. The dictionary should be passed as a parameter (argument to the function). The function should return the word, and also the output its position within the string (stmt) - as a tuple. Points (3)

C) In the main function, call the two functions in turn, and print the dictionary, and the longest word, along with its position+1 within the stmt (unpack the tuple before you print). Points (2)

================ Sample output for Problem 1 ================

{'in': 8, 'spring': 1, '2021,': 2, 'i': 3, 'took': 4, 'a': 9, 'python': 6, 'class': 7, 'hybrid': 10, 'environment': 11}

The longest word is environment and is word 12 within the string.
"""

#-------------------------------------
stmt = "In spring 2021, I took a python class in a hybrid environment"

def create_dict_from_string(stmt):
    
    # Create a list of the words in the statement
    raw_word_lst = stmt.split()
    

    # Remove duplicates by converting to same case
    word_lst = []
    [word_lst.append(x.lower()) for x in raw_word_lst if x.lower() not in word_lst]
    
    # Create an empty dictionary
    temp_dict = {}
    
    # Define key and value of dictionary as the word and relative index in the statement
    for index_of_word, word in enumerate(raw_word_lst):
        temp_dict[word.lower()] = index_of_word
    
    return temp_dict

create_dict_from_string(stmt)

#-------------------------------------
def find_longest_word(dictionary):
    
    max_len = -1
    for ele in stmt_dict.keys():
        if len(ele) > max_len:
            max_len = len(ele)
            res = ele
    
    return (res, dictionary[res])
        
find_longest_word(dictionary = stmt_dict)

#-------------------------------------
def main():
    
    stmt = "In spring 2021, I took a python class in a hybrid environment"
    dictionary = create_dict_from_string(stmt)
    longest_value = find_longest_word(dictionary)
    
    print(dictionary)
    print(f'The longest word is {longest_value[0]} and is word {longest_value[1] + 1} within the string')

main()


#------------------------------------------------------------------------------------------------------------------------------
"""
Q2:

A) Write a function get_names that will read the gradedata.csv file, and return a list of all the rows where students have scored 100s. Points 3

B) Write a function write_names that will take the list of rows returned by get_names, and write to an output file ‘namelist.txt’ the full names, city and state into the file. This is a regular text file and not necessarily a csv file. For each student a line was written like this: (First student). Points 3 Libby Guzman of Dover, NH scored a 100

C) The main function should call the two functions, in turn to generate the desired output.

================ Sample output for Problem 2 ================

"""
#-------------------------------------
import csv
def get_names(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)

        score_100_names = []
        for row in reader:
            if row[6] == '100.0':
                score_100_names.append(row)
    
    return score_100_names

top_scorers = get_names('gradedata.csv')



#------------------------------------------------------------------------------------------------------------------------------
"""
Q3

A) Still staying with the same grade_data csv file. Write code, that will read the file, and calculate the average grades segmented by male and female. In addition, it should output the number of students in each category.

================ Sample output for Problem 3 ================

The average grade for the women is 82.7 The average grade for the men is 82.4 There were 1000 women and 1000 men in the data.

"""
#-------------------------------------

