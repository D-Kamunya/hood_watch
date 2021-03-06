from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect

def user_has_hood(function):
    def wrap(request, *args, **kwargs):
       
        if not request.user.profile.neighbourhood:
            return redirect('home_page')
        else:
            return function(request, *args, **kwargs)
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap