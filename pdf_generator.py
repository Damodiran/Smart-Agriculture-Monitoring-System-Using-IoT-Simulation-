from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors


def margin(c):
    c.line(30, 30, 580, 30)  # top
    c.line(30, 30, 30, 758)  # left
    c.line(30, 758, 580, 758)  # bottom
    c.line(580, 758, 580, 30)  # right

def generate_pdf(moisture_data, temperature_data, humidity_data): 
    c = canvas.Canvas("report.pdf", pagesize=letter)
    margin(c)
    c.setFont("Courier-Bold", 25)
    c.drawString(218, 700, "Land Report ")
    c.setFont("Courier-Bold", 10)
    
    # Define the data for the table
    table_data = [["Humidity", "Temperature", "Moisture"]]
    for i in range(30):
        table_data.append([f"{humidity_data[i]}%", f"{temperature_data[i]}°C", f"{moisture_data[i]}%"])

    humidity_data[0]=60
    # Create the table
    table = Table(table_data)

    # Define style for the table
    style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.gray),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('FONTNAME', (0, 0), (-1, 0), 'Courier-Bold'),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                        ('GRID', (0, 0), (-1, -1), 1, colors.black)])

    # Apply style to the table
    table.setStyle(style)

    # Draw the table on the canvas
    table.wrapOn(c, 400, 200)
    table.drawOn(c, 200, 100)
  
   # send_email("report.pdf",receiver_email = "ndamodirann@gmail.com")

    c.save()

    #data(moisture_data)        

    return "report.pdf"
    