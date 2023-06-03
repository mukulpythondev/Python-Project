#This project help us to send mails in large number in very short time 
import smtplib

smtp_server = "smtp.gmail.com"
smtp_port = 587
sender_email = "mukulgenious123@gmail.com"
sender_password = "drjgedhlehatgynl"
recipient_email = "wpdevmukul@gmail.com"
subject = "Python test"
body = "I love Python"
message = f"Subject: {subject}\n\n{body}"

try:
    # Create an SMTP object
    obj = smtplib.SMTP(smtp_server, smtp_port)
    
    # Identify yourself to the server
    obj.ehlo()
    
    # StartTLS for secure connection
    obj.starttls()
    
    # Login to your Gmail account
    obj.login(sender_email, sender_password)
    
    # Send the email
    obj.sendmail(sender_email, recipient_email, message)
    
    print("Email sent successfully!")
    
except Exception as e:
    print("An error occurred while sending the email:", str(e))

finally:
    # Close the connection
    obj.quit()
