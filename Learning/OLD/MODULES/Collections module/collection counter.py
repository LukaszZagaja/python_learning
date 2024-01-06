from collections import Counter

my_list = [1,1,1,1,2,2,2,3,3,3,3,3,3,3]
print(Counter(my_list))

mylist = ['a', 'a', 'a', 'a', 10, 10, 10]
print(Counter(mylist))
print(Counter("asdasdasddqwadsqw"))

print("\n\n")

sentence = "How many times does each word come in this sentence. Not every word comes twice"
print(Counter(sentence))
print(Counter(sentence.lower().split()))

print("\n\n")

letters = 'aaaaaaaaaaaabbbbbbbbbbbbbcccccccddddddddddddd'
c = Counter(letters)
print(c)
print(c.most_common(2))
print(list(c))

