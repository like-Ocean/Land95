from .models import HomePageContent

def site_contact(request):
    content = HomePageContent.objects.first()
    return {
        "site_phone": content.phone_number if content else "",
        "site_email": content.email if content else "",
    }
