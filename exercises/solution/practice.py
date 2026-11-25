# ****************************String************************
'''
1. Reverse a string without slicing
2. Count vowels
3. Check palindrome
4. Character frequency
5. Remove duplicate characters
6. Longest word in sentence
7. Extract digits only
8. Remove special characters
9. Convert to title case
10. Count words without split()

'''
def rev_str():
    a="rishikesh"
    b=""
    for i in range(len(a)-1, -1, -1):
        b=b+a[i]
    print(b)
# rev_str()

def c_vowel():
    a="rishikesh"
    b=0
    for i in a:
        if i in "aeiouAEIOU":
            b=b+1
    print(b)
# c_vowel()

def char_fre():
    a= "banana" 
    # Output: {'b':1, 'a':3, 'n':2}
    b={}
    for i in a:
        if i in b:
            b[i]=b[i]+1
        else:
            b[i]=1
    print(b)
# char_fre()

def remove_duplicate():
    a="aabbccddd"
    b=""
    for i in a:
        if i not in b:
            b=b+i
    print(b)
# remove_duplicate()

def longest_word():
    a="rishi infosys hydrabad gorakhpur274149"
    s=a.split(" ")
    print(s)
# longest_word()

def digit_only():
    s='gorakhpur274149'
    s1=""
    for i in s:
        if i in "0123456789":
            s1=s1+i
    print(s1)
# digit_only()

def title_case():
    a="rishi infosys hydrabad gorakhpur274149"
    print(a.title())
    print(a)
# title_case()

def no_special():
    a="qwertyu!@#$12345"
    b=""
    for i in a:
        if i.isalnum():
            b=b+i
    print(b)
# no_special() 


#******************************** List ***********************

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

def max_min():
    l=[10, 25, 5, 15, 30]
    #l = [5, 10, 15, 25, 30]
    max=min=l[0]
    for i in l[1:]:
        if i>max:
            max=i
        if i<min:
            min=i
    print(f"max: {max}, min: {min}")
# max_min()       




            






    


