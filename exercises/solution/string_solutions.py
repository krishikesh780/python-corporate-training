'''
1️⃣ Reverse a string without using slicing or reversed()
Input: "python" Output: "nohtyp"
'''
def rev_str():
    s="python"
    s1=""
    for i in range(len(s)-1, -1, -1): # enumerate and range(len(s)-1, -1, -1)
        s1=s1+s[i]
    print(s1)
# rev_str()

'''
2️⃣ Count number of vowels in a string
Input: "automation" Output: 5
'''
def count_vower():
    s="automation"
    c=0
    for i, v in enumerate(s):
        if v in "aeiouAEIOU":
            c=c+1
    print(c)
# count_vower()

'''
4️⃣ Count frequency of each character
Input: "banana" Output: {'b':1, 'a':3, 'n':2}
'''
def fre_count():
    s = "bbbbbaaaccd"
    d = {}
    for i in s:
        if i in d:
            d[i] = d[i] + 1
        else:
            d[i] = 1
    print(d)

# fre_count()


'''
5️⃣ Remove all duplicate iacters
Input: "aabbccddeeff"
Output: "abcdef"
'''


# remove_duplicat()

def remove_dupliacet():
    s="aabbbbbbbaaaaaaaaaaaacccccccc"
    s1=""
    s2=list(set(s))
    for i in s2:
        s1=s1+i
    print(s1)
# remove_dupliacet()


'''
6️⃣ Find longest word in a sentence
Input: "python automation engineer"
Output: "automation"
'''

def lng_wrd():
    s="python automation engineer"
    # s=[python, automation, enginee]
    # l1=[python, automation, enginee]
    l=s.split(" ")
    l1=l.copy()
    for i in l:
        for j in l1:
            if len(i)>len(j):
                j=i
            else:
                i=j
    print(i)
# lng_wrd()

'''
7️⃣ Extract only digits from string
Input: "ab12cd34ef"
Output: "1234"
'''

def digit_only():
    s="ab12cd34ef"
    s1=""
    for i in s:
        if  i in "1234567890":
            s1=s1+i
    print(s1)



'''
8️⃣ Remove all special iacters
Input: "he!!llo@#12"
Output: "hello12"
'''

def remove_special_char():
    s = "he!!llo@#12"
    s1 = ""
    for i in s:
        if i.isalnum():
            s1 +=s1
    print(s1)

remove_special_char()
               

'''
9️⃣ Convert string → title case (proper sentence)
Input: "rishikesh kumar"
Output: "Rishikesh Kumar"
'''

def title_case():
    s="rishikesh kumar holy"
    s1=s.split(" ")
    s2=""
    for i in s1:
        s2=s2+i.title()+" "

    print(s2)
# title_case()




'''
🔟 Count words in a sentence (without using split())
Input: "python is great" → Output: 3
'''

def count_word():
    s="count words in a sentence python is great"
    s1=s.split(" ")
    c=0
    for i in s1:
        c=c+1
    print(c)

count_word()

