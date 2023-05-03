"""
Created on Monday April 24 23:37:00 2023

@author: @Elloisa

"""

#STARTING A SECURE SMTP CONNECTION==============================================================================

import smtplib, ssl
import pandas
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

   

smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "unnilorena@gmail.com"
password = "mmme aahd lexu ruhw"

# Create a secure SSL context
context = ssl.create_default_context()

# Try to log in to server and send email
with smtplib.SMTP(smtp_server, port) as server:
    
    server.starttls(context=context)
    server.login(sender_email, password)

    df = pandas.read_csv('C:\\Users\\CASA\\Portafolio\\digital_NAO\\tienes_un_mensaje\\lista_correos.csv', delimiter = ';', index_col = "Nombre")
             
    try:
        for i in range(len(df)):
            message = MIMEMultipart("alternatives")
            message['Subject'] = 'HAPPY BIRTHDAY!'
            message['from'] = sender_email
            receiver_email = df.iloc[i]['email']

            htmlText="""/
                    <!DOCTYPE html>
                    <html lang="en">
                        <head>
                            <meta charset="UTF-8">
                            <meta name="viewport" content="width-device-width, initial-scale=1.0">
                            <link rel="stylesheet" href="https://github.com/Elloisa/tienes_un_mensaje/blob/main/index.css">
                            <link rel="preconnect" href="https://fonts.gstatic.com">
                            <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Tangerine">
                            <title>Happy Birthday</title>
                        </head>
                        <body>
                            <div class="card">
                                <img src="https://raw.githubusercontent.com/Elloisa/tienes_un_mensaje/3400523c368fb8e2cb9bd4823153d33b09235522/birthday.svg" alt="birthday" class="birthday">
                                <div class="text">
                                    <h1>Happy Birthday</h1>
                                    <p>I hope you have a wonderful birthday</p>
                                    <p class="muted">- WELCOME AGAIN TO OUR FAMILY</p>
                                </div>
                                <div class="space"></div>
                            </div>
                        </body>
                    </html>

                    """
            
            #htmlPart = MIMEMultipart(htmlText, 'html')
            htmlPart = MIMEText(htmlText, 'html')

            message.attach(htmlPart)
            server.sendmail(sender_email, receiver_email, message.as_string())

    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit() 