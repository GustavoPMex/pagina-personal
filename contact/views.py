from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import contactForm
from django.core.mail import EmailMessage

# Create your views here.

def contact(request):
    contact_form = contactForm()
    if request.method == 'POST':
        contact_form = contactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            terms = request.POST.get('terms', '')
            #Enviamos el correo y redireccionamos
            email = EmailMessage(
                'Gustavo Mex: Nuevo mensaje de contacto',
                'De {} <{}>\n\nEscribió:\n\n{}'.format(name, email, content),
                'no-contestar@gmail.com',
                ['django.pruebasemail@gmail.com'],
                reply_to=[email]
            )
            try:
                email.send()
                #Todo ha ido bien
                return redirect(reverse('contact')+'?ok')
            except:
                #Algo no ha ido bien
                return redirect(reverse('contact')+'?fail')

    return render(request, 'contact/contact.html', {'form':contact_form})