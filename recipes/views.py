from os import path
from urllib.parse import urlparse

import requests
from django.core.files.base import ContentFile
from django.db import transaction
from django.shortcuts import redirect
from django.urls import reverse
from recipe_scrapers import scrape_me

from django.views import View
from django.views.generic import DetailView, ListView

from recipes.models import Recipe, RecipeStep, Ingredient


class RecipeView(DetailView):
    model = Recipe
    template_name = "recipe_detail.html"


class RecipeListView(ListView):
    model = Recipe
    template_name = "recipe_list.html"


class AddRecipeByUrlView(View):

    def post(self, request):
        url = request.POST.get("url")
        print(url)
        # TODO: We should try without wild_mode first, and warn the user if it fails.
        # They can then decide if they want to try the experimental mode
        scraper = scrape_me(url, wild_mode=True)
        if not scraper.title():
            return 500
        else:
            image = ContentFile(requests.get(scraper.image()).content)
            image_name = path.basename(urlparse(scraper.image()).path)
            with transaction.atomic():
                recipe = Recipe(
                    title=scraper.title(),
                    portions=scraper.yields(),
                    source_url=url,
                    source=scraper.host().capitalize(),
                    description=scraper.description()
                )
                recipe.image.save(image_name, image)
                recipe.save()
                for step in scraper.instructions_list():
                    RecipeStep(recipe=recipe, description=step).save()
                for ingredient in scraper.ingredients():
                    Ingredient(recipe=recipe, name=ingredient).save()

        return redirect(reverse("recipes"))