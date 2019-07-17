from django_netjsonconfig.models import Template, Vpn
from django_x509.models import Ca, Cert

from .generics import BaseListTemplateView, BaseTemplateDetailView
from .serializers import (CaSerializer, CertSerializer, ListTemplateSerializer, TemplateDetailSerializer,
                          VpnSerializer)


class TemplateDetailView(BaseTemplateDetailView):
    """
    Concrete view to get template details.
    """
    # Dynamically set the serializer models
    template_model = Template
    vpn_model = Vpn
    ca_model = Ca
    cert_model = Cert
    # Specify serializers to be used in base views.
    # This is done so as to enable the base views to
    # be reusable in repos which have some modifications
    # in their serializers.
    template_detail_serializer = TemplateDetailSerializer
    ca_serializer = CaSerializer
    cert_serializer = CertSerializer
    vpn_serializer = VpnSerializer
    queryset = Template.objects.none()


class ListTemplateView(BaseListTemplateView):
    queryset = Template.objects.all()
    template_model = Template
    list_serializer = ListTemplateSerializer


template_detail = TemplateDetailView.as_view()
list_template = ListTemplateView.as_view()