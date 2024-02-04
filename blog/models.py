from django.db import models
from wagtail import blocks
from modelcluster.fields import ParentalKey
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.images.blocks import ImageChooserBlock
from blogcode.myblock import ImageBlock

class Blog (Page):
    
    """ Blog Page """
    body = StreamField([
        ('text', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
    ],use_json_field=True, null=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]