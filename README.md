# Tsdat Pipeline Template

[![tests](https://github.com/tsdat/pipeline-template/actions/workflows/tests.yml/badge.svg)](https://github.com/tsdat/pipeline-template/actions/workflows/tests.yml)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

This repository contains a collection of one or more `tsdat` pipelines (as found under the ``pipelines`` folder).  This
enables related pipelines to be more easily maintained and run together.  New pipelines can be added easily via 
the cookiecutter template mechanism described below.

## Repository Structure

The repository is made up of the following core pieces:

- **`runner.py`**: Main entry point for running a pipeline.

- **`pipelines/*`**: Collection of custom data pipelines using `tsdat`.

- **`pipelines/example_ingest`**: An out-of-the-box example `tsdat` pipeline.

- **`templates/*`**: Template(s) used to generate new pipelines.

- **`shared/*`**: Shared configuration files that may be used across multiple pipelines.

- **`utils/*`**: Utility scripts.

## Prerequisites

The following are required to develop a tsdat pipeline:
1. **A GitHub account.** [Click here to create an account if you don't have one already](https://github.com/)


2. **An Anaconda environment.**  We strongly recommend developing in an Anaconda Python environment to ensure
that there are no library dependency issues.  [Click here for more information on installing Anaconda on your computer](https://docs.anaconda.com/anaconda/install/index.html)

    > **Windows Users** - You can install Anaconda directly to your Windows box OR you can run via a linux
    environment using the Windows Subsystem for Linux (WSL).  See
    [this tutorial on WSL](https://tsdat.readthedocs.io/en/latest/tutorials/wsl.html) for
    how to set up a WSL environment and attach VS Code to it.


## Creating a repository from the pipeline-template
You can create a new repository based upon the tsdat pipeline-template repository in GitHub:

1. Click this '[Use this template](https://github.com/tsdat/pipeline-template/generate)' link and
follow the steps to copy the template repository into to your account.
    > **NOTE:** If you are looking to get an older version of the template, you will need to
    select the box next to 'Include all branches' and set the branch your are interested
    in as your new default branch.

2. On github click the 'Code' button to get a link to your code, then run 
    ```bash
    git clone <the link you copied>
    ```
    from the terminal on your computer where you would like to work on the code.

## Setting up your Anaconda environment
1. Open an appropriate terminal shell from your computer
   1. If you are on Linux or Mac, just open a regular terminal
   2. If you are on Windows, start your Anaconda prompt if you installed Anaconda directly to Windows, OR open a
   WSL terminal if you installed Anaconda via WSL.


2. Run the following commands to create and activate your conda environment, where $REPOSITORY_ROOT represents
the folder where you checked out your pipeline repository:

    ```bash
    conda env create --file=conda-environment.yaml
    conda activate tsdat-pipelines
    ```

    If you get the following warning message when running tsdat commands in your shell:
    ```bash
     UserWarning: pyproj unable to set database path.
   ```

    Then run the following additional commands to permanently remove this warning message:
    ```bash
    conda remove --force pyproj
    pip install pyproj
    ```

## Opening your repository in VS Code
1. Open the cloned repository in VS Code. *(This repository contains default settings for
VS Code that will make it much easier to get started quickly.)*

2. Install the recommended extensions (there should be a pop-up in VS Code with recommendations).

3. Tell VS Code to use your new environment:
    - Press `F1` to bring up the command pane in VS Code
    - Type `Python: Select Interpreter` and select it.
    - Select the newly-created `ingest` conda environment from the drop-down list.
        > You may need to refresh the list (cycle icon in the top right) to see it.
    - Bring up the command pane and type `Developer: Reload Window` to reload VS Code
    and ensure the settings changes propagate correctly.


## Adding a new pipeline

1. Ensure your development environment is set up according to the instructions above

2. Use a cookiecutter template to generate a new pipeline folder.  From your top level repository folder, run:

    ```bash
    make cookies
    ```

    The `make cookies` command is a memorable shortcut for `cookiecutter templates/ingest -o pipelines`

    > Cookiecutter will show some text in the prompts, but more information on these
    prompts can be found in the [template README.md](templates/ingest/README.md)

3. Once cookiecutter is done you will see your new pipeline folder appear inside `pipelines/`. Please see the README.md file inside 
that folder for more information on how to configure, run, test, and debug your pipeline. 

**This repository supports adding as many pipelines as you want - just rinse and repeat the steps above.**


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
