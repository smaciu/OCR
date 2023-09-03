# OCR to extract text from scanned documents

Optical Character Recognition (OCR) is a technology used to convert different types of documents, such as scanned paper documents, PDF files, or images captured by a digital camera, into editable and searchable data. Here's a simplified explanation of how OCR generally works:

Steps in OCR:

Preprocessing:

The image is preprocessed to improve the OCR results. Preprocessing steps can include converting the image to grayscale, resizing, and applying techniques like thresholding and noise removal.
Text Localization:

The algorithm identifies the regions of the image where text is present. This is important in documents where text and non-text elements (like images and graphs) are mixed.
Text Segmentation:

The localized text regions are further broken down into lines, words, and then into individual characters. This is often one of the most challenging steps, especially for languages where characters can be connected or vary significantly in size and shape.
Character Recognition:

Each segmented character is then recognized individually. This is typically done using machine learning algorithms that have been trained on thousands of examples of each character. The algorithm identifies the character that most closely matches the segmented image.
Post-processing:

After characters are recognized, post-processing steps like spell-checking and context analysis can be applied to correct any errors and improve accuracy.
Output Generation:

Finally, the recognized text is output in a structured format. This could be a simple text file, an annotated image, or more complex structures like tables and forms, depending on the application.
Technologies and Algorithms:

Template Matching: Early OCR systems used template matching, where each character is compared to a set of templates.

Feature Extraction: Modern systems use feature extraction, where characteristics like lines, loops, and intersections are extracted from the image of each character for recognition.

Machine Learning: Advanced OCR systems use machine learning algorithms, including neural networks, to improve accuracy and adapt to different fonts and styles.

Natural Language Processing (NLP): Some OCR systems use NLP techniques for post-processing to improve recognition results based on the context and semantics of the text.

In the case of pytesseract, the library is a Python binding for Google's Tesseract-OCR Engine, which is one of the most accurate open-source OCR engines available. It uses a combination of the above techniques, including machine learning algorithms trained on a large dataset of text in various languages, fonts, and formats.

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
