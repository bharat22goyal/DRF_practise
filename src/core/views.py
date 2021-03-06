from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PostSerializer
from .models import Post

# Create your views here.
# def test_view(request):
#     test={
#         'name':'Bharat',
#         'age':25
#     }
#     return JsonResponse(test)

class TestView(APIView):
    def get(self, request, *args, **kwargs):
        qs=Post.objects.all()
        serializer=PostSerializer(qs,many=True)
        return Response(serializer.data)

    def post(self,request,*args, **kwargs):
        serializer=PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

