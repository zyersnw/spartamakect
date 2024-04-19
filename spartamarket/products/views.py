from django.shortcuts import render, get_object_or_404, redirect
from .models import Item, Like, Favorite
from .forms import ItemForm
from .forms import CommentForm

def item_list(request):
    items = Item.objects.all().order_by('-pk')
    return render(request, 'item_list.html', {'items': items})

def item_detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    return render(request, 'item_detail.html', {'item': item})
def item_create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():

            item = form.save(commit=False)
            item.seller = request.user
            item.save()
            return redirect('item_list')
    else:
        form = ItemForm()
    return render(request, 'item_create.html', {'form': form})

def item_update(request):
    pass

def item_delete(request):
    pass

def add_comment_to_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.item = item
            comment.author = request.user
            comment.save()
            return redirect('item_detail', item_id=item_id)
    else:
        form = CommentForm()
    return render(request, 'add_comment_to_item.html', {'form': form})

def like_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    like, created = Like.objects.get_or_create(user=request.user, item=item)
    if not created:
        like.delete()
    return redirect('item_detail', item_id=item_id)

def favorite_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    favorite, created = Favorite.objects.get_or_create(user=request.user, item=item)
    if not created:
        favorite.delete()
    return redirect('item_detail', item_id=item_id)