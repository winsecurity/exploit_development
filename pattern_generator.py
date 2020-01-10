import random


data = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',\
    'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',\
        '1','2','3','4','5','6','7','8','9','0']


length = int(input("enter length of the pattern size "))

pattern = ''

for i in range(length):
    pattern += data[random.randint(0,61)]


#print("pattern generated")
print(pattern)

item = input("enter string to find offset ")

#index1 = pattern.find(item)
indexes = [] 

item_length = len(item)

for i in range(0,len(pattern),item_length):
    temp = pattern[i:i+item_length]
    if temp == item:
        indexes.append(i)

for every in indexes:
    print(every)


