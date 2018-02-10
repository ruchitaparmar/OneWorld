import django_filters
from .models import Refugee


class RefugeeFilter(django_filters.FilterSet):
    firstName = django_filters.CharFilter(lookup_expr='icontains')
    lastName = django_filters.CharFilter(lookup_expr='icontains')
    ID = django_filters.CharFilter(lookup_expr='exact')
    nationality = django_filters.CharFilter(lookup_expr='icontains')
    bID = django_filters.CharFilter(lookup_expr='exact')
    fullNameOfSpouse = django_filters.CharFilter(lookup_expr='icontains')
    fullNameOfOffspring = django_filters.CharFilter(lookup_expr='icontains')
    fullNameOfFather = django_filters.CharFilter(lookup_expr='icontains')
    fullNameOfMother = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Refugee
        fields = ['firstName', 'lastName', 'ID', 'nationality', 
        'bID', 'fullNameOfMother', 'fullNameOfFather', 'fullNameOfOffspring', 
        'fullNameOfSpouse', 'maritalStatus']