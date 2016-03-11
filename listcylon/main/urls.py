from django.conf.urls import url
from django.views.static import serve

from main import views
from listcylon.settings import MEDIA_ROOT


urlpatterns = [
    url(r'^home/$', views.Home.as_view(), name='home'),
    url(r'^media/(?P<path>.*)/$', serve, {'document_root': MEDIA_ROOT}),
    url(r'^job/(?P<pk>\d+)/$', views.JobDetail.as_view(), name='job_detail'),
    url(r'^jobs/newest/$', views.NewestAccounting.as_view(), name='newest_accounting'),
    url(r'^jobs/highest/$', views.HighestAccounting.as_view(), name='highest_accounting'),
    url(r'^jobs/lowest/$', views.LowestAccounting.as_view(), name='lowest_accounting'),
    url(r'^accounting/jobs/post/$', views.AccountingPosting.as_view(), name='create_accounting_job'),
    url(r'^accounting/thumbnail/$', views.AccountingThumbnail.as_view(), name='accounting_thumbnail'),
    url(r'^buisness/jobs/post/$', views.BuisnessPosting.as_view(), name='create_buisness_job'),
    url(r'^education/jobs/post/$', views.EducationPosting.as_view(), name='create_education_job'),
    url(r'^real_estate/jobs/post/$', views.RealEstatePosting.as_view(), name='create_real_estate_job'),
    url(r'^government/jobs/post/$', views.GovernmentPosting.as_view(), name='create_government_job'),
    url(r'^technology/jobs/post/$', views.TechnologyPosting.as_view(), name='create_technology_job'),
    url(r'^accounting/jobs/$', views.AccountingJobs.as_view(), name='accounting'),
    url(r'^buisness/jobs/$', views.BuisnessJobs.as_view(), name='buisness'),
    url(r'^education/jobs/$', views.EducationJobs.as_view(), name='education'),
    url(r'^real_estate/jobs/$', views.RealEstateJobs.as_view(), name='real_estate'),
    url(r'^government/jobs/$', views.GovernmentJobs.as_view(), name='government'),
    url(r'^technology/jobs/$', views.TechnologyJobs.as_view(), name='technology'),
    url(r'^jobs/$', views.AllJobsCity.as_view(), name='all_jobs_city'),
    url(r'^cars/acura/$', views.Acura.as_view(), name='acura'),
    url(r'^cars/audi/$', views.Audi.as_view(), name='audi'),
    url(r'^cars/BMW/$', views.BMW.as_view(), name='BMW'),
    url(r'^cars/buick/$', views.Buick.as_view(), name='buick'),
    url(r'^cars/acura/post/$', views.AcuraPosting.as_view(), name='create_acura_post'),
    url(r'^cars/audi/post/$', views.AudiPosting.as_view(), name='create_audi_post'),
    url(r'^cars/bmw/post/$', views.BMWPosting.as_view(), name='create_bmw_post'),
    url(r'^cars/buick/post/$', views.BuickPosting.as_view(), name='create_buick_post'),
    url(r'^cars/(?P<pk>\d+)/$', views.CarDetail.as_view(), name='car_detail'),
    url(r'^cars/$', views.AllCarsCity.as_view(), name='all_cars_city'),
]
