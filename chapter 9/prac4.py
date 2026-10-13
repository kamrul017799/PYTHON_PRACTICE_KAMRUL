# Write a regex program to find all words that start with b, end with d, and contain one or more letters between them.
import re
rule = re.compile(r'\bb[a-zA-Z]+d\b')
text = rule.findall('The bird flew beyond the board beside a bad road.')
print(text)
