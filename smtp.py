#!/usr/bin/env python3
"""Script to send dummy emails using Python features"""

import smtplib

FROM = "user@from.domain.com"
TO = ["user@to.domain.com"]
SUBJECT = "Hey! I'm sending an email to you!"
HOST = "mail.server.com"
PORT = 999
PASSWORD = ""  # get the password somehow
message = f"""\
From: {FROM}
To: {', '.join(TO)}
Subject: {SUBJECT}

This is an email sent using Python programming language.
"""
if __name__ == "__main__":
    with smtplib.SMTP(host=HOST, port=PORT) as smtp_server:
        smtp_server.starttls()
        smtp_server.login(FROM, PASSWORD)
        smtp_server.sendmail(FROM, TO, message.encode("utf-8"))
