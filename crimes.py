from collections import Counter
import os
from termcolor import colored, cprint
import csv

BASE_DIR = '/Users/newuser/GIT/crime_data/data/'

def welcome():
    banner = colored(f'''
    ************************************   
                                           
        WELCOME TO CRIME DOG ver 7.8       
        WHAT WOULD YOU LIKE TO SEE?        
                                           
                                           
    ************************************   ''', 'yellow', attrs=['reverse', 'blink'])
                    
    print(banner)


def alligator(paths):  

    """
    this function loops over all csv files and finds things for the menu!
    """
    dataset = dict()
    for path in paths:                                                        #im looping over all csv files
        full_path = os.path.join(BASE_DIR, path)                              #then i turn all the data into list of strings
        with open(full_path, 'r') as f:                                       #now im a dict with lists with strings!
            reader = csv.DictReader(f)                                        
            yeardata = list()
            for row in reader:
                yeardata.append(row['Major Offense Type'])
            dataset[path] = yeardata

    #import pdb; pdb.set_trace()
    return dataset

def menu():
    user_selection = set()

    paths = os.listdir(BASE_DIR)
    options = {p.split('_')[-1].split('.')[0]: p for p in paths} 
    for year, file_n in options.items():
        print(year, file_n, sep='------------')
    
    while True:
        cmd = input('choose year above or type done  >? ')
        if cmd == 'done':
            break
        file_name = options[cmd]
        user_selection.add(file_name)

    dataset = alligator(user_selection)
    crimey = dict()
    for year in dataset:
        counter = Counter(dataset[year])
        c_most_common = counter.most_common(1)
        least = Counter(counter.items()).most_common()[-1][0]
        total_crime = sum(counter.values())
        crimey[year] = total_crime
        print(year, c_most_common, least)
    print(max(crimey.items(), key=lambda t: t[1]))    #items is a dict method that returns a list of tuples 
                                                      #lambda is an anon function

if __name__ == '__main__':
    welcome()
    menu()