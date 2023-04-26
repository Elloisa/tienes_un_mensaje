"""
Created on Monday April 24 23:37:00 2023

@author: @Elloisa

"""

#STARTING A SECURE SMTP CONNECTION==============================================================================

import smtplib, ssl

smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "unnilorena@gmail.com"
receiver_email = "lorena.tito.ramos@gmail.com"
password = input("Type your password and press enter: ")
message = """\
Subject: Hi there

This message is sent from Python."""

# Create a secure SSL context
context = ssl.create_default_context()


# Try to log in to server and send email
with smtplib.SMTP(smtp_server, port) as server:
    server.starttls(context=context)
    server.login(sender_email, password)

    try:
        server.sendmail(sender_email, receiver_email, message)

    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit() 

