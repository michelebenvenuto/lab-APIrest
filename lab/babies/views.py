from guardian.shortcuts import assign_perm
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from permissions.services import APIPermissionClassFactory
from babies.models import Babie
from babies.serializers import BabieSerializer

class BabieViewSet(viewsets.ModelViewSet):
    queryset = Babie.objects.all()
    serializer_class = BabieSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='BabyPermission',
            permission_configuration={
                'base': {
                    'create': lambda user, req: user.is_authenticated,
                    'list': True,
                },
                'instance': {
                    'retrieve': 'babies.view_baby',
                    'destroy': False,
                    'update': True,
                    'addEvent':'babies.change_events',
                    'removeEvent':'babies.change_events',

                }
            }
        ),
    )
    
    def perform_create(self, serializer):
        babie = serializer.save()
        user = self.request.user
        assign_perm('babies.change_events', user, babie)
        assign_perm('babies.view_baby', user, babie)
        return Response(serializer.data)

    @action(detail = True, methods = ['patch'])
    def addEvent(self, request, pk = None):
        babie = self.get_object()
        babie.eventsToBaby.add(request.data.get('event_id'))
        return Response({})

    @action(detail = True, methods = ['patch'])
    def removeEvent(self,request,pk = None):
        babie = self.get_object()
        babie.eventsToBaby.remove(request.data.get('event_id'))