'''
1️⃣ Count frequency of each character in a string

Input: "banana"
Output: {'b':1, 'a':3, 'n':2}

2️⃣ Find key with the highest value

Input:
data = {"a": 10, "b": 55, "c": 32}
Output: "b"

3️⃣ Merge two dictionaries manually (without update())

Input:
d1 = {"x":1}
d2 = {"y":2}

4️⃣ Reverse keys and values in a dictionary

Input: {"a":1, "b":2}
Output: {1:"a", 2:"b"}

5️⃣ Convert two lists into a dictionary

Input:
Keys → ["name","age","city"]
Values → ["Rishi", 27, "GKP"]

6️⃣ Remove all items with value = None

Input:
{"a":1, "b":None, "c":3, "d":None}
Output: {"a":1, "c":3}

7️⃣ Sort dictionary by values

Input: {"x":5, "y":1, "z":3}
Output sorted by value → [("y",1), ("z",3), ("x",5)]

8️⃣ Create dictionary of word counts from a sentence

Input: "python automation python engineer"
Output: {"python":2, "automation":1, "engineer":1}

9️⃣ Nested dictionary — access keys safely

Input:

emp = {
    "name": "Rishikesh",
    "salary": 50000,
    "details": {
        "city": "GKP",
        "pincode": 273153
    }
}


Print → city & pincode

🔟 Convert dictionary values list → flatten

Input:

d = {
    "a": [1,2],
    "b": [3,4],
    "c": [5]
}


Output: [1,2,3,4,5]

'''


# 1️⃣ Count frequency of each character
def char_frequency(s):
    freq = {}
    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    return freq


# 2️⃣ Find key with the highest value
def max_value_key(data):
    max_key = None
    max_value = float("-inf")

    for key in data:
        if data[key] > max_value:
            max_value = data[key]
            max_key = key
    return max_key


# 3️⃣ Merge two dictionaries manually
def merge_dicts(d1, d2):
    merged = {}

    for key in d1:
        merged[key] = d1[key]

    for key in d2:
        merged[key] = d2[key]

    return merged


# 4️⃣ Reverse keys and values
def reverse_dict(d):
    rev = {}
    for key in d:
        rev[d[key]] = key
    return rev


# 5️⃣ Convert two lists into a dictionary
def lists_to_dict(keys, values):
    result = {}
    for i in range(len(keys)):
        result[keys[i]] = values[i]
    return result


# 6️⃣ Remove all items with value = None
def remove_none_values(d):
    clean = {}
    for key in d:
        if d[key] is not None:
            clean[key] = d[key]
    return clean


# 7️⃣ Sort dictionary by values (basic)
def sort_dict_by_value(d):
    items = list(d.items())

    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i][1] > items[j][1]:
                items[i], items[j] = items[j], items[i]

    return items


# 8️⃣ Word count from a sentence
def word_count(sentence):
    words = sentence.split()
    count = {}

    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count


# 9️⃣ Safely access nested dictionary
def get_city_pincode(emp):
    city = None
    pincode = None

    if "details" in emp:
        if "city" in emp["details"]:
            city = emp["details"]["city"]
        if "pincode" in emp["details"]:
            pincode = emp["details"]["pincode"]

    return city, pincode


# 🔟 Flatten dictionary values list
def flatten_dict_values(d):
    flat = []
    for key in d:
        for val in d[key]:
            flat.append(val)
    return flat


# ==========================================
# FUNCTION CALLS (Testing)
# ==========================================

print("1️⃣", char_frequency("banana"))

data = {"a": 10, "b": 55, "c": 32}
print("2️⃣", max_value_key(data))

print("3️⃣", merge_dicts({"x": 1}, {"y": 2}))

print("4️⃣", reverse_dict({"a": 1, "b": 2}))

print("5️⃣", lists_to_dict(
    ["name", "age", "city"],
    ["Rishi", 27, "GKP"]
))

print("6️⃣", remove_none_values(
    {"a": 1, "b": None, "c": 3, "d": None}
))

print("7️⃣", sort_dict_by_value({"x": 5, "y": 1, "z": 3}))

print("8️⃣", word_count("python automation python engineer"))

emp = {
    "name": "Rishikesh",
    "salary": 50000,
    "details": {
        "city": "GKP",
        "pincode": 273153
    }
}
print("9️⃣", get_city_pincode(emp))

print("🔟", flatten_dict_values({
    "a": [1, 2],
    "b": [3, 4],
    "c": [5]
}))

# ==========================================
# END OF FILE
# ==========================================


