from collections import defaultdict

d = {'a': 10}

print(d)
print(d['a'])

# d["this_doesnt_exist"]   <-  KeyError

'''
Default dictionary 
'''

d = defaultdict(lambda: 0)
d["correct"] = 100
print(d["correct"])
print(d['WRONG KEY!'])