from multiprocessing import context
from django.shortcuts import render
from datetime import datetime
from mifamilia.models import Family_members

def my_dad(request):
    today = datetime.now().date
    family_member = Family_members.objects.create(name = 'John Smith',
    age = '50',
    job = 'teacher',
    Last_active_whapp = (today))
    context = {context}
    return render(request, 'family_member',context=context)
    



