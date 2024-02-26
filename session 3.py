# iterate over string backwards using while
text = "abcdefg"
i = -1
while i >= -7:
    print(text[i])
    i -= 1

text = "abcdefghi"
i = 0
while i < len(text):
    print(text[len(text)-1-i])
    i += 1

#string slice

base = "abcdefghijklmnopqrstuvwxyz"

print("here are some slices")
print(base[0:3])
print(base[0:5])
print(base[10:]) #all the way to the end
print(base[:10]) #all the way from the beginning
print(base[:]) # the whole string
print(base[::2]) # every other letter
print(base[5:15:3]) #ebery third letter from the 5th to the 15th
print(base[::-1]) #the whole string backwards



