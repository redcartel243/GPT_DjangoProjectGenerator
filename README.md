# **Django Project Generator**

This project is a command-line tool for generating and updating Django projects. It uses GPT-3.5 to create HTML templates based on user descriptions, automates project creation, and supports custom templates, CSS, and JavaScript files. Additionally, it handles user authentication.

**Features**

- Create multiple-page Django websites
- Optional predefined or custom templates, CSS, and JavaScript files
- Generate Django models and forms based on user input
- Authentication features (registration, login, and logout)
- GPT-3.5 generated HTML content for each page
- Update existing HTML templates using GPT-3.5

**Prerequisites**

- Python 3.8 or later
- Django 3.2 or later
- OpenAI Python Library

**Setup**

1. Install the required packages using pip:

pip install -r requirements.txt

1. Set your OpenAI API key as an environment variable or update the openai.api\_key value in gpt.py.
2. Run the Django project generator:

python main.py create \<project\_name\> \<app\_name\> \<num\_pages\> --template \<template\_name\> --custom\_template\_path \<custom\_template\_path\> --custom\_css\_path \<custom\_css\_path\> --custom\_js\_path \<custom\_js\_path\> --models \<model\_descriptions\>

- \<project\_name\>: Name of the Django project
- \<app\_name\>: Name of the Django app
- \<num\_pages\>: Number of pages to create
- \<template\_name\>: (Optional) Predefined template to use (template1 or template2)
- \<custom\_template\_path\>: (Optional) Path to the custom HTML template
- \<custom\_css\_path\>: (Optional) Path to the custom CSS file
- \<custom\_js\_path\>: (Optional) Path to the custom JavaScript file
- \<model\_descriptions\>: (Optional) List of model descriptions

1. Update an existing Django project:

python main.py update \<html\_template\_path\> \<description\>

- \<html\_template\_path\>: Path to the HTML template to update
- \<description\>: Description of the changes to make to the existing HTML template

**Project Structure**

The project is organized into the following modules:

1. main.py: Entry point of the application
2. gpt.py: GPT-3.5 functions for generating content and updating templates
3. project\_creation.py: Functions for creating and updating Django projects and apps
4. static\_files.py: Functions for handling static files (CSS and JavaScript)
5. authentication.py: Functions for generating user authentication views, templates, and URLs

Refer to the source code for detailed information on each module's functionality.

**Notes**

- This project uses GPT-3.5, which requires an API key from OpenAI. Make sure to set your OpenAI API key in the gpt.py file.
- The GPT-3.5 model has a token limit. If the generated content exceeds this limit, the output might be incomplete. Adjust the max\_response\_tokens and total\_tokens variables in gpt.py as needed.
