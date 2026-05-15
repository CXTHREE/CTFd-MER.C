# TODO: Read the file
import re

def find_flag():
    with open("CTF-W3_expanded_access_logs.txt", "r") as f:
        for line in f:
            # Look for lines with FLAG pattern hidden in password field
            if "FLAG{" in line:
                # Extract the FLAG{...} pattern from the line
                flags = re.findall(r'FLAG\{.*?\}', line)
                for flag in flags:
                    print(f"Suspicious Login Found!")
                    print(f"Hidden Flag: {flag}")

find_flag()