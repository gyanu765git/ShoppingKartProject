from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Product, Category
from django.views import View
from .forms import RegistrationForm
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.models import User

class Index(View):

    # def post(self , request):
    #     product = request.POST.get('product')
    #     remove = request.POST.get('remove')
    #     cart = request.session.get('cart',{})
    #     if cart:
    #         quantity = cart.get(product)
    #         if quantity:
    #             if remove:
    #                 if quantity<=1:
    #                     cart.pop(product)
    #                 else:
    #                     cart[product]  = quantity-1
    #             else:
    #                 cart[product]  = quantity+1

    #         else:
    #             cart[product] = 1
    #     else:
    #         cart = {}
    #         cart[product] = 1

    #     request.session['cart'] = cart
    #     print('cart' , request.session['cart'])
    #     return redirect('homepage')
       
    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart', {})
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print('cart', request.session['cart'])

        if 'cart' in request.META.get('HTTP_REFERER', ''):
            return redirect('cart')
        else:
            return redirect('homepage')


    def get(self , request):
        return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}') 

def store(request):
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    products = None
    categories = Category.objects.all()
    category_id = request.GET.get('category')
    
    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()
    data = {
        'products': products,
        'categories': categories
    }
    # data['products'] = products
    # data['categories'] = categories

    # print('you are : ', request.session.get('email'))
    return render(request, 'index.html', data) 


class Cart(View):
    def get(self, request):
        product_ids = request.session.get('cart', {}).keys()
        products = Product.objects.filter(id__in=product_ids)
        return render(request, 'cart.html', {'products': products})
    
    def post(self, request):
        product_id = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart', {})
        
        if remove:
            if product_id in cart:
                del cart[product_id]
        
        request.session['cart'] = cart
        return redirect('cart')
 

def SignUp_Request(request):
	if request.method == "POST":
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful.")
			return redirect('login')
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = RegistrationForm()
	return render (request=request, template_name="signup.html", context={"signup_form":form})

  
def Login_Request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect('homepage')
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})


def Logout_Request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect('homepage')
      
      
def NextStep(request):
    return render(request, "pending.html")      
	

     
	

      	





   
