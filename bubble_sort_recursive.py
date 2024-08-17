def bubble_sort(my_list, tim=0):    # tim is a number of times to control each element in the list.
    if tim != len(my_list)-1:       # len-1 for avoiding an error, out of range in the list due to n+1 in a comparision in if-condition. 
        for n in range(len(my_list)-1):
            if my_list[n] > my_list[n+1]:
                my_list[n], my_list[n+1] = my_list[n+1], my_list[n]     # Swap the values into each place
        tim += 1
        return bubble_sort(my_list, tim)
    else:
        return my_list

#print(bubble_sort([2, 3, 7, 6, 1])) -> Test example

