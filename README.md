📄 PDF Comparison Tool (Python)

A lightweight Python tool to compare two PDF files and check whether they are identical using cryptographic hashing.

This project demonstrates file handling, binary processing, and hash-based comparison in Python.

🚀 Features
1. Compares two PDF files efficiently
2. Uses cryptographic hashing for accurate comparison
3. Reads files in chunks for memory efficiency
4. Simple command-line interface (CLI)
5. Cross-platform support (Windows / Linux / Mac)
   
🧠 How It Works
Each file is read in binary mode and processed in chunks. A hash is generated for each file, and both hashes are compared.
If hashes match → files are identical
If hashes differ → files are not identical
Think of it as a digital fingerprint system for files.

🏗️ Tech Stack
Python 3.x
hashlib
os module

📁 Project Structure
'''
pdf-compare-project/
├── compare2pdfs.py
├── .gitignore
└── README.md
'''

⚙️ How to Run

1️⃣ Clone the repository
git clone https://github.com/your-username/pdf-compare-project.git
2️⃣ Move into project folder
cd pdf-compare-project
3️⃣ Run the script
python compare2pdfs.py file1.pdf file2.pdf
🧾 Example Output

Files are identical
OR
Files are not identical

💡 Real-World Use Cases
1. File integrity verification
2. Backup validation systems
3. Cloud sync checking
4. Duplicate file detection
5. Cybersecurity validation
   
🔮 Future Improvements
1. Upgrade to SHA-256 hashing
2. Show similarity percentage
3. Add Streamlit GUI
4. Folder-to-folder comparison
5. PDF content diff viewer
   
Built to learn:
1. File handling in Python
2. Cryptographic hashing
3. Real-world utility tool design
   
⚠️ Important Note
1. Ensure correct file paths
2. Files must exist before running
3. Use Python 3.x
   
