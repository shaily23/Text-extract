import PyPDF2

b = PyPDF2.PdfReader('a.pdf')
print(len(b.pages))
page = b.pages[0]


for i in range(len(b.pages)):
    str += b.pages[i]
    print(page.extract_text())


with open("text.txt", "w", encoding='utf-8') as f:   
    f.write(page.split(".")[1])
