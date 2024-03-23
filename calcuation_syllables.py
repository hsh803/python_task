import math

def get_lines(text_file):
    f = open(text_file)
    r = f.readlines()
    f.close()
    return r

def get_lexicon(word_file):
    f = open(word_file)
    r = f.read()
    w_lst = r.split()
    return w_lst

def get_text(text_file):
    text_lst = get_lines(text_file)
    text_word_lst = []
    for line in text_lst:
        split_w = line.split()
        for w in split_w:
            text_word_lst.append(w)
    return text_word_lst

def is_vowel(char):
    v = ["a", "e", "i", "o", "u", "ä", "å", "ö"]
    if char.lower() in v:
        return True
    else:
        return False
      
def get_vowel_count(word_str):
    v = []
    for i in word_str:
        v_control = is_vowel(i)
        if v_control == True:
            v.append(i)
    return len(v)
           
def get_word_vowels(lst_word):
    dic = {}
    for i in lst_word:
        i = i.lower()
        dic[i] = get_vowel_count(i)
    return dic

def get_token_vowels(lst_text, dic):
    lst = []
    for i in lst_text:
        i = i.lower().strip("\"\'.,!?")
        if i in dic:
            lst.append(dic.get(i))
    return lst #len(lst) = 264 (not found words in dic: Chomsky, sond, NLP-kursen, datalingvister, tokenisering)
      
def get_mean(int_lst):
    int_sum = 0 
    for i in int_lst:
        int_sum += i 
        avr = int_sum/len(int_lst)
    return avr #1.7803030303030303

def get_stadev(int_lst):
    n_lst = []
    for i in int_lst:
        avr = get_mean(int_lst)
        s = (i - avr)**2
        n_lst.append(s)
    result = math.sqrt(sum(n_lst)/(len(int_lst)-1))
    return result     

def main():
    result = get_stadev(get_token_vowels(get_text("swe-sentences.txt"), get_word_vowels(get_lexicon("sv-utf8.txt"))))
    return round(result,3)

print(main()) #1.0118265976524938

