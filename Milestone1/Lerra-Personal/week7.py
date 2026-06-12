import csv
import re
import base64

def decode_payload(data):
    try:
        return base64.b64decode(data).decode("utf-8")
    except:
        return None

with open("CTF-W7_large_leaked_transactions.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        decoded = decode_payload(row[3])

        if decoded:
            match = re.search(r"FLAG\{.*?\}", decoded)
            if match:
                print("Flag found:", match.group())
                break