from rest_framework import serializers
from .models import ProjectInfo, Pekerjaan, Aktivitas

class AktivitasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aktivitas
        fields = '__all__'

class PekerjaanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pekerjaan
        fields = '__all__'

class ProjectInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectInfo
        fields = '__all__'
