from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import ProjectSerializer, MessageSerializer, SendMessageSerializer
from pyqt_app.models import Project, Review
from users_app.models import Message


@api_view(['GET'])
def get_routes(request):
    routes = [
        # PyQt Projects
        {'GET': '/api/pyqt-projects'},
        {'GET': '/api/pyqt-projects/id'},
        {'POST': '/api/pyqt-projects/id/vote'},

        # Users
        {'POST': '/api/users/token'},
        {'POST': '/api/users/token/refresh'},

        # Inbox
        {'GET': '/api/inbox'},
        {'GET': '/api/inbox/message/id'},
        {'POST': '/api/inbox/delete-all-messages'},
        {'POST': '/api/inbox/message/id/delete-message'},
        {'POST': '/api/inbox/send-message'},
    ]

    return Response(routes)


@api_view(['GET'])
def get_pyqt_projects(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)

    return Response({"success": serializer.data})


@api_view(['GET'])
def get_pyqt_project(request, project_id):
    projects = Project.objects.get(id=project_id)
    serializer = ProjectSerializer(projects, many=False)

    return Response({"success": serializer.data})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def pyqt_project_vote(request, project_id):
    project = Project.objects.get(id=project_id)
    user = request.user.profile
    data = request.data

    review, created = Review.objects.get_or_create(
        user=user,
        project=project,
    )

    review.value = data['value']
    review.save()
    project.likes_count

    serializer = ProjectSerializer(project, many=False)

    return Response({"success": serializer.data})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_inbox(request):
    user = request.user.profile
    all_user_messages = user.messages.all()
    serializer = MessageSerializer(all_user_messages, many=True)

    if serializer.data:
        return Response({"success": serializer.data})
    return Response({'success': 'You have no messages'})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_message(request, message_id):
    user = request.user.profile
    message = Message.objects.get(id=message_id)
    if message.recipient != user:
        return Response({"error": 'You are not the recipient'})
    serializer = MessageSerializer(message, many=False)

    return Response({"success": serializer.data})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delete_all_messages(request):
    user = request.user.profile
    all_messages = user.messages.all()

    if all_messages:
        all_messages.delete()
        return Response({'success': 'All messages have been deleted'})
    return Response({'success': 'You have no messages'})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delete_message(request, message_id):
    user = request.user.profile
    message = Message.objects.get(id=message_id)

    if message.recipient != user:
        return Response({'error': 'You are not the recipient'})

    message.delete()
    return Response({'success': 'The message has been deleted'})


@api_view(['POST'])
def send_message(request):
    serializer = SendMessageSerializer(data=request.data, context={'request': request})
    if serializer.is_valid(raise_exception=True):
        serializer.save()

    return Response({"success": serializer.data})
