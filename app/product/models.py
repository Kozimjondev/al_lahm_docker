from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_resized import ResizedImageField


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated'))

    class Meta:
        abstract = True


class Product(BaseModel):
    name = models.CharField(_("Product Name"), max_length=150)
    price = models.PositiveIntegerField(_("Product Price"), default=0)
    amount = models.PositiveIntegerField(_("Amount"), default=0)
    image = ResizedImageField(size=[380, 340], upload_to='images/')

    def __str__(self):
        return self.name


class Accessory(BaseModel):
    name = models.CharField(_("Accessory Name"), max_length=150)
    price = models.PositiveIntegerField(_("Accessory Price"), default=0)
    number = models.PositiveIntegerField(_("Accessory Number"), default=0)
    image = ResizedImageField(size=[380, 340], upload_to='images/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Accessories'
        ordering = ('-created_at', )


class Review(BaseModel):
    MARKS = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    )
    full_name = models.CharField(_("Full Name"), max_length=100)
    mark = models.CharField(_("Mark"), max_length=10, choices=MARKS)
    description = models.CharField(_("Description"), max_length=2000)

    def __str__(self):
        return self.full_name


class Connection(BaseModel):
    _validate_phone = RegexValidator(
        regex=r"^\+?\d{9,13}$",
        message="Telefon raqamingiz 9 bilan boshlanishi va 12 ta belgidan oshmasligi lozim. "
                "Masalan: +998993451545", )
    full_name = models.CharField(_("Full Name"), max_length=100)
    phone_number = models.CharField(_("Phone number"), max_length=50, validators=[_validate_phone])
    message = models.CharField(_("Message"), max_length=2000)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = _("Connection")
        verbose_name_plural = _("Connections")
        ordering = ('-created_at', )
