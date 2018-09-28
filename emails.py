import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from settings import *

def send_result_by_email(self):
    # todo: use a gmail address
    fromaddr = EMAIL_FROM
    # todo: use any address
    toaddr = EMAIL_TO
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Daya"
    body = "something"
    msg.attach(MIMEText(body, 'plain'))

    # todo: work on the path here
    path = ?????

    attachment = open(path, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % EXCEL_FILENAME)

    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # todo: password
    server.login(fromaddr, EMAIL_PASSWORD)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
