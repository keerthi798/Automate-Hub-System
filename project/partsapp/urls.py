from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView
from.import views
from django.contrib.auth import views as auth_views
from .views import logout_view
from .views import booking, select_time_slot
from .views import Vehicle_Add
from .views import download_brochure
from .views import vehicleorder 
from .views import generate_pdf
from .views import servicebranchdashboard, deliveryboydashboard, partsmanagerdashboard, insurancecompanydashboard
from .views import add_insurance, insurance_list

urlpatterns = [
   path('',views.index,name="index"),
   path('signup/',views.signup, name="signup"),
   path('login/', views.login, name="login"),
   path('dashboard/',views.dashboard,name="dashboard"),
#    path('logout/', views.logout_confirm,name='logout'),
   path('logout/', logout_view, name='logout'),
    path('change_password/', views.change_password, name='change_password'),
   path('partsorder.html', views.partsorder, name='partsorder'),
   
   path('customer_dash/', views.customer_dash, name='customer_dash'),
   path('parts_list/', views.parts_list, name='parts_list'),

   path('admindashboard/userprofile/', views.admindashboard, name='admindashboard'),
   
   path('servicebranchdashboard/', views.servicebranchdashboard, name='servicebranchdashboard'),
   path('deliveryboydashboard/', views.deliveryboydashboard, name='deliveryboydashboard'),
   path('partsmanagerdashboard/', views.partsmanagerdashboard, name='partsmanagerdashboard'),
   
   path('insurancecompanydashboard/', views.insurancecompanydashboard, name='insurancecompanydashboard'),
   



   path('userdetails/', views.userdetails, name='userdetails'),
   path('service_branch/', views.service_branch, name='service_branch'),
   path('userprofile/', views.userprofile, name='userprofile'),
   
   path('delete_part/<int:part_id>/', views.delete_part, name='delete_part'),
   path('delete_branch/<int:user_id>/', views.delete_branch, name='delete_branch'),
    path('update_part/<int:part_id>/', views.update_part, name='update_part'),
    path('parts_add/', views.parts_add, name='parts_add'),

    path('Vehicle_Add/', views.Vehicle_Add, name='Vehicle_Add'),


    path('add_worker/', views.add_worker, name='add_worker'),

   

    path('parts_managers/', views.parts_managers, name='parts_managers'),

   
    # path('add_to_wishlist/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),

    
    # path('view_wishlist/', views.view_wishlist, name='view_wishlist'),
   
    path('all_products/', views.all_products, name='all_products'),

    
    path('booking/', views.booking, name='booking'),
    path('booking/confirm/<int:booking_id>/', views.confirm_booking, name='confirm_booking'),
    path('booking/reject/<int:booking_id>/', views.reject_booking, name='reject_booking'),


    #  path('buy_now/<int:product_id>/', views.buy_now_view, name='buy_now'),

    path('edit_profile/', views.edit_profile, name='edit_profile'),
   
    path('download-parts-list/', views.download_parts_list, name='download_parts_list'),
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),

    # path('filter_by_price/', views.filter_by_price, name='filter_by_price'),
   

    path('vehicleorder/<str:model>/', views.vehicleorder, name='vehicle_order_model'),

    path('partsorder/<str:category>/', views.partsorder, name='parts_order_category'),
    
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    
    path('increase-cart-item/<int:product_id>/',views.increase_cart_item, name='increase-cart-item'),
    path('decrease-cart-item/<int:product_id>/',views.decrease_cart_item, name='decrease-cart-item'),
    path('fetch-cart-count/', views.fetch_cart_count, name='fetch-cart-count'),
    path('view_cart/', views.view_cart, name='view_cart'),
    
    path('create-order/', views.create_order, name='create-order'),
    path('handle-payment/', views.handle_payment, name='handle-payment'),
    path('checkout/', views.checkout, name='checkout'),  

    path('api/order/<int:order_id>/', views.order_details_api, name='order_details_api'),

    path('billinvoice/',views.bill_invoice, name='bill_invoice'),
    path('view_more/<int:part_id>/',views.view_more, name='view_more'),
    path('Timeslot/', views.select_time_slot, name='select_time_slot'),
    
     path('Vehicle_list/', views.vehicle_list, name='vehicle_list'),
     path('delete-vehicle/<int:vehicle_id>/', views.delete_vehicle, name='delete_vehicle'),

     path('vehicle-details/<int:vehicle_id>/', views.vehicle_details, name='vehicle_details'),

     path('download-brochure/<int:vehicle_id>/', views.download_brochure, name='download_brochure'),

    path('book_now/<int:vehicle_id>/', views.book_now, name='book_now'),
  
    path('payment_success/', views.payment_success, name='payment_success'),
    
    path('insurance_renewal/', views.insurance_renewal, name='insurance_renewal'),
    path('insurance_new/', views.insurance_new, name='insurance_new'),

    path('insurance_process/', views.insurance_process, name='insurance_process'),
    path('insurance_package/', views.insurance_package, name='insurance_package'),


    path('booking_history/', views.booking_history, name='booking_history'),
    
    path('generate_pdf/', generate_pdf, name='generate_pdf'),
    
    path('add_insurance_content/', views.add_insurance, name='insurance_add'),

    path('insurance-list/', views.insurance_list, name='insurance_list'),
    
    path('delete-insurance/<int:entry_id>/', views.delete_insurance, name='delete_insurance'),

    path('update_insurance/<int:entry_id>/', views.update_insurance, name='update_insurance'),

    path('previous_insurance_list/', views.previous_insurance_list, name='previous_insurance_list'),

    path('checkout_process/', views.checkout_process, name='checkout_process'),

    path('insurance_success_payment/', views.insurance_success_payment, name='insurance_success_payment'),
   
    path('wishlist/', views.wishlist, name='wishlist'),
    path('wishlist/toggle/<int:vehicle_id>/', views.toggle_wishlist, name='toggle_wishlist'),
    path('wishlist/remove/', views.remove_from_wishlist, name='remove_from_wishlist'),

    path('booking_uservehicle/', views.booking_uservehicle, name='booking_uservehicle'),

    path('confirm_booking/<int:booking_id>/', views.confirm_booking_vehicle, name='confirm_booking_vehicle'),

    path('mark_as_delivered/<int:booking_id>/', views.mark_as_delivered_vehicle, name='mark_as_delivered_vehicle'),
    
     path('confirmed_vehicle_details/', views.confirmed_vehicle_details, name='confirmed_vehicle_details'),

     path('generate_registration_numbers/', views.generate_registration_numbers, name='generate_registration_numbers'),

     path('package_details/', views.package_details, name='package_details'),

     path('insurance_success/', views.insurance_success, name='insurance_success'),

     path('payment_records_list/', views.payment_records_list, name='payment_records_list'),

     path('confirm_payment/', views.confirm_payment, name='confirm_payment'),
     
     path('generate_pdf_email_template/', views.render_generate_pdf_email_template, name='generate_pdf_email_template'),
    path('generate_pdf_and_send_email/', views.generate_pdf_and_send_email, name='generate_pdf_and_send_email'),

    path('policies/', views.policy_list, name='policy_list'),

   
     
]
       
    
