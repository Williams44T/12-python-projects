# a few different methods to concatenate strings:
name = "Travis"
print("my name is " + name)
print("my name is {}".format(name))
print(f"my name is {name}")

def madlib():
    noun1 = input("Noun: ")
    verb1 = input("Verb: ")
    verb2 = input("Verb: ")
    adj1 = input("Adjective: ")
    adverb1 = input("Adverb: ")
    place = input("Place: ")
    name = input("Name: ")
    body_part = input("body_part: ")

    madlib = f"The first thing I do every morning is {verb1}. It's a small \
thing, but it makes me extremely {adj1}. After that I grab my \
{noun1} before I head to {place}. I always say hi to {name}, but {adverb1} \
I want to {verb2} they're {bodypart}!"

    print(madlib)