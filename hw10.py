import random
def bigram_count(sentence):
    '''
    Purpose: Creates a dictionary of for bigrams within a string given. The
        keys in the dictionary will be a word within the string and the values
        in the dictionary will be a list of the word or words (if key word
        repeats within the string).
    Input Parameter(s):
        sentence: the string wanted to be seperated into bigrams
    Return Value:
        A dictionary with the keys being all the words within the string
        (disregarding the last word in the string) and the values being a list
        of all the words that come right after the key word in the string.
    '''
    bigram_dict = {}
    bigram_split = sentence.split()
    for i in range(len(bigram_split)-1):
        if bigram_split[i] not in bigram_dict:
            bigram_dict[bigram_split[i]] = []
    for x in range(len(bigram_split)-1):
        bigram_dict[bigram_split[x]] += [bigram_split[x+1]]
    return bigram_dict

def random_sentence(bigram_counts, start_word, length):
    '''
    Purpose: Takes a bigram dictionary and creates a random sentence of a
        certain word length by using the starting word and choosing a
        random word within the value of the starting word key and then
        the randomly chosen word will be the new key looked at for the next
        word until the word length requested is reached.
    Input Parameter(s):
        bigram_counts: the bigram dictionary
        start_word: the word wanted to start the random sentence
        length: the amount of words wanted in the random sentence
    Return Value: The random sentence made by coorelating one word in
        the given dictionary to the next until the length is met. (if the
        value word is not a key word then the next word is the start_word)
    '''
    new_key = start_word
    sentence = new_key
    for i in range(length-1):
        if new_key not in bigram_counts.keys():
            new_key = start_word
            sentence = sentence+' '+new_key
        else:
            val_list = bigram_counts[new_key]
            index = random.choice(range(len(val_list)))
            val = val_list[index]
            sentence = sentence+' '+val
            new_key = val
    return sentence

def rand_sent_file(file, length):
    '''
    Purpose: Takes a file and runs bigram_count(sentence) to make a dictionary
        of bigrams of the txt file and then creates a random sentence by
        running the random_sentence(bigram_counts, start_word, length) function.
        The starting word is randomly chosen from the key words within the
        bigram dictionary.
    Input Parameter(s):
        file: the file wanted to be used to create a random sentence
        length: the word length of the random sentence
    Return Value: (Look at return value of the random_sentence function)
    '''
    file_read = open(file, 'r')
    file_bigram = bigram_count(file_read.read())
    bigram_list = []
    for i in file_bigram.keys():
        bigram_list.append(i)
    file_read.close()
    index = random.choice(range(len(bigram_list)))
    start = bigram_list[index]
    return random_sentence(file_bigram, start, length)
