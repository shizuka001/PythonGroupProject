import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, content):
    # Set your email and password
    #user can add the sender email, password and recipient accordingly.
    #it has been removed by the project members for the purpose of safety and security and and be demostrated on request.
    sender_email = ""
    sender_password = ""
    recipient = ""

    
    # Create the MIME object
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient
    message["Subject"] = subject

    # Add the email body
    body = content + "\nRegards,\nSakshi"
    message.attach(MIMEText(body, "plain"))

    # Establish a connection to the SMTP server (in this case, Gmail's SMTP server)
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        # Start the TLS connection
        server.starttls()

        # Log in to the email account
        server.login(sender_email, sender_password)

        # Send the email
        server.sendmail(sender_email, recipient, message.as_string())

    print("Email sent successfully.")
    return(1)
