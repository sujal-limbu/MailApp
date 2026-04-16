from django.shortcuts import render
from .forms  import EmailForm
from django.contrib import messages
from django.core.mail import send_mail
# Create your views here.

def home(request):
    form = EmailForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            recipient = form.cleaned_data['recipient']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            try:
                send_mail(
                    recipient_list=[recipient],
                    subject=subject,
                    message=message,
                    from_email=None,
                )
                messages.success(request,'Email Sent Successfully')
                form = EmailForm()
            except Exception as e:
                messages.error(request,f'Error: {str(e)}')
    return render(request, 'email.html', {'form':form})
        



        