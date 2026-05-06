# MO-IT143 - Ethical Hacking S3101 | A.Y. 2025 - 2026
# Team C / MER/C : Dela Cruz, L.M., Tubera, K.G., & Samaniego, M.Y.

#Week 2 - Data Heist

import json
import re
import base64

# define the path 
file_path = 'Milestone1/Milestone1-Files/CTF-W2_expanded_security_logs.json'

try:
    # open the json file in read-only mode to prevent accidental data modification
    with open(file_path, 'r') as f:
        # use json.load to parse the file into a python list of dictionaries
        # allows access to log entries by their keys like 'message' or 'flagged'

        logs = json.load(f)

    # iterate through each log entry to find suspicious activity
    for entry in logs:
        # logic from kyle: only target entries where the 'flagged' boolean is set to true
        # filters out normal traffic and focuses on potential interference

        if entry.get('flagged') == True:
            # retrieve the base64 encoded string from the message field
            encoded_message = entry.get('message', '')
            
            try:
                # convert the base64 string into bytes, then decode those bytes into a utf-8 string
                # reveals the hidden text hidden by enemy agents within the logs
                decoded_bytes = base64.b64decode(encoded_message)
                decoded_text = decoded_bytes.decode('utf-8')

                # logic from maja: use a regular expression to find the exact flag pattern
                # r'FLAG\{.*?\}' ensures we capture the literal prefix and the closing brace
                if re.search(r'FLAG\{.*?\}', decoded_text):
                    # output the successful match to the vs code terminal
                    print(f"Found Flag!: {decoded_text}")
                else:
                    # team addition: print a notification if a flagged entry was a decoy
                    # this helps in auditing the dataset for misleading information
                    print(f"flagged entry found, but no flag pattern in: {decoded_text[:20]}...")

            except Exception:
                # skip entries that are not valid base64 or utf-8 to keep the script running
                continue

# catch specific errors to help troubleshoot the vs code environment
except FileNotFoundError:
    # this triggers if the terminal is looking in the wrong directory context
    print(f"error: the file at {file_path} was not found. check your workspace folder.")
except json.JSONDecodeError:
    # while this triggers if the mystery json file is corrupted or improperly formatted
    print("error: the file is not a valid json format.")