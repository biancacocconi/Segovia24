# Iterate over a string backward using while
text = "abcdefghijkl"
i = 0
while i < len(text):
    print(text[len(text)-1-i])
    i += 1




def to_lowercase(input):
    return input.lower()

name = "Gabriela Senan"
print(f"{to_lowercase(name)} thinks she's funny.")




template = "Today is %s"
print(template % "Tuesday")

# Tuple
template = "%s I have seen %d %s."
print(template % ("Today", 3, "dogs"))
print(template % ("On Monday", 7, "cats"))


base = "abcdefghijklmnopqrstuvwxyz"

print("here are some slices")
print(base[0:3])
print(base[0:5])
print(base[10:]) # From position 10 to the end.
print(base[:10]) # From the beginning to position 10 (excluding 10).
print(base[:]) # The whole string -> not really a slice.
print(base[::2]) # Every other letter.
print(base[5:15:3]) # Every third letter from the 5th to 15th.
print(base[::-1]) # The whole string backwards.



hi = "Hello world!"

# List Methods
print(dir(hi))

# Get a short description of a method.
print(help(hi.lower))

# Some more useful methods.
s = "hello world my name is John"
print(s.capitalize())
print(s.center(40))
print(s.count(" "))
print(s.replace(" ", "!!"))
print(s.split())

#CLASS EXAMPLE
text = "abcdefg"
print(dir(text))
help(text.isidentifier)
print(text.isidentifier()) # Is abcdefg a valid identifier?
print("1234".isidentifier()) # Is 1234 a valid identifier?
print("anananananananana".count("ana"))
print("anananananananana".replace("ana", "banana"))
print("anananananananana".find("ana", 1))
print("bbbabbbbbabbbbbabbabb".split("a"))
print("this is a sentence and i want the words".split(" "))
sentence = "Hello, kind-sir; how may! I be of service today?"
punctuation = ",-;?!"

# Sanitize the sentence.
for p in punctuation:
    sentence = sentence.replace(p, " ") # Replace the punctuation with nothing.
print(sentence)
sentence = sentence.replace("  ", " ") # Replace double spaces with single spaces.

# Split the sentence into words.
words = sentence.split(" ")
print(words)

text = "cat"
print(text.upper())
print(text)

name = "John"
second_name = "Bob"
print(f"Hi, {name} how are you? My name is {second_name}")
name = "Jane"
second_name = "Mary"
print(f"Hi, {name} how are you? My name is {second_name}")




# Indexing
hi = "Hello"
print(hi[1])
print(hi[-1])

# Addition
bye = "Bye"
print(hi+bye)
print(hi + " " + bye)

# Multiplication
print(3 * "abc")
bye = hi * 4
print(bye)

#Length
hi = "Hello!"
print(len(hi))

# For
str = "Hello world!"
print(str[1:3])
print(str[:4])
print(str[4:])
print(str[::3])
print(str[::-1])

# Comparison
hi = "banana"
print(hi == "banana")
print(hi == "Banana")
print(hi < "Banana")
print(hi > "bana")

# In
print("ba" in hi)
print("baN" in hi)
