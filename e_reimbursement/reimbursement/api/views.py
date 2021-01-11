from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from django_multitenant.models import get_current_tenant

from e_reimbursement.reimbursement.api.serializers import ReimbursementSerializers
from e_reimbursement.reimbursement.models import Reimbursement


class ReimbursementViewSet(CreateModelMixin, RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = ReimbursementSerializers
    queryset = Reimbursement.objects.all()
    lookup_field = "pk"

    def get_queryset(self, *args, **kwargs):
        if get_current_tenant():
            kwargs.update({"employee": get_current_tenant()})
        return self.queryset.filter(**kwargs)

    @action(detail=True, methods=["GET", "PUT"])
    def reject(self, request, pk):
        print(request, pk)
        queryset = Reimbursement.objects.get(pk=pk)
        queryset.status = Reimbursement.STATUS_CHOICES.rejected
        queryset.save()
        serializer = self.get_serializer(queryset, many=False)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @action(detail=True, methods=["GET", "PUT"])
    def accept(self, request, pk):
        queryset = Reimbursement.objects.get(pk=pk)
        queryset.status = Reimbursement.STATUS_CHOICES.accepted
        queryset.save()
        serializer = self.get_serializer(queryset, many=False)
        return Response(status=status.HTTP_200_OK, data=serializer.data)