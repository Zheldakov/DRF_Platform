from imghdr import tests
from multiprocessing.connection import answer_challenge

from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from sections.models import Section, SectionContent, Tests
from sections.permissioms import IsModerator
from sections.searializers.section_searializers import SectionListSerializer, SectionSerializer
from sections.searializers.section_content_searializers import SectionContentListSerializer, SectionContentSerializer
from sections.searializers.tests_searilizers import TestSerializer, TestQuestionSerializer
from sections.paginators import SectionPaginator, SectionContentPaginator, TestsPaginator


class SectionListAPIView(ListAPIView):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = SectionPaginator


class SectionCreateAPIView(CreateAPIView):
    serializer_class = SectionSerializer
    pagination_classes = [IsAuthenticated, IsAdminUser | IsModerator]


class SectionRetrieveAPIView(RetrieveAPIView):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    permission_classes = [IsAuthenticated]


class SectionUpdateAPIView(UpdateAPIView):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser | IsModerator]


class SectionDestroyAPIView(DestroyAPIView):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser | IsModerator]


class ContentListAPIView(ListAPIView):
    serializer_class = SectionContentSerializer
    queryset = SectionContent.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = SectionContentPaginator


class ContentCreateAPIView(CreateAPIView):
    serializer_class = SectionContentSerializer
    permission_classes = [IsAuthenticated, IsAdminUser | IsModerator]


class ContentRetrieveAPIView(RetrieveAPIView):
    serializer_class = SectionSerializer
    queryset = SectionContent.objects.all()
    permission_classes = [IsAuthenticated]


class ContentUpdateAPIView(UpdateAPIView):
    serializer_class = SectionContentSerializer
    queryset = SectionContent.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser | IsModerator]


class ContentDestroyAPIView(DestroyAPIView):
    serializer_class = SectionContentSerializer
    queryset = SectionContent.objects.all()
    pagination_class = [IsAuthenticated, IsAdminUser|IsModerator]


class TestListAPIView(ListAPIView):
    serializer_class = TestSerializer
    queryset = Tests.objects.all()
    permission_classes = [IsAuthenticated]


class TestQuestionRetrieveAPIView(RetrieveAPIView):
    serializer_class = TestQuestionSerializer
    queryset = Tests.objects.all()

    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        answers = [tests.answer for test in Tests.objects.all()]
        answer = answers[self.kwargs.get('pk') - 1].lower()
        user_answer = request.data.get('user_answer').lower()
        is_correct = user_answer == answer
        return Response({'is_correct': is_correct})