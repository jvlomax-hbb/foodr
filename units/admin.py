from django.contrib import admin
from django import forms
from units.models import Unit, UnitCategory, UnitConversionRatio


# Register your models here.
class UnitInline(admin.TabularInline):
    model = Unit


@admin.register(UnitCategory)
class UnitCategeoryAdmin(admin.ModelAdmin):
    inlines = [UnitInline]


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    pass


class UnitConversionModelForm(forms.ModelForm):
    reversable = forms.BooleanField()

    class Meta:
        model = UnitConversionRatio
        fields = '__all__'

    def save(self, commit=True):
        reversable = self.cleaned_data.get("reversable", False)
        if reversable:
            ratio = 1 / self.cleaned_data.get("ratio")
            cr = UnitConversionRatio(from_unit=self.cleaned_data.get("to_unit"), to_unit=self.cleaned_data.get("from_unit"), ratio=ratio)
            cr.save()
        return super().save(commit=commit)


@admin.register(UnitConversionRatio)
class UnitConversionRatioAdmin(admin.ModelAdmin):
    form = UnitConversionModelForm

    list_display = ["__str__", "ratio"]