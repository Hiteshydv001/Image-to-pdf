Image to PDF Converter
This is a simple web application built using Flask that allows users to upload 
multiple image files (JPG, PNG, JPEG) and convert them into a PDF. The user can choose 
the output PDF name, and the images will be inserted into the PDF, each centered on its 
own page.
Features
- Upload multiple image files.
- Select a custom name for the output PDF file.
- The images are automatically resized to fit within the standard A4 size (8.5" x 11").
- Each image is centered on a separate page in the PDF.
Technologies Used
- Flask: Python-based web framework.
- HTML/CSS: For the frontend interface.
- ReportLab: For PDF generation.
- Pillow: For image processing.
Installation
### Prerequisites
Ensure you have the following installed:
- Python (>= 3.6)
- pip (Python package manager)
### Steps
1. Clone the repository to your local machine:
```bash
git clone https://github.com/Hiteshydv001/Image-to-pdf.git
```
2. Navigate into the project directory:
```bash
cd Image-to-pdf
```
3. Install the required Python libraries:
```bash
pip install -r requirements.txt
```
4. Run the Flask app:
```bash
python app.py
```
The app will start on `http://127.0.0.1:5000/`.
How to Use
1. Go to the home page of the app.
2. Click on the "Drag & Drop Your Images Here or Click to Upload" area to upload your image files (JPG, PNG, or JPEG).
3. Enter a name for the output PDF.
4. Click on the **Convert to PDF** button to generate and download the PDF file containing the uploaded images.
Contributing
Feel free to fork this repository and submit issues or pull requests. If you have any 
suggestions for improvements or enhancements, please let me know!
License
This project is licensed under the MIT License - see the LICENSE file for details.
Made with ❤️ by [Hitesh](https://github.com/Hiteshydv001).
