#!/usr/bin/python3

from datetime import datetime
import logging
import smtplib
from tqdm import tqdm
import base64
from pathlib import Path

logging.basicConfig(filename='reportLOGS.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S %p %Z')

def send_mail(rep_date, rep_time):
    print(rep_time)

    print("\n")

    pbar = tqdm(total=100, ascii=True, desc="Mailing")

    display_time = rep_time if (rep_time != '16') else 4

    display_am_pm = 'AM' if (rep_time != '16') else 'PM'

    # filename = f'{str(Path.cwd())}/OUTPUT/Route Report ({datetime.now().strftime("%d-%m-%Y")}) {display_time} {display_am_pm}.xlsx'

    filename = f'{str(Path.cwd())}/OUTPUT/alarms.xlsx'

    # Read a file and encode it into base64 format
    fo = open(filename, "rb")
    filecontent = fo.read()
    encodedcontent = base64.b64encode(filecontent)  # base64

    sender = 'routereports@truesecurity.co.tz'
    receivers = ['routereports@truesecurity.co.tz, routereports@truesecurity.co.tz']

    marker = "AUNIQUEMARKER"

    body ="""
    This is a test email to send an attachement.
    """
    # Define the main headers.
    part1 = """From: Route Reports <routereports@truesecurity.co.tz>
    To: Michael Francis <youraveragecoder@gmail.com>
    Subject: %s
    MIME-Version: 1.0
    Content-Type: multipart/mixed; boundary=%s
    --%s
    """ % (filename, marker, marker)

    # Define the message action
    part2 = """Content-Type: text/plain
    Content-Transfer-Encoding:8bit

    %s
    --%s
    """ % (body,marker)

    # Define the attachment section
    part3 = """Content-Type: multipart/mixed; name=\"%s\"
    Content-Transfer-Encoding:base64
    Content-Disposition: attachment; filename=%s

    %s
    --%s--
    """ %(filename, filename, encodedcontent, marker)
    message = part1 + part2 + part3

    try:
        smtpObj = smtplib.SMTP_SSL('mail.truesecurity.co.tz', 465)
        pbar.update(20)
        smtpObj.ehlo()
        pbar.update(20)
        smtpObj.login('routereports@truesecurity.co.tz', 'TrueReports123!')
        pbar.update(20)
        smtpObj.sendmail(sender, receivers, message)   
        pbar.update(20)
        smtpObj.quit()      
        pbar.update(20)
        pbar.close()
        print("Successfully sent email\n")
    except Exception as e:
        print(e)
        logging.debug('ERROR')
        logging.debug(e)
        print("Error: unable to send email\n")
        return False


    return True

