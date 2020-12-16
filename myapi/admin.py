from django.contrib import admin
from .models import Note
from .models import Word
from .models import WordSource
# Register your models here.
admin.site.register(Note)
admin.site.register(Word)
admin.site.register(WordSource)
