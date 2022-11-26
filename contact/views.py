from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import ContactForm, NewsletterForm
from .models import Newsletter

# Create your views here.


def contact_us(request):
    """ A view to handle the customer contact form """

    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for contacting us. We will \
                be in touch shortly.')
            return redirect(reverse('contact_us'))

    context = {
        'form': form
    }

    return render(request, 'contact/contact_us.html', context)


def newsletter(request):
    """newsletter page view"""

    form = NewsletterForm()

    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            if Newsletter.objects.filter(
                    email=instance.email).exists():
                messages.add_message(
                    request,
                    40,
                    "You are already subscribed."
                )
            else:
                instance.save()
                messages.add_message(
                    request,
                    25,
                    "Successfully subscribed to our newsletter."
                )
                return redirect(reverse('home'))

    context = {
        'form': form,
    }

    return render(request, 'contact/newsletter.html')
