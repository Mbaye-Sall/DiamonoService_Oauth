import random
from django.core.mail import send_mail
from django.conf import settings
from authServ.models import UserAccount


def sendMail(email):
    """opt_set = [x for x in range(10)]
    opt_item = []

    for i in range(6):
        num = random.choice(opt_set)
        opt_item.append(num)

    otp_code = "".join(str(item) for item in opt_item)

    opt = otp_code"""

    otp = random.randint(1000, 9999)

    subject = "email verification"
    message = "your code is " + str(otp)
    email_from = settings.EMAIL_HOST
    send_mail(subject, message, email_from, [email], fail_silently=False)

    user = UserAccount.objects.get(email=email)
    user.opt = str(otp)

    user.save()






