
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['snacks'] = [
            {
                "image_url": "https://cdn.tasteatlas.com//images/dishes/6c6bf2d585b74d319a57c0cdfba98b10.jpg?w=905&h=510",
                "title": "tiropitakia",
                "description": "My favorite Greek snacks.",
                "reference_url": "https://www.tasteatlas.com/most-popular-snacks-in-greece"
            }, {
                "image_url": "https://www.sofiaskaleidoscope.com/media/Ion-Amygdalou.jpg.webp",
                "title": "Ion Chocolate",
                "description": "More Greek snacks in this case chocolate",
                "reference_url": "https://www.sofiaskaleidoscope.com/journal/top-10-popular-greek-snacks/"
            }, {
                "image_url": "https://www.sofiaskaleidoscope.com/media/Caprice.jpg.webp",
                "title": "Caprice",
                "description": "This Greek snack is made out of chocolate and it looks like a cigare.",
                "reference_url": "https://www.sofiaskaleidoscope.com/journal/top-10-popular-greek-snacks/"
            },
        ]

        return context


class AboutView(TemplateView):
    template_name = 'about.html'
