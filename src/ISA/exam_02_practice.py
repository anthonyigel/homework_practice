#------------------------------------------------------------------------------------------------------------------------------
"""
Q1:
Read the csv file statePopulation.csv. Write the first five rows that have a population less than 5Million into a list st_list.  (Use a csv.reader as opposed to csv.DictReader).

================ Sample output for Problem 1 ================

```[['AK, Alaska', '63.588753', '-154.493062', 'Juneau', '724357'], 
['AL, Alabama', '32.318231', '-86.902298', 'Montgomery', '4934190'], 
['AR, Arkansas', '35.20105', '-91.831833', 'Little Rock', '3033950'],
['CT, Connecticut', '41.603221', '-73.087749', 'Hartford', '3552820'], 
['DC, District of Columbia', '38.905985', '-77.033418', 'Washington', '714153']]```
"""

#-------------------------------------
import csv
_filename = 'statePopulation.csv'

def get_top_five(filename):
    with open(filename, 'r', newline = '') as file:
        statereader = csv.reader(file)
        header = next(statereader, None)

        pop_indx = header.index('Population')
        st_list = []
        count = 0
        for population in statereader:
            if int(population[pop_indx]) < 5000000:
                st_list.append(population)
                count +=1
            if count == 5: 
                break
        return(st_list)

get_top_five(filename = _filename)


### ALTERNATE
#-------------------------------------
def read_data(filename):
    
    with open(filename, 'r', newline = '') as file:
        statereader = csv.reader(file)
        header = next(statereader, None)
        
        
        state_list = []
        for row in statereader:
            state_list.append(row)

    return state_list, header
    
state_df, state_header = read_data(filename=_filename)

#-------------------------------------
def get_top_five(df, indx):
    st_list = []
    count = 0
    for row in df:
        if int(row[indx]) < 5000000:
            st_list.append(row)
            count +=1
        if count == 5: 
            break
    return(st_list)

get_top_five(state_df, header.index('Population'))

#------------------------------------------------------------------------------------------------------------------------------
"""
Q2:
Write a function get_state_population. It should take a row, and return a tuple (stname,stcode,population). For simplicity assume you know the indexes of the fields, we are interested in.

================ Sample output for Problem 2 ================
Interim Check of Output for Q2 (Not asked for)
```
('Alaska','AK', 724357)
```
"""
#-------------------------------------
def get_state_population(st_list):
    state = st_list[0].split(',')
    stname = state[1].strip()
    stcode =  state[0].strip()
    population = st_list[4]
    return(stname,stcode,population)

top5_rows = get_top_five(filename = _filename)
get_state_population(top5_rows[0])


#------------------------------------------------------------------------------------------------------------------------------
"""
Q3:
Using the get_state_population, and state_list, use a combination of map, filter or list comprehension to generate a list state_population of tuples with stname, population. 
(PS: I first did a map to get all the tuples, then used a list comprehension to select the two fields needed from the tuple).

================ Sample output for Problem 3 ================
```
[('Alaska', 724357), ('Alabama', 4934190), ('Arkansas', 3033950), ('Connecticut', 3552820), ('District of Columbia', 714153)]
```
"""
#-------------------------------------
