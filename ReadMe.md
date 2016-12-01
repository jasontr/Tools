# Tools    
## NCR2utf8  
This is a tool to change NCR to UTF8.
```python:NCR2utf8.py  
from HTMLParser import HTMLParser  
import sys  
filepath = sys.argv[1]  
text = []  
with open(filepath, 'r') as f:  
	lines = f.readlines()  
		for line in lines:  
			text.append(HTMLParser().unescape(line))  
  
with open(str(filepath) + '.utf8.txt', 'w') as w:  
	for line in text:  
		w.write(line.encode('utf-8'))  
```