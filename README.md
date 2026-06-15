# PDF Comparison Tool using Python

This project compares two PDF files and checks whether they are identical using cryptographic hashing.

## FEATURES

- Compares two PDF files
- Uses hashing for file comparison
- Processes files in chunks for efficiency
- Simple command-line execution
- Works on Windows, Linux, Mac

## HOW IT WORKS

1. Each file is read in binary mode.
2. Data is processed in chunks.
3. A hash value is generated for each file.

4. If hash values are the same → files are identical
5. If hash values are different → files are not identical

## TECH STACK

Python 3
hashlib
os

## PROJECT STRUCTURE
```
pdf-compare-project/
├── compare2pdfs.py                 
├── .gitignore            
├── requirements.txt       
└── README.md  
```
## HOW TO RUN

## 1. Clone the repository

```
git clone https://github.com/your-username/pdf-compare-project.git

```
## 2. Enter project folder
```
cd pdf-compare-project
Run script
python compare2pdfs.py file1.pdf file2.pdf

```

## EXAMPLE OUTPUT

Files are identical

OR

Files are not identical

## USE CASES

1. File integrity checking
2. Backup validation
3. Cloud sync verification
4. Duplicate file detection
5. Security validation

FUTURE IMPROVEMENTS

Upgrade to SHA-256 hashing
Add similarity scoring
Build GUI using Streamlit
Folder comparison support
PDF content difference detection

AUTHOR

Built for learning Python file handling and hashing concepts.
