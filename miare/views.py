from rest_framework.views import APIView
from . import models, serializers
from rest_framework.response import Response


class CapacityReportView(APIView):

    def get(self, *args, **kwargs):
        capacities = models.Capacity.objects.all()

        for capacity in capacities:

            counted_couriershift = models.CourierShift.objects.filter(
                area=capacity.area, 
                shift=capacity.shift,
                shift_begin__lte=capacity.date,
                shift_end__gte=capacity.date).count()

            capacity.free_capacity = capacity.capacity - counted_couriershift

        capacities_data = serializers.CapacitySerializer(instance=capacities, many=True).data

        return Response(capacities_data)                  
