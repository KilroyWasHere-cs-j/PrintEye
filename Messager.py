import smtplib
import UI


def Send_Email(message):
    receiver = UI.Query_Config("email - ")
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login("printeye2021@gmail.com", "PrintEyeAdmin")  # Need to find a way to make this secretive
    server.sendmail("printeye2021@gmail.com", receiver, message)
    server.quit()
    print("Message Sent")


def Send_SMS(receiver, message):
    print("Not working")
    # this may never be used


def Hello():
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login("printeye2021@gmail.com", "PrintEyeAdmin")
    server.sendmail("printeye2021@gmail.com", UI.Query_Config("email - "), "Hello Welcome to print eye")
    print("Sent")
