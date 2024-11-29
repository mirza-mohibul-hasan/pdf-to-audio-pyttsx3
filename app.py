import pyttsx3
import pdfplumber
import PyPDF2

file = "I:/BrainHouse/pdf-to-audio/Behavioral_Interview.pdf"

f = open(file, 'rb')
pdf_R = PyPDF2.PdfReader(f)

pages = len(pdf_R.pages)

with pdfplumber.open(file) as pdf:
    for i in range(0, pages):
        page = pdf.pages[i]
        text = page.extract_text()
        print(text)
        s = pyttsx3.init()
        s.save_to_file(text, 'behave.mp3')
        s.runAndWait()
f.close()
