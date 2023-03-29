import argparse
from gpt import gpt_3_5_assistant, generate_django_model, generate_django_form, generate_form_html, update_html_template
from project_creation import create_django_project, create_django_app, create_multiple_pages_django_website
from static_files import create_static_folder, include_css_js_files, create_css_js_files
from authentication import generate_auth_views, generate_auth_templates, add_auth_urls

def main():
    parser = argparse.ArgumentParser(description="Django Project Generator")
    subparsers = parser.add_subparsers(dest="command", help="Choose a command to execute")

    create_parser = subparsers.add_parser("create", help="Create a new Django project")
    create_parser.add_argument("project_name", help="Name of the Django project")
    create_parser.add_argument("app_name", help="Name of the Django app")
    create_parser.add_argument("num_pages", type=int, help="Number of pages to create")
    create_parser.add_argument("--template", choices=["template1", "template2", "custom"], default=None, help="Choose a predefined template or provide your own custom template")
    create_parser.add_argument("--custom_template_path", default=None, help="Path to the custom HTML template")
    create_parser.add_argument("--custom_css_path", default=None, help="Path to the custom CSS file")
    create_parser.add_argument("--custom_js_path", default=None, help="Path to the custom JavaScript file")
    create_parser.add_argument("--models", nargs="*", default=[], help="List of model descriptions")

    update_parser = subparsers.add_parser("update", help="Update an existing Django project")
    update_parser.add_argument("html_template_path", help="Path to the HTML template to update")
    update_parser.add_argument("description", help="Describe the changes to make to the existing HTML template")

    args = parser.parse_args()

    if args.command == "create":
        project_name = args.project_name
        app_name = args.app_name
        num_pages = args.num_pages

        if args.template == "custom" and args.custom_template_path:
            with open(args.custom_template_path, "r") as f:
                base_template = f.read()
        elif args.template:
            with open(f"templates/{args.template}.html", "r") as f:
                base_template = f.read()
        else:
            base_template = None

        pages = {}
        for i in range(num_pages):
            page_name = input(f"Enter the name for page {i + 1}: ")
            page_description = input(f"Describe the content for page {i + 1}: ")
            page_content_prompt = f"Create an HTML template for a page in a Django website based on the following description: {page_description}"
            page_content = gpt_3_5_assistant(page_content_prompt, template=base_template)
            pages[page_name] = page_content

        create_multiple_pages_django_website(project_name, app_name, pages)
        create_static_folder(project_name, app_name)
        create_css_js_files(project_name, app_name, custom_css_path=args.custom_css_path, custom_js_path=args.custom_js_path)
        generate_auth_views(project_name, app_name)
        generate_auth_templates(project_name, app_name)
        add_auth_urls(project_name, app_name)

        for page_name, html_content in pages.items():
            html_content = include_css_js_files(html_content, app_name)
            with open(f"{project_name}/{app_name}/templates/{app_name}/{page_name}.html", "w") as f:
                f.write(html_content)

        # Generate Django models
        models_code = ""
        for model_description in args.models:
            model_code = generate_django_model(model_description)
            models_code += f"{model_code}\n"

        if models_code:
            models_code = f"from django.db import models\n\n{models_code}"
            with open(f"{project_name}/{app_name}/models.py", "w") as f:
                f.write(models_code)

            print(f"Created a multiple-page Django website in the '{project_name}' project and '{app_name}' app with the following content:\n")
            for page_name, page_content in pages.items():
                print(f"{page_name}.html:\n{page_content}\n")

        if models_code:
            print("Generated the following Django models:\n")
            print(models_code)

        # Generate forms
        num_forms = int(input("Enter the number of forms you want to create: "))
        forms_code = "from django import forms\n\n"
        for i in range(num_forms):
            form_description = input(f"Describe the form {i + 1}: ")
            form_code = generate_django_form(form_description)
            forms_code += f"{form_code}\n"

        if num_forms > 0:
            with open(f"{project_name}/{app_name}/forms.py", "w") as f:
                f.write(forms_code)
            print("Generated the following Django forms:\n")
            print(forms_code)

    elif args.command == "update":
        html_template_path = args.html_template_path
        description = args.description

        with open(html_template_path, "r") as f:
            html_template = f.read()

        updated_template = update_html_template(html_template, description)

        with open(html_template_path, "w") as f:
            f.write(updated_template)

        print("Updated the HTML template with the following content:\n")
        print(updated_template)

    else:
        parser.print_help()

if __name__ == "__main__":
    main()