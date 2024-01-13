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
def calculate_september_calls(call):
    tmp_date = call[2].split(' ')[0]
    if "09-2016" in tmp_date:
        september_call_dict[call[0]] = september_call_dict.get(call[0], 0) + int(call[3])

for call in calls:
    calculate_september_calls(call)


max_key = max(september_call_dict, key = lambda k: september_call_dict[k])
max_value = september_call_dict[max_key]
        
print(f"{max_key} spent the longest time, {max_value} seconds, on the phone during September 2016.")