from tika import parser
import os
import time
import re


def convert_pdf_to_txt(pdf_path, txt_path):
    start_time_whole = time.time()

    for pdf_file in os.listdir(pdf_path):
        if not pdf_file.endswith('.pdf'):
            continue

        start_time = time.time()

        parsed = parser.from_file(os.path.join(pdf_path, pdf_file))
        txt_file = pdf_file.replace('.pdf', '.txt')

        with open(os.path.join(txt_path, txt_file), 'w', encoding='utf-8') as f_out:
            print(parsed['content'], file=f_out)

        end_time = time.time()

        print('Conversion (PDF -> TXT) for {}, {:.2f} seconds.'.format(txt_file, end_time - start_time))

    print('Conversion Ended. Total {:.2f} seconds elapsed.'.format(time.time()-start_time_whole))


def regex_txt(pattern, txt_path, regex_path):
    start_time_whole = time.time()
    re_filter = re.compile(pattern)  # filter setting

    for txt_file in os.listdir(txt_path):
        if not txt_file.endswith('.txt'):
            continue

        start_time = time.time()
        with open(os.path.join(txt_path, txt_file), 'r', encoding='utf-8') as f_in:
            with open(os.path.join(regex_path, txt_file), 'w', encoding='utf-8') as f_out:
                while True:
                    line = f_in.readline()
                    if line:
                        f_out.write(re_filter.sub('', line))
                    else:
                        break

        end_time = time.time()

        print('Extraction for {}, {:.2f} seconds.'.format(txt_file, end_time - start_time))

    print('Extraction Ended. Total {:.2f} seconds elapsed.'.format(time.time()-start_time_whole))


