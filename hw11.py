import os
def palindrome(phrase):
    '''
    Purpose: Identifies if the phrase inputted is a palindrome (can be
        written forwards or backwards and the phrase will be the same)
    Input Parameter(s):
        phrase: the string wanted to be tested to see if it's a palindrome
    Return Value: True if the phrase is a palindrome and False if not.
    '''
    if len(phrase) <= 1:
        return True
    else:
        if phrase[0] == ' ':
            phrase = phrase[1:]
        if phrase[-1] == ' ':
            phrase = phrase[:-1]
        if phrase[0] == phrase[-1]:
            return palindrome(phrase[1:-1])
        else:
            return False

def collatz(integer):
    '''
    Purpose: Uses the collatz idea to get a select integer to the number
        1. If the integer is odd then it is multiplied by three and added
        1. If the integer is even then it gets divided by 2. This repeats
        until the integer becomes 1.
    Input Parameter(s):
        integer: the initial integer wanted to change to 1.
    Return Value: A list of all the numbers that the collatz program went
    through including the initial integer and 1.
    '''
    if integer == 1:
        return [1]
    elif integer%2 != 0:
        return [integer]+collatz(integer*3+1)
    else:
        return [integer]+collatz(integer//2)

def count_e_vs_t(path):
    '''
    Purpose: Looks at the files within the folder selected and finds the
        difference between the amount of t's and e's within the files
        within the folder selected.
    Input Parameter(s):
        path: the folder selected to analyze all the files within the folder
    Return Value: The difference between the collective amount of t's and e's
        found in the files within the folder.
    '''
    count = 0
    for file in os.listdir(path):
        if os.path.isfile(path+'/'+file):
            fp = open(path+'/'+file)  #This is a file, print out the path
            read = fp.read()
            low = read.lower()
            count += low.count('e')
            count -= low.count('t')
            fp.close()
        else:
            count += count_e_vs_t(path+'/'+file)  #Go into a subdirectory
    return count
