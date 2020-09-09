## Author : Rishabh Gautam
## Program for regex matching using re library

# Import relevant libraries
import re

# Example 1 (Match A Symbol)
text = '$100'
re.findall(r'\$', text)

# Example 2 (Match a unicode character)
text = 'Microsoft™.'
re.findall(r'\u2122', text)

# Example 3 (Find any word of three letters)
text = 'The quick brown fox jumped over the lazy brown bear.'
re.findall(r'\b...\b', text)

# Example 4 (Find anything with a 'T' and then the next two characters)
text = 'The quick brown fox jumped over the lazy brown bear.'
re.findall(r'T..', text)

# Example 5 (Find any of fox, snake, or bear)
text = 'The quick brown fox jumped over the lazy brown bear.'
re.findall(r'fox|snake|bear', text)
