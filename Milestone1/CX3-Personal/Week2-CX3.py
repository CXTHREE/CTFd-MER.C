# MO-IT143 - Ethical Hacking S3101 | A.Y. 2025 - 2026
# Team C / MER/C : Dela Cruz, L.M., Tubera, K.G., & Samaniego, M.Y.

#Week 2 - Data Heist

import json
import re
import base64

# define the path to the log file
file_path = 'Milestone1/Milestone1-Files/CTF-W2_expanded_security_logs.json'

try:
    # open the file in read mode
    with open(file_path, 'r') as f:
        # use json.load to convert the file content into a python list of dictionaries
        # this is more efficient than reading the whole file as a raw string
        logs = json.load(f)

    # iterate through every log entry in the list
    for entry in logs:
        # check if the 'flagged' key is set to true
        if entry.get('flagged') == True:
            # retrieve the encoded string from the 'message' field
            encoded_message = entry.get('message', '')
            
            try:
                # convert the base64 string into bytes, then decode those bytes into a utf-8 string
                decoded_bytes = base64.b64decode(encoded_message)
                decoded_text = decoded_bytes.decode('utf-8')

                # search for the specific flag pattern within the decoded text
                if re.match(r'FLAG\{.*?\}', decoded_text):
                    print(f"Found Flag!: {decoded_text}")

            except Exception:
                # skip entries that fail to decode properly to prevent the script from crashing
                continue

except FileNotFoundError:
    print(f"Error: The file at {file_path} was not found.")
except json.JSONDecodeError:
    print("Error: The file is not a valid JSON format.")