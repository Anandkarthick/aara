import re
from collections import Counter

def words(text): return re.findall(r'\w+', text.lower())

print(words("here is a test word"))
#WORDS = Counter(words(open('big.txt').read()))