
from django.shortcuts import render
from django.http import HttpResponse
from .tasks import send_sms
from .forms import SMSSendForm


def send_sms_view(request):
    if request.method == 'POST':
        form = SMSSendForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            send_sms.delay(phone_number)
            return HttpResponse("SMS надіслано асинхронно.")
    else:
        form = SMSSendForm()
    return render(request, 'send_sms.html', {'form': form})

