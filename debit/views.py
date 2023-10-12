from django.shortcuts import render, redirect
from .models import data, credit
from django.contrib.auth.models import User
from .forms import debit_form, credit_form, category, delete_record, delete_category
from account.models import Profile
from django.views import View
from rest_framework import generics, viewsets, mixins
from .serializers import CreditSerializer, DebitSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.response import Response




def check_email_verify(user_id):
    return Profile.objects.filter(user_id=user_id).values()[0]["email_verify"]


class view_debit(View):
    template_name = "debit/debit.html"
    form_1 = debit_form()
    form_2 = category()
    form_3 = delete_record()
    form_4 = delete_category()
    categoryJSON = {}
    user_id: int

    def get(self, request):
        if_verify = False
        form_1 = debit_form()
        form_4 = delete_category()
        debit_categories = []
        if request.user.is_authenticated:
            self.user_id = self.get_userID(request)
            if_verify = check_email_verify(self.user_id)
            self.categoryJSON = self.get_category(user_id=self.user_id)
            debit_categories = self.categoryJSON["debit"].copy()
        records = data.objects.filter(user_id=self.user_id).order_by("-id")
        return render(
            request,
            "debit/debit.html",
            {
                "debit_form": form_1,
                "category_form": self.form_2,
                "delete_record_form": self.form_3,
                "delete_category": form_4,
                "records": records,
                "verify": if_verify,
                "debit_categories": debit_categories,
            },
        )

    def get_category(self, user_id):
        if Profile.objects.filter(user_id=user_id).exists():
            categoryJSON = Profile.objects.filter(user_id=user_id).values()[0][
                "category"
            ]
        return categoryJSON

    def get_userID(self, request):
        user_id = User.objects.filter(username=f"{request.user}").values()[0]["id"]
        print(user_id)
        return user_id

    def post(self, request):
        self.user_id = self.get_userID(request)
        self.categoryJSON = self.get_category(user_id=self.user_id)
        if "date" in request.POST:
            return self.date_form(request)
        elif "category" in request.POST:
            return self.category_form(request)
        elif "record_id" in request.POST:
            data.delete(request=request.POST)
            return redirect(to="http://127.0.0.1:8000/data/debit")
        elif "del_category" in request.POST:
            return self.del_category(request)

    def date_form(self, request):
        form_1 = debit_form(request.POST)
        db_form = form_1.create_db_form(self.user_id, request)
        data.record(form=db_form)
        return redirect(to="http://127.0.0.1:8000/data/debit")

    def category_form(self, request):
        form_2 = category(request.POST)
        if form_2.is_valid():
            if not request.POST["category"] in self.categoryJSON["debit"]:
                self.categoryJSON["debit"].append(request.POST["category"])
            Profile.objects.filter(user_id=self.user_id).update(
                category=self.categoryJSON
            )
        return redirect(to="http://127.0.0.1:8000/data/debit")

    def del_category(self, request):
        if request.POST["del_category"] in self.categoryJSON["debit"]:
            print(self.categoryJSON)
            self.categoryJSON["debit"].remove(request.POST["del_category"])
            Profile.objects.filter(user_id=self.user_id).update(
                category=self.categoryJSON
            )
        return redirect(to="http://127.0.0.1:8000/data/debit")
    
class CreditAPIList(generics.ListAPIView):
    # queryset = credit.objects.all()
    serializer_class = CreditSerializer
    permission_classes = (IsAuthenticated, )
    
    def get(self, request, *args, **kwargs):
        user_id = User.objects.filter(username=f"{request.user}").values()[0]["id"]
        self.queryset = credit.objects.filter(user_id=user_id).order_by("-id")
        return super().get(request, *args, **kwargs)
    
class DebitAPIList(generics.ListAPIView):
    # queryset = data.objects.all()
    serializer_class = DebitSerializer
    permission_classes = (IsAuthenticated, )
    
    def get(self, request, *args, **kwargs):
        user_id = User.objects.filter(username=f"{request.user}").values()[0]["id"]
        self.queryset = data.objects.filter(user_id=user_id).order_by("-id")
        return super().get(request, *args, **kwargs)
    
class CreditAPICreate(generics.CreateAPIView):
    serializer_class = DebitSerializer
    permission_classes = (IsAuthenticated, )
    
    def post(self, request, *args, **kwargs):     
        serializer = DebitSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post' : serializer.data})

    

class view_credit(View):
    template_name = "debit/debit.html"
    form_1 = credit_form()
    form_2 = category()
    form_3 = delete_record()
    form_4 = delete_category()
    categoryJSON = {}
    user_id: int

    def get(self, request):
        if_verify = False
        form_1 = credit_form()
        form_4 = delete_category()
        credit_categories = []
        if request.user.is_authenticated:
            self.user_id = self.get_userID(request)
            if_verify = check_email_verify(self.user_id)
            self.categoryJSON = self.get_category(user_id=self.user_id)
            credit_categories = self.categoryJSON["credit"].copy()
        records = credit.objects.filter(user_id=self.user_id).order_by("-id")
        return render(
            request,
            "debit/credit.html",
            {
                "debit_form": form_1,
                "category_form": self.form_2,
                "delete_record_form": self.form_3,
                "delete_category": form_4,
                "records": records,
                "verify": if_verify,
                "credit_categories": credit_categories,
            },
        )

    def get_category(self, user_id):
        if Profile.objects.filter(user_id=user_id).exists():
            categoryJSON = Profile.objects.filter(user_id=user_id).values()[0][
                "category"
            ]
        return categoryJSON

    def get_userID(self, request):
        user_id = User.objects.filter(username=f"{request.user}").values()[0]["id"]
        return user_id

    def post(self, request):
        self.user_id = self.get_userID(request)
        self.categoryJSON = self.get_category(user_id=self.user_id)
        if "date" in request.POST:
            return self.date_form(request)
        elif "category" in request.POST:
            return self.category_form(request)
        elif "record_id" in request.POST:
            credit.delete(request=request.POST)
            return redirect(to="http://127.0.0.1:8000/data/credit")
        elif "del_category" in request.POST:
            return self.del_category(request)

    def date_form(self, request):
        form_1 = credit_form(request.POST)
        db_form = form_1.create_db_form(self.user_id, request)
        credit.record(form=db_form)
        return redirect(to="http://127.0.0.1:8000/data/credit")

    def category_form(self, request):
        form_2 = category(request.POST)
        if form_2.is_valid():
            if not request.POST["category"] in self.categoryJSON["credit"]:
                self.categoryJSON["credit"].append(request.POST["category"])
            Profile.objects.filter(user_id=self.user_id).update(
                category=self.categoryJSON
            )
        return redirect(to="http://127.0.0.1:8000/data/credit")

    def del_category(self, request):
        if request.POST["del_category"] in self.categoryJSON["credit"]:
            print(self.categoryJSON)
            self.categoryJSON["credit"].remove(request.POST["del_category"])
            Profile.objects.filter(user_id=self.user_id).update(
                category=self.categoryJSON
            )
        return redirect(to="http://127.0.0.1:8000/data/credit")
