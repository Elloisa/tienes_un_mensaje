"""
Created on Monday April 24 23:37:00 2023

@author: @Elloisa

"""

#STARTING A SECURE SMTP CONNECTION==============================================================================
import smtplib, ssl
import pandas

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
            receiver_email = df.iloc[i]['email']
            message = f"""\
            Subject: Hi there

            {df.iloc[i]['Mensaje']}"""
            server.sendmail(sender_email, receiver_email, message)

    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit() 

