from django.shortcuts import render
from urllib import response
import requests
import json
import os
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CreatorSerializers, PlayerSerializers, ContentSerilizers
from .models import Creator, Player, Content, Ratings
from django.http import JsonResponse
from .forms import VideoForm


@api_view(['POST'])
def add_creator(request):
    try:
        data = request.data
        serializer = CreatorSerializers(data=data)
        if serializer.is_valid():
            # print(serializer.data)
            serializer.save()
            return Response({
                'status': True,
                'message': 'successfully added',
                'data': serializer.data
            })
        return Response({
            'status': False,
            'message': 'invalid data',
            'data': serializer.errors})
    except Exception as e:
        print(e)

    return Response({
        'status': False,
        'message': 'Something went wrong'
    })


@api_view(['GET'])
def get_creator(request):
    creator_objs = Creator.objects.all()
    serializer = CreatorSerializers(creator_objs, many=True)

    return Response({
        'status': True,
        'message': 'creator data fetched',
        'data': serializer.data
    })


@api_view(['POST'])
def add_player(request):
    try:
        data = request.data
        serializer = PlayerSerializers(data=data)
        if serializer.is_valid():
            # print(serializer.data)
            serializer.save()
            return Response({
                'status': True,
                'message': 'successfully added',
                'data': serializer.data
            })
        return Response({
            'status': False,
            'message': 'invalid data',
            'data': serializer.errors})
    except Exception as e:
        print(e)

    return Response({
        'status': False,
        'message': 'Something went wrong'
    })


@api_view(['GET'])
def get_player(request):
    creator_objs = Player.objects.all()
    serializer = CreatorSerializers(creator_objs, many=True)

    return Response({
        'status': True,
        'message': 'creator data fetched',
        'data': serializer.data
    })

@api_view(['POST'])
def add_content(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            #print(file.name)
            # handle_uploaded_file(file)
            return Response({
                'status': True,
                'message': 'successfully added',
                'data': form.data
            })
    else:
        form = VideoForm()
    return Response({
        'status': False,
        'message': 'Something went wrong'
    })

@api_view(['POST'])
def rate_content(request):
    if request.method == 'POST':
        el_id = request.POST.get('el_id')
        val = request.POST.get('val')
        print(val)
        obj = Ratings.objects.get(id=el_id)

        # storing_prev_rated_number = obj.rated_number

        obj.rated_number = val

        obj.count = obj.count + 1
        store_count = obj.count
        old_addition_values = obj.storing_prev_now_rated_value

        obj.storing_prev_now_rated_value = int(old_addition_values) + int(val)

        store_storing_prev_now_rated_value = obj.storing_prev_now_rated_value
        print(store_storing_prev_now_rated_value)

        obj.avg_rating = float(
            store_storing_prev_now_rated_value // store_count)

        j = obj.avg_rating
        print(j)
        obj.save()
        return JsonResponse({'success': 'true', 'rated_number': val}, safe=False)
    return JsonResponse({'success': 'false'})
