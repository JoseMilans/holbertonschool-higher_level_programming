#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_sum = 0
    if my_list:
        uniq_set = set(my_list)
        for num in uniq_set:
            uniq_sum += num
    return uniq_sum
