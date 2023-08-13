import PyPDF2
import sys

# water_mark = sys.argv[1]
# pdf_files = sys.argv[2:]

# def waterMarkStamp(watermark_pdf, pdf_list):
    
#     with open(watermark_pdf, 'rb') as watermark_file:
#         watermark_reader = PyPDF2.PdfReader(watermark_file)
#         watermark_page = watermark_reader.pages[0]

        
#         writer = PyPDF2.PdfWriter()

        
#         for pdf_file in pdf_list:
#             with open(pdf_file, 'rb') as input_file:
#                 pdf_reader = PyPDF2.PdfReader(input_file)

#                 for index in range(len(pdf_reader.pages)):
#                     page = pdf_reader.pages[index]
#                     page.merge_page(watermark_page)
#                     writer.add_page(page)

        
#         with open('new_attachment.pdf', 'wb') as output_file:
#             writer.write(output_file)

# waterMarkStamp(water_mark, pdf_files)


                


inputs = sys.argv[1:]

def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write('super.pdf')
        

pdf_combiner(inputs)

# with open('dummy.pdf', 'rb') as pdf_file:
#     pdf_reader = PyPDF2.PdfReader(pdf_file)
#     page = pdf_reader.pages[0]
#     pdf_writer = PyPDF2.PdfWriter()
#     pdf_writer.add_page(page)
#     with open('tilt.pdf', 'wb') as new_file:
#         pdf_writer.write(new_file)


# with open('dummy.pdf', 'rb') as pdf_file2:
#     pdf_reader2 = PyPDF2.PdfReader(pdf_file2)
#     page = pdf_reader2.pages[0]
#     rotate_page = page.rotate(90)
#     with open('new_tilt.pdf', 'wb') as new_pdf2:
#         pdf_writer = PyPDF2.PdfWriter()
#         pdf_writer.add_page(rotate_page)
#         pdf_writer.write(new_pdf2)

    # print(page.rotateClockwise(90))
    # print(len(pdf_reader.pages))
    # print(pdf_reader.pages[0])

# if __name__ == '__main__':

# with open('twopage.pdf', 'rb') as file2:
#     second_reader = PyPDF2.PdfReader(file2)
#     print(len(second_reader.pages))
    

