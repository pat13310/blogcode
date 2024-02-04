from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.images.blocks import ImageChooserBlock




class HomePage(Page):
    titre = RichTextField(blank=True, default='Titre')
    body = RichTextField(blank=True)
    intro_title = RichTextField(blank=True)
    intro_content = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('titre', classname="full"),
        FieldPanel('body', classname="full"),
        FieldPanel('intro_title', classname="full"),
        FieldPanel('intro_content', classname="full"),
        InlinePanel('gallery_images', label="Gallery images"),

    ]


class HomePageGalleryImage(Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+', blank=True, null=True
    )

    panels = [
        FieldPanel('image'),
    ]




