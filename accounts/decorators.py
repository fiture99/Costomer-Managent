from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapped_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return view_func(request, *args, **kwargs)
    return wrapped_func

def allowed_users(allowed_reles=[]):
    def decorator(view_func):
        def wrapped_func(request, *args, **kwargs):
            
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group  in allowed_reles:
                return view_func(request, *args, **kwargs )
            else:
                return HttpResponse("You are not Authorized to ")
            
        return wrapped_func
    return decorator


def admin_only(view_func):
    def wrapped_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        
        if group == 'customer':
            return redirect('user-page')
        
        if group == 'admin':
            return view_func(request, *args, **kwargs )
    return wrapped_function