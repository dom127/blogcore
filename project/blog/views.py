from django.shortcuts import render

posts = [
    {
        'author': 'Dominik J',
        'title': 'Riders on the storm',
        'date_posted': '19.10.2018',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi libero nulla, facilisis quis eleifend sed, faucibus a velit. Nulla tellus urna, finibus sed aliquet id, ullamcorper vel sapien. Morbi at tempus nisl, id bibendum mi. Mauris id auctor urna. Cras vulputate convallis erat eu blandit. Etiam auctor ex in odio sodales lacinia. Ut rutrum nisi in quam porta aliquam. Aenean diam metus, laoreet at dui vel, tincidunt varius tortor. Proin sed lacus dignissim libero sagittis sodales sed quis lorem. Aenean vitae faucibus felis. Duis quis leo commodo, sodales mauris quis, volutpat dui. Ut convallis tellus nec dui sodales porttitor. '
    },
    {
        'author': 'Michal J',
        'title': 'Something new',
        'date_posted': '18.10.2018',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi libero nulla, facilisis quis eleifend sed, faucibus a velit. Nulla tellus urna, finibus sed aliquet id, ullamcorper vel sapien. Morbi at tempus nisl, id bibendum mi. Mauris id auctor urna. Cras vulputate convallis erat eu blandit. Etiam auctor ex in odio sodales lacinia. Ut rutrum nisi in quam porta aliquam. Aenean diam metus, laoreet at dui vel, tincidunt varius tortor. Proin sed lacus dignissim libero sagittis sodales sed quis lorem. Aenean vitae faucibus felis. Duis quis leo commodo, sodales mauris quis, volutpat dui. Ut convallis tellus nec dui sodales porttitor. '
            },
    {
        'author': 'Milena J',
        'title': 'Eyelashes',
        'date_posted': '17.10.2018',
        'content': 'Some content here'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About this page'})