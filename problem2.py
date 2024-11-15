"""
##### Problem 2
Retrieve the contents of the sd.deltasd.bc.ca webpage.
Remove all of the HTML and display just the real contents of the page.
"""

import requests
from bs4 import BeautifulSoup

x = requests.get("https://sd.deltasd.bc.ca")
y = BeautifulSoup(x.text, 'html.parser')
text = y.get_text(separator='\n')
z = '\n'.join(line.strip() for line in text.splitlines() if line.strip())
print(z)  