import json

def convert_json_to_md(json_file, md_file, css_file=None):
    with open(json_file, 'r') as file:
        data = json.load(file)

    title = data['title']
    authors = ', '.join(data['authors'])
    description = data['description']
    instructions = data['instructions']

    md_content = "---\n"
    md_content += "marp: true\n"
    md_content += "theme: default\n"
    md_content += "---\n\n"
    
    if css_file:
        with open(css_file, 'r') as css_file:
            css_content = css_file.read()
        md_content += "<style>\n"
        md_content += css_content
        md_content += "\n</style>\n\n"
    
    md_content += f"# {title}\n\n"
    md_content += f'<p class="tutorial_info">{description}</p>\n\n'
    md_content += f'<p class="tutorial_info">Authors: {authors}</p>\n\n'

    for instruction in instructions:
        action = instruction['action']
        steps = ', '.join(instruction['steps-to-follow'])
        image = instruction['image'].replace(' ', '%20')

        md_content += "---\n"
        md_content += f'\n<img class="icon" src="Resources/3D-Slicer-Mark.svg">\n'
        md_content += f"\n## {action}\n\n"
        md_content += f"{steps}\n\n"
        md_content += f'<img class="screenshot" src="{image}">\n\n'
        
        

    with open(md_file, 'w') as file:
        file.write(md_content)

# Usage example
input_user_generated_content_for_tutorial = 'user_generates_this_file_from_the_tool.json'
output_md_tutorial_file = 'output_tutorial.md'
css_file = 'custom_style.css'
convert_json_to_md(input_user_generated_content_for_tutorial, output_md_tutorial_file, css_file)