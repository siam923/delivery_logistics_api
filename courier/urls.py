from django.contrib import admin
from django.urls import path, include
import debug_toolbar
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from rest_framework_swagger.views import get_swagger_view

API_TITLE = 'Courier API'  # new
API_DESCRIPTION = 'A Web API for managing courier app.'
schema_view = get_swagger_view(title=API_TITLE)

admin.site.site_header = 'Courier Admin'
admin.site.index_title = 'Admin'


urlpatterns = [
    path('admin/', admin.site.urls),
    # auth
    path('accounts/', include('allauth.urls')),
    # Api Auth for login in the browsable api view
    path('api-auth/', include('rest_framework.urls')),
    # API for user auth from front end
    path('api/v1/dj-rest-auth/', include('dj_rest_auth.urls')),
    path('api/v1/dj-rest-auth/registration/',
         include('dj_rest_auth.registration.urls')),
    # App url
    path('api/v1/', include('parcels.urls')),
    path('api/v1/location/', include('area.urls')),
    path('api/v1/profile/', include('profiles.urls')),
    # Extra
    path('__debug__/', include(debug_toolbar.urls)),
    path('docs/', include_docs_urls(title=API_TITLE,
                                    description=API_DESCRIPTION)),
    path('swagger-docs/', schema_view),

]
