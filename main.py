import os
from subprocess import check_output
from pathlib import Path


BASE_DIR = Path(__file__).parent

out = check_output([
    'pdf2md',
    os.path.join(BASE_DIR, 'resume.pdf'),
])

print(out)
