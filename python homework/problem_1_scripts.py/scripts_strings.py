

#1 Capitalize!
ef solve(s):
    # Use the title() function to capitalize the first letter of each word
    capitalized_string = s.title()
    return capitalized_string
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()


#2 sWAP cASE
def swap_case(s):
    return s.swapcase()


#3 String Split and Join
def split_and_join(l):
    a=l.split(" ")
    a="-".join(a)
    return a
    

#4 What's Your Name?
def print_full_name(first, last):
    print("Hello "+first+" "+last+"! You just delved into python.")
if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)


#5 Mutations
def mutate_string(string, position, character):
    string=string[:position]+character+string[position+1:]
    return(string)




#6 Find a string
def count_substring(string, sub_string):
    count = 0
    start = 0
    
    while start < len(string):
        
        index = string.find(sub_string, start)
        
        if index != -1:
            count += 1
           
            start = index + 1
        else:
            
            break
    
    return count


#7 String Validators
def check_string_properties(S):
  
    has_alphanumeric = any(char.isalnum() for char in S)
  
    has_alphabetical = any(char.isalpha() for char in S)
   
    has_digits = any(char.isdigit() for char in S)
   
    has_lowercase = any(char.islower() for char in S)
   
    has_uppercase = any(char.isupper() for char in S)
    print(has_alphanumeric)
    print(has_alphabetical)
    print(has_digits)
    print(has_lowercase)
    print(has_uppercase)

if __name__ == '__main__':
    S = input().strip()
    check_string_properties(S)


#8 Text Alignment
thickness = int(input())  # This must be an odd number
c = 'H'

# Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1) + c + (c*i).ljust(thickness-1))

# Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2) + (c*thickness).center(thickness*6))

# Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

# Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2) + (c*thickness).center(thickness*6))    

# Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness) + c + (c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))



#9 Text Wrap
import textwrap

def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(width=max_width) 
    word_list = wrapper.fill(text=string) 
    return word_list
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


#10 Designer Door Mat
# Input: N and M (space-separated)
N, M = map(int, input().strip().split())

# Top part of the mat
for i in range(1, N, 2):
    pattern = '.|.' * i
    print(pattern.center(M, '-'))

# Center part with 'WELCOME'
print('WELCOME'.center(M, '-'))

# Bottom part of the mat
for i in range(N-2, 0, -2):
    pattern = '.|.' * i
    print(pattern.center(M, '-'))


#11 String Formatting
def print_formatted(number):
  
    width = len(bin(number)) - 2  # '-2' to exclude the '0b' prefix
    
    # Iterate through the range from 1 to 'number'
    for i in range(1, number + 1):
        # Print the values in the required format: Decimal, Octal, Hexadecimal, Binary
        # Each value is right-aligned to match the width of the binary representation of 'number'
        print(f"{i:>{width}d} {i:>{width}o} {i:>{width}X} {i:>{width}b}")




#12 Alphabet Rangoli
import string

def print_rangoli(size):
    alphabets = string.ascii_lowercase  #

    lines = []
    
 
    for i in range(size):
        
        s = "-".join(alphabets[size-1:i:-1] + alphabets[i:size])
        lines.append(s.center(4*size - 3, "-"))
    print("\n".join(lines[::-1] + lines[1:]))



#13 The Minion Game
def minion_game(string):
    # Initialize scores
    kevin_score = 0
    stuart_score = 0
    
    # Get the length of the string
    length = len(string)
    
    # Loop through the string
    for i in range(length):
        # Check if the character is a vowel
        if string[i] in 'AEIOU':
            # Kevin scores all substrings starting from this position
            kevin_score += length - i
        else:
            # Stuart scores all substrings starting from this position
            stuart_score += length - i
    
    # Determine the winner
    if kevin_score > stuart_score:
        print("Kevin", kevin_score)
    elif stuart_score > kevin_score:
        print("Stuart", stuart_score)
    else:
        print("Draw")


