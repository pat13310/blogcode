from django.shortcuts import render

from django.http import HttpResponseRedirect
from wagtail.contrib.forms.views import handle_form_submission
from .models import ContactPage  # Assurez-vous d'importer votre modèle ContactPage

def contact_page(request, page_id):
    contact_page = ContactPage.objects.get(id=page_id)

    if request.method == 'POST':
        response = handle_form_submission(request, contact_page)

        if response.status_code == 302:
            return HttpResponseRedirect('/confirmation/')  # Remplacez '/confirmation/' par l'URL souhaitée

    return render(request, 'contact_page.html', {'page': contact_page})