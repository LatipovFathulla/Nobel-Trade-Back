from rest_framework.serializers import ModelSerializer, SerializerMethodField

from product.models import CategoryModel, SubCategoryModel, ProductModel


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ['id', 'title', 'description', 'created_at']


class CategoryTitleSerializer(ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ['title']


class SubCategoryModelSerializer(ModelSerializer):
    category = CategoryTitleSerializer(read_only=True)

    class Meta:
        model = SubCategoryModel
        fields = ['id', 'category',  'subcategory', 'description', 'created_at']


class SubCategoryTitleSerializer(ModelSerializer):
    class Meta:
        model = SubCategoryModel
        fields = ['subcategory']


class ProductModelSerializer(ModelSerializer):
    category = CategoryTitleSerializer(many=True, read_only=True)
    subcategory = SubCategoryTitleSerializer(read_only=True)

    class Meta:
        model = ProductModel
        fields = ['id', 'title', 'is_new', 'category', 'subcategory', 'short_descriptions', 'descriptions',
                  'image', 'objectPDF',
                  'updated_at', 'created_at']

    def get_img_url(self, obj):
        return self.context['request'].build_absolute_url(obj.image.url)


class TestSubCategorySerializer(ModelSerializer):
    products = ProductModelSerializer(many=True, read_only=True, source='pr_subcategories')

    class Meta:
        model = SubCategoryModel
        fields = ['id', 'subcategory', 'description', 'created_at', 'products']


class TestCategorySerializer(ModelSerializer):
    subcategories = TestSubCategorySerializer(many=True, read_only=True, source='subcategory')
    products = SerializerMethodField()

    class Meta:
        model = CategoryModel
        fields = ['id', 'title', 'description', 'created_at', 'subcategories', 'products']

    def get_products(self, obj):
        # Получаем продукты, которые принадлежат данной категории, но не принадлежат подкатегориям
        products = ProductModel.objects.filter(category=obj, subcategory__isnull=True)
        return ProductModelSerializer(products, many=True).data