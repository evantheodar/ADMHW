###1 Standardize Mobile Number Using Decorators
def wrapper(f):
    def fun(l):
        # Normalize each number to its last 10 digits
        formatted_numbers = ['+91 ' + number[-10:-5] + ' ' + number[-5:] for number in l]
        # Sort the formatted numbers and pass to the original function
        return f(formatted_numbers)
    return fun
  @wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 


###2 Decorators 2 - Name Directory
import operator

def person_lister(f):
    def inner(people):
        # Sort people by age (index 2)
        sorted_people = sorted(people, key=lambda person: int(person[2]))
        # Apply the formatting function to the sorted list
        return [f(person) for person in sorted_people]
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')
