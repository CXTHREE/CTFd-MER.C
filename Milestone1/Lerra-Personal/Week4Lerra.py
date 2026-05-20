# TODO: Read the webpage
import re
import requests
from bs4 import BeautifulSoup, Comment

def find_flag():
    # Fetch the webpage HTML source
    url = "https://mmdc-isd.s3.us-east-2.amazonaws.com/Ethical%20Hacking/index.html"
    response = requests.get(url)
    html = response.text

    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")

    # Approach 1: Find all HTML comments and search for FLAG
    print("=== SEARCHING IN COMMENTS ===")
    comments = soup.find_all(string=lambda text: isinstance(text, Comment))
    for comment in comments:
        print(f"Comment Found: {comment.strip()}")
        flags = re.findall(r'FLAG\{.*?\}', comment)
        for flag in flags:
            print(f"Hidden Flag: {flag}")

    # Approach 2: Search the RAW HTML source directly
    print("\n=== SEARCHING IN RAW HTML ===")
    flags = re.findall(r'FLAG\{.*?\}', html)
    for flag in flags:
        print(f"Hidden Flag: {flag}")

    # Approach 3: Print the full raw HTML so we can see everything
    print("\n=== FULL RAW HTML SOURCE ===")
    print(html)

find_flag()