from django.conf.urls import include, patterns, url
from django.views.generic import TemplateView
from tastypie.api import Api

from api import ActualReceiptResource, ExpectedReceiptResource, BlockResource, ClusterResource, CountryResource, DistrictResource, PersonResource, LoanResource, LoanSubTypeResource, LoanTypeResource, SHGBaseLineResource, StateResource, SublocationResource, VillageResource
from views import coco_v2, debug, login, logout, record_full_download_time, reset_database_check

v1_api = Api(api_name='v1')
v1_api.register(CountryResource())
v1_api.register(StateResource())
v1_api.register(DistrictResource())
v1_api.register(BlockResource())
v1_api.register(SublocationResource())
v1_api.register(VillageResource())
v1_api.register(PersonResource())
v1_api.register(ClusterResource())
v1_api.register(SHGBaseLineResource())
v1_api.register(LoanTypeResource())
v1_api.register(LoanSubTypeResource())
v1_api.register(LoanResource())
v1_api.register(ExpectedReceiptResource())
v1_api.register(ActualReceiptResource())
#===============================================================================
# v1_api.register(DistrictResource())
# v1_api.register(LanguageResource())
# v1_api.register(PartnerResource())
# v1_api.register(VillageResource())
# 
# v1_api.register(MediatorResource())
# v1_api.register(PersonAdoptVideoResource())
# v1_api.register(PersonResource())
# v1_api.register(PersonGroupResource())
# v1_api.register(ScreeningResource())
# v1_api.register(VideoResource())
#===============================================================================

urlpatterns = patterns('',
    (r'^api/', include(v1_api.urls)),
    (r'^coco/login/', login),
    (r'^coco/logout/', logout),
    (r'^debug/', debug),
    (r'^$', coco_v2),
    url(r'^faq/$', TemplateView.as_view(template_name='faq.html'), name="faq"),
    (r'^coco/record_full_download_time/', record_full_download_time),
    (r'^coco/reset_database_check/', reset_database_check),
)
