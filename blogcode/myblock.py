from wagtail.blocks import StructBlock, CharBlock, RichTextBlock, StreamBlock, ListBlock
from wagtail.images.blocks import ImageChooserBlock


class ImageBlock(StructBlock):
    image= ImageChooserBlock()
    caption=CharBlock()


class TitleCommentBlock(StructBlock):
    title=CharBlock()
    comment=CharBlock()


class ImageTextBlock(StructBlock):
    image1=ImageChooserBlock()
    caption1=CharBlock()
    image2=ImageChooserBlock()
    caption2=CharBlock()


class QuoteBlock(StructBlock):
    quote_by= CharBlock
    quote_content= RichTextBlock()


class BodyBlock(StreamBlock):
    h1= CharBlock()
    paragraph= RichTextBlock()
    carousel= ListBlock(ImageChooserBlock())
    bulletLlist=ListBlock(CharBlock())
    image= ImageTextBlock()
    quote= QuoteBlock()
    titleComment= TitleCommentBlock()


    