from rest_framework import serializers 
from drf.models import Women
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
import io

# class WomenModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content

# class WomenSerializer(serializers.Serializer):
#     title=serializers.CharField(max_length=255)
#     content=serializers.CharField()

# def encode():
#     model=WomenModel("Adda","Addadaad")
#     model_sr=WomenSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep="\n")
#     json=JSONRenderer().render(model_sr.data)
#     print(json)

# def decode():
#     stream=io.BytesIO(b'{"title":"Abba","content":"Content:ABBA"}')
#     data=JSONParser().parse(stream)
#     serializer=WomenSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)
#------------------------------------------------------------
# class WomenSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Women
#         fields=('title', 'cat_id')
#-----------------------------------------------------
# class WomenSerializer(serializers.Serializer):
#     title=serializers.CharField(max_length=255)
#     content=serializers.CharField()
#     time_create=serializers.DateTimeField(read_only=True)
#     time_update=serializers.DateTimeField(read_only=True)
#     is_published=serializers.BooleanField(default=True)
#     cat_id=serializers.IntegerField()

#     def create(self, validated_data):
#         return Women.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.content = validated_data.get('content', instance.content)
#         instance.time_update = validated_data.get('time_update', instance.time_update)
#         instance.is_published=validated_data.get('is_published', instance.is_published)
#         instance.cat_id = validated_data.get('cat_id', instance.cat_id)
#         instance.save()
#         return instance
#------------------------------------------------------------
class WomenSerializer(serializers.ModelSerializer):
    class Meta:
        model=Women
        fields=('id','title', 'content', 'cat')
        #fields='__all__'