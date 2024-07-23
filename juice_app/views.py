from django.views.generic import TemplateView

class IndexView(TemplateView):
    """
    View to display home page.
    """
    template_name = "juice_app/index.html"
