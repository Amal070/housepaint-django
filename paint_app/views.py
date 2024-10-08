from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
import os
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    return render(request,'index.html')


#########################shop panel #######################################
##########################################################

#########shop home #################
def shop_home(request):
    user=request.user.id
    view=Book.objects.filter(shop_id=user)
    context={
        'view':view
    }
    return render(request,'shop/index.html',context)


############ cateres register ##############
def shop_register(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        passw1 = request.POST.get("password")
        passw2= request.POST.get("password1")
        email= request.POST.get("email")
        if passw1 ==passw2:
            if User.objects.filter(username=uname).exists():
                messages.error(request, 'Username already exists.')
                return render(request, 'shop/register.html')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'email id already exists.')
                return render(request, 'shop/register.html')
            else:
                user = User.objects.create_user(
                    username=uname,
                    password=passw1,
                    email=email,
                    is_shop=True,
                )
                user.save()
                # Add a success message
                messages.success(request, 'Registration successful. You can now log in.')
                return redirect('shop_login')
        else:
            messages.error(request, 'password not matching.')
            return redirect('shop_register')
        
    else:
        return render(request, "shop/register.html")

#############login #########################
def shop_login(request):  
    if request.method == 'POST':
        uname = request.POST.get('username')
        passw = request.POST.get('password')

        user = User.objects.filter(username=uname).first()
        
        if user is not None and user.check_password(passw) and user.is_shop:
            login(request, user)
            return redirect('shop_home')
        else:
            messages.error(request, 'Invalid login credentials.')
    return render(request, "shop/login.html")


################ add shop details #################
def add_profile(request):
    if request.method == "POST":
        # Retrieve form data from request.POST
        name = request.POST.get("name")
        
        address = request.POST.get("address")
        mobile = request.POST.get("phone")
        email = request.POST.get("email")
       
        gst = request.POST.get("gst")
        
        image=request.FILES.get('img')

      
        # Create a new user or retrieve the current user (assuming the donor is logged in)
        if request.user.is_authenticated:
            current_user = request.user
        else:
            current_user = User.objects.create_user(username="a_random_username", password="a_random_password", is_shop=True)
         # Update the user's details with the form data
        current_user.name = name
        
        current_user.address = address
        current_user.mobile = mobile
        current_user.email = email
        current_user.GST = gst
        
        current_user.photo = image

        # Save the user object with the updated details
        current_user.save()
        return redirect('shop_home')  # Redirect to the donor's dashboard or a success page
    

    return render(request,'shop/add_profile.html')



################view shop details ####################

def view_profile(request,pk):
    view = get_object_or_404(User, id=pk, is_shop=True)
    context={
        'view':view
    }
    return render(request,'shop/view_profile.html',context)

######################update shop details ######################
def Update_profile(request, pk):
    update = get_object_or_404(User, id=pk, is_shop=True)
    if request.method == 'POST':
        if 'img' in request.FILES:
            if len(update.photo) > 0:
                os.remove(update.photo.path)
            update.photo = request.FILES['img']
        update.name=request.POST.get('name')
        update.mobile=request.POST.get('phone')
        update.address=request.POST.get('address')
        update.email=request.POST.get('email')
        update.GST=request.POST.get('gst')      
        update.save()
        messages.success(request,"Update successfully")
        return redirect('view_profile', pk=pk)

    context = {
        'update': update
        }
    return render(request, 'shop/update_profile.html',context)

########## add worker ################

def add_worker(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        place = request.POST.get('place')
        age = request.POST.get('age')
        image=request.FILES.get('img')
        user=request.user
        add=Worker.objects.create(
            shop=user,
            name=name,
            age=age,
            mobile=phone,
            place=place,
            images=image


        )
        add.save()
        return redirect('view_worker')
    return render(request,'shop/add_worker.html')

############# view worker ################

def view_worker(request):
    user=request.user
    view=Worker.objects.filter(shop=user)
    context={
        'view':view
    }
    return render(request,'shop/view_worker.html',context)

############# update worker ################

def update_worker(request,pk):
    
    edit=Worker.objects.get(pk=pk)
    if request.method == 'POST':
        if 'img' in request.FILES:
            if len(edit.images) > 0:
                os.remove(edit.images.path)
            edit.images = request.FILES['img']
        edit.name=request.POST.get('name')
        edit.mobile=request.POST.get('phone')
        edit.age=request.POST.get('age')
        edit.place=request.POST.get('place')    
        edit.save()
        messages.success(request,"Update successfully")
        return redirect('view_worker')

    context={
        'edit':edit
    }
    return render(request,'shop/update_worker.html',context)

############# delete worker ###############

def delete_worker(request,pk):
    dele=Worker.objects.get(pk=pk)
    dele.delete()
    return redirect('view_worker')

############### add package #################

def add_package(request):
    if request.method == "POST":
        name = request.POST.get('name')
        descr = request.POST.get('description')
        rate = request.POST.get('rate')
        warranty = request.POST.get('warranty')
        
        user=request.user
        add=Package.objects.create(
            shop_1=user,
            name=name,
            description=descr,
            rate=rate,
            Warranty=warranty,

        )
        add.save()
        return redirect('shop_home')
    return render(request,'shop/add_package.html')

#############view package ################

def view_package(request):
    user=request.user
    view=Package.objects.filter(shop_1=user)
    context={
        'view':view
    }
    return render(request,'shop/view_package.html',context)

############# update package ################

def update_package(request,pk):
    
    edit=Package.objects.get(pk=pk)
    if request.method == 'POST':
        
        edit.name=request.POST.get('name')
        edit.description=request.POST.get('description')
        edit.rate=request.POST.get('rate')
        edit.Warranty=request.POST.get('warranty')  
        edit.save()
        messages.success(request,"Update successfully")
        return redirect('view_package')

    context={
        'edit':edit
    }
    return render(request,'shop/update_package.html',context)

############# delete Package ###############

def delete_package(request,pk):
    dele=Package.objects.get(pk=pk)
    dele.delete()
    return redirect('view_package')

############## view purchased request ######################

def view_request(request):
    user=request.user.id
    view=Book.objects.filter(shop_id=user)
    context={
        'view':view
    }
    return render(request,'shop/approve_request.html',context)

############## approve request ###################
def approve_request(request, pk):
    # Get the BloodRequest object
    package_request = get_object_or_404(Book, id=pk)

    # Check if the donor is the requester
    if package_request.shop_id == request.user.pk:
        # Update the status to approved
        package_request.status = True
        package_request.save()

    return redirect('view_request') 

############# add message ##################

def add_message(request,pk):
    clien=Book.objects.get(pk=pk)
    if request.method=='POST':
        site=request.POST.get('name')
        worker=request.POST.get('worker')
        start=request.POST.get('start')
        end=request.POST.get('end')
        images=request.FILES.get('img')
        date=request.POST.get('date')
        clien=request.POST.get('client_id')

        
        send=Message.objects.create(
            site=site,
            worker=worker,
            start=start,
            end=end,
            images=images,
            date=date,
            client_id=clien
        )
        send.save()
        return redirect('shop_home')
    contect={'clie':clien}
    
    return render(request,'shop/work_message.html',contect)

########### view Approved Customer ################

def approved_client(request):
    id = request.user.pk
    
    view=Book.objects.filter(status=True, shop_id=id)
    context={
        'view':view
    }
    
    return render(request,'shop/view_approved_customer.html',context)

############## generate billl ###############
def generat_bill(request,pk):
    view=Book.objects.get(pk=pk)
    if request.method == 'POST':
        shop_id=request.POST.get('Shop_id')
        client_id=request.POST.get('user_id')
        bill_no=request.POST.get('Bill')
        package_name=request.POST.get('Packagename')

        package_price=request.POST.get('Price')
        shop_name=request.POST.get('Shopname')
        shop_phone=request.POST.get('Shopnumber')
        client_name=request.POST.get('Clientname')
        client_address=request.POST.get('Clientaddress')
        square_feet=request.POST.get('feet')
        square_feet_rate=request.POST.get('rate')
        product_name=request.POST.get('Product')
        total_price=request.POST.get('total')
        create=Bill.objects.create(
            shop_id=shop_id,
            client_id=client_id,
            bill_no=bill_no,
            package_name=package_name,
            package_price=package_price,
            shop_name=shop_name,
            shop_phone=shop_phone,
            client_name=client_name,
            client_address=client_address,
            square_feet=square_feet,
            square_feet_rate=square_feet_rate,
            product_name=product_name,
            total_price=total_price,

        )
        create.save()
        messages.success(request,'successfully send bills')
        return redirect('approved_client')
    context={
        'view':view
    }
    return render(request,'shop/generate_bill.html',context)

def shop_SignOut(request):
     logout(request)
     return redirect('user_home')
########################################user panel #############################################
###################################################################

#########user home #################
def user_home(request):
    package=Package.objects.all()
    context={
        'package':package
    }
    return render(request,'user/index.html',context)


############ user register ##############
def user_register(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        passw1 = request.POST.get("password")
        passw2= request.POST.get("password1")
        email= request.POST.get("email")
        if passw1 ==passw2:
            if User.objects.filter(username=uname).exists():
                messages.error(request, 'Username already exists.')
                return render(request, 'user/register.html')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'email id already exists.')
                return render(request, 'user/register.html')
            else:
                user = User.objects.create_user(
                    username=uname,
                    password=passw1,
                    email=email,
                    is_user=True,
                )
                user.save()
                # Add a success message
                messages.success(request, 'Registration successful. You can now log in.')
                return redirect('user_login')
        else:
            messages.error(request, 'password not matching.')
            return redirect('user_register')
        
    else:
        return render(request, "user/register.html")

#############login #########################
def user_login(request):  
    if request.method == 'POST':
        uname = request.POST.get('username')
        passw = request.POST.get('password')

        user = User.objects.filter(username=uname).first()
        
        if user is not None and user.check_password(passw) and user.is_user:
            login(request, user)
            return redirect('user_home')
        else:
            messages.error(request, 'Invalid login credentials.')
    return render(request, "user/login.html")

################ add user details #################
@login_required(login_url='user_login')
def add_user_profile(request):
    if request.method == "POST":
        # Retrieve form data from request.POST
        name = request.POST.get("name")
        
        address = request.POST.get("address")
        mobile = request.POST.get("phone")
        email = request.POST.get("email")
        
        image=request.FILES.get('img')

      
        # Create a new user or retrieve the current user (assuming the donor is logged in)
        if request.user.is_authenticated:
            current_user = request.user
        else:
            current_user = User.objects.create_user(username="a_random_username", password="a_random_password", is_user=True)
         # Update the user's details with the form data
        current_user.name = name
        
        current_user.address = address
        current_user.mobile = mobile
        current_user.email = email
        current_user.photo = image

        # Save the user object with the updated details
        current_user.save()
        return redirect('user_home')  # Redirect to the donor's dashboard or a success page
    

    return render(request,'user/add_profile.html')

################view user details ####################
@login_required(login_url='user_login')
def view_user_profile(request,pk):
    view = get_object_or_404(User, id=pk, is_user=True)
    context={
        'view':view
    }
    return render(request,'user/view_profile.html',context)

######################update user details ######################
@login_required(login_url='user_login')
def Update_user_profile(request, pk):
    update = get_object_or_404(User, id=pk, is_user=True)
    if request.method == 'POST':
        if 'img' in request.FILES:
            if len(update.photo) > 0:
                os.remove(update.photo.path)
            update.photo = request.FILES['img']
        update.name=request.POST.get('name')
        update.mobile=request.POST.get('phone')
        update.address=request.POST.get('address')
        update.email=request.POST.get('email')     
        update.save()
        messages.success(request,"Update successfully")
        return redirect('view_user_profile', pk=pk)

    context = {
        'update': update
        }
    return render(request, 'user/update_profile.html',context)


########## view packages details###############
def view_package_detils(request,pk):
    view=Package.objects.get(pk=pk)
    context={
        'view':view
    }
    return render(request,'user/package_details.html',context)

########### package request form ####################
@login_required(login_url='user_login')
def send_package_request(request,pk):

    view=Package.objects.get(pk=pk)
    if request.method=='POST':
        shop_id=request.POST.get('shop_id')
        shop_name=request.POST.get('shop_name')
        shop_address=request.POST.get('shop_address')
        shop_phone=request.POST.get('shop_phone')
        packg_id=request.POST.get('pack_id')
        packg_name=request.POST.get('pack_name')
        warranty=request.POST.get('warranty')
        rate=request.POST.get('rate')
        cust_id=request.POST.get('cus_id')
        cust_name=request.POST.get('cus_name')
        cust_address=request.POST.get('cus_address')
        cust_phone=request.POST.get('cus_phone')

        create=Book.objects.create(
            shop_id=shop_id,
            shop_name=shop_name,
            shop_address=shop_address,
            shop_phone=shop_phone,
            packg_id=packg_id,
            packg_name=packg_name,
            warranty=warranty,
            rate=rate,
            cust_id=cust_id,
            cust_name=cust_name,
            cust_address=cust_address,
            cust_phone=cust_phone
            )
        create.save()
        return redirect('success_message')


    context={
        'view':view
    }
    return render(request,'user/send_request.html',context)

################ success message ################
@login_required(login_url='user_login')
def success_message(request):   
    return render(request,'user/succeess_book.html')


############ view Purchase history ##############
@login_required(login_url='user_login')
def purchase_history(request):
    user=request.user.id
    view= Book.objects.filter(cust_id=user)
    context={
        'view':view
    }
    return render(request,'user/purchase_history.html',context)



########### view work message ################
@login_required(login_url='user_login')
def view_worked(request):
    user=request.user.id
    view=Message.objects.filter(client_id=user)
    context={
        'view':view
    }
    
    return render(request,'user/view_work_progress.html',context)

################ view bills ###############
@login_required(login_url='user_login')
def view_bill(request):
    user=request.user.id
    view=Bill.objects.filter(client_id=user)
    context={
        'view':view
    }
    return render(request,'user/view_bill.html',context)

############ logout #############
@login_required(login_url='user_login')
def client_SignOut(request):
     logout(request)
     return redirect('user_home')
