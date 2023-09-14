# Generating the HTML examples

For each example folder there are a `before` and `after` folder. It's assumed
that you run the `before` examples in a "before virtual environment" and `after`
examples in a "after virtual enviroment".

## Make Python virtual enviroments for before and after version 0.20.0

### Before

On Windows

    python -m venv .venv_before
    .venv_before\Scripts\activate
    pip install -r requirements-before.txt

### After

    python -m venv .venv_after
    .venv_before\Scripts\activate
    pip install -r requirements-after.txt


## class-folder

### Generate the "before" HTML

Assuming you activated the "before" virtual environment:

    cd sphinxcontrib-matlabdomain-examples\0.20.0\class-folder\before\
    make html

The output HTML is then in `_build\html\index.html`

### Generate the "after" HTML

Assuming you activated the "after" virtual environment:

    cd sphinxcontrib-matlabdomain-examples\0.20.0\class-folder\after\
    make html

The output HTML is then in `_build\html\index.html`

## see-also-auto-linking

### Generate the "before" HTML

Assuming you activated the "before" virtual environment:

    cd sphinxcontrib-matlabdomain-examples\0.20.0\see-also-auto-linking\before\
    make html

The output HTML is then in `_build\html\index.html`

### Generate the "after" HTML

Assuming you activated the "after" virtual environment:

    cd sphinxcontrib-matlabdomain-examples\0.20.0\see-also-auto-linking\after\
    make html

The output HTML is then in `_build\html\index.html`
