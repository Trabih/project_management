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
        extra_kwargs = {
            'is_archived': {'write_only': True},
            'signature_picture': {'write_only': True},
        }

class ProjectInfoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectInfo
        fields = ['tangsel_project', 'status_project']

class PekerjaanUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pekerjaan
        fields = ['tangsel_pek', 'status_pek']

class AktivitasUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aktivitas
        fields = ['eval_akti', 'ren_akti', 'status_akti']   