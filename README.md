# About this repository
- My Python program codes that are written when taking the Python programming course at Uppsala University.

# Python programs
## 1. Calcuate syllables
- A program that gives the mean and standard deviation of the number of syllables in a Swedish text. Syllables is approximated to the number of vowels in words.
- Command line in terminal: Text and lexicon data files are placed in the same dictionay as the Python file. (Text: swe-sentences.txt, Lexicon: sv-utf8.txt)
```
python3 calculation_syllabbles.py
```

## 2. Swedish words test
- A program that tests the user on Swedish words. It should be possible to run the program and pass in a .csv-file using sys.argv[1], in which commas separate English words and their Swedish translations. In this code, I uses color.csv file for testing.
- Command line in terminal: Test file (color.csv) are placed in the same dictionay as Swedish_words_test.py.
```
python3 Swedish_words_test.py color.csv
```

## 3. Recursive sort function by listing random numbers
- Generate a list including 100 random numbers to start, and then increase the list size by 10 numbers. During generating the list, sort values using the Bubble sort algorithm.
- Measure the running time of Bubble sort and save the measurements in a file called bubble_times.csv with two columns, one for the time it took to sort the list and another for the data size.
- Command line in terminal: Python files (get_random_list.py, bubble_sort_recursive.py) are placed in the same dictionay as main.py. 
```
python3 main.py > bubble_times.csv
```

### 4. Speech rate and word surprisal
- A program to implement a method to investigate the inverse relation between speech rate and surprisal to work. (*Articulation rate is used in this program)
*Articulation rate: The number of syllables per second, excluding pauses.
- Munich Automatic Segmentation System (MAUS) is used for obtaining the speech rate of the audio file (file.wav).
  (https://clarin.phonetik.uni-muenchen.de/BASWebServices/interface/WebMAUSBasic)
- Surprisal is the negative log of the probability of a word.
- For calculating surprisal I generated two dictionaries  by using a corpus data. One with bigrams and another with unigrams along with their frequencies.
- The python code generate duration_sursprisal.csv for calculation at the end.
- Command line in terminal: The corpus(corpus.txt) and csv file (file.csv) are placed in the same dictionay as speech_rate_surprisal.py.
```
python3 speech_rate_surprisal.py < corpus.txt
```

### 5. Auto spell-correction
- This program generates a message (phrase or sentence) by correcting typed words successively.
- There are four methods (insertion, deletion, substitution, and swapping) in a class to correct the misspelled words.
- Using a lexicon file (usenglish-utf8.txt) and a corpus file (UNv1.0.testset.en) to create seperate bigram dictionay.
- Command line in terminal: The corpus(UNv1.0.testset.en) and lexicon file (usenglish-utf8.txt) are placed in the same dictionay as speech_rate_surprisal.py.
```
python3 auto_correct.py usenglish-utf8.txt UNv1.0.testset.en
```

### 6. Generate anagrams
- A program that finds anagrams for a word typed by the user.
- The program uses a lexicon file (sv-utf8.txt) to generate anagrams and a bubble sort algorithm.
- Command line in terminal: The lexicon file (sv-utf8.txt) is placed in the same dictionay as anagram_1.py.
```
python3 anagram_1.py sv-utf8.txt
``` 
