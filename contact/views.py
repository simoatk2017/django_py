from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from smtplib import SMTPException
from django.core.mail import send_mail, BadHeaderError


def contact_me(request):
    if request.method == 'POST':
        print(request.POST.get('name'))
        try:
            print('sending.....')
            send_mail(
                'That’s your subject',
                'That’s your message body',
                'ggr_fi@hotmail.com',
                ['simoatk@yahoo.com', ],
                fail_silently=False,
            )
            # test = send_mail('Subject here', 'Here is the message.', 'simoatk@yahoo.com', ['simoatk@yahoo.com',])
            print('send.....(:')
        except BadHeaderError:  # If mail's Subject is not properly formatted.
            print('Invalid header found.')
        except SMTPException as e:  # It will catch other errors related to SMTP.
            print('There was an error sending an email.' + e)

        except Exception as err:  # It will catch All other possible errors.
            print("Mail Sending Failed! ", err)
        # set the variable initially created to True
        messageSent = True

    return render(request, 'contact/contact.html')
    # send the email to the
