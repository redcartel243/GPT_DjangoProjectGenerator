import os

def create_django_project(project_name):
    os.system(f"django-admin startproject {project_name}")

def create_django_app(project_name, app_name):
    os.chdir(project_name)
    os.system(f"python manage.py startapp {app_name}")
    os.chdir("..")


def create_multiple_pages_django_website(project_name, app_name, pages):
    create_django_project(project_name)
    create_django_app(project_name, app_name)

    # Modify settings.py to include the app
    with open(f"{project_name}/{project_name}/settings.py", "r") as f:
        settings = f.read()

    settings = settings.replace("INSTALLED_APPS = [", f"INSTALLED_APPS = [\n    '{app_name}',")
    with open(f"{project_name}/{project_name}/settings.py", "w") as f:
        f.write(settings)

    # Create a template folder
    os.makedirs(f"{project_name}/{app_name}/templates/{app_name}")

    # Generate HTML content for each page and create corresponding files
    for page_name, html_content in pages.items():
        with open(f"{project_name}/{app_name}/templates/{app_name}/{page_name}.html", "w") as f:
            f.write(html_content)

    # Modify views.py to render each page
    with open(f"{project_name}/{app_name}/views.py", "w") as f:
        f.write("from django.shortcuts import render\n\n")
        for page_name in pages.keys():
            f.write(f"def {page_name}_view(request):\n")
            f.write(f"    return render(request, '{app_name}/{page_name}.html')\n\n")

    # Modify urls.py in the app folder to include the views
    with open(f"{project_name}/{app_name}/urls.py", "w") as f:
        f.write("from django.urls import path\n\n")
        f.write("from . import views\n\n")
        f.write("urlpatterns = [\n")
        for page_name in pages.keys():
            f.write(f"    path('{page_name}/', views.{page_name}_view, name='{page_name}_view'),\n")
        f.write("]\n")

    # Modify urls.py in the project folder to include the app's URLs and the admin URL
    with open(f"{project_name}/{project_name}/urls.py", "r") as f:
        project_urls = f.read()

    project_urls = project_urls.replace("from django.urls import path", "from django.urls import path, include")
    project_urls = project_urls.replace("urlpatterns = [", f"""urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('{app_name}.urls')),
    """)
    with open(f"{project_name}/{project_name}/urls.py", "w") as f:
        f.write(project_urls)