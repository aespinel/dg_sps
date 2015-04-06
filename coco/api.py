from functools import partial
from django.core.exceptions import ObjectDoesNotExist
from django.forms.models import model_to_dict, ModelChoiceField
from tastypie import fields
from tastypie.authentication import SessionAuthentication
from tastypie.authorization import Authorization
from tastypie.exceptions import NotFound
from tastypie.resources import ModelResource, NOT_AVAILABLE
from tastypie.validation import FormValidation

from coco.models import *

# Will need to changed when the location of forms.py is changed
#from dashboard.forms import AnimatorForm, PersonAdoptPracticeForm, PersonForm, PersonGroupForm, ScreeningForm, VideoForm


### Reference for below class https://github.com/toastdriven/django-tastypie/issues/152
class ModelFormValidation(FormValidation):
    """
        Override tastypie's standard ``FormValidation`` since this does not care
        about URI to PK conversion for ``ToOneField`` or ``ToManyField``.
        """
    
    def uri_to_pk(self, uri):
        """
        Returns the integer PK part of a URI.

        Assumes ``/api/v1/resource/123/`` format. If conversion fails, this just
        returns the URI unmodified.

        Also handles lists of URIs
        """

        if uri is None:
            return None

        # convert everything to lists
        multiple = not isinstance(uri, basestring)
        uris = uri if multiple else [uri]
        # handle all passed URIs
        converted = []
        for one_uri in uris:
            try:
                # hopefully /api/v1/<resource_name>/<pk>/
                converted.append(int(one_uri.split('/')[-2]))
            except (IndexError, ValueError):
                raise ValueError(
                    "URI %s could not be converted to PK integer." % one_uri)

        # convert back to original format
        return converted if multiple else converted[0]

    def is_valid(self, bundle, request=None):
        data = bundle.data
        # Ensure we get a bound Form, regardless of the state of the bundle.
        if data is None:
            data = {}
        # copy data, so we don't modify the bundle
        data = data.copy()
        # convert URIs to PK integers for all relation fields
        relation_fields = [name for name, field in
                           self.form_class.base_fields.items()
                           if issubclass(field.__class__, ModelChoiceField)]
        
        for field in relation_fields:
            if field in data:
                data[field] = self.uri_to_pk(data[field])
        
        # validate and return messages on error
        if request.method == "PUT":
            #Handles edit case
            form = self.form_class(data, instance = bundle.obj.__class__.objects.get(pk=bundle.data['id']))
        else:
            form = self.form_class(data)
        if form.is_valid():
            return {}
        return form.errors

def many_to_many_to_subfield(bundle, field_name, sub_field_names):
    sub_fields = getattr(bundle.obj, field_name).values(*sub_field_names)
    return list(sub_fields)

def foreign_key_to_id(bundle, field_name,sub_field_names):
    field = getattr(bundle.obj, field_name)
    if(field == None):
        dict = {}
        for sub_field in sub_field_names:
            dict[sub_field] = None 
    else:
        dict = model_to_dict(field, fields=sub_field_names, exclude=[])
    return dict

def dict_to_foreign_uri(bundle, field_name, resource_name=None):
    field_dict = bundle.data.get(field_name)
    if field_dict.get('id'):
        bundle.data[field_name] = "/api/v1/%s/%s/"%(resource_name if resource_name else field_name, 
                                                    str(field_dict.get('id')))
    else:
        bundle.data[field_name] = None
    return bundle

def dict_to_foreign_uri_m2m(bundle, field_name, resource_name):
    m2m_list = bundle.data.get(field_name)
    resource_uri_list = []
    for item in m2m_list:
        try:
            resource_uri_list.append("/api/v1/%s/%s/"%(resource_name, str(item.get('id'))))
        except:
            return bundle
    bundle.data[field_name] = resource_uri_list
    return bundle


#===============================================================================
# class VillagePartnerAuthorization(Authorization):
#     def __init__(self, field):
#         self.village_field = field
#     
#     def read_list(self, object_list, bundle):
#         villages = CocoUser.objects.get(user_id= bundle.request.user.id).get_villages()
#         kwargs = {}
#         kwargs[self.village_field] = villages
#         kwargs['partner_id'] = get_user_partner_id(bundle.request.user.id)
#         return object_list.filter(**kwargs).distinct()
# 
#     def read_detail(self, object_list, bundle):
#         # Is the requested object owned by the user?
#         kwargs = {}
#         kwargs[self.village_field] = CocoUser.objects.get(user_id= bundle.request.user.id).get_villages()
#         kwargs['partner_id'] = get_user_partner_id(bundle.request.user.id)
#         obj = object_list.filter(**kwargs).distinct()
#         if obj:
#             return True
#         else:
#             raise NotFound( "Not allowed to download" )
# 
# class VillageAuthorization(Authorization):
#     def __init__(self, field):
#         self.village_field = field
#     
#     def read_list(self, object_list, bundle):
#         villages = CocoUser.objects.get(user_id= bundle.request.user.id).get_villages()
#         kwargs = {}
#         kwargs[self.village_field] = villages
#         return object_list.filter(**kwargs).distinct()
# 
#     def read_detail(self, object_list, bundle):
#         # Is the requested object owned by the user?
#         kwargs = {}
#         kwargs[self.village_field] = CocoUser.objects.get(user_id= bundle.request.user.id).get_villages()
#         obj = object_list.filter(**kwargs).distinct()
#         if obj:
#             return True
#         else:
#             raise NotFound( "Not allowed to download Village" )
# 
# class MediatorAuthorization(Authorization):
#     def read_list(self, object_list, bundle):        
#         return object_list.filter(id__in= get_user_mediators(bundle.request.user.id))
#     
#     def read_detail(self, object_list, bundle):
#         if bundle.obj.id in get_user_mediators(bundle.request.user.id):
#             return True
#         # Is the requested object owned by the user?
#         else:
#             raise NotFound( "Not allowed to download Mediator")
# 
# class VideoAuthorization(Authorization):
#     def read_list(self, object_list, bundle):        
#         return object_list.filter(id__in= get_user_videos(bundle.request.user.id))
#     
#     def read_detail(self, object_list, bundle):
#         #To add adoption for the video seen which is outside user access
#         if bundle.obj.id in get_user_videos(bundle.request.user.id):
#             return True
#         else:
#             raise NotFound( "Not allowed to download video")
#===============================================================================

class BaseResource(ModelResource):
    
    def full_hydrate(self, bundle):
        bundle = super(BaseResource, self).full_hydrate(bundle)
        bundle.obj.user_modified_id = bundle.request.user.id
        return bundle
    
    def obj_create(self, bundle, **kwargs):
        """
        A ORM-specific implementation of ``obj_create``.
        """
        bundle.obj = self._meta.object_class()

        for key, value in kwargs.items():
            setattr(bundle.obj, key, value)

        self.authorized_create_detail(self.get_object_list(bundle.request), bundle)
        bundle = self.full_hydrate(bundle)
        bundle.obj.user_created_id = bundle.request.user.id
        return self.save(bundle)


class CountryResource(BaseResource):
    class Meta:
        max_limit = None
        queryset = Country.objects.all()
        resource_name = 'country'
        authentication = SessionAuthentication()
        authorization = Authorization()
        always_return_data = True


class StateResource(BaseResource):
    country = fields.ForeignKey('coco.api.CountryResource', 'country')
    dehydrate_country = partial(foreign_key_to_id, field_name='country',sub_field_names=['id','country_name'])
    hydrate_country = partial(dict_to_foreign_uri, field_name ='country')
    class Meta:
        max_limit = None
        queryset = State.objects.all()
        resource_name = 'state'
        authentication = SessionAuthentication()
        authorization = Authorization()
        always_return_data = True


class DistrictResource(BaseResource):
    state = fields.ForeignKey('coco.api.StateResource', 'state')
    dehydrate_state = partial(foreign_key_to_id, field_name='state',sub_field_names=['id','state_name'])
    hydrate_state = partial(dict_to_foreign_uri, field_name ='state')
    class Meta:
        max_limit = None
        queryset = District.objects.all()
        resource_name = 'district'
        authentication = SessionAuthentication()
        authorization = Authorization()
        always_return_data = True


class BlockResource(BaseResource):
    district = fields.ForeignKey('coco.api.DistrictResource', 'district')
    dehydrate_district = partial(foreign_key_to_id, field_name='district', sub_field_names=['id','district_name'])
    hydrate_district = partial(dict_to_foreign_uri, field_name='district')

    class Meta:
        max_limit = None
        queryset = Block.objects.all()
        resource_name = 'block'
        authentication = SessionAuthentication()
        authorization = Authorization()
        always_return_data = True


class SublocationResource(BaseResource):
    block = fields.ForeignKey('coco.api.BlockResource', 'block')
    dehydrate_block = partial(foreign_key_to_id, field_name='block', sub_field_names=['id','block_name'])
    hydrate_block = partial(dict_to_foreign_uri, field_name='block')

    class Meta:
        max_limit = None
        queryset = Sublocation.objects.all()
        resource_name = 'sublocation'
        authentication = SessionAuthentication()
        authorization = Authorization()
        always_return_data = True


class VillageResource(BaseResource):
    sublocation = fields.ForeignKey('coco.api.SublocationResource', 'sublocation')
    dehydrate_sublocation = partial(foreign_key_to_id, field_name='sublocation', sub_field_names=['id','sublocation_name'])
    hydrate_sublocation = partial(dict_to_foreign_uri, field_name='sublocation')

    class Meta:
        max_limit = None
        queryset = Village.objects.all()
        resource_name = 'village'
        authentication = SessionAuthentication()
        authorization = Authorization()
        always_return_data = True


class PersonResource(BaseResource):
    village = fields.ForeignKey('coco.api.VillageResource', 'village')
    dehydrate_village = partial(foreign_key_to_id, field_name='village', sub_field_names=['id','village_name'])
    hydrate_village = partial(dict_to_foreign_uri, field_name='village')

    class Meta:
        max_limit = None
        queryset = Person.objects.all()
        resource_name = 'person'
        authentication = SessionAuthentication()
        authorization = Authorization()
        always_return_data = True


class ClusterResource(BaseResource):
    village = fields.ForeignKey('coco.api.VillageResource', 'village')
    dehydrate_village = partial(foreign_key_to_id, field_name='village', sub_field_names=['id','village_name'])
    hydrate_village = partial(dict_to_foreign_uri, field_name='village')

    class Meta:
        max_limit = None
        queryset = Cluster.objects.all()
        resource_name = 'cluster'
        authentication = SessionAuthentication()
        authorization = Authorization()
        always_return_data = True


class SHGBaseLineResource(BaseResource):
    cluster = fields.ForeignKey('coco.api.ClusterResource', 'cluster')
    dehydrate_cluster = partial(foreign_key_to_id, field_name='cluster', sub_field_names=['id','cluster_name'])
    hydrate_cluster = partial(dict_to_foreign_uri, field_name='cluster')

    class Meta:
        max_limit = None
        queryset = SHGBaseLine.objects.all()
        resource_name = 'shgbaseline'
        authentication = SessionAuthentication()
        authorization = Authorization()
        always_return_data = True


class SHGProgramResource(BaseResource):
    person = fields.ForeignKey('coco.api.PersonResource', 'person')
    dehydrate_person = partial(foreign_key_to_id, field_name='person', sub_field_names=['id','person_name'])
    hydrate_person = partial(dict_to_foreign_uri, field_name='person')

    class Meta:
        max_limit = None
        queryset = SHGProgram.objects.all()
        resource_name = 'shgprogram'
        authentication = SessionAuthentication()
        authorization = Authorization()
        always_return_data = True


class LoanTypeResource(BaseResource):
    class Meta:
        max_limit = None
        queryset = LoanType.objects.all()
        resource_name = 'loantype'
        authentication = SessionAuthentication()
        authorization = Authorization()
        always_return_data = True


class LoanSubTypeResource(BaseResource):
    type = fields.ForeignKey(LoanTypeResource, 'type')
    dehydrate_type = partial(foreign_key_to_id, field_name='type', sub_field_names=['id','type_name'])
    hydrate_type = partial(dict_to_foreign_uri, field_name='type', resource_name='loantype')

    class Meta:
        max_limit = None
        queryset = LoanSubType.objects.all()
        resource_name = 'loansubtype'
        authentication = SessionAuthentication()
        authorization = Authorization()
        always_return_data = True


class LoanResource(BaseResource):
    type = fields.ForeignKey('coco.api.LoanTypeResource', 'type')
    subtype = fields.ForeignKey('coco.api.LoanSubTypeResource', 'subtype')
    dehydrate_type = partial(foreign_key_to_id, field_name='type', sub_field_names=['id','type_name'])
    hydrate_type = partial(dict_to_foreign_uri, field_name='type', resource_name='loantype')
    dehydrate_subtype = partial(foreign_key_to_id, field_name='subtype', sub_field_names=['id','subtype_name'])
    hydrate_subtype = partial(dict_to_foreign_uri, field_name='subtype', resource_name='loansubtype')

    class Meta:
        max_limit = None
        queryset = Loan.objects.all()
        resource_name = 'loan'
        authentication = SessionAuthentication()
        authorization = Authorization()
        always_return_data = True


class ExpectedReceiptResource(BaseResource):
    class Meta:
        max_limit = None
        queryset = ExpectedReceipt.objects.all()
        resource_name = 'expectedreceipt'
        authentication = SessionAuthentication()
        authorization = Authorization()
        always_return_data = True


class ActualReceiptResource(BaseResource):
    class Meta:
        max_limit = None
        queryset = ActualReceipt.objects.all()
        resource_name = 'actualreceipt'
        authentication = SessionAuthentication()
        authorization = Authorization()
        always_return_data = True
