# Simple CV Creator

Simple CV Creator is a small Python project that generates a CV in PDF format.

The script creates a structured resume with sections for contact information, professional summary, education, technical skills, soft skills, languages, and additional information.

## Features

- Generates a PDF CV automatically
- Uses a simple section-based layout
- Supports custom fonts with `DejaVuSans.ttf`
- Creates a clean A4 document
- Easy to edit and adapt for another person

## Technologies

- Python
- ReportLab

## Project Structure

```text
Simple_CV_Creator/
├── CV_Creator.py
├── DejaVuSans.ttf
├── Maksim_Ivanouski_CV.pdf
└── Maksim_Ivanouski1_CV.pdf
```

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/maksimIvanouski/Simple_CV_Creator.git
```

2. Open the project folder:

```bash
cd Simple_CV_Creator
```

3. Install the required library:

```bash
pip install reportlab
```

4. Run the script:

```bash
python CV_Creator.py
```

After running the script, a PDF file will be generated in the project folder.

## How to Customize

To create your own CV, open `CV_Creator.py` and edit the text inside the sections. You can change personal information, skills, education, languages, and other details.

## Author

Maksim Ivanouski
