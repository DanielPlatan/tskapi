from rest_framework import serializers
from tsk.models import Metrics


class MetricsPreviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metrics
        fields = ['date', 'channel', 'country', 'os', 'impressions', 'clicks', 'installs', 'spend', 'revenue', 'cpi']

    def __init__(self, *args, **kwargs):
        super(MetricsPreviewSerializer, self).__init__(*args, **kwargs)

        fields = self.context['request'].query_params.get('col')
        if fields:
            fields = fields.split(',')
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)