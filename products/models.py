from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    parent=models.ForeignKey('self',verbose_name='parent',blank=True,null=True,on_delete=models.CASCADE) #categories,subcategories
    title=models.CharField(_('name'),max_length=50)     # _ for translation
    description=models.TextField(_('description'),blank=True)
    avatar=models.ImageField(blank=True,upload_to='categories/')
    is_enable=models.BooleanField(default=True)
    created_time=models.DateTimeField(auto_now_add=True)
    updated_time=models.DateTimeField(auto_now=True)

    class Meta:
        db_table='categories' #name in db
        verbose_name='Category' #name in admin panel
        verbose_name_plural= 'Categories' 





class Product(models.Model):
    title=models.CharField(_('title'),max_length=50)    
    description=models.TextField(_('description'),blank=True)
    avatar=models.ImageField(blank=True,upload_to='products/')
    is_enable=models.BooleanField(default=True)
    categories=models.ManyToManyField('Category',verbose_name='categories',blank=True)
    created_time=models.DateTimeField('created time',auto_now_add=True)
    updated_time=models.DateTimeField('updated time',auto_now=True)
    class Meta:
        db_table='products' 
        verbose_name=_('Product')
        verbose_name_plural= 'Products' 


class File(models.Model):
    product=models.ForeignKey('Product',verbose_name=_('Product'),on_delete=models.CASCADE)
    title=models.CharField(_('title'),max_length=50)
    file=models.FileField('file',upload_to='files/%Y/%m/%d/')
    is_enable=models.BooleanField(default=True)
    created_time=models.DateTimeField('created time',auto_now_add=True)
    updated_time=models.DateTimeField('updated time',auto_now=True)
    class Meta:
        db_table='files' 
        verbose_name=_('File')
        verbose_name_plural= 'Files' 
