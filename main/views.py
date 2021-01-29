from django.shortcuts import render, HttpResponse, redirect
from .models  import ToDo, Book

def homepage(request):
   return render(request, "index.html")

def test(request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html",{"todo_list":todo_list})

def go(request):
    return render(request, "go.html")

def second(request):
    return HttpResponse("Second test page.")

def third(request):
    return HttpResponse("This is third test page")



def add_todo(request):
    form = request.POST
    text = form["todo_text"]
    todo = ToDo(text = text)
    todo.save() 
    return redirect(test)

def delete_todo(request, id):
    todo = ToDo.objects.get(id = id)
    todo.delete()
    return redirect(test)

def marked_todo(request, id):
    todo = ToDo.objects.get(id = id)
    todo.is_favorites = True
    todo.save() # сохраняет изменения  
    return redirect(test)

def unmarked_todo(request, id):
    todo = ToDo.objects.get(id = id)
    todo.is_favorites = False
    todo.save() # сохраняет изменения  
    return redirect(test)

def close_todo(request, id):
    todo = ToDo.objects.get(id = id)
    todo.is_done = True
    todo.save()  
    return redirect(test)

 
def books(request):
    books = Book.objects.all()
    return render(request, "books.html",{"books": books})

def add_book(request):
    form = request.POST #переменная форм из тега Form)
    book = Book(
        title=form["title"],
        subtitle=form["subtitle"],
        description=form["description"],
        price=form["price"],
        genre=form["genre"],
        author=form["author"],
        year=form["year"][:10],
    )
    book.save()
    return redirect(books) # передаю функцию books, которую прописала выше

def unmarked_book(request, id):
    books = Book.objects.get(id = id)
    books.is_favorites = False
    books.save() 
    return redirect(books)

def marked_book(request, id):
    books = Book.objects.get(id = id)
    books.is_favorites = False
    books.save() 
    return redirect(books)

def delete_book(request, id):
    books = Book.objects.get(id = id)
    books.delete()
    return redirect(books)