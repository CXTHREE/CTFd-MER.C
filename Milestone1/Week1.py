# MO-IT143 - Ethical Hacking S3101 | A.Y. 2025 - 2026
# Team C / MER/C : Dela Cruz, L.M., Tubera, K.G., & Samaniego, M.Y.

#Week 1 - Flagged for Extraction
import re 

#Reads the file , line by line. Use regex to search for patterns that match the format of flags (FLAG{...}). Store the extracted flags in a list for further processing using the loop in the later part of the code. 
with open('Milestone1/Milestone1-Files/CTF-W1_mystery_text_file.txt', 'r') as f: 
    content = f.read()
    flags = re.findall(r'FLAG\{.*?\}',content)

#Finds the unique message. Flag counter logic to count the occurrences of each unique flag. Use a dictionary to store the flags as keys and their counts as values. Finally, print out each unique flag along with its count.
flag_counts = {}
for f in flags:
    flag_counts[f] = flag_counts.get(f,0) + 1

#Print the unique flags and their counts. Iterate through the dictionary of flag counts and print each flag along with its corresponding count.
for f, count in flag_counts.items():
    print(f"{f} = {count}")


