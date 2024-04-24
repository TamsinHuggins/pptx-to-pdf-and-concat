# PowerPoint to PDF Converter and Merger
Allows you to convert all PowerPoint (.pptx) files in a specified directory to PDF format, and then merges them into a single PDF file.
Useful for consolidating multiple presentations into one PDF document for distrubution,

## Requirements
argparse - For parsing command line options
pptxtopdf - For converting PowerPoint files to PDF (ensure you have this installed or replace it with your preferred library)
pypdf - For merging PDF files

To install requirements:

```
pip install -r requirements.txt
```

Usage
To use this script, follow the steps below:
Ensure all .pptx files that need to be converted are placed in a single directory.
Run the script using the command line by providing the directory of PowerPoint files and the desired output PDF file name.


```
python pptx_to_pdf_merger.py <input_directory> <output_file_name.pdf>

```
