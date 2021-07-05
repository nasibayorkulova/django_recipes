from django.urls import path
from .views import (
    BaseView, RecipeDetail,
    RecipeByCategoryView, AddRecipeView,
    EditRecipeView, UserRegisterView,
    UserLogoutView,
    UserLoginView, view_user_profile
)

# localhost:8000/recipe-detail/2
urlpatterns = [
    path('', BaseView.as_view(), name='home'),
    path('recipe-detail/<int:pk>', RecipeDetail.as_view(), name='recipe_detail'),
    path('category/<int:pk>', RecipeByCategoryView.as_view(), name='category'),

    path("add-recipe/", AddRecipeView.as_view(), name="add_recipe"),
    path("edit-recipe/<int:pk>", EditRecipeView.as_view(), name="edit_recipe"),

    path("register/", UserRegisterView.as_view(), name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path(r'<username>', view_user_profile, name="profile")
]
