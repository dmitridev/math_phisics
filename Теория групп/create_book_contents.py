import os

def create_link(mainheader: str, subheader: str, name: str):
    return '- [{0}]({1})'.format(name,os.path.join(mainheader.rstrip(), subheader.rstrip(),name.rstrip())
			 .replace(' ', '%20') + '.md')

path = os.path.abspath('./')

filename = 'Содержание.md'

# теперь нужно обработать файл
lines = []

with open(filename, 'r+', encoding='utf-8') as file:
    lines = [line.rstrip() for line in file.readlines()]

    mainheader = ''
    subheader = ''
    name = ''

    for i in range(0, len(lines)):
        line = lines[i].strip()
        if (line.startswith('## ')):
            mainheader = line[3:]

        if (line.startswith('### ')):
            subheader = line[4:]

        if (line.startswith('-')):
            name = line[2:]
            line = create_link(mainheader, subheader, name)

        line = line + '\n'
        lines[i] = line
        print(mainheader,subheader,name)

    file.seek(0)
    file.writelines(lines)
