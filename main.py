from get_random_list import get_random
from bubble_sort_recursive import bubble_sort
import time

def main():
    print("time", ",", "size")
    n = 100             # a number of elements for creating a random list of numbers at the beginning. 
    while n != 500:     # 500 is a number of time to create the list. It can be up to 1000 to run recursive functions in the algorithms.
        ran_lst = get_random(1000, n)   # 1000 is the maximum range number to pick numbers randomly.
        sort_start = time.time()        # start to measure time before starting sorting the created list of numbers.
        lst_sort = bubble_sort(ran_lst, tim=0)
        sort_stop = time.time()         # stop to measure time after sorting the list.
        sort_running_time = sort_stop - sort_start  # The time to take for sorting the list.
        print(sort_running_time, ",", len(ran_lst))
        n+= 10          # Adding 10 elements every time the list is created.         

if __name__ == "__main__":
    main()
