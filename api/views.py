from rest_framework import viewsets
from .serializers import *
from tsk.models import Metrics
from api.forms import MtrxValidationForm
from django.db.models import F
from django.db.models import Sum, Case, When, FloatField


class MetricsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Metrics.objects.all()

    def get_serializer_class(self):
        return MetricsPreviewSerializer

    def get_queryset(self):
        if self.request.method == 'GET':
            form = MtrxValidationForm(self.request.query_params)
            if form.is_valid():
                revenue = form.cleaned_data['revenue']
                country = form.cleaned_data['country']
                os = form.cleaned_data['os']
                channel = form.cleaned_data['channel']
                date_of = form.cleaned_data['date_of']
                date_to = form.cleaned_data['date_to']
                order_by = form.cleaned_data['order_by']
                group_by = form.cleaned_data['group_by']
                sort = form.cleaned_data['sort']
                cpi_annotation = Case(
                    When(installs=0, then=0.0),
                    default=F('spend') / F('installs'),
                    output_field=FloatField()
                )
                group_by = group_by.split(',')
                queryset = Metrics.objects.values(*group_by).annotate(
                    **{'installs': Sum('installs'), 'clicks': Sum('clicks'), 'revenue': Sum('revenue'),
                     'impressions': Sum('impressions')}).annotate(**{'cpi': cpi_annotation})
                if date_of != None and date_to != None:
                    if date_of == date_to:
                        queryset = queryset.filter(date=date_of)
                    else:
                        queryset = queryset.filter(date__gte=date_of, date__lte=date_to)
                else:
                    if date_of != None:
                        queryset = queryset.filter(date__gte=date_of)
                    if date_to != None:
                        queryset = queryset.filter(date__lte=date_to)
                if country:
                    queryset = queryset.filter(country=country)
                if os:
                    queryset = queryset.filter(os=os)
                if channel:
                    queryset = queryset.filter(channel=channel)
                if revenue:
                    queryset = queryset.filter(revenue=revenue)
                if order_by and sort:
                    if sort == 'desc':
                        sign = '-'
                    else:
                        sign = ''
                    queryset = queryset.order_by(sign+order_by)
                return queryset