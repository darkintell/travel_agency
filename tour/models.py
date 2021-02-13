from django.template.defaultfilters import slugify
from froala_editor.fields import FroalaField
from django.contrib.postgres import fields
from django_jalali.db import models as jmodel
from django.db import models



class CityModel(models.Model):
    name = models.CharField(max_length=50, verbose_name= "نام‌شهر")
    name_en = models.CharField(max_length=50, verbose_name= "نام‌شهر-انگلیسی", default='')
    image = models.ImageField(upload_to='cities', verbose_name= "تصویر")
    country = models.CharField(max_length=100, verbose_name= "کشور")
    continent = models.CharField(max_length=50, verbose_name= "قاره")
    description = models.TextField(verbose_name= "توضیحات")
    geographic_place = models.CharField(max_length=100, verbose_name= "موقعیت جغرافیایی")
    currency = models.CharField(max_length=30, verbose_name= "ارز رایج")
    language = models.CharField(max_length=30, verbose_name= "زبان")
    religion = models.CharField(max_length=30, verbose_name= "دین")
    description_content = FroalaField(verbose_name="توضیحات کامل")


    class Meta:
        verbose_name = "شهر"
        verbose_name_plural = "شهر ها"
        
    
    def slug(self):
        return slugify(self.name_en)
  
    def __str__(self):
        return self.name


def ImagePath(instance, filename):
    return ('/'.join(['tours',instance.city.slug(), filename]))
    
class TourModel(models.Model):
    title = models.CharField(max_length=50, verbose_name="عنوان")
    title_en = models.CharField(max_length=50, verbose_name="عنوان-انگلیسی", default='')
    image = models.ImageField(upload_to=ImagePath, verbose_name="تصویر")
    city = models.ForeignKey('CityModel',on_delete=models.CASCADE, verbose_name="شهر")
    label = models.CharField(max_length=20, verbose_name="برچسب")
    description = models.TextField(verbose_name="توضیحات")
    wearings = models.CharField(max_length=250, null=True, verbose_name="پوشیدنی ها")
    tour_duration = models.CharField(max_length=100, verbose_name="مدت زمان تور")
    included_costs = fields.ArrayField(models.CharField(max_length=50), verbose_name="هزینه های مشمول")
    not_included_costs = fields.ArrayField(models.CharField(max_length=50), verbose_name="هزینه های مستثنی")
    features = fields.ArrayField(models.CharField(max_length=50), verbose_name="امکانات")
    score = models.IntegerField(default=0, verbose_name="امتیاز")
    adult_price = models.IntegerField(verbose_name="قیمت مسافران بالغ")
    child_price = models.IntegerField(default=0, verbose_name="قیمت مسافران کودک")
    start_date = jmodel.jDateField(verbose_name="تاریخ شروع تور")
    end_date = jmodel.jDateField(verbose_name="تاریخ اتمام تور")
    passengers = models.IntegerField(verbose_name="تعداد مسافران")
    passengers_left = models.IntegerField(default=passengers, verbose_name="مسافران باقیمانده")
    tour_type = models.CharField(max_length=30, verbose_name="نوع تور")
    off_percent = models.IntegerField(default=0, verbose_name="درصد تخفیف")
    is_active = models.BooleanField(default=0, verbose_name="تور فعال است")
    date_created = jmodel.jDateTimeField(auto_now_add=True)
    
    
    class Meta:
        verbose_name = "تور گردشگری"
        verbose_name_plural = "تور های گردشگری"
        ordering = ["-start_date"]
    
    def slug(self):
        return slugify(self.title_en)
    
    def __str__(self):
        return self.title
    