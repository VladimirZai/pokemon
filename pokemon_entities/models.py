from django.db import models

class Pokemon(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, )
    title = models.CharField(max_length=200, blank=True, )
    title_en = models.CharField(max_length=200, blank=True, )
    title_jp = models.CharField(max_length=200, blank=True, )
    description = models.TextField(blank=True, )
    image = models.ImageField(upload_to='pokemons', null=True, blank=True)

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')
    appeared_at = models.DateTimeField(blank=True, null=True)
    disappeared_at = models.DateTimeField(blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    health = models.IntegerField(blank=True, null=True)
    strength = models.IntegerField(blank=True, null=True)
    defence = models.IntegerField(blank=True, null=True)
    stamina = models.IntegerField(blank=True, null=True)
