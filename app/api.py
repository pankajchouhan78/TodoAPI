
from .models import Todo
from  .serializer import TodoSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def ViewTodo(request):
    try:
        tasks = Todo.objects.all()
        serializer = TodoSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # tasks = Todo.objects.all()
    # serializer = TodoSerializer(tasks, many=True)
    # return Response(serializer.data)


@api_view(['POST'])
def CreateTodo(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

@api_view(['POST'])
def UpdateTodo(request,pk):
    task = Todo.objects.get(pk=pk)
    serializer = TodoSerializer(data=request.data, instance = task)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
@api_view(['DELETE'])
def DeleteTodo(request,pk):
    task = Todo.objects.get(pk=pk).delete()
    return Response('successfully deleted')

