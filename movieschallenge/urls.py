"""conduit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^api/', include('conduit.apps.articles.urls', namespace='articles')),
    # url(r'^api/', include('conduit.apps.authentication.urls', namespace='authentication')),
    # url(r'^api/', include('conduit.apps.profiles.urls', namespace='profiles')),
]



# from django.contrib import admin
# from django.urls import path, include
# from django.conf.urls import url

# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi
# from rest_framework import permissions
# from rest_framework.documentation import include_docs_urls

# from authentication.backends import JWTAuthentication

# schema_view = get_schema_view(
#     openapi.Info(
#         title="Reviews API",
#         default_version='v1',
#         description="Test description",
#         terms_of_service="https://www.google.com/policies/terms/",
#         contact=openapi.Contact(email="contact@snippets.local"),
#         license=openapi.License(name="BSD License"),
#     ),
#     validators=['flex', 'ssv'],
#     public=True,
#     permission_classes=(permissions.AllowAny,),
# )


# urlpatterns = [

#     path('admin/', admin.site.urls),
#    	path(r'api/v1/', include(('authentication.urls',
#                               'authentication'), namespace='auth')),
#    	path(r'api/v1/', include(('reviews.urls', 'reviews'), namespace='reviews')),
#    	path(r'api/v1/', include(('companies.urls', 'companies'), namespace='companies')),
#     url(r'^swagger(?P<format>\.json|\.yaml)$',
#         schema_view.without_ui(cache_timeout=0), name='schema-json'),
#     url(r'^swagger/$', schema_view.with_ui('swagger',
#                                            cache_timeout=0), name='schema-swagger-ui'),
#     url(r'^redoc/$', schema_view.with_ui('redoc',
#                                          cache_timeout=0), name='schema-redoc'),
#    	path(r'docs/', include_docs_urls(title='Reviews API',
#                                      authentication_classes=[JWTAuthentication, ], permission_classes=[])),

# ]
