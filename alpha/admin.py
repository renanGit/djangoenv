from django.contrib import admin
from .models import AlphaBoard
from .forms import AlphaBoardForm

# Register your models here.

# admin.site.register(AlphaBoard)

class AlphaBoardAdmin(admin.ModelAdmin):
    form = AlphaBoardForm


admin.site.register(AlphaBoard, AlphaBoardAdmin)



# from django.db import models
# from django.forms import TextInput, Textarea
#   formfield_overrides = {
#       models.CharField: {'widget': TextInput(attrs={'size': '20'})},
#       models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 40})},
#   }
