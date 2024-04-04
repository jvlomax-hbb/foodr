from django.db import models


# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=255, help_text="Name of the recipe", unique=True, db_index=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True)
    source = models.CharField(max_length=255, null=True, blank=True)
    source_url = models.URLField(null=True, blank=True)
    portions = models.CharField(null=True, blank=True, max_length=128)

    def __str__(self):
        return self.title


class RecipeStep(models.Model):
    description = models.TextField()
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="steps")

    def __str__(self):
        return f"Recipe Step for {self.recipe}"


class IngredientGroup(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="ingredient_groups")
    title = models.CharField(max_length=255)
    amount = models.PositiveSmallIntegerField(null=True, blank=True)

    def __str__(self):
        return self.title


class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="ingredients")
    ingredient_group = models.ForeignKey(IngredientGroup, on_delete=models.SET_NULL, null=True, related_name="group_ingredients", blank=True)
    #4unit = models.ForeignKey("Unit", on_delete=models.PROTECT)

    def __str__(self):
        return self.name
