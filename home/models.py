from django.db import models

class About(models.Model):
    title = models.CharField(max_length=48, verbose_name = 'عنوان')
    description = models.TextField(verbose_name = 'توضیحات')
    image = models.ImageField(upload_to="about_pictures", verbose_name = 'تصویر')

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = "در باره ما"
        verbose_name_plural = "در باره ما"

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


class Title_Expenses(models.Model):
    title = models.CharField(max_length=40, verbose_name='عنوان')

    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name = 'عنوان بخش بودجه'
        verbose_name_plural = 'عناوین بودجه'


class Expenses(models.Model):
    title = models.CharField(max_length=50, verbose_name='عنوان')
    count = models.CharField(max_length=100, verbose_name='مقدار')

    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name = 'بودجه'
        verbose_name_plural = 'بودجه'


class Contact(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')
    email = models.EmailField(verbose_name='ایمیل')
    phone = models.CharField(max_length=100, verbose_name='شماره های تماس')
    address = models.CharField(max_length=100, verbose_name='نشانی')


    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name = 'تماس'
        verbose_name_plural = 'تماس ها'


class Footer(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    address =models.CharField(max_length=100, verbose_name='آدرس')
    phone = models.CharField(max_length=100, verbose_name='شماره های تماس')
    email = models.EmailField(verbose_name='ایمیل')
    whatsapp = models.CharField(max_length=100, verbose_name='واتساپ')
    facebook = models.CharField(max_length=100, verbose_name='فسبوک')


    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name = 'شبکه های اجتماعی'
        verbose_name_plural = 'شبکه های اجتماعی'