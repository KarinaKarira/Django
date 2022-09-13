from unicodedata import category
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db import connection
from .models import Product,Category

# Create your views here.
def home(request):
    return render(request,'list/home.html')
def show(request):
    # cursor=connection.cursor()
    # cursor.execute('SELECT id,name,summary,color,size,price,cname FROM products_table NATURAL JOIN category;')

    # columns=[col[0] for col in cursor.description]
    # products_info=[
    #     dict(zip(columns,row))
    #     for row in cursor.fetchall()
    # ]
    # print(products_info)

    products_info=Product.objects.filter(softDelete=0)
    print(products_info)
    context={
        'keyproducts':products_info
    }
    # return HttpResponse('<h1>Welcome to home</h1>')
    return render(request,'list/view_products.html',context)

def addProduct(request):
    # cursor=connection.cursor()
    # cursor.execute('select cId,cName from category')
    # columns=[col[0] for col in cursor.description]
    # # categories=[{},{},{}]
    # categories=[
    #     dict(zip(columns,row))
    #     for row in cursor.fetchall()
    # ]
    # context={key:[{},{},{}]}
    categories=Category.objects.all()
    print(categories)
    context={
        'keycategories':categories
    }
    return render(request,'list/add_product.html',context)
    
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
    return redirect('/blog/home')


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
    return redirect('/blog/home')


def delete(request,pk):
    # cursor=connection.cursor()
    # cursor.execute(f'update products_table set softdelete=1 where id={pk}')
    productToDelete=Product.objects.get(id=pk)
    productToDelete.softDelete=1
    productToDelete.save()
    return redirect('/blog/show')

#categories
# [{'id': 1, 'name': 'Electronics'}, {'id': 2, 'name': 'Food'}, {'id': 3, 'name': 'BeautyProducts'}, {'id': 4, 'name': 'Clothes'}, {'id': 5, 'name': 'HomeAppliances'}, {'id': 6, 'name': 'Toys'}, {'id': 7, 'name': 'Accesories'}]
#context
# {'keyproduct': {'id': 14, 'name': 'Nykaa shirts', 'summary': 'Known for elegance', 'color': 'black', 'size': 'small', 'price': 900.0, 'softdelete': b'\x00', 'Buy': None, 'date': datetime.datetime(2022, 8, 6, 11, 51, 6), 'user': None, 'cId': 4}, 'keycategories': [{'id': 1, 'name': 'Electronics'}, {'id': 2, 'name': 'Food'}, {'id': 3, 'name': 'BeautyProducts'}, {'id': 4, 'name': 'Clothes'}, {'id': 5, 'name': 'HomeAppliances'}, {'id': 6, 'name': 'Toys'}, {'id': 7, 'name': 'Accesories'}], 'keyCategoryName': 'Clothes'}

 