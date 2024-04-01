from django.contrib import admin
from .models import Category
from .models import Product
# Register your models here.
from .models import Order
from .models import OrderItem

from .models import ProductDetailsList
from .models import ProductDetailsListItems
from .models import ProductDetailsListItem

from .models import Address
from .models import Payment
from import_export.admin import ImportExportModelAdmin

from .models import ProductMetas
from .models import ProductKeywordsSet
from .models import ProductKeywords
from .models import Brand

from .models import TaxSettings
from .models import TaxRate
from .models import Newsletters
from .models import ShippingCarrier
from .models import ShippingSettings


from .models import ProductVariations
from .models import ProductVariable
from .models import VariableColor
from .models import ProductVariableProductImageGallery
from .models import ProductVariationImage
from .models import ProductVariationType

from .models import Reviews
from .models import ProductColor
from .models import Refunds



from mptt.admin import MPTTModelAdmin

from mptt.admin import DraggableMPTTAdmin


import adminactions.actions as actions

from advanced_filters.admin import AdminAdvancedFiltersMixin

from .models import ProductStockManagement


@admin.register(ProductStockManagement)
class ProductStockManagementAdmin(ImportExportModelAdmin):
	pass
@admin.register(Reviews)
class ReviewsAdmin(AdminAdvancedFiltersMixin,ImportExportModelAdmin):
	list_display = ['title','slug']
	prepopulated_fields = {
		'slug':('title',)
	}

admin.site.register(Refunds)

@admin.register(Newsletters)
class NewslettersAdmin(ImportExportModelAdmin):
	list_display = ['email_address']
	prepopulated_fields = {}


@admin.register(ProductColor)
class ProductColorAdmin(ImportExportModelAdmin):
	list_display = ['title','slug','color']
	prepopulated_fields = {
		'slug':('title',)
	}
from .models import ProductSizeSet
from .models import ProductSize
@admin.register(ProductSizeSet)
class ProductSizeSetAdmin(ImportExportModelAdmin):
	list_display = ['title','slug']
	prepopulated_fields = {
		'slug':('title',)
	}
@admin.register(ProductSize)
class ProductSizeAdmin(ImportExportModelAdmin):
	pass

from .models import ProductSpecificationsSets
from .models import ProductSpecifications
from .models import ProductSpecification




from .models import ProductAttributesSets
from .models import ProductAttributes
from .models import ProductAttribute



from .models import Wishlist


@admin.register(Wishlist)
class WishlistAdmin(ImportExportModelAdmin):
	list_display = ['title','slug']
	prepopulated_fields = {
		'slug':('title',)
	}


@admin.register(ProductAttributesSets)
class ProductAttributesSetsAdmin(ImportExportModelAdmin):
	pass

@admin.register(ProductAttributes)
class ProductAttributesAdmin(ImportExportModelAdmin):
	pass

@admin.register(ProductAttribute)
class ProductAttributeAdmin(ImportExportModelAdmin):
	pass



	


@admin.register(ProductSpecificationsSets)
class ProductSpecificationsSetsAdmin(ImportExportModelAdmin):
	pass

@admin.register(ProductSpecifications)
class ProductSpecificationsAdmin(ImportExportModelAdmin):
	pass

@admin.register(ProductSpecification)
class ProductSpecificationAdmin(ImportExportModelAdmin):
	pass






@admin.register(ProductVariations)
class ProductVariationsAdmin(ImportExportModelAdmin):
	pass

@admin.register(ProductVariable)
class ProductVariableAdmin(ImportExportModelAdmin):
	list_display = ['title','slug', 'price_regular','price_sale','price_final','MSRP_price','MAP_price']
	prepopulated_fields = {
		'slug':('title',)
	}
	list_editable = ['price_regular','price_sale','price_final','MSRP_price','MAP_price']
	search_fields = ['title','slug','price_regular','price_sale','price_final','MSRP_price','MAP_price']




@admin.register(VariableColor)
class VariableColorAdmin(ImportExportModelAdmin):
	pass


@admin.register(ProductVariableProductImageGallery)
class ProductVariableProductImageGalleryAdmin(ImportExportModelAdmin):
	pass

@admin.register(ProductVariationImage)
class ProductVariationImageAdmin(ImportExportModelAdmin):
	pass

@admin.register(ProductVariationType)
class ProductVariationTypeAdmin(ImportExportModelAdmin):
	pass


from .models import Coupon
@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
	list_display = ['title','slug']
	prepopulated_fields = {
		'slug':('title',)
	}

@admin.register(ShippingCarrier)
class ShippingCarrierAdmin(admin.ModelAdmin):
	list_display = ['title','slug']
	prepopulated_fields = {
		'slug':('title',)
	}

@admin.register(ShippingSettings)
class ShippingSettingsAdmin(admin.ModelAdmin):
	list_display = ['title','slug']
	prepopulated_fields = {
		'slug':('title',)
	}


@admin.register(TaxSettings)
class TaxSettingsAdmin(admin.ModelAdmin):
	list_display = ['title','slug']
	prepopulated_fields = {
		'slug':('title',)
	}

@admin.register(TaxRate)
class TaxRateAdmin(admin.ModelAdmin):
	pass



@admin.register(ProductMetas)
class ProductMetasAdmin(admin.ModelAdmin):
	pass

@admin.register(ProductKeywordsSet)
class ProductKeywordsSetAdmin(admin.ModelAdmin):
	pass

@admin.register(ProductKeywords)
class ProductKeywordsAdmin(admin.ModelAdmin):
	pass

@admin.register(Brand)
class BrandAdmin(ImportExportModelAdmin):
	list_display = ['title','slug']
	prepopulated_fields = {
		'slug':('title',)
	}

from .models import ProductTagsCloud
from .models import ProductTagsClouds
from .models import ProductTagsCloudsSet
@admin.register(ProductTagsCloud)
class ProductTagsCloudAdmin(ImportExportModelAdmin):
	pass
@admin.register(ProductTagsClouds)
class ProductTagsCloudsAdmin(ImportExportModelAdmin):
	pass
@admin.register(ProductTagsCloudsSet)
class ProductTagsCloudsSetAdmin(ImportExportModelAdmin):
	pass


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
	pass
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
	pass


admin.site.register(
    Category,
    DraggableMPTTAdmin,
    list_display=(

        'tree_actions',
        'indented_title',
        # ...more fields if you feel like it...
        'title',
    	'slug',
    	'category_cover_image'
    ),
    list_display_links=(
        'indented_title',
    ),
    prepopulated_fields = {
		'slug':('title',)
	},
	list_editable = ['category_cover_image']
)

'''
@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
	list_display = ['id','title','slug','description']
	prepopulated_fields = {
		'slug':('title',)
	}
	list_editable = ['title','slug']
'''
@admin.register(Product)
class ProductAdmin(AdminAdvancedFiltersMixin,ImportExportModelAdmin):
	list_display = ['id','title','slug','product_status','price_regular','price_sale','product_type','brand']
	prepopulated_fields = {
		'slug':('title',)
	}
	list_editable = ['title','slug','product_status','price_regular','price_sale','product_type','brand']
	search_fields = ['title','slug','product_status','price_regular','price_sale','product_type']
	list_filter =  ['title','slug','product_status','price_regular','price_sale','product_type']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
	pass
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
	pass



@admin.register(ProductDetailsList)
class ProductDetailsListAdmin(admin.ModelAdmin):
	list_display = ['title','slug']
	prepopulated_fields = {
		'slug':('title',)
	}
@admin.register(ProductDetailsListItems)
class ProductDetailsListItemsAdmin(admin.ModelAdmin):
	pass
@admin.register(ProductDetailsListItem)
class ProductDetailsListItemAdmin(admin.ModelAdmin):
	list_display = ['title','slug']
	prepopulated_fields = {
		'slug':('title',)
	}


from .models import ProductGalleryImage
from .models import ProductGalleryImagesSet
from .models import ProductImageGallery


@admin.register(ProductGalleryImage)
class ProductGalleryImageAdmin(ImportExportModelAdmin):
	pass

@admin.register(ProductGalleryImagesSet)
class ProductGalleryImagesSetAdmin(ImportExportModelAdmin):
	pass

@admin.register(ProductImageGallery)
class ProductImageGalleryAdmin(ImportExportModelAdmin):
	pass