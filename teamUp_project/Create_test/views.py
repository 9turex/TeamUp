from django.shortcuts import render
from django.utils.crypto import get_random_string
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *


def generate_test():
    """
    Method for create uniq login in database, and create new CreateTest object
    """
    new_login = get_random_string(length=10, allowed_chars='ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    while CreateTest.objects.filter(login=new_login):
        new_login = get_random_string(length=10)
    CreateTest.objects.create(login=new_login)
    return new_login


def head_page(request):
    return render(request, 'head_page.html')


class CreateTestAPIView(APIView):
    """
    API method for create new test and login
    url: api/v1/create_test/
    type method: GET
    return: {'login': created login} (JSON)
    """
    def get(self, request):
        new_login = generate_test()
        return Response({'login': new_login})


class SaveIqResultAPIView(APIView):
    """
     API method for save IQ test result
     url: api/v1/save_iq_result/
     type method: POST
     params: {'login' (str): 10 letters, 'score' (int) : 0-50}
     return: {"id": id object,
    "score": score,
    "login": login CreatedTest} (JSON)
     """
    def post(self, request):
        serializer_class = IqTestSerializer(data=request.data)
        serializer_class.is_valid(raise_exception=True)
        try:
            login_object = CreateTest.objects.get(login=request.data['login'])
        except:
            return Response({'result': 'Error. Login is not found'})
        new_iq_test = IqTest.objects.create(score=request.data['score'], login=login_object)
        return Response(IqTestSerializer(new_iq_test).data)


class SaveEqResultAPIView(APIView):
    """
        API method for save EQ test result
        url: api/v1/save_eq_result/
        type method: POST
        params: {'login' (str): 10 letters, 'score' (int) : 0-50, 'answer' (str): 5 letters}
        return: {"id": id object,
       "score": score,
       "finish_time": date created,
       "login": login CreatedTest,
       "answer": answer} (JSON)
        """
    def post(self, request):
        serializer_class = EqTestSerializer(data=request.data)
        serializer_class.is_valid(raise_exception=True)

        try:
            login_object = CreateTest.objects.get(login=request.data['login'])
        except:
            return Response({'result': 'Error. Login is not found'})
        new_eq_test = EqTest.objects.create(score=request.data['score'], answer=request.data['answer'], login=login_object)
        return Response(EqTestSerializer(new_eq_test).data)


class FindAllAnswerAPIView(APIView):
    """
    API method for get all EQ and IQ results
    URL: api/v1/find_result/
    type method: GET
    params: {'login' (str): 10 letters} (JSON)
    """

    def get(self, request):
        login = request.data['login']
        try:
            all_answers = CreateTest.objects.get(login=login)
        except:
            return Response({'result': 'Error. Login is not found'})

        iq_test = all_answers.iqtest_set.all()
        eq_test = all_answers.eqtest_set.all()
        context = {
            "request": request,
        }
        iq_serializer = IqTestSerializer(iq_test, many=True, context=context)
        eq_serializer = EqTestSerializer(eq_test, many=True, context=context)
        return Response({'login': login, 'iq_result': iq_serializer.data, 'eq_result': eq_serializer.data})

