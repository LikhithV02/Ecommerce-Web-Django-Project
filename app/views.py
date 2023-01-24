from django.shortcuts import render, redirect
from django.views import View
from .models import customer,category,cart,seller,product,payment,warehouse
from .forms import CustomerRegistrationForm, CustomerProfileForm
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse

class ProductView(View):
    def get(self, request):
        fashion = product.objects.filter(category_id='1')
        electronics = product.objects.filter(category_id='2')
        books = product.objects.filter(category_id='3')
        grocery = product.objects.filter(category_id='4')
        return render(request, 'app/home.html',{'fashion': fashion, 'electronics':electronics,'books':books, 'grocery':grocery})


class ProductDetailView(View):
    def get(self, request, pk):
        pro = product.objects.get(pk=pk)
        return render(request, 'app/productdetail.html', {'product':pro})

def add_to_cart(request):
    user=request.user
    product_id = request.GET.get('prod_id')
    pro = product.objects.get(pr_id=product_id)
    cart(user=user, Product=pro).save()
    return redirect('/cart')

def show_cart(request):
    if request.user.is_authenticated:
        user = request.user
        Cart = cart.objects.filter(user=user)
        #print(Cart)
        amount = 0.0
        shipping_amt = 120.0
        total_amt = 0.0
        cart_product = [p for p in cart.objects.all() if p.user==user]
        #print(cart_product)
        if cart_product:
            for p in cart_product:
                tempamt = (p.order_quantity * p.Product.pr_price)
                amount += tempamt
                total_amt = amount + shipping_amt
            return render(request, 'app/addtocart.html', {'carts': Cart, 'total_amt': total_amt
            , 'amount': amount})
        else:
            return render(request, 'app/emptycart.html')

def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        print(prod_id)
        c = cart.objects.get(Q(Product=prod_id) & Q(user=request.user))
        c.order_quantity+=1
        c.save()
        amount = 0.0
        shipping_amt = 120.0
        cart_product = [p for p in cart.objects.all() if p.user==request.user]
        for p in cart_product:
            tempamt = (p.order_quantity * p.Product.pr_price)
            amount += tempamt

    data={
        'quantity': c.order_quantity,
        'amount': amount,
        'total_amt': amount + shipping_amt
    }
    return JsonResponse(data)

def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = cart.objects.get(Q(Product=prod_id) & Q(user=request.user))
        c.order_quantity-=1
        c.save()
        amount = 0.0
        shipping_amt = 120.0
        cart_product = [p for p in cart.objects.all() if p.user==request.user]
        for p in cart_product:
            tempamt = (p.order_quantity * p.Product.pr_price)
            amount += tempamt

    data={
            'quantity': c.order_quantity,
            'amount': amount,
            'total_amt': amount + shipping_amt
        }
    return JsonResponse(data)

def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = cart.objects.get(Q(Product=prod_id) & Q(user=request.user))
        c.delete()
        amount = 0.0
        shipping_amt = 120.0
        cart_product = [p for p in cart.objects.all() if p.user==request.user]
        for p in cart_product:
            tempamt = (p.order_quantity * p.Product.pr_price)
            amount += tempamt

    data={
        'amount': amount,
        'total_amt': amount + shipping_amt
    }
    return JsonResponse(data)




def buy_now(request):
 return render(request, 'app/buynow.html')


def address(request):
    add = customer.objects.filter(user=request.user)
    return render(request, 'app/address.html', {'c_add': add, 'active':'btn-primary'})

def orders(request):
 return render(request, 'app/orders.html')

def electronics(request, data=None):
    if data==None:
        elec =product.objects.filter(category_id='2')
    elif data=='below':
        elec = product.objects.filter(category_id='2').filter(pr_price__lt=10000)
    elif data=='above':
        elec = product.objects.filter(category_id='2').filter(pr_price__gt=10000)
    return render(request, 'app/electronics.html', {'electronics':elec})


class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html',
        {'form':form})
    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulations!! Registered Successfully')
            form.save()
        return render(request, 'app/customerregistration.html',{'form':form})

def checkout(request):
 return render(request, 'app/checkout.html')

class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(request, 'app/profile.html', {'form':form, 'active':'btn-primary'})

    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            usr = request.user
            name = form.cleaned_data['c_name']
            email = form.cleaned_data['email_id']
            mobile_no = form.cleaned_data['mobile_no']
            customer_address = form.cleaned_data['c_add']
            reg = customer(user = usr, c_name=name, email_id=email, mobile_no=mobile_no, c_add=customer_address)
            reg.save()
            messages.success(request, 'Congratulations!!! Profile has been Updated Successfully')
        return render(request, 'app/profile.html', {'form':form, 'active':'btn-primary'})