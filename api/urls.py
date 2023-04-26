from rest_framework import routers
from .views import AccountView, ChatGView, ChatOView, BuyView, ComentariyaView, ProductView

route = routers.DefaultRouter()
route.register('api/user', AccountView)
route.register('api/buy', BuyView)
route.register('api/chat/global', ChatGView)
route.register('api/chat/only', ChatOView)
route.register('api/cometariya', ComentariyaView)
route.register('api/product', ProductView)

urlpatterns=route.urls