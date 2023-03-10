import PyPDF2

b = PyPDF2.PdfReader('a.pdf')
str = ""


for i in range(0,20):
    str += b.pages[i].extract_text()


with open("text.txt", "w", encoding='utf-8') as f:   
    f.write(str.split(".")[1])
print(str.split(".")[1])
