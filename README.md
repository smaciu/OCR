# OCR: extract text from scanned documents

Optical Character Recognition (OCR) is a technology used to convert different types of documents, such as scanned paper documents, PDF files, or images captured by a digital camera, into editable and searchable data. 


## Installing and Running

To clone and run this application, you'll need [Git](https://git-scm.com) and [Python](https://www.python.org/downloads/) installed on your computer. 

pdf_to_text.py accepts 3 arguments: 
- path_to_file: str
- start_page: int [ptional]
- end_page: int [optional]

If "**start_page**" and "**end_page**" argumenrs **are not selected**, the entire document is processed.

Extracted text is saved under **file_name**.txt under the path: "**path_to_scanned_pdf**".

Text of individual pages is saved under the directiory "file_name"

From your command line:

```
conda create --name ocr #create python virtual environment
conda activate ocr #activate the environment

$ git clone https://github.com/smaciu/OCR.git
$ cd ocr
$ pip install -r requirements.txt # install OCR packages
$ python pdf_to_text.py "path_to_scanned_pdf/file_name.pdf" 4 5 # extaract tecxt from 5th page
or
$ python pdf_to_text.py "path_to_scanned_pdf/file_name.pdf" # extract text from all pages

```

## Contact

Slawek Maciura 
email: slamaciu@icloud.com

## License

This project is licensed under the terms of the MIT license.
