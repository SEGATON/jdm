import django_filters

from .models import Product,ProductColor, Brand



class ProductFilter(django_filters.FilterSet):






    price__gt = django_filters.AllValuesFilter(field_name='price_regular', lookup_expr='gt')
    price__lt = django_filters.AllValuesFilter(field_name='price_regular', lookup_expr='lt')
 

    brand = django_filters.ModelMultipleChoiceFilter(queryset=Brand.objects.all())
    

    def colors(request):
        
        return ProductColor.objects.all()


    product_color = django_filters.filters.ModelMultipleChoiceFilter(queryset=colors)

    class Meta:
        model = Product
        fields = ['price_sale','price_regular', 'date_added','product_color']


class ProductRegularPriceFilter(django_filters.FilterSet):

    
    price_regular= django_filters.AllValuesFilter()



    class Meta:
        model = Product
        fields = ['price_sale','price_regular', 'date_added','product_color']