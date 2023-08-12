import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path


html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = 'Mail Tester'
email['to'] = 'hemakulate28@gmail.com'
email['subject'] = 'You won a million dollars!'

email.set_content(html.substitute({'name': 'Shola'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()  # Start TLS encryption
    smtp.login('hemarkmailtester@gmail.com', '08148337000')
    smtp.send_message(email)
    print('all good boss!')



# email = EmailMessage()
# email['from'] = 'Mail Tester'
# email['to'] = 'hemakulate28@gmail.com'
# email['subject'] = 'You won a million dollars!'

# email.set_content("I'm a Python developer")

# with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
#     smtp.ehlo()
#     smtp.starttls()  # Start TLS encryption
#     smtp.login('hemarkmailtester@gmail.com', '08148337000')
#     smtp.send_message(email)
#     print('all good boss!')
    # smtp.login('zerotomastery')
