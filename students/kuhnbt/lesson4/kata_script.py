# My book is Dante's inferno, the first of the three books of the divine comedy
import requests
import string
import random
url = 'https://www.gutenberg.org/files/1001/1001-h/1001-h.htm'

full_text = requests.get(url).text

start = 'Inferno: Canto I'
end = 'End of the Project Gutenberg EBook'

full_text = full_text[full_text.find(start):full_text.find(end)]

full_text = full_text.replace('\n',' ').replace('\r',' ')
for s in string.punctuation:
    full_text = full_text.replace(s, '')

full_text = full_text.split()

def generate_dict(txt):
    #find other dict methd to do this
    d = {}
    for idx in range(len(txt)-2):
        wd_one, wd_two, wd_three = txt[idx], txt[idx+1], txt[idx+2]
        if d.get((wd_one, wd_two)):
            d[(wd_one, wd_two)].append(wd_three)
        else:
            d[(wd_one, wd_two)] = [wd_three]
    return d

def generate_text(trigrams_dict, length):
    """Generate text with given number of words using trigrams_dict"""
    start_loc = random.randint(0, len(trigrams_dict))
    start_key = list(trigrams_dict.keys())[start_loc]
    results = [start_key[0], start_key[1]]
    for _ in range(length):
        next_word_choices = trigrams_dict[start_key]
        next_word = next_word_choices[random.randint(0, len(next_word_choices))]
        start_key = (start_key[1], next_word)
        results.append(next_word)
    return results