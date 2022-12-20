from rest_framework import serializers
from pyqt_app.models import Project, Review
from users_app.models import Profile, Message


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    sender = ProfileSerializer(many=False)
    recipient = ProfileSerializer(many=False)

    class Meta:
        model = Message
        fields = '__all__'


class SendMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = [
            'sender',
            'recipient',
            'first_name',
            'email',
            'subject',
            'body',
        ]

    def create(self, validated_data):
        request = self.context['request']
        try:
            sender = request.user.profile
        except:
            sender = None

        if sender:
            first_name = sender.first_name
            email = sender.email
        else:
            first_name = None
            email = None

        message = Message.objects.create(sender=sender, first_name=first_name, email=email, **validated_data)

        return message


class ProjectSerializer(serializers.ModelSerializer):
    owner = ProfileSerializer(many=False)
    reviews = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = '__all__'

    def get_reviews(self, obj):
        reviews = obj.review_set.all()
        serializer = ReviewSerializer(reviews, many=True)
        return serializer.data
