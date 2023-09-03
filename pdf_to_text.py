import sys
from PIL import Image
import pytesseract
from pdf2image import convert_from_path
import os
from tqdm import tqdm

def main(pdf_path, start_page=None, end_page=None):
    file_name = pdf_path.split('.')[0]

    # Convert pages of the PDF to images
    if start_page and end_page:
        pages = convert_from_path(pdf_path, 500, first_page=int(start_page), last_page=int(end_page))
    else:
        pages = convert_from_path(pdf_path, 500)

    print(f'{file_name} has: {len(pages)} pages.')

    # Create a directory to store the images
    if not os.path.exists(file_name):
        os.makedirs(file_name)

    # Initialize an empty string to store text
    book_text = ""

    # Loop through the list of images and perform OCR
    for i, page in enumerate(tqdm(pages, desc="Processing pages")):
        image_path = f'{file_name}/page_{i+1}.png'
        page.save(image_path, 'PNG')
        
        # Perform OCR on the saved image
        text = pytesseract.image_to_string(Image.open(image_path))

        # Append the text to book_text
        book_text += text
        
        # Save the extracted text to a text file for each page
        text_file_path = f'{file_name}/page_{i+1}.txt'
        with open(text_file_path, 'w') as f:
            f.write(text)
        
    # Save the extracted text to a text file
    with open(f'{file_name}.txt', 'w') as f:
        f.write(book_text)

    print(f'Printed extracted the entire text to {file_name}.txt')

if __name__ == "__main__":
    pdf_path = sys.argv[1]
    start_page = sys.argv[2] if len(sys.argv) > 2 else None
    end_page = sys.argv[3] if len(sys.argv) > 3 else None
    main(pdf_path, start_page, end_page)
