from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import ContactForm, NewsletterForm
from .models import Newsletter

# Create your views here.


def contact(request):
    """Contact Page View"""

    if request.method == 'POST':
        form = ContactForm(request.post)
        if form.is_valid():
            form.save()
            messages.add_message(
                request,
                25,
                "Your message has been sent. Thank you for you input!"
            )
            return redirect('contact')
        else:
            form = ContactForm()
            messages.add_message(
                request,
                40,
                "There was an error with your form, please try again."
            )

        context = {
            'form': form,
        }

        return render(request, 'contact/contact.html', context)


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
