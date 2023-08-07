from django.contrib.auth import get_user_model, login
from django.contrib.auth import views as auth_views
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as generic_views
from django.contrib.auth import mixins as auth_mixins

from PizzaProject import settings
from PizzaProject.user_authentication.forms import RegisterForm, ChangePasswordForm

UserModel = get_user_model()


class RegisterUser(generic_views.CreateView):
    template_name = 'user_authenticate/registration-form.html'
    model = UserModel
    form_class = RegisterForm
    success_url = reverse_lazy('home_page')

    def form_valid(self, form):
        response = super().form_valid(form)

        login(self.request, self.object)

        return response


class LoginUser(auth_views.LoginView):
    template_name = 'user_authenticate/login-form.html'
    success_url = reverse_lazy('home_page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['next'] = self.request.GET.get('next', '')

        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponse(self.get_success_url())
        return super().dispatch(request, *args, **kwargs)


class LogoutUser(auth_mixins.LoginRequiredMixin, auth_views.LogoutView):
    pass


class DeleteRequest(auth_mixins.LoginRequiredMixin, generic_views.TemplateView):
    template_name = 'form_templates/delete-profile.html'


class DeleteProfileConfirm(auth_mixins.LoginRequiredMixin, generic_views.DeleteView):
    template_name = 'form_templates/delete-profile-confirm.html'
    model = UserModel
    success_url = reverse_lazy('home_page')


class ChangePassword(auth_mixins.LoginRequiredMixin, auth_views.PasswordChangeView):
    template_name = 'form_templates/change-password.html'
    success_url = reverse_lazy('home_page')
    form_class = ChangePasswordForm


class PasswordReset(auth_views.PasswordResetView):
    template_name = 'user_authenticate/password_reset_start.html'
    html_email_template_name = 'emails/reset_password_email.html'
    success_url = reverse_lazy('password_reset_done')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['website_email'] = settings.EMAIL_HOST_USER
        context['expiration_time'] = settings.PASSWORD_RESET_TIMEOUT

        return context

    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home_page')

        return super().dispatch(*args, **kwargs)


class PasswordResetDone(auth_views.PasswordResetDoneView):
    template_name = 'user_authenticate/reset_email_sent.html'

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home_page')

        return super().dispatch(request, *args, **kwargs)


class PasswordResetConfirm(auth_views.PasswordResetConfirmView):
    template_name = 'user_authenticate/password-reset-confirm.html'
    success_url = reverse_lazy('password_reset_complete')

    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home_page')

        return super().dispatch(*args, **kwargs)


class PasswordResetComplete(auth_views.PasswordResetCompleteView):
    template_name = 'user_authenticate/password_reset_complete.html'

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home_page')

        return super().dispatch(request, *args, **kwargs)
