from django.core.files.storage import storages
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from datetime import date, datetime
from reportlab.pdfbase import pdfmetrics
import textwrap

def process_stp(response, mode, branch, remittance, correspondant, refnumber, civilid, remittername, stp_reason, reissue_yn):
    pdfmetrics.registerFont(TTFont('Sen', 'Sen-ExtraBold.ttf'))
    stp_pdf = canvas.Canvas(response, pagesize=A4)
    path_to_img = "City Exchange_Logo_RGB.png"
    stp_pdf.drawImage(path_to_img,25, 725, 500, 100 )
    stp_pdf.line(25,720,600,720)

    stp_pdf.setFont("Sen", 12)
    stp_pdf.drawString(50, 670, f"Date: {date.today().strftime("%d-%m-%Y")}")
    stp_pdf.drawString(165, 670, str(datetime.now().strftime("%H:%M:%S")) )
    stp_pdf.drawString(50, 650, f"Mode: {mode}")
    stp_pdf.drawString(50, 630, f"Branch: {branch}")
    stp_pdf.drawString(50, 610, f"Remittance: {remittance}")
    stp_pdf.drawString(50, 590, f"Refnumber: {refnumber}")
    stp_pdf.drawString(50, 570, f"Correspondant: {correspondant}")
    stp_pdf.drawString(50, 550, f"Civil ID: {civilid}")
    stp_pdf.drawString(50, 530, f"Remitter Name: {remittername}")
    stp_pdf.drawString(50, 510, f"Stop Payment Reason: {stp_reason}")
    stp_pdf.drawString(50, 490, f"Reissue: {reissue_yn}")
    start_x = 50
    interval = 4
    start_y = 250
    for i in range(250):  # Adjust the range for how many asterisks you want
        stp_pdf.drawString(start_x + i * interval, start_y, "*")  # Draw an asterisk at each position
    stp_pdf.drawString(50,225, "I agree that City Exchange is not responsible for any costs or losses for funds incurred in doing this stop payment.")
    for i in range(250):  # Adjust the range for how many asterisks you want
        stp_pdf.drawString(start_x + i * interval, start_y, "*")
    stp_pdf.line(50,125,150,125)
    stp_pdf.line(200,125,350,125)
    stp_pdf.line(400,125,500,125)
    stp_pdf.drawString(50, 100,"Staff Signature")
    stp_pdf.drawString(200, 100,"Customer Signature")
    stp_pdf.drawString(400, 100,"HO Signature")
    stp_pdf.showPage()
    stp_pdf.save()

def process_recall(response, mode, branch, remittance, correspondant, refnumber, civilid, remittername, recall_reason):
    pdfmetrics.registerFont(TTFont('Sen', 'Sen-ExtraBold.ttf'))
    recall_pdf = canvas.Canvas(response, pagesize=A4)
    path_to_img = "City Exchange_Logo_RGB.png"
    recall_pdf.drawImage(path_to_img,25, 725, 500, 100 )
    recall_pdf.line(25,720,600,720)

    recall_pdf.setFont("Sen", 12)
    recall_pdf.drawString(50, 670, f"Date: {date.today().strftime("%d-%m-%Y")}")
    recall_pdf.drawString(165, 670, str(datetime.now().strftime("%H:%M:%S")) )
    recall_pdf.drawString(100, 650, f"Mode: {mode}")
    recall_pdf.drawString(100, 630, f"Branch: {branch}")
    recall_pdf.drawString(100, 610, f"Remittance: {remittance}")
    recall_pdf.drawString(100, 590, f"Refnumber: {refnumber}")
    recall_pdf.setFont("Sen", 12)
    recall_pdf.drawString(100, 570, f"Correspondant: {correspondant}")
    recall_pdf.drawString(100, 550, f"Civil ID: {civilid}")
    recall_pdf.drawString(100, 530, f"Remitter Name: {remittername}")
    recall_pdf.drawString(100, 510, f"Recall Reason: {recall_reason}")
    start_x = 50
    interval = 4
    start_y = 250
    for i in range(250):  # Adjust the range for how many asterisks you want
        recall_pdf.drawString(start_x + i * interval, start_y, "*")  # Draw an asterisk at each position
    recall_pdf.drawString(50,225, "I agree that City Exchange is not responsible for any costs or losses for funds recall due to incorrect details I provided.")
    start_y = 200
    for i in range(250):  # Adjust the range for how many asterisks you want
        recall_pdf.drawString(start_x + i * interval, start_y, "*")
    recall_pdf.line(50,125,150,125)
    recall_pdf.line(200,125,350,125)
    recall_pdf.line(400,125,500,125)
    recall_pdf.drawString(50, 100,"Staff Signature")
    recall_pdf.drawString(200, 100,"Customer Signature")
    recall_pdf.drawString(400, 100,"HO Signature")
    recall_pdf  .showPage()
    recall_pdf.save()

def process_amendment(response, mode, branch, remittance, correspondant, refnumber, civilid, remittername, amendment_field):
    pdfmetrics.registerFont(TTFont('Sen', 'Sen-ExtraBold.ttf'))
    path_to_img = "City Exchange_Logo_RGB.png"

    amend_pdf = canvas.Canvas(response, pagesize=A4)
    amend_pdf.drawImage(path_to_img,25, 725, 500, 100 )
    amend_pdf.line(25,720,600,720)

    amend_pdf.setFont("Sen", 12)
    amend_pdf.drawString(50, 670, f"Date: {date.today().strftime("%d-%m-%Y")}")
    amend_pdf.drawString(165, 670, str(datetime.now().strftime("%H:%M:%S")) )
    amend_pdf.setFont("Helvetica", 12)
    amend_pdf.drawString(100, 750, f"Mode: {mode}")
    amend_pdf.drawString(100, 730, f"Branch: {branch}")
    amend_pdf.drawString(100, 710, f"Remittance: {remittance}")
    amend_pdf.drawString(100, 690, f"Refnumber: {refnumber}")
    amend_pdf.drawString(100, 670, f"Correspondant: {correspondant}")
    amend_pdf.drawString(100, 650, f"Civil ID: {civilid}")
    amend_pdf.drawString(100, 630, f"Remitter Name: {remittername}")
    amend_pdf.drawString(100, 610, f"Amendment Field: {amendment_field}")
    amend_pdf.drawString(50, 500, "I agree that the City International Exchange Company will not be held responsible in any way in case the amendment is not carried out for any reasons, also I agree that City International Exchange Company will not be held responsible in case the funds are paid/credited before affecting the Amendment.")
    amend_pdf.line(50,125,150,125)
    amend_pdf.line(200,125,350,125)
    amend_pdf.line(400,125,500,125)
    amend_pdf.drawString(50, 100,"Staff Signature")
    amend_pdf.drawString(200, 100,"Customer Signature")
    amend_pdf.drawString(400, 100,"HO Signature")
    amend_pdf.showPage()
    amend_pdf.save()