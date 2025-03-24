import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os
import sys

# Load environment variables from .env file
load_dotenv()

# Get credentials and recipient from .env
username = os.getenv("EMAIL_USERNAME").strip()
password = os.getenv("EMAIL_PASSWORD").strip()
recipient_email = os.getenv("EMAIL_RECIPIENT").strip()

# Compose the email
msg = EmailMessage()
msg["From"] = f"Follow-Up <{username}>"

msg["To"] = recipient_email
msg["Subject"] = "Abu Rmeileh Abd Elkarim"

msg.set_content("""Hi Abu Rmeileh Abd Elkarim,

I’m writing to kindly follow up regarding a few outstanding responsibilities we discussed earlier. I would really appreciate it if you could let me know how you plan to move forward with them.

Thanks in advance for your time and understanding. I’m happy to hear from you whenever you’re ready.
""")

msg.add_alternative("""
<html>
  <body style="background-color: #f4f4f4; padding: 30px; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">
    <div style="max-width: 600px; margin: auto; background-color: #fce8d5; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); padding: 30px;">
      <p style="font-size: 16px; color: #333;">Hi Abu Rmeileh Abd Elkarim,</p>

      <p style="font-size: 15px; color: #444; line-height: 1.6;">
        I’m writing to kindly follow up regarding a few outstanding responsibilities we discussed earlier.
        I would really appreciate it if you could let me know how you plan to move forward with them.
      </p>

      <p style="font-size: 15px; color: #444; line-height: 1.6;">
        Thanks in advance for your time and understanding. I’m happy to hear from you whenever you’re ready.
      </p>

      <div style="margin-top: 30px; background-color: #000; color: #fff; border-radius: 8px; padding: 15px 20px;">
        <p style="margin: 0;">Sincerely,<br>
        Damian Rychlicki<br>
        </p>
      </div>
    </div>
  </body>
</html>
""", subtype='html')



# Send the email

# Validate environment variables
if not username or not password or not recipient_email:
    print("❌ Error: Missing required environment variables (EMAIL_USERNAME, EMAIL_PASSWORD, EMAIL_RECIPIENT).")
    sys.exit(1)
try:
    with smtplib.SMTP("mail.privateemail.com", 587) as server:
        server.starttls()
        server.login(username, password)
        server.send_message(msg)
        print("Email sent successfully.")
except Exception as e:
    print(f"Failed to send email: {e}")
