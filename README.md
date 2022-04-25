# INGEST-TEMPLATE

[![tests](https://github.com/tsdat/ingest-template/actions/workflows/tests.yml/badge.svg)](https://github.com/tsdat/ingest-template/actions/workflows/tests.yml)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

This repository provides a way to group related `tsdat` pipelines so they can be more
easily maintained and run together.


## Structure

The repository is made up of the following core pieces:

- **`runner.py`**: Main entry point.

- **`pipelines/*`**: Collection of custom data pipelines using `tsdat`.

- **`templates/*`**: Template(s) used to generate boilerplate for new pipelines.

- **`shared/*`**: Hosts configuration files.

- **`utils/*`**: Utility scripts.

## Getting Started

Please take the following steps to start using this repository for the first time:

> **Windows Users** - we strongly recommend developing in a linux environment to help
mitigate common python packaging and path issues. See
[this tutorial on WSL](https://tsdat.readthedocs.io/en/latest/tutorials/wsl.html) for
how to set up a WSL environment and attach VS Code to it.

1. Click '[Use this template](https://github.com/tsdat/ingest-template/generate)' and
follow the steps to copy this into to your account.
    > If you are looking to get an older version of the template, you will need to
    select the box next to 'Include all branches' and set the branch your are interested
    in as your new default branch.

2. On github click the 'Code' button to get a link to your code, then run `git clone <the link you copied>` from the terminal on your computer where you would like to work on the code.

3. Open the cloned repository in VS Code. This repository contains default settings for
VS Code that will make it much easier to get started quickly.

4. Install the recommended extensions (there should be a pop-up in VS Code with recommendations).

5. We highly recommend using [conda](https://docs.anaconda.com/anaconda/install/) to
manage dependencies in your development environment. 
    ```bash
    $ conda create --name tsdat-pipelines python=3.8
    $ conda activate tsdat-pipelines
    (tsdat-pipelines) $ pip install -r requirements-dev.txt
    ```

6. Tell VS Code to use your new environment:
    - Press `F1` to bring up the command pane in VS Code
    - Type `Python: Select Interpreter` and select it.
    - Select the newly-created `ingest` conda environment from the drop-down list.
        > You may need to refresh the list (cycle icon in the top right) to see it.
    - Bring up the command pane and type `Developer: Reload Window` to reload VS Code
    and ensure the settings changes propogate correctly.


## Adding a new pipeline

1. Ensure your development environment is set up according to the instructions above

4. Use a cookiecutter template to generate boilerplate pipeline code:

    ```bash
    cookiecutter templates/ingest -o pipelines
    ```

    > Cookiecutter will show some text in the prompts, but more information on these
    prompts can be found in the [template README.md](templates/ingest/README.md)

5. Once cookiecutter is done you will see a new folder appear inside `pipelines/`. That
folder contains information on how to customize the generated boilerplate code. 

This repository supports adding as many pipelines as you want. Just rinse and repeat with
the steps above.

## Additional resources

- Learn more about `tsdat`:
    - GitHub: https://github.com/tsdat/tsdat
    - Documentation: https://tsdat.readthedocs.io
    - Data standards: https://github.com/tsdat/data_standards
- Learn more about `xarray`: 
    - GitHub: https://github.com/pydata/xarray
    - Documentation: https://xarray.pydata.org
- Learn more about 'pydantic':
    - GitHub: https://github.com/samuelcolvin/pydantic/
    - Documentation: https://pydantic-docs.helpmanual.io
- Other useful tools:
    - VS Code: https://code.visualstudio.com/docs
    - Docker: https://docs.docker.com/get-started/
    - `pytest`: https://github.com/pytest-dev/pytest
    - `black`: https://github.com/psf/black
    - `matplotlib` guide: https://realpython.com/python-matplotlib-guide/
