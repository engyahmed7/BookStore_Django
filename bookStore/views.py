from django.shortcuts import render, redirect
from .models import BokkStore
from .forms import BookForm

# Create your views here.
  
def index(request):
    books = BokkStore.objects.all()
    return render(request, 'index.html', {'books': books})

# def create(request):
#     return render(request, 'create_book.html')

def create(request):
    form = BookForm()
    if request.method == 'POST':
       form = BookForm(data=request.POST)
       if form.is_valid():
           form.save()
           return redirect('bookStore:getAll')
    return render(request, 'create_book.html',{'form': form})

def update(request,pk):
    book = BokkStore.objects.get(pk=pk)
    form = BookForm(instance=book)
    if request.method == 'POST':
       form = BookForm(data=request.POST, instance=book)
       if form.is_valid():
           form.save()
           return redirect('bookStore:getAll')
    return render(request, 'edit_book.html',{'form': form , 'pk': pk})


def show(request , pk):
    book=BokkStore.objects.get(pk=pk)
    return render(request, 'book.html', {'book': book})

def destroy(request,pk):
    book=BokkStore.objects.get(pk=pk)
    book.delete()
    return redirect('bookStore:getAll')