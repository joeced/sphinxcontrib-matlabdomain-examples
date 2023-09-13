# Generating the HTML

## Before

On Windows

    python -m venv .venv_before
    .venv_before\Scripts\activate
    pip install -r requirements-before.txt
    cd before
    make html
    _build\html\index.html

## After

On Windows

    python -m venv .venv_after
    .venv_before\Scripts\activate
    pip install -r requirements-after.txt
    cd after
    make html
    _build\html\index.html