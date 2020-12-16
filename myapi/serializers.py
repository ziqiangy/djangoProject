from rest_framework import serializers

from .models import Note
from .models import Word
from .models import WordSource

class NoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Note
        fields = ('id', 'title', 'content', 'insert_date', 'user_id')


class WordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Word
        fields = ('id', 'word', 'trans', 'user_id', 'source_id')


class WordSourceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WordSource
        fields = ('id', 'source_from', 'user_id')
