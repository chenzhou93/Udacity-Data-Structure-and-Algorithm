"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

# Part A
number_prefixes = []
def is_mobile(called_number):
    return ' ' in called_number and len(called_number.split(' ')) == 2 and called_number[0] in {'7', '8', '9'}

def get_prefix(called_number):
    prefix_result = ''
    
    if '(0' in called_number:
        substr_start = called_number.index('(0')
        substr_end = called_number.index(')')
        prefix_result = called_number[substr_start + 1 : substr_end]
    elif is_mobile(called_number):
        #print(called_number.split(' '))
        prefix_result = (called_number.split(' ')[0])[0:4]
    elif called_number[0:3] == '140':
        prefix_result = '140'
    
    #print(prefix_result)
    return prefix_result

# Process all calls and find (080)
# Time Complexity: O(n)        
for call in calls:
    calling_number = call[0]
    if '(080)' in calling_number:
        called_number = call[1]
        prefix_number = get_prefix(called_number)
        number_prefixes.append(prefix_number)

# Print the result
if len(number_prefixes) > 0:
    # Time Complexity: O(nlogn)
    number_prefixes.sort()
    numbers_set = set()
    print('The numbers called by people in Bangalore have codes:')
    # Time Complexity: O(n)
    for num in number_prefixes:
        if num not in numbers_set:
            print(num)
            numbers_set.add(num)

# Part B
total_calls = 0
bgl_calls = 0

# Count calls to different groups
# Time Complexity: O(n)
for call in calls:
    calling_number = call[0]
    if '(080)' in calling_number:
        total_calls += 1
        called_number = call[1]
        if '(080)' in called_number:
            bgl_calls += 1

percetage = round(bgl_calls / total_calls, 4) * 100

print(f"{percetage} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")
