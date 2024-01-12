"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

september_call_dict = {}
def add_september_calls(call):
    tmp_date = call[2].split(' ')[0]
    if "09-2016" in tmp_date:
        september_call_dict[call[0]] = call[-1]

for call in calls:
    add_september_calls(call)

max_time_val = -1
max_num, max_time = "", ""

# Time Complexity: O(n)
for call_number, duration in september_call_dict.items():
    if duration > max_time:
        max_time = duration
        max_num = call_number

        
print(f"{max_num} spent the longest time, {max_time} seconds, on the phone during September 2016.")