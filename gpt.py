import openai

openai.api_key = "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"

def gpt_3_5_assistant(prompt, template=None, max_response_tokens=100, total_tokens=4096):
    response_text = ""
    tokens_used = len(prompt)
    remaining_tokens = total_tokens - tokens_used

    if template:
        prompt = f"Update the following HTML template based on this description: {prompt}\n\nHTML template:\n{template}\n\nUpdated HTML template:"

    while remaining_tokens > 0:
        print(remaining_tokens)
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=min(max_response_tokens, remaining_tokens),
            n=1,
            stop=None,
            temperature=0.7,
        )

        generated_text = response.choices[0].text.strip()
        response_text += generated_text
        tokens_used += len(generated_text)
        remaining_tokens = total_tokens - tokens_used

        if len(generated_text) < max_response_tokens:
            break

        prompt = prompt.strip() + " " + generated_text

    return response_text

def generate_django_model(model_description):
    prompt = f"Create a Django model based on the following description: {model_description}\n\nModel code:"
    return gpt_3_5_assistant(prompt)

def generate_django_form(form_description):
    prompt = f"Create a Django form class based on the following description: {form_description}\n\nForm class code:"
    return gpt_3_5_assistant(prompt)

def generate_form_html(form_class_name, app_name):
    prompt = f"Create the HTML code to render a Django form with the form class '{form_class_name}' in the '{app_name}' app\n\nHTML code:"
    return gpt_3_5_assistant(prompt)

def update_html_template(html_template, description):
    prompt = f"Update the following HTML template based on this description: {description}\n\nHTML template:\n{html_template}\n\nUpdated HTML template:"
    return gpt_3_5_assistant(prompt)