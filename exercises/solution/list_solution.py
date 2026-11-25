'''
List Practice Questions (Loop + List combined)

1️⃣ Find the largest and smallest number in a list (without max/min)

Example:
Input → [10, 25, 5, 99, 45]
Output → Largest = 99, Smallest = 5

2️⃣ Reverse a list without using reverse() or slicing

Example:
Input → [1,2,3,4]
Output → [4,3,2,1]

3️⃣ Remove duplicates from list (without using set)

Example:
Input → [1,2,2,3,4,4,5]
Output → [1,2,3,4,5]

4️⃣ Find the second largest number in a list

Example:
Input → [10, 30, 20, 50, 40]
Output → 40

5️⃣ Count frequency of each element using list + dict

Example:
Input → [1,2,2,3,3,3]
Output → {1:1, 2:2, 3:3}

6️⃣ Merge two lists index-wise

Example:
Input →
A = [1,2,3]
B = [4,5,6]
Output → [(1,4), (2,5), (3,6)]

7️⃣ Check if list is palindrome (same forward & backward)

Example:
Input → [1,2,3,2,1]
Output → True

8️⃣ Find common elements between two lists (without using set)

Example:
A = [1,2,3,4]
B = [3,4,5,6]
Output → [3,4]

9️⃣ Rotate list by n positions

Example:
Input → [1,2,3,4,5], rotate by 2
Output → [4,5,1,2,3]

🔟 Sort list without using sort() (Bubble Sort logic)

Example:
Input → [5,1,4,2,8]
Output → [1,2,4,5,8]


'''
#1. 
def max_min():
    l = [10, 25, 5, 99, 45]    
    min_val = max_val = l[0]
    for v in l[1:]:
        if v < min_val:
            min_val = v 
        if v > max_val:
            max_val = v

    print("Largest =", max_val, "Smallest =", min_val)

# max_min()  


'''
2️⃣ Reverse a list without using reverse() or slicing
Example:
Input → [1,2,3,4]
Output → [4,3,2,1]
'''
def reverse_():
    l=[1,2,3,4]
    l1=[]
    for i in range(len(l)-1, -1, -1):
        l1.append(l[i])
    print(l1)
# reverse_()


'''


3️⃣ Remove duplicates from list (without using set)

Example:
Input → [1,2,2,3,4,4,5]
Output → [1,2,3,4,5]
'''
l=[1,2,2,3,4,4,5]
l2=[]
for i in l:
    if i not in l2:
        l2.append(i)
print(l2)

    

'''
5️⃣ Count frequency of each element using list + dict
Example:
Input → [1,2,2,3,3,3]
Output → {1:1, 2:2, 3:3}
'''
l=[1,2,2,3,3,3]
d={}
for i in l:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1
print(d)



'''
4️⃣ Find the sorting  list

'''
def sort_():
    l = [30, 10, 20, 50, 40]
    n = len(l) #5
    
    # Bubble sort: compare adjacent elements
    
    '''
    | Pass (i) | j chalega | Last sorted |
    | -------- | --------- | ----------- |
    | 0        | 0–3:0123  | 1 element   |
    | 1        | 0–2       | 2 elements  |
    | 2        | 0–1       | 3 elements  |
    | 3        | 0         | 4 elements  |

    '''
    for i in range(n):
        for j in range(n - 1 - i): # n-1=Last element ka pair nahi hota
            if l[j] > l[j + 1]:
                # Swap
                temp=l[j ]
                l[j] = l[j + 1] 
                l[j + 1]= temp    
    print(l)

sort_()



"""
Example:
A = [1,2,3,4, 4]
B = [3,4,5, 4, 6]
Output → [3,4]"""

A = [1,2,3,4]
B = [3,4,5,6]
C=[]
for i in A:
    for j in B:
        if i==j:
            C.append(i)
print(C)


