import hashlib

# Read all hashes
with open("CTF-W5-Milestone 1_large_hashed_passwords.txt", "r") as f:
    hashed_passwords = [line.strip() for line in f if line.strip()]

# Read all candidate passwords
with open("CTF-W5-Milestone 1_large_wordlist.txt", "r") as f:
    wordlist = [line.strip() for line in f if line.strip()]

# Store all matched plaintext passwords
matches = []

# Dictionary attack: hash each word and compare against all stored hashes
for word in wordlist:
    generated_hash = hashlib.sha256(word.encode()).hexdigest()

    if generated_hash in hashed_passwords:
        print("Final password to submit:", word)
        break
else:
    print("No matches found.")