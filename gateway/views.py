import logging
from django.urls import reverse
from django.shortcuts import  redirect

from azbankgateways import bankfactories, models as bank_models, default_settings as settings
from azbankgateways.exceptions import AZBankGatewaysException
from django.http import HttpResponse, Http404
from django.contrib import messages



def go_to_gateway_view(request):
    # خواندن مبلغ از هر جایی که مد نظر است
    amount= 5000000
    # تنظیم شماره موبایل کاربر از هر جایی که مد نظر است
    # user_mobile_number = '+989112221234'  # اختیاری
    user_mobile_number = request.user.profile.phone_number if request.user.is_authenticated else None
    # print(user_mobile_number)

    factory = bankfactories.BankFactory()
    try:
        bank = factory.auto_create() # or factory.create(bank_models.BankType.BMI) or set identifier
        bank.set_request(request)
        bank.set_amount(amount)
        # یو آر ال بازگشت به نرم افزار برای ادامه فرآیند
        bank.set_client_callback_url(reverse('gateway:callback'))
        bank.set_mobile_number(user_mobile_number)  # اختیاری
    
        # در صورت تمایل اتصال این رکورد به رکورد فاکتور یا هر چیزی که بعدا بتوانید ارتباط بین محصول یا خدمات را با این
        # پرداخت برقرار کنید. 
        bank_record = bank.ready()
        
        # هدایت کاربر به درگاه بانک
        return bank.redirect_gateway()
    except AZBankGatewaysException as e:
        logging.critical(e)
        # TODO: redirect to failed page.
        messages.error(request, "اتصال به درگاه پرداخت ناموفق بود ، لطفااتصال خود را به اینترنت برسی نمایید و  دوباره امتحان کنید")
        return redirect('userpanel:index')
        



def callback_gateway_view(request):
    tracking_code = request.GET.get(settings.TRACKING_CODE_QUERY_PARAM, None)
    if not tracking_code:
        logging.debug("این لینک معتبر نیست.")
        raise Http404

    try:
        bank_record = bank_models.Bank.objects.get(tracking_code=tracking_code)
    except bank_models.Bank.DoesNotExist:
        logging.debug("این لینک معتبر نیست.")
        raise Http404

    # در این قسمت باید از طریق داده هایی که در بانک رکورد وجود دارد، رکورد متناظر یا هر اقدام مقتضی دیگر را انجام دهیم
    if bank_record.is_success:
        # پرداخت با موفقیت انجام پذیرفته است و بانک تایید کرده است.
        # می توانید کاربر را به صفحه نتیجه هدایت کنید یا نتیجه را نمایش دهید.
        # messages.success(request, 'پرداخت با موفقیت انجام شد.')
        return redirect('orders:create')
    messages.success(request, 'پرداخت با شکست مواجه شده است. اگر پول از حساب کم شده است ظرف مدت ۴۸ ساعت پول به حساب شما بازخواهد گشت.')
    return redirect('website:home') 