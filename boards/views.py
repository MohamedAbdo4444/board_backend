import statistics
from django.shortcuts import render, get_object_or_404
from .models import Board, Topic
from django.http import JsonResponse
from django.db.models import Count
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import BoardSerlializer, TopicSerlializer, PostSerlializer
from rest_framework import status
from rest_framework import generics
from rest_framework import viewsets


# Create your views here.

class BoardViewSets(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerlializer





# def boards_list(request):
#     boards = Board.objects.all()
#     data = {'Results':list(boards.values('pk', 'name', 'description'))}
#     return JsonResponse(data)
# class BoardList(APIView):
#     def get(self, request):
#         boards = Board.objects.all()
#         data = BoardSerlializer(boards, many = True).data
#         return Response(data)
    
# class BoardList(generics.ListCreateAPIView):
#     queryset =Board.objects.all()
#     serializer_class =BoardSerlializer
    
#     def post(self, request):
#         serializer = BoardSerlializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class BoardTopics(generics.ListCreateAPIView):
#     queryset =Topic.objects.all()
#     serializer_class =TopicSerlializer
# class BoardTopics(APIView):
#     def get(self, request, id):
#         board = get_object_or_404(Board, id=id)
#         topics =board.topics.order_by('-created_dt').annotate(comments=Count('posts'))
#         data = TopicSerlializer(topics, many= True).data
#         return Response(data)
    

    # def post(self, request, id):
    #     serializer = TopicSerlializer(data=request.data)
    #     topic_details = request.data
    #     if serializer.is_valid():
    #         topic = serializer.save()
    #         post_serializer = PostSerlializer(data={'message':topic_details['message'], 'topic':topic.pk, 
    #         'created_by':topic.created_by,'created_dt':topic.created_dt, 'updated_by':topic.updated_by, 'updated_dt':topic.updated_dt})
    #         if post_serializer.is_valid():
    #             post_serializer.save()
    #             return Response(post_serializer.data, status=status.HTTP_201_CREATED)
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class BoardDetails(generics.RetrieveUpdateDestroyAPIView):
#     queryset =Board.objects.all()
#     serializer_class =BoardSerlializer
#     lookup_field = 'id'


    
# class BoardDetails(APIView):
#     def get(self, request, id):
#         board = get_object_or_404(Board, pk = id)
#         data = BoardSerlializer(board).data
#         return Response(data)
    
#     def post(self, request):
#         serializer = BoardSerlializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# def board_topics(request, id):
#     board = get_object_or_404(Board, id=id)
#     topics =board.topics.order_by('-created_dt').annotate(comments=Count('posts'))
#     data = {'results':{
#         'name':board.name,
#         'description':board.description
#     }, 'topics': list(topics.values('pk', 'subject', 'board', 'created_by', 'created_dt'))
#     }
#     return JsonResponse(data)
