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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
texts_set = set()
calls_set = set()

for text in texts:
    texts_set.add(text[0])
    texts_set.add(text[1])

for call in calls:
    calls_set.add(call[0])
    calls_set.add(call[1])

# Time Complexity: O(1)
print(f"There are {len(texts_set | calls_set)} different telephone numbers in the records.")

