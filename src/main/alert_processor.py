import yagmail
from constants import EMAIL_PASSWORD, RECEIVER_MAIL, SENDER_MAIL


class AlertProcessor:
    default_receiver = RECEIVER_MAIL
    default_body = "Hello there from Yagmail"
    sender_email = SENDER_MAIL
    default_subject = "Yagmail test with attachment"

    def __init__(self, receiver=default_receiver, body=default_body, subject=default_subject,
                 yag=yagmail.SMTP(sender_email, EMAIL_PASSWORD)):
        self.receiver = receiver
        self.body = body
        self.subject = subject
        self.yag = yag

    def send_mail(self,**kwargs) -> None:
        if kwargs:
            customsubject=kwargs['customsubject']
            customcontents=kwargs['customcontents']
        else:
            customcontents=self.body
            customsubject=self.subject
        self.yag.send(
            to=self.receiver,
            subject='WFH Status for {} '.format(customsubject),
            contents=customcontents
        )
