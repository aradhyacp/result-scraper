# 🎓 DSCE Endsem Results Scraper

A Python script to automatically fetch and extract end-semester results from the DSCE (Dayananda Sagar College of Engineering) results. It downloads result using USNs, extracts SGPA, student names, and roll numbers, and saves the data into a clean CSV file.

---

## 📌 Features

- 📥 Downloads student result without PDFs from the DSCE server.
- 🧾 Extracts SGPA, name, and USN from each PDF.
- 📊 Outputs all data to a CSV file for easy access.
- ⚙️ Simple setup and easy automation with a USN list.

---

## 📄 Input Format

Create a file called `roll.txt` in the same directory with one USN per line:

```
1DS20CS001
1DS20CS002
1DS20CS003
...
```
---

## 🛠️ Requirements

Install the required Python packages:

```bash
pip install requests PyPDF2
```
---

## How to Run
Make sure roll.txt is ready, then run the script:

```bash
python results_scraper.py
```

It will:
Read USNs from roll.txt
Fetch each student's result as a PDF but wont download any pdf on you local machine.
Extract SGPA, Name, and USN
Save the data to exam_results_sem3.csv

---

## 🗃️ Output
The script generates a file:
```
exam_results_sem3.csv
```
With columns:
USN / Roll No
Name of the Student
SGPA

---

## ⚠️Disclaimer
This tool pulls data from a public-facing DSCE IP.
Use only for personal, academic, or authorized purposes.
DSCE may change their server IP or PDF format, which could break the script.

---
Happy scraping! 🚀
