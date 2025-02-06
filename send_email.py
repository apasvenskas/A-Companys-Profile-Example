import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "audrius13toto@gmail.com"
    password = "cqdx bfes xmyt zxuo"

    receiver = "audrius13toto@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)