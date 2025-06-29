import requests
import PyPDF2
import re
import csv
from io import BytesIO

def extract_text_from_pdf_url(pdf_url):
    response = requests.get(pdf_url)
    pdf_stream = BytesIO(response.content)
    text = ''
    pdf_reader = PyPDF2.PdfReader(pdf_stream)
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()
    return text

def extract_sgpa_and_student_info(pdf_text):
    sgpa_pattern = r"SGPA\s+([\d.]+)"
    name_pattern = r"Name of the Student:\s*(.*)"
    usn_pattern = r"USN \/ Roll No:\s*(.*)"

    sgpa_match = re.search(sgpa_pattern, pdf_text)
    name_match = re.search(name_pattern, pdf_text)
    usn_match = re.search(usn_pattern, pdf_text)

    sgpa_value = None
    student_name = None
    usn_roll = None

    if sgpa_match:
        sgpa_value = sgpa_match.group(1)
    if name_match:
        student_name = name_match.group(1)
    if usn_match:
        usn_roll = usn_match.group(1)

    return sgpa_value, student_name, usn_roll

with open("roll.txt", "r") as file:
    roll_numbers = [line.strip() for line in file]

with open("exam_results_sem3.csv", "w", newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["USN / Roll No", "Name of the Student", "SGPA"])
    for roll_number in roll_numbers:
        pdf_url = f'http://14.99.184.178:8080/birt/frameset?__report=mydsi/exam/Exam_Result_Sheet_dsce.rptdesign&__format=pdf&USN={roll_number}' #DSCE official ip
        pdf_text = extract_text_from_pdf_url(pdf_url)
        sgpa, student_name, usn_roll = extract_sgpa_and_student_info(pdf_text)
        csv_writer.writerow([usn_roll, student_name, sgpa])
