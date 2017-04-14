import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

msg = MIMEText('Hello Jane!','html')
msg['Subject'] = 'Test'
msg['From'] = 'John Doe <"john@example.com">'
msg['To'] = 'jane@example.com'

s = smtplib.SMTP('localhost')
s.sendmail(str(msg['From']), str(msg['To']), msg.as_string())
s.quit()