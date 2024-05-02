from django.shortcuts import render

# Create your views here.

book_list = [
            {
                'id':1,
                'title': 'Book 1',
                'author': 'Author 1',
                'description': 'This is the description for Book 1.',
            },
            {
                'id':2,
                'title': 'Book 2',
                'author': 'Author 2',
                'description': 'This is the description for Book 2.',
            },
            {
                'id':3,
                'title': 'Book 3',
                'author': 'Author 3',
                'description': 'This is the description for Book 3.',
            },
            {
                'id':4,
                'title': 'Book 4',
                'author': 'Author 4',
                'description': 'This is the description for Book 4.',
            },
            {
                'id':5,
                'title': 'Book 5',
                'author': 'Author 5',
                'description': 'This is the description for Book 5.',
            },
        ]

def get_books(request):
    return render(request, 'all-books.html', {'books': book_list});


def get_book(request,*args,**kwargs):
    book_id = kwargs.get('id')
    book = None
    for b in book_list:
        if b['id'] == book_id:
            book = b
            break
    return render(request, 'book.html', {'book': book});


def _get_task(book_id):
    for book in book_list:
        if 'id' in book and book['id'] == book_id:
            return book
    return None
    

def edit_book(request,*args,**kwargs):

    book_id = kwargs.get('book_id')
    book = _get_task(book_id)
    if request.method == 'POST':
        book['title'] = request.POST['title']
        book['author'] = request.POST['author']
        book['description'] = request.POST['description']
        return render(request, 'book.html', {'book': book});
    else:
        return render(request, 'edit_book.html', {'book': book});


def delete_book(request,*args,**kwargs):
    book_id = kwargs.get('book_id')
    book = _get_task(book_id)
    book_list.remove(book)
    return render(request, 'all-books.html', {'books': book_list});
    

def create_book(request):
    if request.method == 'POST':
        book = {
            'id': len(book_list) + 1,
            'title': request.POST['title'],
            'author': request.POST['author'],
            'description': request.POST['description']
        }
        book_list.append(book)
        return render(request, 'all-books.html', {'books': book_list});
    else:
        return render(request, 'create_book.html')