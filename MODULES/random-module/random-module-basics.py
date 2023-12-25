import random

print(random.randint(0, 100))
#random.seed(101)
#print(random.randint(0,101))
#print(random.randint(0,101))
#print(random.randint(0,101))
#print(random.randint(0,101))
print("\n")

print("List and picking random value from it")
mylist = list(range(0,20))
print(mylist)
print(random.choice(mylist))

print("\nSAMPLE WITH REPLACEMENT") 
print(random.choices(population=mylist, k=10))

print("\nSAMPLE WITHOUT REPLACEMENT")
random.sample(population=mylist, k=10)

print("\nList before shuffling it:")
print(mylist)
print("\nList after shuffling it (It is permanently changed)")
random.shuffle(mylist)
print(mylist)

print("\nProbability distributions (float numbers with high precision, every number has the same % chances of getting picked)")
random.uniform(a=0, b=100)

print("\nNormal or gaussian distribution")
random.gauss(mu=0, sigma=1)