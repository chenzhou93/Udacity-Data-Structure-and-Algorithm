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
month_list = ["January", "Feburary", "March", "April", "May",
              "June", "July", "August", "September", "October",
              "November", "December"]

def getFormatDate(call):
    tmp_date = call[2].split(' ')[0].split('-')
    month_index = int(tmp_date[0])
    month = month_list[month_index - 1]
    year = tmp_date[2]
    return month + " " + year

max_time_val = -1
max_num, max_time, max_date = "", "", ""

# Time Complexity: O(n)
for call in calls:
    if int(call[3]) > max_time_val:
        max_time_val = int(call[3])
        max_num = call[0]
        max_time = call[3]
        max_date = getFormatDate(call)
        
        
print(f"{max_num} spent the longest time, {max_time} seconds, on the phone during {max_date}.")

