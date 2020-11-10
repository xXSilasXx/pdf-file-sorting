import os
from PyPDF2 import PdfFileReader, PdfFileWriter


pdf_file_path1 = 'Your file path' # take the document

file_base_name1 = pdf_file_path1.replace('.pdf','') 

output_folder_path = os.path.join(os.getcwd(), 'Your path') # specify the path where the splitted files are transferred to be concetenated

pdf1 = PdfFileReader(pdf_file_path1) # create PdfFileReader object


counter = 2

sec_count = 1

for page_num in range(pdf1.numPages): # for all the pages in the document
    pdfWriter1 = PdfFileWriter()
    pdfWriter1.addPage(pdf1.getPage(page_num))

    if counter% 2 == 0:
        with open(os.path.join(output_folder_path, 'a{1}.pdf'.format(file_base_name1, sec_count)), 'wb')as f: #take the first page of the n-th contract
            pdfWriter1.write(f)
            f.close()

    else:
        with open(os.path.join(output_folder_path, 'b{1}.pdf'.format(file_base_name1, sec_count)), 'wb')as f: #take the second page of the n-th contract
            pdfWriter1.write(f)
            f.close()
            sec_count += 1



    counter -= 1
