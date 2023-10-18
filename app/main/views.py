from django.shortcuts import render, redirect
from .encyrption import *
from account.forms import *

# Create your views here.


def index(request):
    if not request.user.is_authenticated:
        return redirect("login")
    
    if request.user.is_superuser==True:
        return redirect("admin/")

    text = "idrisjaf"
    key_t = "DHU2023"
    plaintext = string_to_binary(text)
   
    key = string_to_binary(key_t)
    ciphertext = des_encrypt(plaintext,key)
    real_data = des_decrypt(ciphertext,key)
    my_data = binary_to_string(real_data)

    print(plaintext)
    
    print(my_data)
   
    return render(request,"index.html")



def apps(request):
    return render(request,"apps.html")


def encyrption(request):
    context = {}
    data = {}
    if request.method == 'POST':
        print("I am in first if")
        form = EncyrptionForm(request.POST)

        if form.is_valid():
            text = form.cleaned_data['text']
            key = form.cleaned_data['key']


            plaintext = string_to_binary(text)
            binary_key = string_to_binary(key)
            ciphertext = des_encrypt(plaintext,binary_key)

            print(ciphertext)

            context["result"] = ciphertext
            context["key"] = binary_key

            print(text)
            print(key)
            print(data)
            # retur n redirect("encyrption")
          
    else:
        form = EncyrptionForm()

    print(data)

    context["form"] = form
    

    return render(request,"encyrpt.html",context)



def decyrption(request):
    context = {}
    data = {}
    if request.method == 'POST':
        print("I am in first if")
        form = DecyrptionForm(request.POST)

        if form.is_valid():
            text = form.cleaned_data['text']
            key = form.cleaned_data['key']


            
            
            real_data = des_decrypt(text,key)

            

            context["result"] = binary_to_string(real_data).strip()
            context["key"] = binary_to_string(key).strip()

            print(text)
            print(key)
            print(data)
            # retur n redirect("encyrption")
          
    else:
        form = DecyrptionForm()

    print(data)

    context["form"] = form
    

    return render(request,"decrypt.html",context)