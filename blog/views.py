from multiprocessing import context
from django.shortcuts import render

posts = [
    {
        'author': 'John Doe',
        'title': 'First Post',
        'content': 'This is a sample content.',
        'date_posted': 'August 15, 2021'
    },
    {
        'author': 'Jane Doe',
        'title': 'Second Post',
        'content': 'Another sample content.',
        'date_posted': 'August 20, 2021'
    },
    {
        'author': 'John Doe',
        'title': 'Third Post',
        'content': 'Yet another sample content.',
        'date_posted': 'August 25, 2021'
    },
    {
        'author': 'Jane Doe',
        'title': 'Fourth Post',
        'content': 'The final sample content.',
        'date_posted': 'September 1, 2021'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})
