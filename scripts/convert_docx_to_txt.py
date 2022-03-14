# import pypandoc

# # Example file:
# docxFilename = 'files\input\6. SINIF MATEMATİK SESLENDİRME YENİ (2).docx'
# output = pypandoc.convert_file(docxFilename, 'plain', outputfile= docxFilename[:-5]+".txt")
# assert output == ""

import aspose.words as aw
from os import path

basepath = path.dirname(__file__)
input_file_name = "6. SINIF MATEMATİK SESLENDİRME YENİ (2).docx"
input_file_path = path.abspath(path.join(basepath, "..", "files", "input_docx", input_file_name))
output_file_path = path.abspath(path.join(basepath, "..", "files", "input_txt", input_file_name[:-5] + ".txt"))

doc = aw.Document(input_file_path)
doc.save(output_file_path)