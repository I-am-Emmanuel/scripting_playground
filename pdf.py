import PyPDF2

# with open('dummy.pdf', 'rb') as pdf_file:
#     pdf_reader = PyPDF2.PdfReader(pdf_file)
#     page = pdf_reader.pages[0]
#     pdf_writer = PyPDF2.PdfWriter()
#     pdf_writer.add_page(page)
#     with open('tilt.pdf', 'wb') as new_file:
#         pdf_writer.write(new_file)


with open('dummy.pdf', 'rb') as pdf_file2:
    pdf_reader2 = PyPDF2.PdfReader(pdf_file2)
    page = pdf_reader2.pages[0]
    rotate_page = page.rotate(90)
    with open('new_tilt.pdf', 'wb') as new_pdf2:
        pdf_writer = PyPDF2.PdfWriter()
        pdf_writer.add_page(rotate_page)
        pdf_writer.write(new_pdf2)

    # print(page.rotateClockwise(90))
    # print(len(pdf_reader.pages))
    # print(pdf_reader.pages[0])

# if __name__ == '__main__':

# with open('twopage.pdf', 'rb') as file2:
#     second_reader = PyPDF2.PdfReader(file2)
#     print(len(second_reader.pages))
    

