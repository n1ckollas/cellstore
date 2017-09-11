from django.contrib import admin

# Register your models here.

from .models import Product, Variation, ProductImage, Category, ProductFeatured

class VariationInline(admin.TabularInline):
	model = Variation
	extra = 0
	max_num = 10

class VariationAdmin(admin.ModelAdmin):
	model = Variation
	list_display = ['id',  'product', '__unicode__',]

class ProductImageInline(admin.TabularInline):
	model = ProductImage
	extra = 0
	max_num = 10

class ProductAdmin(admin.ModelAdmin):
	list_display = ['__unicode__', 'price']

	inlines = [
		VariationInline,
		ProductImageInline,
		]

	class Meta:
		model = Product

admin.site.register(Product, ProductAdmin)
admin.site.register(Variation, VariationAdmin)
# admin.site.register(ProductImage)
admin.site.register(Category)
admin.site.register(ProductFeatured)

