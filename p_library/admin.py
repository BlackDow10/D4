from django.contrib import admin
from p_library.models import Book, Author, Redaction

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	
	@staticmethod
	def author_full_name(obj):
		return obj.author.full_name
	list_display = ('title', 'author_full_name',)
	fields = ('ISBN', 'title', 'description', 'year_release', 'author', 'price', 'copy_count', 'redact')


@admin.register(Author)
class AdminAuthor(admin.ModelAdmin):
	pass

@admin.register(Redaction)
class AdminRedaction(admin.ModelAdmin):
	pass