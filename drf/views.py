from django.forms import model_to_dict
from rest_framework import generics,viewsets
from django.shortcuts import render
from drf.models import Women, Category
from drf.serializers import WomenSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action

def index(request):
    print('REQUEST',request.user)
    context={

    }
    return render(request, "drf/index.html", context)
#-------------------------------------------------
# class WomenAPIView(APIView):
#     # def get(self, request):
#     #     post=Women.objects.all().values()    
#     #     return Response({"title":list(post)})

#     def get(self, request):
#         w=Women.objects.all()
#         return Response({"posts":WomenSerializer(w, many=True).data})
        
#     def post(self, request):
#         serializer=WomenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post":serializer.data})
#         # post_new=Women.objects.create(
#         #     title=request.data['title'],
#         #     content=request.data['content'],
#         #     cat_id=request.data['cat_id'],
#         # )
#         # return Response({"post":model_to_dict(post_new)})
#         #return Response({"post":WomenSerializer(post_new).data})
#     def put(self,request, *args, **kwargs):
#         pk=kwargs.get('pk', None)
#         if not pk:
#             return Response({"error":"Method PUT not alloved!"})
#         try:
#             instance=Women.objects.get(pk=pk)
#         except:
#             return Response({"error":"Object does not exists"})
        
#         serializer=WomenSerializer(data=request.data, instance=instance)
#         serializer.save()
#         return Response({"post":serializer.data})

#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error":"Method DELETE not allowed"})
        
#         return Response({"post":"delete post" + str(pk)})
#------------------------------------------------------


# class WomenAPIView(generics.ListAPIView):
#     queryset=Women.objects.all()
#     serializer_class=WomenSerializer
#-----------------------------------------------------
# class WomenAPIList(generics.ListCreateAPIView):
#     queryset=Women.objects.all()
#     serializer_class=WomenSerializer

# class WomenAPIUpdate(generics.UpdateAPIView):
#     queryset=Women.objects.all()
#     serializer_class=WomenSerializer

# class WomenAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset=Women.objects.all()
#     serializer_class=WomenSerializer

#----------ViewSet избавляет от дублирования кода выше---------
class WomenViewSet(viewsets.ModelViewSet):
    #queryset=Women.objects.all()
    serializer_class=WomenSerializer

    # def get_queryset(self):
    #     return Women.objects.all()[:3]

    def get_queryset(self):
        pk=self.kwargs.get("pk")
        if not pk:
            return Women.objects.all()[:3]
        return Women.objects.filter(pk=pk)
    

    # @action(methods=['get'], detail=False) #вывод всех сатегорий
    # def category(self, request):
    #     cats=Category.objects.all()
    #     return Response({"cats":[c.name for c in cats]})

    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        cats=Category.objects.get(pk=pk)
        return Response({'cats':cats.name})
    