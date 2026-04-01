# SSH BRUTEFORCE TOOL
Simple SSH BRUTEFORCE tool built in Python using Paramiko.
Designed for learning purposes.

---

# Features
- SSH password bruteforce
- Wordlist support
- Clean and simple CLI interface
- Error handling

---

# Requirements
- Python 3
- Paramiko

---

# Usage

```bash
python3 ssh-bruteforce.py -i <host> -u <username> -w <wordlist> -t <threads>
```

---

# Arguments

|Argument   | Description         |
|:---------:|---------------------|
|-i         | Target IP           |
|-u         | Username            |
|-w         | Password wordlist   |  
|-t         | Threads             |

---
# Notes!

- SSH servers may limit or block reapeted login attemps
- This tool includes basic handling for such cases
- This tool is not intended for large-scale brute force attacks

---

# Disclaimer!!!
- This tool is intended for **educational purposes only**. 
- Do not use it against systems without explicit permission
- **Unauthorized access to systems is illegal**

---

# Author

Developed by Educhnn.
