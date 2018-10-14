from rest_framework import serializers
from vimarsh18.models import session_vim

class session_vimSerializer(serializers.ModelSerializer):
    class Meta:
        model = session_vim
        fields = '__all__'