__author__ = 'nisahu'
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from models import Post
from serializer import PostSerializer
#from tumblelog.forms import PostForm



@api_view(['GET'])
def post_collection(request):
   if request.method == 'GET':
       posts = Post.objects.all()
       serializer = PostSerializer(posts, many=True)
       return Response(serializer.data)


@api_view(['GET'])
def post_element(request, _id):
   try:
       post = Post.objects.get(_id=_id)
   except Post.DoesNotExist:
       return HttpResponse(status=404)

   if request.method == 'GET':
       serializer = PostSerializer(post)
       return Response(serializer.data)