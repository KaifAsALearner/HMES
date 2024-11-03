# app/decorators.py
from django.shortcuts import render,redirect
from functools import wraps

def role_required(allowed_roles):
    """
    Decorator to restrict access based on user roles.
    
    :param allowed_roles: A list or tuple of roles that are allowed to access the view.
    """
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated:
                user_role = request.user.userinfo.role_def  # Adjust this line based on your user model
                if user_role in allowed_roles:
                    return view_func(request, *args, **kwargs)
            return render(request,'error_403.html')
        return _wrapped_view
    return decorator


def redirect_authenticated_user(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            # Redirect authenticated users to the homepage
            return redirect('home')  # Replace 'home' with your homepage route name
        return view_func(request, *args, **kwargs)
    return _wrapped_view
