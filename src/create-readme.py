table = open('../docs/table.md').read()
readme_template = open('../docs/readme-template.md').read()
output = readme_template.replace('__TABLE__\n', table)

with open('../README.md', 'w') as file:
    file.write(output)
