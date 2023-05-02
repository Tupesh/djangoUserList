from django.shortcuts import render
from appTwo.models import users


# Create your views here.
def user(response):
    webpages_list=users.objects.order_by('id') 
    head={'value1':'Users','value2':'Welcome to User list','details':webpages_list}
    return render(response, 'appTwo\index.html', context=head)

def main(response):
    head={'value1':'Mainpage','value2':'This is home page','value3':'Add /users to view list of users'}
    return render(response, 'appTwo\index.html', context=head)