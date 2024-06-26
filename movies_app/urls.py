from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('Eadmin/',views.Eadmin,name='Eadmin'),
    path('Euser/',views.Euser,name='Euser'),
    path('loginpage/',views.loginpage,name='loginpage'),
    path('signuppage/',views.signuppage,name='signuppage'),
    path('uprofile/',views.uprofile,name='uprofile'),
    path('add_movie',views.add_movie,name='add_movie'),
    path('edit_movie/<int:od>',views.edit_movie,name='edit_movie'),
    path('add_category',views.add_category,name='add_category'),
    path('edit_category/<int:od>',views.edit_category,name='edit_category'),
    path('showmovie',views.showmovie,name='showmovie'),
    path('show_category',views.show_category,name='show_category'),
    path('show_user',views.show_user,name='show_user'),

    path('cart/',views.cart,name='cart'),
    path('Login/',views.Login,name='Login'),
    path('Signup/',views.Signup,name='Signup'),
    path('Logout/',views.Logout,name='Logout'),
    path('eprofile/',views.eprofile,name='eprofile'),
    path('a_movie',views.a_movie,name='a_movie'),
    path('e_movie/<int:od>',views.e_movie,name='e_movie'),
     path('delete_movie/<int:od>',views.delete_movie,name='delete_movie'),
    path('a_category',views.a_category,name='a_category'),
    path('e_category/<int:od>',views.e_category,name='e_category'),
    path('deletecust/<int:od>',views.deletecust,name='deletecust'),
    path('add_cart/<int:od>',views.add_cart,name='add_cart'),
    path('deletecart_item<int:od>',views.deletecart_item,name='deletecart_item'),
    path('search/',views.search,name='search'),
    path(' delete_movie/',views. delete_movie,name=' delete_movie'),
    
    path('feed/',views.feed,name='feed'),
    path('show_feed/',views.show_feed,name='show_feed'),
    path('tfeed/',views.tfeed,name='tfeed'),
    path('delete_feed/<int:od>',views.delete_feed,name='delete_feed'),
    # path('efeed/',views.efeed,name='efeed'),
    path('show_efeed/',views.show_efeed,name='show_efeed'),
    # path('etfeed/',views.etfeed,name='etfeed'),
    #path('delete_efeed/<int:od>',views.delete_efeed,name='delete_efeed'),

]