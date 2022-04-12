"""

Dora Akbulut

Step 0 of the NLP pipeline. Converts .docx files into .txt files.

Input: Texts of MORPA or Wikipedia.
Input format: .docx
Read folder: input_docx

Output: Texts of MORPA or Wikipedia.
Output format: .txt
Output to: input_txt

"""

import aspose.words as aw
from os import path

basepath = path.dirname(__file__)
input_file_name = "6. SINIF MATEMATİK SESLENDİRME YENİ (2).docx"
input_file_path = path.abspath(path.join(basepath, "..", "files", "input_docx", input_file_name))
output_file_path = path.abspath(path.join(basepath, "..", "files", "input_txt", input_file_name[:-5] + ".txt"))

doc = aw.Document(input_file_path)
doc.save(output_file_path)