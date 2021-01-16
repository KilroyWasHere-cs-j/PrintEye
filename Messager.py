import smtplib


def Send_Email(receiver, message):
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login("emmanoaa945@gmail.com", "ThisIsEmma")
    server.sendmail("emmanoaa945@gmail.com", receiver, message)
    server.quit()
