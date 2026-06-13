# MO-IT143 - Ethical Hacking S3101 | A.Y. 2025 - 2026
# Team C / MER/C : Dela Cruz, L.M., Tubera, K.G., & Samaniego, M.Y.

#Week 7 - The Hidden Code

import csv
import re
import base64

def decode_payload(data):
   
    try:
        # base64.b64decode() forces the payload into raw bytes
        # .decode("utf-8") translates thw raw bytes into readable text
        return base64.b64decode(data).decode("utf-8")
    except:
        # so the script doesn't crash
        return None


with open("Milestone2\Milestone2-Files\CTF-W7_large_leaked_transactions.csv", "r") as file:
    reader = csv.reader(file)
    
    # skip the very first row because it contains column headers 
    next(reader)

    print("Scanning for Flags...")
    
    # iterate through every single transaction row in the CSV
    for row in reader:
        # row[3] targets the 4th column, which contains the 'encoded_data'
        decoded = decode_payload(row[3])

        if decoded:

            # r"FLAG\{.*?\}" looks for "FLAG{", any characters, and then the first "}"
            match = re.search(r"FLAG\{.*?\}", decoded)
            
            # if the regex scanner found the hidden flag pattern...
            if match:
                print("Target Flag Extracted.")
                print(f"Traced to Row ID: {row[0]} | User: {row[2]}")
                print(f"FLAG: {match.group()}")
                
                # stop the loop immediately to save processing time
                break
