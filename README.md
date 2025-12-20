# Ex.06 Book Front Cover Page Design
## Date: 19.12.2025
# Reference No: 25018782

## AIM:
To design a book front cover page using HTML and CSS.

## DESIGN STEPS:

### Step 1:
Create a Django Admin project.

### Step 2:
Create an app in the Django interface.

### Step 3:
Create a folder named 'static' in the app folder.

### Step 4:
Create a new HTML file in the static folder.

### Step 5:
Write the HTML code with relevant CSS properties.

### Step 6:
Choose the appropriate style and color scheme.

### Step 7:
Insert the images in their appropriate places.

### Step 8:
Publish the website in the LocalHost.

## PROGRAM:

~~~
cover.html
-----------
<head>
  <title>Book Cover</title>
</head>
<body style="margin: 0; padding: 0; display: flex; justify-content: center; align-items: center; height: 100vh; background: #fff;">

<div style="width: 350px; height: 500px; background: linear-gradient(135deg, #cb2dffd4, #0510e3); color: white; padding: 20px; position: relative; border: 5px solid #fff;">

    <p style="font-size: 14px; font-weight: bold; color: rgb(10, 6, 119);"></p>
    <hr>
    <h1 style="font-size: 30px; color: #000; font-weight: bold; text-align: center; line-height: 1.4;">The Psychology <br> Of Money<br></h1>
    <hr>
    <p style="font-size: 20px; text-align: center;">Morgan Housel</p>
    
    <p style="font-size: 14px; text-align: center;">TOP SELLER OF 2025</p>

<div style="display: flex; align-items: center;">
        
        <div style="position:absolute;bottom:100px;right:30px;width: 80px; height: 80px;border:5px solid grey;border-radius:25%;overflow:hidden;">
        <img src="Sabii.jpg" alt="Picture" style="width: 100%; height: 100%;"></div>
            
    
        <div><p style="position:absolute;bottom:80px;right:36px;font-size: 14px; margin: 0;text-shadow:-1px -1px 0 #000,1px -1px 0 #000,-1px 1px 0 #000,1px 1px 0 #000;">Sabeeshwaran</p>
        <p style="position:absolute;bottom:65px;right:46px;font-size: 14px; margin: 0;text-shadow:-1px -1px 0 #000,1px -1px 0 #000,-1px 1px 0 #000,1px 1px 0 #000;">2025-2029</p></div>
    
</div>

    
    

</div>
</body>
</html>



views.py
---------
from django.shortcuts import render
def bookapp(request):
    return render(request,'book.html')


urls.py
-------
from django.contrib import admin
from django.urls import path
from bookapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.bookapp),
]

~~~


## OUTPUT:
![alt text](<Screenshot 2025-12-19 161445.png>)


## RESULT:
The program for designing book front cover page using HTML and CSS is completed successfully.
