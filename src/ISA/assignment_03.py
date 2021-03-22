"""
Please read the entire specification first and understand what is being asked. 

1. The input string is ‘Two pounds of plain flour, mixed with three pounds of self raising flour and six ounces of butter’ 
2. Write a function find_all with two  input arguments - the containing string, and string to search for.  It should return a list with the position of all the occurrences of the searched string within the containing string. (3 points) Hint: Remember find returns -1 when it does not find the string The function should be general, and work on any string and search string. It should  not count on the fact that there are only two instances of flour within the above given input string.
3. Within the function main() 

    a. Use the find_all  to get the occurrences of flour in this input string and Report their position within the string 1 point 
    
    b. Extract the text between the two instances of flour 1 point 

    c. Use two print statements with format strings within print to output (a) and (b) (No need for a format string here)  in two separate lines (1 point) d. Write the output to a file (assign3_2.txt) and turn in the file (2 points) Make sure you use a With construct to open and close the file

"""

#-------------------------------------
input_str = 'Two pounds of plain flour, mixed with three pounds of self raising flour and six ounces of butter'
def find_all(search_str, target_str):
    start = 0
    while True:
        start = search_str.find(target_str, start)
        if start == -1: 
            return
        yield start
        # start += len(sub) # use start += 1 to find overlapping matches
        start += 1

list(find_all(search_str=input_str, target_str='flour'))

#-------------------------------------
def find_all2(search_str, target_str):
    start_position = 0
    position_ls = []
    while start_position <= len(search_str):
        start_position = search_str.find(target_str, start_position)
        
        if start_position == -1:
            return position_ls
        else:
            position_ls.append(start_position)
            start_position += 1
    
    return position_ls
        
x = find_all2(search_str = input_str, target_str = 'flour')
print(x)

#-------------------------------------
def find_between(search_str, first, last ):
    try:
        start = search_str.index( first ) + len( first )
        end = search_str.index( last, start )
        return search_str[start:end]
    except ValueError:
        return ""
    
find_between(search_str=input_str, first='flour', last='flour')
