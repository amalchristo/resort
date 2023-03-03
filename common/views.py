from django.shortcuts import render,redirect
from common.models import Bookroom, Customer, Review

from resort_admin.models import Add_room

def index(request):
    # profile_list = Customer.objects.get(id = request.session['customer'])
    rewiew_list = Review.objects.all()
    room_list = Add_room.objects.all()
    msg = ""
    if request.method == 'POST':
        if 'add_review' in request.POST:
            add_review = request.POST['review']
            newreview = Review(
                add_review = add_review
            )
            newreview.save()
        if 'registration' in request.POST:
            customer_username = request.POST['customer_username']
            customer_email = request.POST['customer_email']
            customer_password = request.POST['customer_password']
            newcustomer = Customer(
                customer_username = customer_username,
                customer_email = customer_email,
                customer_password = customer_password
            )
            newcustomer.save()
        if 'bookroom' in request.POST:
            book_name = request.POST['book_name']
            book_email = request.POST['book_email']
            check_in = request.POST['check_in']
            check_out = request.POST['check_out']
            newbookroom = Bookroom(
                book_name = book_name,
                book_email = book_email,
                check_in = check_in,
                check_out = check_out,
            )
            newbookroom.save()
        if 'login' in request.POST:
            login_name = request.POST['login_name']
            login_password = request.POST['login_password']
            try :
                customerlog = Customer.objects.get(
                    customer_username = login_name,
                    customer_password = login_password
                    )
                request.session['customer'] = customerlog.id
                return redirect ('common:index')
            except :
                msg = 'invalid password or username'
   
    return render(request,'index.html',{ 'reviews' : rewiew_list , 'room_lists' : room_list , 'msg' : msg })

def profile(request):
    profile_list = Customer.objects.get( id = request.session['customer'] )
    return render (request,'profile.html',{ 'profile' : profile_list })

def logout(request):
    del request.session['customer']
    return redirect('common:index')



# Create your views here.
