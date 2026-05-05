# TODO: Read the file
import re
import base64
import json

with open("CTF-W2_expanded_security_logs.json", "r") as f:
    logs = json.load(f)

# Find flagged entries and decode their messages
for log in logs:
    if log["flagged"] == True:
        try:
            decoded = base64.b64decode(log["message"]).decode('utf-8')
            # Identify the Hidden Flag that follows the pattern: FLAG{hidden_code_here}
            if re.search(r'FLAG\{.*?\}', decoded):
                print(f"Flag found: {decoded}")
                break
        except:
            continue
