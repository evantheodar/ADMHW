 ###1 Exceptions

def integer_division(a, b):
    try:
        # Attempt integer division
        result = a // b
        return result
    except ZeroDivisionError as e:
      
        return "Error Code: " + str(e)
    except ValueError as e:
       
        return "Error Code: " + str(e)

T = int(input())

for _ in range(T):
    try:
        a, b = map(int, input().split())
        print(integer_division(a, b))
    except ValueError as e:
        print("Error Code: " + str(e))


