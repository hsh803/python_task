import sys
from nltk import word_tokenize
from collections import defaultdict
import random

class AutoCorrect:
    def __init__(self, word_list, alpha): # Constructor or method. word_list and alpha are instance attributes
        self.w_l = word_list # Each time object is created. method is called.
        self.a = alpha
        self.w_set = set()
    def insertion(self, word):
        w_lst = []
        for c in range(len(word)+1):
            for s in self.a:
                w_lst.append(word[:c] + s + word[c:])
        self.combine(w_lst)

    def deletion(self, word):
        w_lst = []
        for c in range(len(word)):
            w_lst.append(word[:c] + word[c+1:])
        self.combine(w_lst)
    
    def substitution(self, word):
        w_lst = []
        for c in range(len(word)):
            for s in self.a:
                w_lst.append(word[:c] + s + word[c+1:])
        self.combine(w_lst)
    
    def swapping(self, word):
        w_lst = []
        w = list(word)
        for c in range(len(word)-1):
            w[c], w[c+1] = w[c+1], w[c]
            w_lst.append(''.join(w))
            w = list(word)
        self.combine(w_lst)

    def combine(self, w_lst):
        for w in w_lst:
            if w in self.w_l: # complete bring the lexicon file
                self.w_set.add(w)
        return self.w_set

def my_dic(file):
    dic = defaultdict(int)
    with open(file, 'r') as f:
        tokens = word_tokenize(f.read())
    for w in range(len(tokens)-1):
        bi_str = (tokens[w].strip(" :;.,!?-_\'\""), tokens[w+1].strip(" :;.,!?-_\'\""))
        if bi_str in dic:
            dic[bi_str] += 1
        else:
            dic[bi_str] = 1

    new_dic = sorted(dic.items(),key=lambda x:x[1],reverse=True)
    return new_dic

def type_input(i, text, lex, dic):
    if i in lex:
        text.append(i)
        print("Your text is so far: " + " ".join(text))
        type_input_yes(i, text, lex, dic)
    if not i in lex:
        type_input_no(i, text, lex, dic)
    
def type_input_yes(i, text, lex, dic):
    c = 0
    select = []
    print("Either select a word below: ")
    for bi in dic:
        if text[len(text)-1] == bi[0][0]:
            select.append(bi[0][1])
    if len(select) < 3:
        l = len(select)
        while l < 3:
            r = random.randint(0, len(lex)-1)
            select.append(lex[r])
            l += 1
    
    for index, value in enumerate(select):
        if c == 3:
            break
        else:
            print(index, ":", value)
            c += 1
        
    print("OR type something: ")
    i = input()
    
    if i in ['0', '1', '2']:
        type_input(select[int(i)], text, lex, dic)
    else:
        type_input(i, text, lex, dic)
 
def type_input_no(i, text, lex, dic):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    my_obj = AutoCorrect(lex, alpha)
    my_obj.insertion(i)
    my_obj.deletion(i)
    my_obj.substitution(i)
    my_obj.swapping(i)
    
    if my_obj.w_set:
        print("Did you mean word(s) below? Then select a word.")
        select = []
        c  = 0
        for w in my_obj.w_set:
            select.append(w)

        if len(select) < 3:
            l = len(select)
            while l < 3:
                r = random.randint(0, len(lex)-1)
                select.append(lex[r])
                l += 1

        for index, value in enumerate(select):
            if c == 3:
                break
            else:
                print(index, ":", value)
                c += 1

        print("OR type something: ")
        i = input()

        if i in ['0', '1', '2']:
            type_input(select[int(i)], text, lex, dic)
        else:
            type_input(i, text, lex, dic)

    else:
        print("That word is not in the lexicon. Here are random suggestions for the next word:")
        select = []
        c = 0
        while c < 3:
            r = random.randint(0, len(lex)-1)
            select.append(lex[r])
            c += 1
        for index, value in enumerate(select):
            print(index, ":", value)
        print("OR type something: ")
        i = input()
    
        if i in ['0', '1', '2']:
            type_input(select[int(i)], text, lex, dic)
        else:
            type_input(i, text, lex, dic)


if __name__ == "__main__":
    print("Type in a word: ")
    i = input()
    text = []
    f = open(sys.argv[1], 'r') # usenglish-utf8.txt
    lex = [x.strip("\n") for x in f.readlines()]
    dic_function = my_dic(sys.argv[2]) # UNv1.0.testset.en 
    type_input(i, text, lex, dic_function)

