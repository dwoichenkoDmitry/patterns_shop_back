from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import smtplib
from email.mime.text import MIMEText
from email.header import Header


# Create your views here.
@api_view(['POST'])
def customers_list(request):
    if request.method == 'POST':
        from django.contrib.auth.models import User
        user = User.objects.create_user(username=request.data['login'],
                                        email=request.data['mail'],
                                        password=request.data['password'])
        user.save()
        return Response({'data': user}, status=status.HTTP_201_CREATED)


def sendMailRegistration(request):
    if request.method == 'POST':
        print("___request___")
        print(request.POST)
        # sender = "dwoichenko@mail.ru"
        # password = "JchUzAv7tnb7aTgthVVk"
        # code = "QWERT"
        # server = smtplib.SMTP("smtp.mail.ru", 587)
        # server.starttls()
        #
        # msg = MIMEText(f'{code}', 'plain', 'utf-8')
        # msg['Subject'] = Header('Код авторизации', 'utf-8')
        return ([{'result': "send"}])
        # print("send")
        # try:
        #     server.login(sender, password)
        #     server.sendmail(sender, "dwoichenko@yandex.ru", msg.as_string())
        #     return ([{'result': "send"}])
        # except Exception as ex:
        #     print(ex)
        # finally:
        #     server.quit()

