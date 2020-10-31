from noting import views
from django.urls import path

app_name="noting"
urlpatterns=[
    path('',views.note_list.as_view(),name='note_list'),
    path('write/',views.CreateNote.as_view(),name='make_note'),
    path('ndetail/<slug:slug>',views.note_detail,name="note_detail"),
    path('edit/<slug:slug>',views.edit_blog.as_view(),name="edit_blog")
]
