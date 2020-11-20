import smtplib, ssl

port = 465
sender_email = "my@gmail.com"
receiver_email = "your@gmail.com"
password = input("Type your password and press enter: ")
message = """\
Subject: Hi there

The weather is good in germany

Mit freundlichen Grüßen
Luca Isenburg
"""

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)








