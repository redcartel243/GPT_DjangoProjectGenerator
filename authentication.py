

def generate_auth_views(project_name, app_name):
    auth_views_code = '''
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib import messages

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created for {{username}}!")
            return redirect("login_view")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{{msg}}: {{form.error_messages[msg]}}")
    form = UserCreationForm()
    return render(request, "{app_name}/register.html", context={{"form": form}})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {{username}}.")
                return redirect("/")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request, "{app_name}/login.html", context={{"form": form}})

def logout_view(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("login_view")
'''
    auth_views_code = auth_views_code.format(app_name=app_name)
    with open(f"{project_name}/{app_name}/views.py", "a") as f:
        f.write(auth_views_code)
def generate_auth_templates(project_name, app_name):
    register_template = '''
{% extends "base.html" %}

{% block content %}
    <h2>Register</h2>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Register</button>
    </form>
{% endblock %}
'''
    login_template = '''
{% extends "base.html" %}

{% block content %}
    <h2>Login</h2>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Login</button>
    </form>
{% endblock %}
'''

    with open(f"{project_name}/{app_name}/templates/{app_name}/register.html", "w") as f:
        f.write(register_template)

    with open(f"{project_name}/{app_name}/templates/{app_name}/login.html", "w") as f:
        f.write(login_template)


def add_auth_urls(project_name, app_name):
    auth_url_patterns = '''
    path("register/", views.register_view, name="register_view"),
    path("login/", views.login_view, name="login_view"),
    path("logout/", views.logout_view, name="logout_view"),
'''

    with open(f"{project_name}/{app_name}/urls.py", "r") as f:
        contents = f.readlines()

    insert_index = 0
    for i, line in enumerate(contents):
        if "urlpatterns = [" in line:
            insert_index = i + 1
            break

    contents.insert(insert_index, auth_url_patterns)

    with open(f"{project_name}/{app_name}/urls.py", "w") as f:
        f.writelines(contents)