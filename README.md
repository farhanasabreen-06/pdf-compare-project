📄 PDF Comparison Tool (Python)

A lightweight Python tool to compare two PDF files and check whether they are identical using cryptographic hashing.

This project demonstrates file handling, binary data processing, and hash-based comparison in Python.

🚀 Features
Compares two PDF files efficiently
Uses cryptographic hashing for accurate comparison
Reads files in chunks for memory efficiency
Simple command-line interface (CLI)
Works across Windows, Linux, and macOS

🧠 How It Works

Each PDF file is processed in binary mode. The file is read in small chunks instead of loading everything at once. A hash value is generated for each file, and the two hashes are compared.

If the hashes match → files are identical
If they differ → files are not identical

Think of it as generating a unique digital fingerprint for each document.

🏗️ Tech Stack
Python 3.x
hashlib
os module
📁 Project Structure

pdf-compare-project/
├── compare2pdfs.py
├── .gitignore
└── README.md

⚙️ How to Run

Run the script using:

python compare2pdfs.py file1.pdf file2.pdf

🧾 Example Output

Files are identical

OR

Files are not identical

💡 Real-World Use Cases

File integrity verification
Backup validation systems
Cloud storage sync checks
Duplicate file detection
Cybersecurity validation
🔮 Future Improvements
Add SHA-256 support for stronger hashing
Show similarity percentage instead of binary output
Build a GUI using Streamlit or Tkinter
Compare entire folders of PDFs
Add text-based PDF difference highlighting


Built to practice:
File handling in Python
Cryptographic hashing concepts
Building simple real-world utility tools
