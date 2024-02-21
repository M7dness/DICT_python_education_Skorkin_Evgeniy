import re

formatters = ['plain', 'bold', 'italic', 'header', 'link', 'inline-code', 'ordered-list', 'unordered-list', 'line-break']

def print_help():
    print('Available formatters:', *formatters)
    print('Special commands: !help !done')

def format_plain(text):
    return text

def format_bold(text):
    return f'**{text}**'

def format_italic(text):
    return f'*{text}*'

def format_header(level, text):
    return '#' * level + ' ' + text

def format_link(label, url):
    return f'[{label}]({url})'

def format_inline_code(text):
    return f'`{text}`'

def format_ordered_list(items):
    return '\n'.join([f'{i + 1}. {item}' for i, item in enumerate(items)])

def format_unordered_list(items):
    return '\n'.join([f'* {item}' for item in items])

def apply_formatter(formatter, text):
    if formatter == 'plain':
        return format_plain(text)
    elif formatter == 'bold':
        return format_bold(text)
    elif formatter == 'italic':
        return format_italic(text)
    elif formatter == 'header':
        level = int(input('Level: '))
        if level < 1 or level > 6:
            print('The level should be within the range of 1 to 6.')
            return None
        return format_header(level, text)
    elif formatter == 'link':
        label = input('Label: ')
        url = input('URL: ')
        return format_link(label, url)
    elif formatter == 'inline-code':
        return format_inline_code(text)
    elif formatter == 'ordered-list':
        while True:
            num_rows = int(input('Number of rows: '))
            if num_rows > 0:
                break
            else:
                print('The number of rows should be greater than zero.')
        items = [input(f'Row #{i + 1}: ') for i in range(num_rows)]
        return format_ordered_list(items)
    elif formatter == 'unordered-list':
        while True:
            num_rows = int(input('Number of rows: '))
            if num_rows > 0:
                break
            else:
                print('The number of rows should be greater than zero.')
        items = [input(f'Row #{i + 1}: ') for i in range(num_rows)]
        return format_unordered_list(items)
    elif formatter == 'line-break':
        return '\n'

def save_to_file(filename, content):
    with open(filename, 'w') as f:
        f.write(content)

print('Choose a formatter:')
print('!help shows available formatters, !done exits')

markdown_text = ''

while True:
    fmt = input('> ')
    if fmt == '!help':
        print_help()
    elif fmt == '!done':
        save_to_file('output.md', markdown_text)
        break
    elif fmt not in formatters:
        print('Unknown formatting type or command')
    else:
        if fmt != 'line-break':
            text = input('Text: ')
        else:
            text = ''

        formatted_text = apply_formatter(fmt, text)
        if formatted_text is not None:
            markdown_text += formatted_text + '\n\n'
            print(markdown_text)
