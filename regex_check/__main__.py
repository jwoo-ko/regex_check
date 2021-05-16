import os
import time
from regex_check import Checklist
from pdf_to_txt import convert_pdf_to_txt, regex_txt


pdf_path = r'..\resources\pdf'
txt_path = r'..\resources\txt'
regex_path = r'..\resources\regex'
checklist_path = r'..\resources'
pattern = r'[^가-힣a-zA-Z0-9(){}\[\].%]'

convert_pdf_to_txt(pdf_path=pdf_path, txt_path=txt_path)
regex_txt(pattern, txt_path=txt_path, regex_path=regex_path)
checklist = Checklist(checklist_path=checklist_path)

for txt_file in os.listdir(regex_path):
    if not txt_file.endswith('.txt'):
        continue

    time_start = time.time()
    checklist.reset()

    with open(os.path.join(regex_path, txt_file), 'r', encoding='utf-8') as f_in:
        while True:
            line = f_in.readline()
            if line:
                checklist.check(line)

            else:
                break

    checklist.update()
    time_end = time.time()

    with open(r'..\result.txt', 'a') as log_out:
        log_out.write('Check for file "{}": {:.2f} seconds.\n'.format(txt_file, time_end - time_start))
        log_out.write(checklist.error_log())

del checklist
