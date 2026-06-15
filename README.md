PDF Comparison Tool (Python)

A lightweight Python tool to compare two PDF files and check whether they are identical using cryptographic hashing.

FEATURES

Compares two PDF files efficiently
Uses cryptographic hashing for accuracy
Reads files in chunks for memory efficiency
Simple command-line interface
Works on Windows, Linux, and Mac

HOW IT WORKS

Each file is read in binary mode. Data is processed in chunks and a hash value is generated for each file.

If both hash values match, files are identical.
If hash values differ, files are not identical.

Think of it as a digital fingerprint for files.

TECH STACK

Python 3.x
hashlib module
os module

PROJECT STRUCTURE

pdf-compare-project/
├── compare2pdfs.py
├── .gitignore
└── README.md

HOW TO RUN

Step 1: Clone the repository
git clone https://github.com/your-username/pdf-compare-project.git

Step 2: Move into project folder
cd pdf-compare-project

Step 3: Run the script
python compare2pdfs.py file1.pdf file2.pdf

EXAMPLE OUTPUT

Files are identical

OR

Files are not identical

REAL WORLD USE CASES

File integrity checking
Backup validation
Cloud sync verification
Duplicate file detection
Security validation systems

FUTURE IMPROVEMENTS

Upgrade to SHA-256 hashing
Show similarity percentage
Add GUI using Streamlit
Compare entire folders
Add PDF content difference detection

AUTHOR

Built to understand:

File handling in Python
Cryptographic hashing
Practical utility tool design

IMPORTANT NOTE

Ensure file paths are correct
Ensure files exist before running
Use Python 3.x
