from django.shortcuts import render, redirect
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse
from code_green.forms import UserProfileForm
from code_green.models import UserProfile, Mission


class IndexView(View):
    def get(self, request):
        return render(request, 'code_green/index.html')


class RegisterProfileView(View):
    form = UserProfileForm()
    context_dict = {}

    def get(self, request):
        self.context_dict['form'] = self.form
        return render(request, 'code_green/profile_registration.html', context=self.context_dict)

    def post(self, request):
        self.form = UserProfileForm(request.POST, request.FILES)

        if self.form.is_valid():
            profile = self.form.save(commit=False)
            profile.user = request.user
            profile.save()
        else:
            print(self.form.errors)

        return redirect(reverse('code_green:index'))


class ProfileView(View):
    def get_user_details(self, username):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return None

        user_profile = UserProfile.objects.get_or_create(user=user)[0]
        form = UserProfileForm({'website': user_profile.website,
                                'picture': user_profile.picture})

        return user, user_profile, form

    @method_decorator(login_required)
    def get(self, request, username):
        try:
            (user, user_profile, form) = self.get_user_details(username)
        except TypeError:
            return redirect(reverse('code_green:index'))

        context_dict = {'user_profile': user_profile,
                        'selected_user': user,
                        'form': form}

        return render(request, 'code_green/profile.html', context_dict)

    @method_decorator(login_required)
    def post(self, request, username):
        try:
            (user, user_profile, form) = self.get_user_details(username)
        except TypeError:
            return redirect(reverse('code_green:index'))

        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)

        if form.is_valid():
            form.save(commit=True)
            return redirect('code_green:profile', user.username)
        else:
            print(form.errors)

        context_dict = {'user_profile': user_profile,
                        'selected_user': user,
                        'form': form}

        return render(request, 'code_green/profile.html', context_dict)


class MissionsView(View):
    @method_decorator(login_required)
    def get(self, request):
        missions = Mission.objects.all()
        return render(request, 'code_green/missions.html', {'missions_list': missions})
