
###1 collections.Counter()
from collections import Counter
X = int(input())
shoe_sizes = Counter(map(int, input().split()))
N = int(input())

total_money = 0
for _ in range(N):
    size, price = map(int, input().split())
    
    # If the desired size is available in the shop
    if shoe_sizes[size] > 0:
    
        total_money += price
        shoe_sizes[size] -= 1



###2 DefaultDict Tutorial
from collections import defaultdict

n, m = map(int, input().split())

group_A = defaultdict(list)

for i in range(1, n + 1):
    word = input().strip()
    group_A[word].append(i)

for _ in range(m):
    word = input().strip()
    if word in group_A:
        print(' '.join(map(str, group_A[word])))
    else:
        print(-1)



###3 Collections.namedtuple()
import csv
N = int(input())
columns = input().split()

# Find the index of the 'MARKS' column
marks_index = columns.index('MARKS')
total_marks = 0

for _ in range(N):
    student_data = input().split()
    total_marks += int(student_data[marks_index])

average_marks = total_marks / N
print(f"{average_marks:.2f}")


###4 Collections.OrderedDict()


###5 Word Order


###6 Collections.deque()
from collections import deque

N = int(input())

d = deque()

for _ in range(N):
    command = input().split()
    
    if command[0] == 'append':
        d.append(command[1])
    elif command[0] == 'appendleft':
        d.appendleft(command[1])
    elif command[0] == 'pop':
        if len(d) > 0:
            d.pop()
    elif command[0] == 'popleft':
        if len(d) > 0:
            d.popleft()

print(' '.join(d))



###7 Company Logo
from collections import Counter
s = input().strip()

count = Counter(s)

sorted_count = sorted(count.items(), key=lambda x: (-x[1], x[0]))

for char, freq in sorted_count[:3]:
    print(char, freq)



###8 Piling Up!
def can_stack_cubes(test_cases):
    results = []
    for case in test_cases:
        n, side_lengths = case
        left, right = 0, n - 1
        last_size = float('inf')
        
        while left <= right:
            if side_lengths[left] >= side_lengths[right]:
                selected = side_lengths[left]
                left += 1
            else:
                selected = side_lengths[right]
                right -= 1
            
            if selected > last_size:
                results.append("No")
                break
            last_size = selected
        else:
            results.append("Yes")
    
    return results

# Input and output handling
if __name__ == "__main__":
    T = int(input())  # Number of test cases
    test_cases = []
    for _ in range(T):
        n = int(input())  # Number of cubes
        side_lengths = list(map(int, input().split()))  # Side lengths of the cubes
        test_cases.append((n, side_lengths))
    
    results = can_stack_cubes(test_cases)
    for result in results:
        print(result)

