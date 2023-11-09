import os
from pyhtml2pdf import converter


p_html = '/Users/otana/Development/md2pdf/test.html'
p_pdf = '/Users/otana/Development/md2pdf/test.pdf'


driver = webdriver.Chrome(service=Service(ChromeDriverManager(version="114.0.5735.90").install()),options=options)

converter.convert(f'file:///{p_html}', p_pdf)
