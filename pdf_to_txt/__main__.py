from pdf_to_txt import convert_pdf_to_txt, regex_txt


pdf_path = r'..\resources\pdf'
txt_path = r'..\resources\txt'
regex_path = r'..\resources\regex'
pattern = r'[^가-힣a-zA-Z0-9(){}\[\].%]'

convert_pdf_to_txt(pdf_path=pdf_path, txt_path=txt_path)
regex_txt(pattern, txt_path=txt_path, regex_path=regex_path)

