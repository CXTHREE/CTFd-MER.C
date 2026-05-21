# TODO: Read the webpage
import re
import requests
from bs4 import BeautifulSoup, Comment

# Fetch the webpage HTML source
url = "https://mmdc-isd.s3.us-east-2.amazonaws.com/Ethical%20Hacking/index.html"
response = requests.get(url)
html = response.text

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Approach 1: Find all HTML comments and search for FLAG
print("=== SEARCHING IN COMMENTS ===")
comments = soup.find_all(string=lambda text: isinstance(text, Comment))

if not comments:
    print("No HTML comments found.")

for comment in comments:
    print(f"Comment Found: {comment.strip()}")
    flags = re.findall(r'FLAG\{.*?\}', comment)
    for flag in flags:
        print(f"Hidden Flag in comment: {flag}")

# Approach 2: Search the raw HTML directly
print("\n=== SEARCHING IN RAW HTML ===")
flags = re.findall(r'FLAG\{.*?\}', html)

if flags:
    for flag in flags:
        print(f"Hidden Flag in raw HTML: {flag}")
else:
    print("No flag found in raw HTML.")