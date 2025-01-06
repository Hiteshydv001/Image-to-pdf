from flask import Flask, render_template, request, send_file, jsonify
import os
from werkzeug.utils import secure_filename
from reportlab.pdfgen import canvas
from PIL import Image

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_images():
    uploaded_files = request.files.getlist("images")
    image_names = []

    for uploaded_file in uploaded_files:
        if uploaded_file and allowed_file(uploaded_file.filename):
            filename = secure_filename(uploaded_file.filename)
            image_names.append(filename)
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            uploaded_file.save(image_path)

    return jsonify(image_names=image_names)

@app.route('/convert', methods=['POST'])
def convert_images_to_pdf():
    uploaded_files = request.files.getlist("images")
    output_pdf_name = request.form.get("pdf_name", "output") + ".pdf"
    output_pdf_path = os.path.join(app.config['UPLOAD_FOLDER'], output_pdf_name)

    if not uploaded_files:
        return "No files uploaded. Please select images to upload.", 400

    # Margin in points
    margin = 36
    page_width, page_height = 612, 792

    # Create PDF
    pdf = canvas.Canvas(output_pdf_path, pagesize=(page_width, page_height))
    for uploaded_file in uploaded_files:
        if uploaded_file and allowed_file(uploaded_file.filename):
            filename = secure_filename(uploaded_file.filename)
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            uploaded_file.save(image_path)

            image = Image.open(image_path)
            available_width = page_width - (2 * margin)
            available_height = page_height - (2 * margin)

            scale_factor = min(available_width / image.width, available_height / image.height)
            new_width = image.width * scale_factor
            new_height = image.height * scale_factor

            x_position = margin + (available_width - new_width) / 2
            y_position = margin + (available_height - new_height) / 2

            pdf.setFillColorRGB(1, 1, 1)
            pdf.rect(0, 0, page_width, page_height, fill=True, stroke=False)
            pdf.drawInlineImage(image_path, x_position, y_position, width=new_width, height=new_height)
            pdf.showPage()

    pdf.save()

    return send_file(output_pdf_path, as_attachment=True)

def allowed_file(filename):
    allowed_extensions = {'png', 'jpg', 'jpeg'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

if __name__ == '__main__':
    app.run()
