import smtplib

sender = "<from@example.com>"
receiver = "<rebob78552@huvacliq.com>"

message = f"""\
Subject: Hi Mailtrap
To: {receiver}
From: {sender}

This is a test e-mail message."""

with smtplib.SMTP("sandbox.smtp.mailtrap.io", 2525) as server:
    server.login("6a60c837e8f376", "699555b4d6d5d9")
    server.sendmail(sender, receiver, message)