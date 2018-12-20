from django.shortcuts import render
from django.views.generic import DetailView, CreateView, UpdateView, View

from mysite.views import ListView
from .models import Member

# Create your views here.
class MemberList(ListView):
    model = Member
    template_name = 'modules/member/member.html'
    context_object_name = 'member_list'
    base_url = 'member:list'