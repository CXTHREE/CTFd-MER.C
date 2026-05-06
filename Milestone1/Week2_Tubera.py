# MO-IT143 - Ethical Hacking S3101 | A.Y. 2025 - 2026
# Team C / MER/C : Dela Cruz, L.M., Tubera, K.G., & Samaniego, M.Y.

#Week 2 - Data Heist
import re
import base64
import json

with open('Milestone1/Milestone1-Files/CTF-W2_expanded_security_logs.json', 'r') as f:
    logs = json.load(f)
# Sir. JR suggested finding Base64 strings using regex: re.findall(r'[A-Za-z0-9+/]{64,}[=]{0,2}')
# I adapted this idea. Instead of using regex on the whole file, I am pulling the 
# Base64 strings directly from the entries where "flagged" is True.
potential_flags_base64 = []
for entry in logs:
    if entry.get("flagged") == True:
        potential_flags_base64.append(entry["message"])

for string in potential_flags_base64:
    try:
        decoded_string = base64.b64decode(string).decode('utf-8')

        # I Want to Filter the output to only show the actual hidden digital fingerprint
        if "FLAG{" in decoded_string:
            print(f"Decoded string: {decoded_string}")
            
    except :
        continue