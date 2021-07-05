from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView
from django.views import View

from .models import Recipes, Categories
from .forms import RecipeForm, UserRegisterForm, UserLoginForm
from django.contrib import messages

from django.contrib.auth import login, logout, admin


# def index(request):
#     recipes = Recipes.objects.all()
#     return render(request, template_name='recipes/index.html', context={'recipes': recipes})


class BaseView(ListView):
    model = Recipes
    template_name = 'recipes/index.html'
    context_object_name = 'recipes'
    extra_context = {
        'title': 'Главная страница'
    }

    def get_queryset(self):
        return Recipes.objects.filter(is_published=True)


class RecipeDetail(DetailView):
    model = Recipes

    # pk_url_kwarg = 'recipe_id'
    # template_name =

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe = Recipes.objects.get(pk=self.kwargs['pk'])
        context['recipe'] = recipe
        context['title'] = recipe.title
        return context


class RecipeByCategoryView(ListView):
    model = Recipes
    template_name = 'recipes/index.html'
    context_object_name = 'recipes'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Categories.objects.get(pk=self.kwargs['pk']).title
        return context

    def get_queryset(self):
        return Recipes.objects.filter(category_id=self.kwargs['pk'], is_published=True)


class AddRecipeView(View):
    def get(self, request, *args, **kwargs):
        form = RecipeForm()
        return render(request, "recipes/edit_recipe.html", {
            "form": form,
            "btn_text": "Добавить рецепт",
            "btn_color": "primary"
        })

    def post(self, request, *args, **kwargs):
        print(request.POST)
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save()
            messages.success(request, "Рецепт успешно добавлен !")
            return redirect(recipe)
        else:
            messages.error(request, "Некоректно заполненые поля !")
            return redirect('add_recipe')


class EditRecipeView(UpdateView):
    form_class = RecipeForm
    template_name = "recipes/edit_recipe.html"
    extra_context = {
        "btn_text": "Изменить рецепт",
        "btn_color": "success",
        "action_url": "edit_recipe"
    }

    def get_queryset(self):
        return Recipes.objects.filter(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        content = super().get_context_data(**kwargs)
        recipe = Recipes.objects.get(pk=self.kwargs["pk"])
        content["recipe"] = recipe
        content["title"] = recipe.title
        return content


class UserLoginView(View):
    def get(self, request, *args, **kwargs):
        form = UserLoginForm()
        return render(request, "recipes/auth_user.html", {
            "form": form,
            "title": "Вход",
            "btn_text": "Вход",
            "btn_color": "primary"
        })

    def post(self, request, *args, **kwargs):
        print(request.POST)
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Вы успешно авторизовались !")
            return redirect("home")
        else:
            messages.error(request, "Ошибка авторизации !")
            return redirect("login")


class UserRegisterView(View):
    def get(self, request, *args, **kwargs):
        form = UserRegisterForm()
        return render(request, "recipes/auth_user.html", {
            "form": form,
            "title": "Регистрация",
            "btn_text": "Регистрация",
            "btn_color": "success"
        })

    def post(self, request, *args, **kwargs):
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Вы успешно авторизовались !")
            return redirect("home")
        else:
            messages.error(request, "Ошибка регистрации !")
            return redirect("register")


class UserLogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, "Вы успешно вышли из аккаунта !")
        return redirect("home")


def view_user_profile(request, username):
    user = get_object_or_404(User, username=username)
    recipe_by_date = Recipes.objects.filter(
        user_id=user_id
    )
    return render(request, 'recipes/profile.html', {
        'profile_user': user
        # ,'recipe': recipe_by_date
    })