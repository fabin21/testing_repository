# Javascript Code
"""
document.addEventListener("scroll", function() {
  var posicaoy = document.scrollTop;
  if (posicaoy == 0) {
    navbar.style.backgroundColor = "trasnparent";
  } else {
    navbar.style.backgroundColor = "white";

  }
});
"""
# Python Code
import pandas as pd 
import pylatex
import pdflatex

def dataframeCollumns_to_latexHeadTable(dataframe):
    collumns_names = dataframe.collumns
    collumn_separator = str(" & ")
    collumn_ender = str(r" \\")
    
    line = collumn_separator.join(collumns_names)
    line =  line + collumn_ender

!pip install pylatex[matrices]
!pip install pylatex[pyplot.matplotlib]
!pip install pylatex[quantities]

def datatrame_to_LatexPDF(dataframe):
    latex_format = dataframe.to_latex()
    pdf_format = latex_format.to_pdf()

# In Python, the . replace() method and the 
# re.sub() function are often used to clean up
# text by removing strings or substrings or
# replacing them."


from pdflatex import PDFLaTeX

pdfl = PDFLaTeX.from_texfile('my_file.tex')
pdf, log, completed_process = pdfl.create_pdf(keep_pdf_file=True, keep_log_file=True)

import os
import pdflatex
import jinja2 

env = pdflatex.JINJA2_ENV
env['loader'] = jinja2.FileSystemLoader(os.path.abspath('.'))
env = jinja2.Environment(**env)
template = env.get_template('jinja.tex')
pdfl = pdflatex.PDFLaTeX.from_jinja2_template(template, data='Hello world!')
pdf, log, cp = pdfl.create_pdf()


JINJA2_ENV = {'block_start_string': '\BLOCK{',
              'block_end_string': '}',
              'variable_start_string': '\VAR{',
              'variable_end_string': '}',
              'comment_start_string': '\#{',
              'comment_end_string': '}',
              'line_statement_prefix': '%%',
              'line_comment_prefix': '%#',
              'trim_blocks': True,
              'autoescape': False }

import pdflatex

with open('my_file.tex', 'rb') as f:
    pdfl = pdflatex.PDFLaTeX.from_binarystring(f.read(), 'my_file')
pdf, log, cp = pdfl.create_pdf()

