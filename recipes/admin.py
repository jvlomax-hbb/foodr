from django.contrib import admin
from django.utils.html import format_html

from recipes.models import Recipe, RecipeStep, Ingredient, IngredientGroup


class RecipeStepInline(admin.StackedInline):
    model = RecipeStep


class IngredientInline(admin.StackedInline):
    model = Ingredient


class IngredientGroupInline(admin.TabularInline):
    model = IngredientGroup
    extra = 0


@admin.register(Recipe)
# Register your models here.
class RecipeAdmin(admin.ModelAdmin):
    inlines = [IngredientGroupInline, IngredientInline, RecipeStepInline]
    list_display = ["title", "source_display"]

    @admin.display(description="Source")
    def source_display(self, obj):
        return format_html(f'<a href={obj.source_url}>{obj.source}</a>')
    source_display.allow_tags = True