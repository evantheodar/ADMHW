#1 List Comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    result = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
print(result)

#2 Find the Runner-Up Score!
if __name__ == '__main__':
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort(reverse=True)
    b=[]
    m=max(a)
    for i in a:
        if i!=m:
            b.append(i)
    print(b[0])


#3 Nested Lists
N = int(input())

records = []
for _ in range(N):
    name = input()
    grade = float(input())
    records.append([name, grade])

grades = sorted(set([grade for name, grade in records]))
second_lowest = grades[1]

second_lowest_students = [name for name, grade in records if grade == second_lowest]

for student in sorted(second_lowest_students):
    print(student)

#4 Finding the percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    tname = input()
    # print(student_marks[tname])
    s=sum(student_marks[tname])
    r=s/3
    res=f"{r:.2f}"
    print(res)


#5 Lists
if __name__ == '__main__':
    lst = []  # Initialize an empty list
    n = int(input())  # Read the number of commands
    
    for _ in range(n):
        command = input().split()  # Read the command and split into parts
        operation = command[0]
        
        if operation == 'insert':
            lst.insert(int(command[1]), int(command[2]))
        elif operation == 'print':
            print(lst)
        elif operation == 'remove':
            lst.remove(int(command[1]))
        elif operation == 'append':
            lst.append(int(command[1]))
        elif operation == 'sort':
            lst.sort()
        elif operation == 'pop':
            lst.pop()
        elif operation == 'reverse':
            lst.reverse()

#6 Tuples
n = int(input())  # Read the integer n
t = tuple(map(int, input().split()))  # Create a tuple from the space-separated integers

print(hash(t))
