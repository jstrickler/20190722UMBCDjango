from django.contrib import admin

# Register your models here.

from superheroes.models import Superhero, Power, Enemy, City # <1>

class PowersInline(admin.TabularInline):
    model = Power
    extra = 0

class SuperheroAdmin(admin.ModelAdmin):
    list_display = (
        "name", "real_name", "city", "secret_identity",
        "_powers",
    )

    search_fields = ["username"]

    inlines = [
        PowersInline,
    ]

    def _powers(self, obj):
        return obj.powers.all().count()

admin.site.register(Superhero, SuperheroAdmin)  # <2>
admin.site.register(City) # <2>
admin.site.register(Enemy) # <2>
admin.site.register(Power)

