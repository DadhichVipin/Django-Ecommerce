from account.models import Customer
from django.shortcuts import redirect, render
from django.http import HttpResponse 
from django.contrib.auth.hashers import make_password, check_password
from django.views import View


# Create your views here.

def register(request):
    if request.method == 'GET':
        return render(request, "account/register.html")
    else:
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        repassword = postData.get('repassword')

        #validation 

        # create dictionry to fach values and save while registration 
        value = {
            'first_name' : first_name,
            'last_name' : last_name,
            'phone' : phone,
            'email' : email
        }

        error_message = None

        customer = Customer(first_name = first_name,
                                last_name = last_name,
                                phone = phone,
                                email = email,
                                password = password 
                                )

        if not first_name:
            error_message = "First Name Required!!"
        elif len(first_name) < 4:
            error_message = "First Name must be 4 char or more"
        elif not last_name:
            error_message = "Last Name Required!!"
        elif len(last_name) < 4:
            error_message = "Last Name must be 4 char or more"
        elif not phone:
            error_message = "Phone Number Required!!"
        elif len(phone) <10:
            error_message = "Phone Number should have 10 digit"
        elif not email:
            error_message = "Mail Required!!"
        elif not password :
            error_message = "Password Required!!"
        elif len(password) < 6:
            error_message = "Password length should be minimum 6"
        elif repassword != password:
            error_message = "Password and Re-Password Not Maching"
        elif customer.isExists():
            error_message = "Email Address Alredy Used.."
        
        # saveing...
        if not error_message:
            customer.password = make_password(customer.password) # password hashimg 
            customer.register()
            return redirect('store')
        else:
            data = {
                'error': error_message,
                'values' : value 
            }
                
            return render(request, "account/register.html", data)
  

# login  view using class or class based view
class Login(View):
    def get(self, request):
        return render(request, 'account/login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password) #decode hase-password and compare with user entered
            if flag:
                #session 
                request.session['customer'] = customer.id
                return redirect('store')
            else:
                error_message = 'Email or Password invalid!!'
        else:
            error_message = 'Email or Password invalid!!'
        return render(request, 'account/login.html', {'error' : error_message})



def logout(request):
    request.session.clear()
    return redirect('store')
        