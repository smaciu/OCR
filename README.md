# OCR to extract text from scanned documents

Optical Character Recognition (OCR) is a technology used to convert different types of documents, such as scanned paper documents, PDF files, or images captured by a digital camera, into editable and searchable data. 


## Installing and Running

To clone and run this application, you'll need [Git](https://git-scm.com) and [Python](https://www.python.org/downloads/) installed on your computer. 

pdf_to_text.py accepts 3 arguments: 
- path to file: str
- start_page: int [ptional]
- end_page: int [optional]

If start and end page argumenrs **are not selected**, entire document is extracted.

From your command line:

```
conda create --name ocr
conda activate ocr

$ git clone https://github.com/smaciu/OCR.git
$ cd ocr
$ pip install -r requirements.txt
$ python pdf_to_text.py "path_to_scanned_pdf/file_name.pdf" 4 5

```

## Contact

Slawek Maciura 
email: slamaciu@icloud.com

## License

This project is licensed under the terms of the MIT license.
