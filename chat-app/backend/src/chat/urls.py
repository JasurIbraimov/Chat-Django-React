from django.contrib import admin
from django.urls import path, include
from chatapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
    # Chat message 
    path("inbox/<user_id>/", views.MyInbox.as_view(), name="inbox"),
    path("chat/<sender_id>/<receiver_id>/", views.GetMessages.as_view(), name="chat"),
    path("chat/send_message/", views.SendMessage.as_view(), name="send")
]
