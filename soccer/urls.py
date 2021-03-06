from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# per Django customizing auth model sample code:
#admin.site.register(MyUser, MyUserAdmin)
#admin.site.unregister(Group)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'soccer.views.home', name='home'),
    # url(r'^soccer/', include('soccer.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('email_auth.backends.urls')),
    url(r'^profiles/', include('user_profile.urls'))
    #(r'^accounts/', include('email_auth.urls')),
      #based on registration.backends.default.urls
)
