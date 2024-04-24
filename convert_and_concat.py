import argparse
from pptxtopdf import convert
from pypdf import PdfMerger
import os

def main(input_dir, name_of_output_pdf):
        """
    Function that converts all pptx files in the specified input directory to pdf format, 
    merges them into a single pdf file, and saves the merged pdf file with the specified output name.

    Parameters:
    input_dir (str): The directory containing the pptx files to be converted. 
                     This should be a string representing the path to the directory.
    name_of_output_pdf (str): The name of the output pdf file. If the '.pdf' extension is not included, it will be appended.
                              If a file with this name already exists, the function will print an error message and exit.

    Returns:
    None

    Example usage:
    main('my_input_dir', 'my_output.pdf')
    """


    all_pdf_dir = "all_pdfs_nufix8Ybsgw"
    
    # if name_of_output_pdf does not end with .pdf, append it
    if not name_of_output_pdf.endswith('.pdf'):
        name_of_output_pdf = f"{name_of_output_pdf}.pdf"

    # if name_of_output_pdf already exists, print an error message and exit
    if os.path.exists(name_of_output_pdf):
        print(f"Error: {name_of_output_pdf} already exists. Either delete {name_of_output_pdf} and re-run, or give a different name for the output file.")
        return

    # check that all_pdf_dir exists and is empty
    if not os.path.exists(all_pdf_dir):
        os.makedirs(all_pdf_dir)
    else:
        for file in os.listdir(all_pdf_dir):
            os.remove(f"{all_pdf_dir}/{file}")
   
    convert(input_dir, all_pdf_dir)

    #  create a list of all the file names in the output directory
    pdf_files = [f for f in os.listdir(all_pdf_dir) if f.endswith('.pdf')]

    #  create a PdfMerger object
    merger = PdfMerger()

    #  loop through the list of file names and add each file to the merger object
    for pdf_file in pdf_files:
        merger.append(f"{all_pdf_dir}/{pdf_file}")

    merger.write(name_of_output_pdf)
    merger.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert pptx files to pdf and merge them')
    parser.add_argument('input_dir', type=str, help='the directory with pptx files')
    parser.add_argument('name_of_output_pdf', type=str, help='the name of the output pdf file')
    args = parser.parse_args()
    main(args.input_dir, args.name_of_output_pdf)