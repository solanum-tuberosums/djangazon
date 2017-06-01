from django.http import HttpResponseForbidden
from django.shortcuts import render
from website.models import Order, Profile

def order_history(request):

    if request.user:
        profile = Profile.objects.get(pk=request.user.id)

        # user_orders = Order.objects.filter(user=request.user)
        user_completed_orders = Order.objects.filter(user=request.user).exclude(payment_type__isnull=True)

        print("\n")
        for order in user_completed_orders:
            print('\nOrder:')



        return render(request, 'order_history.html', {"profile":profile, 'orders':user_completed_orders})
    else:
        return HttpResponseForbidden('''<h1>Not your account, homie.</h1>
            <img src="/website/static/other.jpg">''')


