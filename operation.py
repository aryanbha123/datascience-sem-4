import random
import math
def findLen(ls):
    i = 0
    for j in ls:
        i+=1
    return i

def custom_root(num):
    for i in range(0,num):
        if(i ** 2 == num):
            return i
    return -1

def root(num):
    return math.sqrt(num)

def sort(list):
    for i in range(0,len(list)):
        for j in range(0, len(list)):
            if(list[i] > list[j]):
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
    return list

def shuffle(list):
    n = len(list)
    j = 0
    while(j < n):
        rand = random.randint(j,n-1)
        temp = list[j]
        list[j] = list[rand]
        list[rand] = temp
        j+=1
    return list

list = [164, 167.3 , 170 , 174.2 , 178 , 180,  186]

print(list)
list = shuffle(list)

N = findLen(list)
mean = 0
mediam = -1
mode = -1
sd = -1
variance = -1

# mean
for i in list:
    mean += i
mean /= len(list)


# sorting /  median
list = sort(list)
if(len(list) % 2 == 0):
    median = (list[int(N/2) - 1] + list[int(N/2)])/2
else:
    median = list[int(N/2)]


# mode
map = {}
for i in list:
    map[i] = 0
for j in list:
    map[j] += 1

maxi = [-1,-1]
for j in map:
    if(map[j] > maxi[1]):
        maxi = [j,map[j]]

print(mean)
print(median)
if(maxi[1] == 1):
    print("No Mode all are distinct")
else:
    print(f"Mode {maxi[0]} appearing {maxi[1]}")


"SD & VARIANCE"
sum = 0
for xi in list:
    sum += (xi - mean) ** 2
variance = sum/N
sd = root(sum / N)

print("Standard Deviation " , sd)
print("Variance  " , variance)


