from django.shortcuts import render
from website.models import Order, Profile
from django.http import HttpResponseForbidden

def order_history(request, user_id):

    if request.user == user_id:
        profile = Profile.objects.get(pk=user_id)
        return render(request, 'order_history.html', {"profile":profile})
    else:
        return HttpResponseForbidden('''<h1>Not your account, homie.</h1>
            <img src="/website/static/other.jpg">''')