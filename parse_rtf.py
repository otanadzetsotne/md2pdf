import os


def text(path):
    with open(path, 'r') as f:
        return f.readlines()


# Usage
rtf_path = '/Users/otana/Development/md2pdf/Копия Резюме.rtf'
txt_path = '/Users/otana/Development/md2pdf/Копия Резюме.txt'

rtf = text(rtf_path)
txt = text(txt_path)
print('fgfg')
