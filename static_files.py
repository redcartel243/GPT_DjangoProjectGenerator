import os
def create_static_folder(project_name, app_name):
    os.makedirs(f"{project_name}/{app_name}/static/{app_name}/css")
    os.makedirs(f"{project_name}/{app_name}/static/{app_name}/js")

def include_css_js_files(html_content, app_name):
    head_end_pos = html_content.find("</head>")
    html_content = html_content[:head_end_pos] + f'<link rel="stylesheet" href="/static/{app_name}/css/style.css">\n' + html_content[head_end_pos:]
    body_end_pos = html_content.find("</body>")
    html_content = html_content[:body_end_pos] + f'<script src="/static/{app_name}/js/script.js"></script>\n' + html_content[body_end_pos:]
    return html_content

def create_css_js_files(project_name, app_name, custom_css_path=None, custom_js_path=None):
    if custom_css_path:
        with open(custom_css_path, "r") as custom_css_file:
            css_content = custom_css_file.read()
    else:
        css_content = f"/* Add your CSS styles for the {app_name} app here */\n"

    if custom_js_path:
        with open(custom_js_path, "r") as custom_js_file:
            js_content = custom_js_file.read()
    else:
        js_content = f"// Add your JavaScript code for the {app_name} app here\n"

    with open(f"{project_name}/{app_name}/static/{app_name}/css/style.css", "w") as css_file:
        css_file.write(css_content)
    with open(f"{project_name}/{app_name}/static/{app_name}/js/script.js", "w") as js_file:
        js_file.write(js_content)