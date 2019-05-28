#!/usr/bin/env python
import jinja2 as j2
import yaml
from pathlib import Path

template_dir = Path('templates')
template_env = j2.Environment(
    loader=j2.FileSystemLoader(str(template_dir))
)


def render(page_name, **kwargs):
    raw_html = template_env.get_template(f'{page_name}.j2.html').render(**kwargs)
    target_dir = Path(f'{page_name}' if page_name != "index" else ".")
    target_dir.mkdir(parents=True, exist_ok=True)
    (target_dir / 'index.html').write_text(raw_html)


def main():
    resume = yaml.safe_load((template_dir / 'resume.yaml').read_text())

    render('index')
    render('resume', resume=resume)


if __name__ == "__main__":
    main()
