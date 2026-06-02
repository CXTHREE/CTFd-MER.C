import hashlib

# Read and clean lines from a file
def read_lines(filename):
    with open(filename, "r") as f:
        return [line.strip() for line in f if line.strip()]

# Load stored hashes and candidate passwords
hashed_passwords = set(read_lines("CTF-W5-Milestone 1_large_hashed_passwords.txt"))
wordlist = read_lines("CTF-W5-Milestone 1_large_wordlist.txt")

# Try each word in the wordlist
for word in wordlist:
    # Generate SHA-256 hash of the current word
    generated_hash = hashlib.sha256(word.encode()).hexdigest()

    # Check if the generated hash matches any stored hash
    if generated_hash in hashed_passwords:
        print("Final password to submit:", word)
        break
else:
    print("No matches found.")