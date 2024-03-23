# About this repository
- My Python program codes that are written when taking the Python programming course at Uppsala University.

# Python programs
## 1. calcuation_syllables.py
- A program that gives the mean and standard deviation of the number of syllables in a Swedish text. Syllables is approximated to the number of vowels in words.
- Command line in terminal: Text data are placed in the same dictionay as the Python file.
```
python3 calculation_syllabbles.py
```

## 2. Swedish_words_test.py
- A program that tests the user on Swedish words. It should be possible to run the program and pass in a .csv-file using sys.argv[1], in which commas separate English words and their Swedish translations. In this code, I uses color.csv file for testing.
- Command line in terminal: Text data are placed in the same dictionay as the Python file.
```
python3 Swedish_words_test.py color.csv
```

## 3. main.py, get_random_list.py, bubble_sort_recursive.py 
- Generate a list including 100 random numbers to start, and then increase the list size by 10 numbers. During generating the list, sort values using the Bubble sort algorithm.
- Measure the running time of Bubble sort and save the measurements in a file called bubble_times.csv with two columns, one for the time it took to sort the list and another for the data size.
- Command line in terminal: Text data are placed in the same dictionay as the Python file.
```
python3 main.py > bubble_times.csv
```

### 4. speech_rate_surprisal.py, file.csv
- A program to implement a method to investigate the inverse relation between speech rate and surprisal to work. (*Articulation rate is used in this program)
*The number of syllables per second, excluding pauses.
- Munich Automatic Segmentation System (MAUS) is used for obtaining the speech rate. https://clarin.phonetik.uni-muenchen.de/BASWebServices/interface/WebMAUSBasic
- Surprisal is the negative log of the probability of a word.
- For calculating surprisal, I generated two dictionaries one with bigrams and another with unigrams, along with their frequencies.
- Command line in terminal: Text data are placed in the same dictionay as the Python file.
```
python3 speech_rate_surprisal.py < corpus.txt
```
