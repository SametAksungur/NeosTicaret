from django.contrib import admin
from .models import *
# Register your models here.


class SepetAdmin(admin.ModelAdmin):
    list_display = ('user', 'urun', 'adet', 'toplam', 'odendiMi')


# modeli admin panelinde görüntüleyebilmek için gereklı kod assagıdadır
admin.site.register(Urun)
admin.site.register(Kategori)
admin.site.register(SeriNo)
admin.site.register(AltKategori)
admin.site.register(Sepet, SepetAdmin)
admin.site.register(Odeme)
