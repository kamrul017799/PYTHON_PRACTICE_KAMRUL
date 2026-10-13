# Write a Python program using regex to extract all text inside double quotation marks. The text inside the quotes may contain spaces and punctuation.
import re
rule = re.compile(r'"([^"]*)"')

text = rule.findall('He said "Python is useful", then she replied "I agree completely!"')
print(text)

