
# ce e un string? de ce il folosim? ce e in spate?

var1 = "a"
var2 = "0076"
var3 = 19
var4 = 'string 4'

var5 = """ This is another type of string. its still a string. It's a multi-line string"""
msg = "LLM agents are agents usually process strings as tokens. It tokenizes them."
print(len(msg))
arr1 = [10, 20, 30, 40, 100]
#       0   1   2   3   4 ----> index
print(msg[-5])
print("token" in msg)
print(msg.count("token"))
print(msg.find("tok"))

#strings are immutable
#mutable = list1 =[ 1, 2, 3]
#list1[0] = 300 ---> primul element suporta modificare

print(msg.lower())
#split a string by separator
split_string = msg.split(" ")
print(split_string)
#join a list of strings with separator
print(" ".join(split_string))

#numaram substring-uri
print(msg.count("tok"))

with open("lesson_05_json_data.py", "r") as f:
    content = " ".join(f.readlines())
    print(content)
    print(f"File has {len(content)} characters")
    print(f"json shows up {content.lower().count('json')} times in our file")

#streaming
# f.readline()