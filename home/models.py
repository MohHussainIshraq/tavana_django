from django.db import models

class About(models.Model):
    title = models.CharField(max_length=48, verbose_name = 'عنوان')
    description = models.TextField(verbose_name = 'توضیحات')
    image = models.ImageField(upload_to="about_pictures", verbose_name = 'تصویر')

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = "در مورد توانا"
        verbose_name_plural = "در موارد"

class Donation_Title(models.Model):
    title = models.CharField(max_length=50, verbose_name='عنوان')
    description = models.TextField(verbose_name='جزئیات')

    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name = 'کمک های خیریه'
        verbose_name_plural = 'کمک های خیریه'


class Helpers(models.Model):
    name = models.CharField(max_length=40, verbose_name='نام')
    count = models.CharField(max_length=50, verbose_name='مقدار')
    image = models.ImageField(upload_to="helpers_pictures", verbose_name='تصویر')

    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name = 'کمک کننده'
        verbose_name_plural = 'کمک کننده ها'


class Details_Donations(models.Model):
    title = models.CharField(max_length=50, verbose_name = 'عنوان')
    description = models.TextField(verbose_name='توضیحات بیشتر')

    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name = 'جزئیات کمک'
        verbose_name_plural = 'جزئیات کمک ها'


class Pictures(models.Model):
    image = models.ImageField(upload_to='pictures', verbose_name='تصویر')


    class Meta:
        verbose_name = 'تصویر'
        verbose_name_plural = 'تصاویر'

