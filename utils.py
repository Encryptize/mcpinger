import re

colour_pattern = re.compile(r'\u00A7[0-9a-fk-or]')
version_pattern = re.compile(r'^([a-zA-zZ]+\s)?([\d\-\s.]+)$')

def remove_colours(motd: str) -> str:
    return colour_pattern.sub('', motd)

def parse_version(version: str):
    result = version_pattern.match(version)

    if result:
        return result.group(2)
    else:
        return None 