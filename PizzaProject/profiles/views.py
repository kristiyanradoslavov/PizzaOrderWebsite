from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic as generic_views
from django.contrib.auth import mixins as auth_mixins, get_user_model

from PizzaProject.profiles.forms import ProfileForm
from PizzaProject.profiles.models import Profile

UserModel = get_user_model()


class ProfileDetails(generic_views.UpdateView):
    template_name = 'form_templates/profile-details.html'
    form_class = ProfileForm
    model = Profile
    success_url = reverse_lazy('home_page')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['initial'] = {
            'email': self.request.user.email
        }

        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        image_url = self.request.user.profile.image
        context['image_url'] = image_url
        # context['form'] = ProfileForm

        return context


class Orders(auth_mixins.LoginRequiredMixin, generic_views.TemplateView):
    template_name = 'form_templates/order-history.html'

