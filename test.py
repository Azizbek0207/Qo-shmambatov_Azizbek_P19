from random import randint

from django.core.mail import send_mail

subject = 'Tasqilash kodi'
message = str(randint(1, 1000))
from_email = 'sjushebaxizu@gmail.com'
to_email = 'abbosxanamriyev@gmail.com'
send_mail(subject, message, from_email, to_email)
