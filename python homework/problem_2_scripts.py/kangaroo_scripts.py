
def kangaroo(x1, v1, x2, v2):

    if v1 == v2:
        return "YES" if x1 == x2 else "NO"
    elif (x2 - x1) * (v1 - v2) > 0 and (x2 - x1) % (v1 - v2) == 0:
        return "YES"
    else:
        return "NO"

# Example usage:
x1, v1, x2, v2 = map(int, input().split())  # Input values
print(kangaroo(x1, v1, x2, v2))

