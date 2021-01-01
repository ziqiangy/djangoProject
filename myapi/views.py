from django.shortcuts import render
from rest_framework import viewsets
from .serializers import NoteSerializer
from .serializers import WordSerializer
from .serializers import WordSourceSerializer
from .models import Note
from .models import Word
from .models import WordSource
from braces.views import CsrfExemptMixin


class NoteViewSet(CsrfExemptMixin,viewsets.ModelViewSet):
    authentication_classes = []

    queryset = Note.objects.all().order_by('id')
    serializer_class = NoteSerializer


class WordViewSet(CsrfExemptMixin,viewsets.ModelViewSet):
    authentication_classes = []

    queryset = Word.objects.all().order_by('id')
    serializer_class = WordSerializer


class WordSourceViewSet(CsrfExemptMixin,viewsets.ModelViewSet):
    authentication_classes = []

    queryset = WordSource.objects.all().order_by('id')
    serializer_class = WordSourceSerializer
