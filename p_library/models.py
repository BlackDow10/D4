from django.db import models

class Author(models.Model):
	full_name = models.TextField()
	birth_year = models.SmallIntegerField()
	country = models.CharField(max_length = 2)
	def __str__(self):
		return self.full_name

class Redaction(models.Model):
	name = models.CharField(max_length = 20)
	def __str__(self):
		return self.name
	
class Book(models.Model):
	ISBN = models.CharField(max_length = 13)
	title = models.TextField()
	description = models.TextField()
	year_release = models.SmallIntegerField()
	author = models.ForeignKey(Author, on_delete=models.CASCADE)
	copy_count = models.SmallIntegerField()
	price = models.DecimalField(max_digits=10, decimal_places=2)
	redact = models.ForeignKey(Redaction, on_delete=models.CASCADE, null=True, blank=True)
	def __str__(self):
		return self.title

