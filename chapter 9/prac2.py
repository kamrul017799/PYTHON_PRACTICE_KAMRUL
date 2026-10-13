# Write a Python program using regex to find consecutive repeated words in a sentence. The matching should be case-insensitive.
import re
btext = re.compile(r'\b(\w+)\s+\1+\b', re.IGNORECASE)

text = btext.findall( 'This IS is a very very interesting book, and and I like it.')
print(text)


