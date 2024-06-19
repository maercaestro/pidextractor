import streamlit as st
from PIL import Image
from pdf2image import convert_from_path
import pytesseract
import re
import pandas as pd

# Function to convert PDF to text using Tesseract
def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        images = convert_from_path(pdf)
        for image in images:
            text += pytesseract.image_to_string(image)
    return text

def main():
    st.set_page_config(page_title="MEGAT P&ID Extractor")
    image = Image.open('MEGATLogo.png')

    # Define the scale factor
    scale_factor = 0.25  # Replace with the desired scale factor

    # Calculate the new dimensions based on the scale factor
    new_width = int(image.width * scale_factor)
    new_height = int(image.height * scale_factor)

    # Resize the image
    resized_image = image.resize((new_width, new_height))

    st.image(resized_image)
    st.title("MEGAT P&ID Extractor")
    st.write("Use the app to extract all information from the P&ID")

    raw_text = ""

    with st.sidebar:
        st.subheader("You can upload your P&ID Document here and it will extract the line number for you")
        pdf_docs = st.file_uploader("Upload your PDFs here and click on Process", accept_multiple_files=True)
        if st.button("Process"):
            with st.spinner("Processing"):
                # Get the text from PDF
                raw_text = get_pdf_text(pdf_docs)

    # Find matching pattern
    pattern = re.compile(r'\x83"')  # Match one or more characters in the "Symbol, Other" range
    new_text = re.sub(pattern, '0."', raw_text)

    pattern = re.compile(r'\d{1}"-[a-zA-Z]+\d+-\w+-[a-zA-Z]{2}')
    pattern2 = re.compile(r'0."-[a-zA-Z]+\d+-\w+-[a-zA-Z]{2}')

    # Search for the pattern in the input text
    matches = pattern.findall(new_text)
    matches2 = pattern2.findall(new_text)

    # Combine the matches into a single data
    combine = matches + matches2

    # Create additional columns for size columns
    size1 = [s[0] for s in matches]
    size2 = [0.75 for s in matches2]
    size_combine = size1 + size2

    # Create additional columns for process type
    process_type1 = [p[3:5] for p in matches]
    process_type2 = [p[4:6] for p in matches2]
    process_combine = process_type1 + process_type2

    # Create additional columns for insulation type
    insulation_type = [i[-2:] for i in combine]

    # Create a pandas dataframe
    df = pd.DataFrame({
        'Line Number': combine,
        'Pipe Size': size_combine,
        'Process': process_combine,
        'Insulation Type': insulation_type
    })

    st.write(df)

    # Read that dataframe to CSV
    csv = df.to_csv(index=False).encode('utf-8')

    st.download_button("Press to Download", csv, "PIDLine.csv", "text/csv", key='download-csv')

if __name__ == '__main__':
    main()
