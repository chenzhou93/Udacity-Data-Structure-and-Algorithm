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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
texts_set = set()
receiving_calls = set()
sending_calls = set()

# Add all sender and receiver numbers to texts_set for excluding
# Time Complexity: O(n)
for text in texts:
    texts_set.add(text[0])
    texts_set.add(text[1])

# Collect sending and receving call numbers separately
# Time Complexity: O(n)
for call in calls:
    sending_calls.add(call[0])
    receiving_calls.add(call[1])

# Use set operation
# Time Complexity: (not quite sure set opertion) O(1)
result = sending_calls - texts_set - receiving_calls
result_list = list(result)

# Time Complexity: O(nlogn)
result_list.sort()

# Output the result
# Time Complexity: O(n)
print("These numbers could be telemarketers: ")
for result in result_list:
    print(result)

