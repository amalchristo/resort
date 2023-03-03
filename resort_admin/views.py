from django.shortcuts import render,redirect
from common.models import Bookroom

from resort_admin.models import Add_room, Resort_admin

def admin_master(request):
    return render(request,'admin_template/admin_master.html')

def add_room(request):
    if request.method == 'POST':
        room_name = request.POST['room_name']
        room_capacity = request.POST['room_capacity']
        room_photo = request.FILES['room_photo']
        room_price = request.POST['room_price']
        room_description = request.POST['room_description']
        new_room = Add_room(
            room_name = room_name,
            room_capacity = room_capacity,
            room_photo = room_photo,
            room_price = room_price,
            room_description = room_description,
        )
        new_room.save()
        
    return render(request,'admin_template/add_room.html')

def room_details(request):
    room_details = Add_room.objects.all()
    
    return render(request,'admin_template/room_details.html', { 'room' : room_details })

def staff_details(request):
    return render(request,'admin_template/staff_details.html')

def add_staff(request):
    return render(request,'admin_template/add_staff.html')

def admin_login(request):
    msg = ''
    if request.method == 'POST':
        user_name = request.POST['username']
        password = request.POST['password']
        try :
            resort_admin = Resort_admin.objects.get(
                user_name = user_name,
                password = password,
                )
            request.session['resort_admin'] = resort_admin.id
            return redirect ('resort_admin:admin_master')
        except :
            msg = 'invalid password or username'
    return render(request,'admin_template/admin_login.html',{ 'msg' : msg })

def delete_room(request,room_id):
    delete_rooms = Add_room.objects.get(
        id = room_id
    )
    delete_rooms.delete()
    return redirect('resort_admin:room_details')

# def delete_book(request,book_id):
#     delete_books = Bookroom.objects.get(
#         id = book_id
#     )
#     delete_books.delete()
#     return redirect('Resort_admin:room_book')

def room_book(request):
    room_book = Bookroom.objects.all()
    return render(request,'admin_template/room_book.html',{ 'room_book' : room_book })


    


# Create your views here.
