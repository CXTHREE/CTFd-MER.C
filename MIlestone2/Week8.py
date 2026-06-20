# MO-IT143 - Ethical Hacking S3101 | A.Y. 2025 - 2026
# Team C / MER/C : Dela Cruz, L.M., Tubera, K.G., & Samaniego, M.Y.

#Week 8 - Web Traffic Inspector

import json
import re

file_path = "Milestone2\Milestone2-Files\CTF-W8_large_captured_web_traffic.har"

try:
    print("[+] Initializing deep packet inspection on HAR file...")

    with open(file_path, "r", encoding="utf-8") as file:
        # load JSON structure into Python dictionary
        har_data = json.load(file)
        
    # access the list of captured network events inside the log structure
    entries = har_data["log"]["entries"]
    print(f"[+] Loaded {len(entries)} traffic entries. Scanning payloads...")

    # iterate through each captured web request/response packet
    for index, entry in enumerate(entries):
        # safely extract the response text content from the traffic log
        # .get() prevents crashes if a packet has no textbody
        response_text = entry["response"]["content"].get("text", "")
        
        if response_text:
            # use regex to search for the Cybrian flag format (FLAG{...})
            match = re.search(r"FLAG\{.*?\}", response_text)
            
            if match:
                print("\n[!] SUCCESS! Sensitive Unencrypted Flag Intercepted.")
                print(f"Found in Packet Index: {index}")
                print(f"Request URL: {entry['request']['url']}")
                print(f"Flag: {match.group()}")
                
                # exit the loop instantly to save system processinh time
                break
    else:
        print("[-] Scan complete. No flag patterns found in this archive.")

except FileNotFoundError:
    print(f"[-] Error: Could not locate '{file_path}'. Check your folder path.")
except json.JSONDecodeError:
    print("[-] Error: The file is corrupted or not in a valid JSON/HAR format.")
