from django.core.serializers import serialize
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.views import APIView
from . import models, serializers


#----------------------------Django Normal API-------------------------------------------

def poll_list(request):
    polls = models.Poll.objects.all()
    polls_data = list(polls.values("pk", "question", "created_by", "created_time"))

    return JsonResponse(
        data=polls_data,
        status=200,
        safe=False)

def poll_detail(request, pk):
    poll_obj = get_object_or_404(
        klass=models.Poll,
        pk=pk)
    
    serialized_polls = serialize(
        format="json",
        queryset=[poll_obj],
        fields=(
            "pk",
            "question",
            "created_by",
            "created_time"
        ))

    return HttpResponse(
        content=serialized_polls,
        content_type="application/json"
    )


#----------------------------DRF APIview-------------------------------------------


class PollList(APIView):

    def get(self, request):
        polls = models.Poll.objects.all()

        serialized_polls_data = serializers.PollSerializer(
            instance=polls,
            many=True
        ).data

        return Response(
            data=serialized_polls_data,
            status=status.HTTP_200_OK
        )


class PollDetail(APIView):

    def get(self, request, pk):
        poll_obj = get_object_or_404(
            klass=models.Poll,
            pk=pk
        )

        serialized_poll_data = serializers.PollSerializer(
            instance=poll_obj
        ).data

        return Response(
            data=serialized_poll_data,
            status=status.HTTP_200_OK
        )


class VoteCreateAPIView(APIView):
    serializer_class = serializers.VoteSerializer

    def post(self, request, poll_pk, choice_pk):
        # our goal is customizing the behavior of APIView based on our nested url

        voted_by = request.data.get("voted_by", None)
        
        data = {
            'choice': choice_pk, 
            'poll': poll_pk, 
            'voted_by': voted_by}

        serializer = serializers.VoteSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            data=serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


#----------------------------DRF Genericview-------------------------------------------


class PollListCreate(generics.ListCreateAPIView):
    queryset = models.Poll.objects.all()
    serializer_class = serializers.PollSerializer


class PollDetailRemove(generics.RetrieveDestroyAPIView):
    queryset = models.Poll.objects.all()
    serializer_class = serializers.PollSerializer


class ChoiceListCreate(generics.ListCreateAPIView):
    serializer_class = serializers.ChoiceSerializer

    def get_queryset(self):
        choices_qs = models.Choice.objects.all()
        filtered_choices_qs = choices_qs.filter(poll__pk=self.kwargs.get("pk", None))
        return filtered_choices_qs


class VoteCreate(generics.CreateAPIView):
    serializer_class = serializers.VoteSerializer
