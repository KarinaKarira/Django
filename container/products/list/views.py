from cmath import log
from urllib.parse import uses_relative
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Product,Category,Cart
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request,'list/home.html')

def register(request):
    if (request.method=='POST'):
        form=UserCreationForm(request.POST)
        context={
            'form':form
        }
        if (form.is_valid()):
            form.save()
            return redirect('login')
    else:
        form=UserCreationForm()
        context={
            'form':form
        }
    return render(request,'list/register.html',context)

@login_required
def showUserHome(request):
    return render(request,'list/homeUser.html')

@login_required
def showCategories(request):
    categories=Category.objects.all()
    print(categories)
    context={
        'keyCategories':categories
    }
    return render(request,'list/viewCategories.html',context)

@login_required
def show(request,selectedCat):
    selectedCatObj=Category.objects.get(id=selectedCat)
    products_info=Product.objects.filter(softDelete=0,category=selectedCatObj)
    print(products_info)
    context={
        'keyproducts':products_info,
        'keySelectedCat':selectedCatObj
    }
    return render(request,'list/view_products.html',context)

@login_required
def addProduct(request,selectedCatId):
    # context={key:[{},{},{}]}
    selectedCat=Category.objects.get(id=selectedCatId)
    categories=Category.objects.all()
    print(categories)
    context={
        'keycategories':categories,
        'keySelectedCat':selectedCat
    }
    return render(request,'list/add_product.html',context)

@login_required
def addData(request):
    name=request.POST['productName']
    summary=request.POST['productSummary']
    color=request.POST['productColor']
    size=request.POST['productSize']
    price=request.POST['productPrice']
    category_id=request.POST['productCategory']
    category=Category.objects.get(id=category_id)
    # category=4
    # cursor=connection.cursor()
    # cursor.execute('Insert into products_table(name,summary,color,size,price,cId) values (%s,%s,%s,%s,%s,%s);',(name,summary,color,size,price,category))
    product=Product(name=name,summary=summary,color=color,size=size,price=price,category=category)
    product.save()
    return redirect('/blog/homeUser')

@login_required
def edit(request,pk):
    # cursor=connection.cursor()
    # cursor.execute(f'select * from products_table where id={pk}')
    # columns=[col[0] for col in cursor.description]
    # products=[
    #     dict(zip(columns,row))
    #     for row in cursor.fetchall()
    # ]
    # print(products)
    product=Product.objects.get(id=pk)
    # cursor.execute('select cId,cName from category')
    # columns=[col[0] for col in cursor.description]
    # categories=[
    #     dict(zip(columns,row))
    #     for row in cursor.fetchall()
    # ]
    # print(categories)

    categories=Category.objects.all()
    # selectedCId=products[0]['cId']
    # cursor.execute(f'select cName from category where cId={selectedCId}')
    # categoryName=cursor.fetchone()
    context={
        'keyproduct':product,
        'keycategories':categories,
    }
    print(context)
    return render(request,'list/editForm.html',context)

@login_required
def update(request):
    pk=request.POST['id']
    name=request.POST['productName']
    summary=request.POST['productSummary']
    color=request.POST['productColor']
    size=request.POST['productSize']
    price=request.POST['productPrice']
    category_id=request.POST['productCategory']
    category=Category.objects.get(id=category_id)
    
    # cursor=connection.cursor()
    # cursor.execute('update products_table set name=%s,summary=%s,color=%s,size=%s,price=%s,cId=%s where id=%s',(name,summary,color,size,price,category,pk))
    productToUpdate=Product.objects.get(id=pk)
    productToUpdate.name=name
    productToUpdate.summary=summary
    productToUpdate.color=color
    productToUpdate.size=size
    productToUpdate.price=price
    productToUpdate.category=category
    productToUpdate.save()
    return redirect('/blog/homeUser')

@login_required
def delete(request,pk):
    # cursor=connection.cursor()
    # cursor.execute(f'update products_table set softdelete=1 where id={pk}')
    productToDelete=Product.objects.get(id=pk)
    productToDelete.softDelete=1
    productToDelete.save()
    category=productToDelete.category.id
    return redirect('homeUser')

@login_required
def addToCart(request,productId,userId):
    user=User.objects.get(id=userId)
    product=Product.objects.get(id=productId)
    cart=Cart(user=user,product=product)
    cart.save()
    return redirect('homeUser')

@login_required
def showCart(request,userId):
    user=User.objects.get(id=userId)
    cartObjects=Cart.objects.filter(user=user)
    productsBought=[]
    for obj in cartObjects:
        productsBought.append(obj.product)
    # print(productsBought)
    context={
        'keyproducts':productsBought
    }
    return render(request,'list/showCart.html',context)

@login_required
def viewProductDetails(request,productId):
    selectedProduct=Product.objects.get(id=productId)
    context={
        'keySelectedProduct':selectedProduct
    }
    return render(request,'list/viewProductDetails.html',context)

def showOffers(request):
    return render(request,'list/showOffers.html')

@login_required
def deleteFromCart(request,userId,productId):
    owner=User.objects.get(id=userId)
    productBought=Product.objects.get(id=productId)
    productToDelete=Cart.objects.filter(product=productBought,user=owner)
    print(productToDelete[0].id)
    productToDelete.delete()
    return redirect('homeUser')
@login_required
def addCat(request):
    return render(request,'list/addCategoryPage.html')

def addCatData(request):
    name=request.POST['catName']
    file=request.FILES.get('catImage')
    c=Category(name=name,file=file)
    c.save()
    # print("hi",file,c)
    return redirect('homeUser')
#categories
# [{'id': 1, 'name': 'Electronics'}, {'id': 2, 'name': 'Food'}, {'id': 3, 'name': 'BeautyProducts'}, {'id': 4, 'name': 'Clothes'}, {'id': 5, 'name': 'HomeAppliances'}, {'id': 6, 'name': 'Toys'}, {'id': 7, 'name': 'Accesories'}]
#context
# {'keyproduct': {'id': 14, 'name': 'Nykaa shirts', 'summary': 'Known for elegance', 'color': 'black', 'size': 'small', 'price': 900.0, 'softdelete': b'\x00', 'Buy': None, 'date': datetime.datetime(2022, 8, 6, 11, 51, 6), 'user': None, 'cId': 4}, 'keycategories': [{'id': 1, 'name': 'Electronics'}, {'id': 2, 'name': 'Food'}, {'id': 3, 'name': 'BeautyProducts'}, {'id': 4, 'name': 'Clothes'}, {'id': 5, 'name': 'HomeAppliances'}, {'id': 6, 'name': 'Toys'}, {'id': 7, 'name': 'Accesories'}], 'keyCategoryName': 'Clothes'}

 