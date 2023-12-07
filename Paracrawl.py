"""
Extract individual English words from paracrawl dataset to create vocab
Dataset size: 9 GB approx
Input (number of rows): 50,632,000 lines
Output (vocab => number of words): 4,400,347
"""
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from string import punctuation

# load the english stopwords from NLTK
stop_words = stopwords.words('english')
stop_words.extend(list(punctuation))

# file size - 9 GB approx
# read the file line by line to avoid memory error
fp = open("datasets/en-cs.txt", "r")

line_counter = 0
english_words = set()

for line in fp:
    line_counter += 1

    processed_line = line.split("\t")[0]
    processed_line = processed_line.replace("  ", " ").lower()
    words = word_tokenize(processed_line)

    for word in words:
        if word not in stop_words:
            english_words.add(word)

    if line_counter % 1000 == 0:
        print(f"Processed: {line_counter} lines")

# save the words in text file for future use
with open("features/english_words.txt", "w") as fp:
    fp.writelines([f"{word}\n" for word in english_words])
