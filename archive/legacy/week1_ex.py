"""
. Create a list of marks [45, 67, 89, 34, 90]. Print average and highest marks.
2. Append a new mark to the list and remove one mark.
3. Slice the list to print the first 3 marks.
4. Create a list of squares using list comprehension.
5. Check if an element exists in a list.
6. Interchange first and last elements in a list.
7. Swap two elements in a list (user-defined positions).
8. Count occurrences of a specific number in a list.
9. Count frequency of all elements in a list.
10. Find the smallest element in a list.
11. Find the second largest element in a list.
12. Print only even numbers from a list.
13. Count total even and odd numbers in a list.
14. Print only positive numbers from a list.
15. Find duplicate elements in a list.
16. Remove empty lists/tuples from a nested list.
17. Merge two lists into a list of dictionaries.
18. Find elements present in one list but not in another.

"""


def avg1():
    l=[45, 67, 89, 34, 90]
    # s=0
    # n=len(l)
    # for i in l:
    #     s+=i
    # avg=s/n
    # print(avg)
    l.sort()
    
    print(l[-1])  
    print(l)      
    # return avg
avg1()









