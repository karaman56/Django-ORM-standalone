import os

import django
  
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard

passcards = Passcard.objects.all()
active_passcards = Passcard.objects.filter(is_active=True)
active_passcards_count = active_passcards.count()

if __name__ == '__main__':

    print('Количество пропусков:', Passcard.objects.count())
    print('Количество активных пропусков:',active_passcards_count)