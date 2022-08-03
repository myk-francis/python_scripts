#!/usr/bin/python3


import email, smtplib, ssl
import logging
from tqdm import tqdm
from pathlib import Path
from datetime import datetime
import shutil


from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

logging.basicConfig(filename='reportLOGS.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S %p %Z')


def send_mail(rep_date, rep_time):

    pbar = tqdm(total=100, ascii=True, desc="Mailing")

    display_time = rep_time if (rep_time != '16') else 4

    display_am_pm = 'AM' if (rep_time != '16') else 'PM'

    file_path = f'Route Report ({datetime.now().strftime("%d-%m-%Y")}) {display_time} {display_am_pm}.xlsx'


    subject = f'Route Report ({datetime.now().strftime("%d-%m-%Y")}) {display_time} {display_am_pm}'
    body = f'Route Report ({datetime.now().strftime("%d-%m-%Y")}) {display_time} {display_am_pm}'
    sender_email = "routereports@truesecurity.co.tz"
    # receiver_email = ['routereports@truesecurity.co.tz' ,'cr_gps1@truesecurity.co.tz', 'zoraiz@truesecurity.co.tz', 'Marcus.Selemani@impalaterminals.com', 'Samuel.Kyungu@impalaterminals.com', 'ally@truesecurity.co.tz', 'TTDeskAfrica@impalaterminals.com', 'ImpalaLBBOps@impalaterminals.com']
    receiver_email = ['routereports@truesecurity.co.tz' ,' cr_gps1@truesecurity.co.tz', 'zoraiz@truesecurity.co.tz']
    password = "TrueReports123!"

    pbar.update(20)

    try:
        # Create a multipart message and set headers
        message = MIMEMultipart()
        message["From"] = sender_email
        #message["To"] = "zoraiz@truesecurity.co.tz, Marcus.Selemani@impalaterminals.com, Samuel.Kyungu@impalaterminals.com, ally@truesecurity.co.tz, TTDeskAfrica@impalaterminals.com, ImpalaLBBOps@impalaterminals.com"
        message["To"] = "routereports@truesecurity.co.tz , cr_gps1@truesecurity.co.tz, zoraiz@truesecurity.co.tz"
        message["Subject"] = subject
        message["Cc"] = "cr_gps1@truesecurity.co.tz, routereports@truesecurity.co.tz" 

        pbar.update(20)

        # Add body to email
        message.attach(MIMEText(body, "plain"))

        filename = file_path

        # Open PDF file in binary mode
        with open(filename, "rb") as attachment:
            # Add file as application/octet-stream
            # Email client can usually download this automatically as attachment
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        pbar.update(20)

        # Encode file in ASCII characters to send by email    
        encoders.encode_base64(part)

        # Add header as key/value pair to attachment part
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename}",
        )

        # Add attachment to message and convert message to string
        message.attach(part)
        text = message.as_string()

        pbar.update(20)

        # Log in to server using secure context and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("mail.truesecurity.co.tz", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, text)

        pbar.update(20)
        pbar.close()
        print("Email Sent Successfully\n")

    except Exception as e:
        print(e)
        logging.debug('--------------------ERROR------------------------------')
        logging.debug(e)
        print("Error: Unable to send email\n")
        return False
    else:
        shutil.move(file_path, 'OUTPUT/' + file_path)
        return True


    
