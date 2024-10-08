
###1 Introduction to Sets
def average(arr):
    distinct_heights = set(arr)

    avg_height = sum(distinct_heights) / len(distinct_heights)
    return round(avg_height, 3)



###2 No Idea!
n, m = map(int, input().split())  
array = list(map(int, input().split())) 
A = set(map(int, input().split()))  
B = set(map(int, input().split()))  

happiness = 0
for i in array:
    if i in A:
        happiness += 1
    elif i in B:
        happiness -= 1

print(happiness)


###3 Symmetric Difference
if __name__ == '__main__':
    m = int(input())
    set_m = set(map(int, input().split()))

    n = int(input())
    set_n = set(map(int, input().split()))

    symmetric_difference = set_m.symmetric_difference(set_n)

    for value in sorted(symmetric_difference):
        print(value)


###4 Set .add()

stamps = set()

n = int(input())

for _ in range(n):
    country = input().strip()
    stamps.add(country)

print(len(stamps))



###5 Set .union() Operation
n = int(input())
english_subscribers = set(map(int, input().split()))  
b = int(input())
french_subscribers = set(map(int, input().split())) 
at_least_one_subscription = english_subscribers.union(french_subscribers)
print(len(at_least_one_subscription))



###6 Set .intersection() Operation
n = int(input())
e = set(map(int, input().split()))  
b = int(input())
f = set(map(int, input().split())) 
p = e.intersection(f)
print(len(p))


###7 Set .difference() Operation
a = int(input())
e = set(map(int, input().split()))  
b = int(input())
f = set(map(int, input().split())) 
p = e.difference(f)
print(len(p))



###8 Set .symmetric_difference() Operation
n = int(input())
e = set(map(int, input().split()))  
b = int(input())
f = set(map(int, input().split())) 
p = e.symmetric_difference(f)
print(len(p))



###9 Set Mutations
num_elements_A = int(input()) 
A = set(map(int, input().split()))
N = int(input())
for _ in range(N):
    operation = input().split()[0]  
    other_set = set(map(int, input().split()))  
    
    if operation == "update":
        A.update(other_set)
    elif operation == "intersection_update":
        A.intersection_update(other_set)
    elif operation == "difference_update":
        A.difference_update(other_set)
    elif operation == "symmetric_difference_update":
        A.symmetric_difference_update(other_set)
print(sum(A))



###10 The Captain's Room
from collections import Counter

K = int(input())

room_numbers = list(map(int, input().split()))


room_count = Counter(room_numbers)

for room, count in room_count.items():
    if count == 1:
        print(room)
        break


###11 Check Subset
T = int(input())

for _ in range(T):
    # Size of set A
    a_size = int(input())
    
    # Elements of set A
    set_A = set(map(int, input().split()))
    
    # Size of set B
    b_size = int(input())
    
    # Elements of set B
    set_B = set(map(int, input().split()))
    
    # Check if A is subset of B and print result
    if set_A.issubset(set_B):
        print("True")
    else:
        print("False")



###12 Check Strict Superset

setA = set(map(int, input().split()))

n = int(input())

is_strict_superset = True

for _ in range(n):
    other_set = set(map(int, input().split()))
    if not (setA > other_set): 
        is_strict_superset = False
        break

print(is_strict_superset)

###13 Set .discard(), .remove() & .pop()
n = int(input())  
s = set(map(int, input().split()))  

N = int(input())
for _ in range(N):
    command = input().split()
    
    if command[0] == "pop":
        s.pop()  
    elif command[0] == "remove":
        s.remove(int(command[1])) 
    elif command[0] == "discard":
        s.discard(int(command[1]))   

print(sum(s))



