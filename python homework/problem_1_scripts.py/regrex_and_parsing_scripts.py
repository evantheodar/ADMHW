
###1 Detect Floating Point Number
def is_valid_float(n):
    try:
        float_n = float(n)
    except ValueError:
        return False

    if n.count('.') != 1:
        return False

    if n.endswith('.'):
        return False

    return True
T = int(input())

for _ in range(T):
    N = input().strip()
    print(is_valid_float(N))


###2 Re.split()
regex_pattern = r'[,.]'

import re
print("\n".join(re.split(regex_pattern, input())))


###3 Group(), Groups() & Groupdict()
import re

def find_first_repeating_char(s):
    match = re.search(r'([a-zA-Z0-9])\1', s)
    
    if match:
        return match.group(1)
    else:
        return -1

S = input().strip()
print(find_first_repeating_char(S))



###4 Re.findall() & Re.finditer()


###5 Re.start() & Re.end()
import re
def find_all_substring_indices(s, k):
    result = []
    start = 0

    while start < len(s):
        start_index = s.find(k, start)
        
        if start_index != -1:
            end_index = start_index + len(k) - 1
            result.append((start_index, end_index))
            start = start_index + 1
        else:
            break

    if result:
        for item in result:
            print(item)
    else:
        print((-1, -1))

S = input().strip()
k = input().strip()

find_all_substring_indices(S, k)



###6 Regex Substitution
import re

N = int(input())

for _ in range(N):
    line = input()
    
    line = re.sub(r'(?<= )&&(?= )', 'and', line)
    line = re.sub(r'(?<= )\|\|(?= )', 'or', line)

    print(line)



###7 Validating Roman Numerals (took help from solutions)

regex_pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"  # Do not delete 'r'.
import re
print(str(bool(re.match(regex_pattern, input()))))



###8 Validating phone numbers
import re
regex_pattern = r"^[789]\d{9}$"  #

N = int(input().strip())
for _ in range(N):
    number = input().strip()  
    if re.match(regex_pattern, number):
        print("YES")
    else:
        print("NO")


.
###9 Validating and Parsing Email Addresses
import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z][\w\.-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$'
    return re.match(pattern, email)

n = int(input())

for _ in range(n):
    name, email = input().split()
    email = email[1:-1]
    if is_valid_email(email):
        print(f"{name} <{email}>")



###10 Hex Color Code
import re

N = int(input())

pattern = r'#[0-9A-Fa-f]{3,6}'

inside_braces = False

for _ in range(N):
    line = input().strip()
    

    if '{' in line:
        inside_braces = True
        continue  #
    
    if '}' in line:
        inside_braces = False
        continue 
    
    if inside_braces:
        matches = re.findall(pattern, line)
        
        for match in matches:
            print(match)



###11 HTML Parser - Part 1 (took help from solutions)
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        # Start tag
        print(f"Start : {tag}")
        for i, attr in enumerate(attrs):
            attr_name = attr[0]
            attr_value = attr[1] if attr[1] is not None else 'None'
            print(f"-> {attr_name} > {attr_value}")

    def handle_endtag(self, tag):
        print(f"End   : {tag}")

    def handle_startendtag(self, tag, attrs):
        print(f"Empty : {tag}")
        # Check if the tag has attributes
        for i, attr in enumerate(attrs):
            attr_name = attr[0]
            attr_value = attr[1] if attr[1] is not None else 'None'
            print(f"-> {attr_name} > {attr_value}")

# Input number of lines
n = int(input())

# Read HTML lines from input
html_snippet = ""
for _ in range(n):
    html_snippet += input().strip() + "\n"

# Create an instance of the parser
parser = MyHTMLParser()

# Feed the HTML code to the parser
parser.feed(html_snippet)



###12 HTML Parser - Part 2 (took help from solutions)
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    
    def handle_comment(self, data):
        # Check if the comment is multi-line or single-line
        if '\n' in data:
            print(">>> Multi-line Comment")
        else:
            print(">>> Single-line Comment")
        print(data)
    
    def handle_data(self, data):
       
        if data.strip():
            print(">>> Data")
            print(data)

html = ""
for _ in range(int(input())):
    html += input().rstrip() + '\n'
parser = MyHTMLParser()
parser.feed(html)
parser.close()



###13 Detect HTML Tags, Attributes and Attribute Values
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr_name, attr_value in attrs:
            print(f"-> {attr_name} > {attr_value}")

    def handle_endtag(self, tag):
        pass

    def handle_startendtag(self, tag, attrs):
        print(tag)
        for attr_name, attr_value in attrs:
            print(f"-> {attr_name} > {attr_value}")

n = int(input())

html_snippet = ""
for _ in range(n):
    html_snippet += input().strip() + "\n"
parser = MyHTMLParser()
parser.feed(html_snippet)



###14 Validating UID
def is_valid_uid(uid):
    # Check length
    if len(uid) != 10:
        return False

    uppercase_count = 0
    digit_count = 0
    char_set = set()

    for char in uid:
        if not char.isalnum(): 
            return False
        if char.isupper():
            uppercase_count += 1
        if char.isdigit():
            digit_count += 1
        char_set.add(char)

    if len(char_set) != len(uid):
        return False

    if uppercase_count >= 2 and digit_count >= 3:
        return True
    
    return False

T = int(input())

for _ in range(T):
    uid = input().strip()
    if is_valid_uid(uid):
        print("Valid")
    else:
        print("Invalid")


###15 Validating Credit Card Numbers
import re

def is_valid_credit_card(card_number):
    sanitized_number = card_number.replace("-", "")
    
    pattern = r"^[4-6]\d{15}$"
    
    if re.match(pattern, sanitized_number) and not re.search(r"(\d)\1{3,}", sanitized_number):
        if re.match(r"^(\d{4}-){3}\d{4}$", card_number) or re.match(r"^\d{16}$", card_number):
            return "Valid"
    return "Invalid"

N = int(input())
for _ in range(N):
    card_number = input().strip()
    print(is_valid_credit_card(card_number))



###16 Validating Postal Codes (took help)

regex_integer_in_range = r"^[1-9][0-9]{5}$" 
regex_alternating_repetitive_digit_pair = r"(?=(\d)(?=\d\1))"
import re
P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)



