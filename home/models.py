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
