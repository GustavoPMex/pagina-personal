from .models import link

def ctx_dict(request):
    ctx = {}
    links = link.objects.all()
    for urlink in links:
        ctx[urlink.key] = urlink.url

    return ctx