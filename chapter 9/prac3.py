# Write a program that extracts the username and status code from each log entry using capturing groups. Store the results in a list of tuples.
import re
# find = re.compile(r'user=(\w+)\s+status=(\d{3})')
find =re.compile(r'user=(\w+)\s+status=(\d{3})')
logs = find.findall( '''
user=kamrul status=200
user=alice status=404
user=bob status=500
user=nadia status=200
''')
print(logs)

