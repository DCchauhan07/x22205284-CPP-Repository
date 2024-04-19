from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Recipe
from django.urls import reverse_lazy
import random

def foodquote():
    quotes = [
        "Life is uncertain. Eat dessert first.",
        "Good food is good mood.",
        "There is no love sincerer than the love of food.",
        "All you need is love. But a little chocolate now and then doesn't hurt.",
        "Cooking is love made visible.",
        "One cannot think well, love well, sleep well, if one has not dined well.",
        "Food is symbolic of love when words are inadequate.",
        "People who love to eat are always the best people.",
        "Laughter is brightest in the place where the food is.",
        "Food is the ingredient that binds us together.",
        "The only thing I like better than talking about food is eating.",
        "The secret ingredient is always love.",
        "Food tastes better when you eat it with your family.",
        "Eating is a necessity but cooking is an art.",
        "Happiness is homemade.",
        "There is no sincerer love than the love of food.",
        "First we eat, then we do everything else."
    ]
    return random.choice(quotes)

print('hey')
print(foodquote())

# Create your views here.
def home(request):
    context = {
        'recipes': recipes,
    }
    
    return render(request, "recipes/home.html", context)

class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes/home.html'
    context_object_name = 'recipes'

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipes/recipe_detail.html'
    context_object_name = 'recipe'

class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    fields = ['title', 'description']
    template_name = 'recipes/recipe_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Recipe
    fields = ['title', 'description']
    template_name = 'recipes/recipe_form.html'
    success_url = '/recipes/'

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Recipe
    template_name = 'recipes/recipe_delete.html'
    success_url = reverse_lazy('recipes-home')

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author

def about(request):
    quotes = foodquote()
    context = {
        'quotes' : quotes
    }
    print(context)
    return render(request, "recipes/about.html", {'context' : context})
