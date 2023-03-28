# pip install FPDF

from fpdf import FPDF
import requests

url = 'https://jsonplaceholder.typicode.com/todos'

# Make a request to the API
response = requests.get(url)
data = response.json()

# Create a new PDF object
pdf = FPDF()

# Add a page
pdf.add_page()

# Set the font and font size
pdf.set_font("Arial", size=12)

# Set the header row
pdf.cell(20, 10, "User ID", border=1)
pdf.cell(15, 10, "ID", border=1)
pdf.cell(135, 10, "Title", border=1)
pdf.cell(25, 10, "Status", border=1)
pdf.ln()

# Add the data rows
# here 20 is width of the cell and 10 is height of the cell
"""
pdf.ln() is a method of the FPDF class in the fpdf library, used to move the current position to the next line.
It is used to add a new line after each row of data when generating a PDF document.
"""
for row in data:
    pdf.cell(20, 10, str(row["userId"]), border=1)
    pdf.cell(15, 10, str(row["id"]), border=1)
    pdf.cell(135, 10, row["title"], border=1)
    pdf.cell(25, 10,  str(row["completed"]), border=1)
    pdf.ln()

# Save the PDF
pdf.output("output.pdf")





------------------------------------------------------------------------------------------



# Add background color for entire page



from fpdf import FPDF
import requests

url = 'https://jsonplaceholder.typicode.com/todos'

# Make a request to the API
response = requests.get(url)
data = response.json()

class MyPDF(FPDF):
    def header(self):
        # Set background color
        self.set_fill_color(173, 216, 230)
        self.rect(0, 0, self.w, self.h, 'F')

# Create a new PDF object
pdf = MyPDF()

# Add a page
pdf.add_page()

# Set the font and font size
pdf.set_font("Arial", size=12)

# Set the header row
pdf.cell(20, 10, "User ID", border=1)
pdf.cell(15, 10, "ID", border=1)
pdf.cell(135, 10, "Title", border=1)
pdf.cell(25, 10, "Status", border=1)
pdf.ln()

# Add the data rows
# here 20 is width of the cell and 10 is height of the cell
"""
pdf.ln() is a method of the FPDF class in the fpdf library, used to move the current position to the next line.
It is used to add a new line after each row of data when generating a PDF document.
"""
for row in data:
    pdf.cell(20, 10, str(row["userId"]), border=1)
    pdf.cell(15, 10, str(row["id"]), border=1)
    pdf.cell(135, 10, row["title"], border=1)
    pdf.cell(25, 10,  str(row["completed"]), border=1)
    pdf.ln()

# Save the PDF
pdf.output("output.pdf")

-----------------------------------------------------------------------------------------------------------------------

# background color for header row

from fpdf import FPDF
import requests

url = 'https://jsonplaceholder.typicode.com/todos'

# Make a request to the API
response = requests.get(url)
data = response.json()

# Create a new PDF object
pdf = FPDF()

# Add a page
pdf.add_page()

# Set the font and font size
pdf.set_font("Arial", size=12)

# Set the background color to white
pdf.set_fill_color(255, 255, 255)

# Set the header row
pdf.set_fill_color(173, 216, 230)  # Set background color for header row
pdf.cell(20, 10, "User ID", border=1, fill=True)
pdf.cell(15, 10, "ID", border=1, fill=True)
pdf.cell(135, 10, "Title", border=1, fill=True)
pdf.cell(25, 10, "Status", border=1, fill=True)
pdf.ln()
pdf.set_fill_color(0, 255, 255)  # Set background color back to white

# Add the data rows
for row in data:
    pdf.cell(20, 10, str(row["userId"]), border=1)
    pdf.cell(15, 10, str(row["id"]), border=1)
    pdf.cell(135, 10, row["title"], border=1)
    pdf.cell(25, 10,  str(row["completed"]), border=1)
    pdf.ln()

# Save the PDF
pdf.output("output.pdf")
