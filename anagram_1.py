import sys
from collections import defaultdict

class AnagramFinder:
    def __init__(self, path):
        self.path = path
        self.lexicon = self.load_lexicon()
        self.word_sorted = self.get_dict()
    
    def load_lexicon(self):
        f = open(self.path, 'r')
        self.lexicon = [w.strip("\n") for w in f.readlines()]
        return self.lexicon

    def get_dict(self):
        my_dic = {}        
        for i in self.lexicon:
            x = ''.join(self.bubble_sort([*i], tim=0))
            if x in my_dic:
                my_dic[x] += [i]
            else:
                my_dic[x] = [i]
        return my_dic

    def bubble_sort(self, my_str, tim):
        if tim != len(my_str)-1:
            for n in range(len(my_str)-1):
                if my_str[n] > my_str[n+1]:
                    my_str[n], my_str[n+1] = my_str[n+1], my_str[n]
            tim += 1
            return self.bubble_sort(my_str, tim)
        else:
            return my_str

    def run(self):
        i = str(input("Which word? "))
        x = ''.join(sorted(i))
        if x in self.word_sorted and len(self.word_sorted[x]) != 1:
            for w in self.word_sorted[x]:
                if w != i:
                    print(w)
        else:
            print("There are no anagrams for " + "'" + i + "'.")

        j = input("Again (y/n) ")
        
        while j == "y" or "n":
            if j == "y":
                return self.run()
            elif j == "n":
                print("Thanks for using the program.")
                break
            else:
                j = input("Again (y/n) ")
            
            

def main():
    finder = AnagramFinder(sys.argv[1])
    finder.run()

if __name__ == "__main__":    
    main()
