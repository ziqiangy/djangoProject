from django.shortcuts import render
from rest_framework import viewsets
from .serializers import NoteSerializer
from .serializers import WordSerializer
from .serializers import WordSourceSerializer
from .models import Note
from .models import Word
from .models import WordSource


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all().order_by('id')
    serializer_class = NoteSerializer


class WordViewSet(viewsets.ModelViewSet):
    queryset = Word.objects.all().order_by('id')
    serializer_class = WordSerializer


class WordSourceViewSet(viewsets.ModelViewSet):
    queryset = WordSource.objects.all().order_by('id')
    serializer_class = WordSourceSerializer
