from django.db import models
from django.urls import reverse
from datetime import date

MEALS = (
  ('B', 'Breakfast'),
  ('L', 'Lunch'),
  ('D', 'Dinner')
)

# Create models
class Finch(models.Model):
  name = models.CharField(max_length=100)
  breed = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField()

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('finch-detail', kwargs={'finch_id': self.id})
  
  def fed_for_today(self):
    return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)
   
class Feeding(models.Model):
    date = models.DateField('Feeding date')
    meal = models.CharField(
      max_length=1,
      # add the 'choices' field option
      choices=MEALS,
      # set the default value for meal to be 'B'
      default=MEALS[0][0]
    )

    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)
    
    def __str__(self):
      return f"{self.get_meal_display()} on {self.date}"
    
    class Meta:
      ordering = ['-date']

    