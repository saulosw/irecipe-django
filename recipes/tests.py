from django.test import TestCase
from django.urls import reverse, resolve
from recipes import views

class RecipeURLsTest(TestCase):
    def test_url_home_is_working(self):
        home_url = reverse('recipes:home')
        self.assertEqual(home_url, '/')
    
    def test_url_category_is_working(self):
        category_url = reverse('recipes:category', kwargs={'category_id':1})
        self.assertEqual(category_url, '/recipes/category/1/')

    def test_url_recipe_is_working(self):
        recipe_url = reverse('recipes:recipe', kwargs={'id':1 })
        self.assertEqual(recipe_url, '/recipes/1/')

class RecipeViewsTest(TestCase):
    def test_view_function_home_is_working(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)

    def test_view_function_category_is_working(self):
        view = resolve(reverse('recipes:category', kwargs={'category_id':1 }))
        self.assertIs(view.func, views.category)

    def test_view_function_recipes_is_working(self):
        view = resolve(reverse('recipes:recipe', kwargs={ 'id':1 }))
        self.assertIs(view.func, views.recipes)