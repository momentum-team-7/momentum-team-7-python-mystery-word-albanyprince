STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

# 1. Open file and save it to a variable - jupyter 09
# 2. remove punctuation - jupyter 07

# 3. normalize all words to lowercase
def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    with open(file) as open_file:
        lyrics = open_file.read().lower()
        words_list = {}
    # print('read file', read_file)   
        rm_punct = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        no_punct = ""
        for punct in lyrics:
            if punct not in rm_punct:
                no_punct = no_punct + punct
        print(no_punct)        
        
#  4. remove "stop words" -- words used so frequently they are ignored
        lyrics_list = lyrics.split(' ')
        lyrics_list_copy = lyrics_list.copy 
        for word in lyrics_list:
            if word in STOP_WORDS:
                lyrics_list_copy.remove(word)
            elif word not in words_list: 
                word_count = lyrics_list_copy.count(word)
                words_list[word] = word_count
        print(words_list)          


#  - check each word to see if it is equal to one of the stop words / if it is in the list of the stop words
#  - conditional with if
# 5. go through the file word by word and keep a count of how often each word is used
# use a dictionary to store the keys > words, values > occurances



if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
