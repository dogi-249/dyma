from django.shortcuts import render
from django.http import HttpResponse
from .models import Category,Tag, Clothing
from django.views import generic

# Create your views here.
def test(request):
  return render(request, 'clothing/test.html')

""" タグ一覧 """
def category(request, category):
    category = Category.objects.get(name=category)
    clothing = Clothing.objects.filter(category=category)
    return render(request, 'clothing/index.html',
                   {'category': category, 'clothing': clothing })

def tag(request, tag):
    tag = Tag.objects.get(name=tag)
    clothing = Clothing.objects.filter(tag=tag)
    return render(request, 'clothing/index.html', {'tag': tag, 'clothing': clothing })

def detail(request, clothing_id):

class IndexView(generic.ListView):
    model = Clothing
    template_name = 'clothing/index.html'

    def get_queryset(self):
        queryset = Clothing.objects.order_by('-id')
        return queryset


""" カテゴリー一覧 """
class CategoryView(generic.ListView):
    model = Clothing
    template_name = 'clothing/index.html'

    def get_queryset(self):
        category = Category.objects.get(name=self.kwargs['category'])
        queryset = Clothing.objects.order_by('-id').filter(category=category)
        return queryset

    """ アクセスされた値を取得し辞書に格納 """
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_key'] = self.kwargs['category']
        return context

""" タグ一覧 """
class TagView(generic.ListView):
    model = Clothing
    template_name = 'clothing/index.html'

    def get_queryset(self):
        tag = Tag.objects.get(name=self.kwargs['tag'])
        queryset = Clothing.objects.order_by('-id').filter(tag=tag)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag_key'] = self.kwargs['tag']
        return context

def detail(request, clothing_id):
