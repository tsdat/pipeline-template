from __future__ import annotations
import re
from pathlib import Path
from typing import Any, Callable, Dict, Literal
import typer
from cookiecutter.main import cookiecutter
from slugify import slugify  # type: ignore

app = typer.Typer()


def _to_cookiecutter_bool(value: bool) -> Literal["yes", "no"]:
    return "yes" if value else "no"


def validated_prompt(text: str, validator: Callable[[Any], bool], **kwargs: Any) -> Any:
    value = typer.prompt(text, **kwargs)
    while not validator(value):
        value = typer.prompt(text, **kwargs)
    return value


def valid_module(module: str) -> bool:
    matches_regex = bool(re.match(r"^[a-zA-Z][a-zA-Z0-9_]+$", module))
    if not matches_regex:
        typer.echo(
            f"'{module}' is not a valid python module name. Module names must only"
            " contain alphanumeric and '_' characters and should start with a letter."
            " Using lowercase with words separated by '_' is considered best practice."
        )
    already_exists = (Path("pipelines") / Path(module)).exists()
    if already_exists:
        typer.echo(
            f"'{module}' already exists in the pipelines/ folder. This tool can only be"
            " used to add new pipelines, not to modify or extend an existing pipeline."
            " Please enter a new module name or abort this command (ctrl-C)."
        )
    return matches_regex and not already_exists


def valid_classname(classname: str) -> bool:
    is_valid = bool(re.match(r"^[A-Z][a-zA-Z0-9_]+$", classname))
    if not is_valid:
        typer.echo(
            f"'{classname}' is not a valid python class name. Class names must only"
            " contain alphanumeric and '_' characters and should start with a capital"
            " letter. Using CamelCase is considered best practice."
        )
    return is_valid


@app.command()
def ingest(
    ingest_title: str = typer.Option(
        ...,
        help="The title of the ingest excluding any location details. This will be used"
        " to generate a default pipeline class name and the folder in which it lives."
        " E.g., for a title of 'Halo Lidar', 'HaloLidar' would be the default name of"
        " the pipeline and 'pipelines/halo_lidar' would be the folder created to"
        " contain its code. Note that a later prompt will appear to confirm or modify"
        " these defaults.",
        prompt="What title do you want to give this ingest?\n",
    ),
    ingest_location: str = typer.Option(
        ...,
        help="A label for the location where the data are collected.",
        prompt="What label should be used for the location of the ingest? (E.g., PNNL,"
        " San Francisco, etc.)\n",
    ),
    ingest_description: str = typer.Option(
        ...,
        help="A brief description of the ingest that will be used in the ingest's"
        " README file and in the metadata produced by the pipeline.",
        prompt="Briefly describe the ingest\n",
    ),
    data_standards: str = typer.Option(
        ...,
        help="Data standardization conventions to hold the dataset to. Choose from "
        "'basic'(standard CF conventions), 'ACDD' (Attribute Conventions for Data "
        "Discovery), or 'IOOS' (Integrated Ocean Observing System) standards.",
        prompt="Data standards to use with the ingest dataset ['basic','ACDD','IOOS']\n",
    ),
    use_custom_data_reader: bool = typer.Option(
        False,
        help="Flag to generate boilerplate code for handling inputs stored in a data"
        " format not supported by tsdat out-of-the-box. To see a complete list of"
        " built-in data readers visit"
        " https://tsdat.readthedocs.io/en/latest/autoapi/tsdat/io/readers",
        prompt="Do you want to use a custom DataReader?\n",
    ),
    use_custom_data_converter: bool = typer.Option(
        False,
        help="Flag to generate boilerplate code to apply custom convertions or other"
        " preprocessing actions to the raw data before it enters the data pipeline. Use"
        " this if the built-in data converters are not sufficient. To see a complete"
        " list of built-in DataConverters visit"
        " https://tsdat.readthedocs.io/en/latest/autoapi/tsdat/io/converters",
        prompt="Do you want to use a custom DataConverter?\n",
    ),
    use_custom_qc: bool = typer.Option(
        False,
        help="Flag to generate boilerplate code for applying custom quality checks or"
        " corrections to the data. Use this if the built-in QualityCheckers or"
        " QualityHandlers are not sufficient. To see a complete list of "
        " list of built-in QualityCheckers and QualityHandlers visit"
        " https://tsdat.readthedocs.io/en/latest/autoapi/tsdat/qc",
        prompt="Do you want to use a custom QualityChecker or QualityHandler?\n",
    ),
):
    """Ingest cookiecutter wrapper that adds validation and better dynamic defaults."""

    module = slugify(ingest_title, separator="_")
    classname = module.replace("_", " ").title().replace(" ", "")
    location_id = slugify(ingest_location, separator="_")

    if not typer.confirm(
        f"'{module}' will be the module name (the folder created under 'pipelines/') Is"
        " this OK?\n",
        default=True,
    ):
        module = validated_prompt(
            "What would you like to rename the module to?\n", valid_module
        )

    if not typer.confirm(
        f"'{classname}' will be the name of your IngestPipeline class (the python class"
        " containing your custom python code hooks). Is this OK?\n",
        default=True,
    ):
        classname = validated_prompt(
            "What would you like to rename the pipeline class to?\n", valid_classname
        )

    if not typer.confirm(
        f"'{location_id}' will be the short label used to represent the location where"
        " the data are collected. Is this OK?\n",
        default=True,
    ):
        location_id = typer.prompt(
            "What would you like to rename the location identifier to?\n"
        )

    cookiedough: Dict[str, Any] = {
        "ingest_name": ingest_title,
        "ingest_location": ingest_location,
        "ingest_description": ingest_description,
        "data_standards": data_standards,
        "use_custom_data_reader": _to_cookiecutter_bool(use_custom_data_reader),
        "use_custom_data_converter": _to_cookiecutter_bool(use_custom_data_converter),
        "use_custom_qc": _to_cookiecutter_bool(use_custom_qc),
        "module": module,
        "classname": classname,
        "location_id": location_id,
    }

    typer.echo(
        "\nGenerating templates/ingest cookiecutter with the following answers:\n"
        f" {cookiedough}\n"
    )

    cookiecutter(
        "templates/ingest",
        no_input=True,
        output_dir="pipelines/",
        extra_context={**cookiedough},
    )

    output_dir = Path("pipelines") / module
    typer.echo(f"Created new ingest pipeline in {output_dir.as_posix()}")


@app.command()
def vap(
    title: str = typer.Option(
        ...,
        help="The title of the pipeline excluding any location details. This will be used"
        " to generate a default pipeline class name and the folder in which it lives."
        " E.g., for a title of 'Halo Lidar', 'HaloLidar' would be the default name of"
        " the pipeline and 'pipelines/vap_halo_lidar' would be the folder created to"
        " contain its code. Note that a later prompt will appear to confirm or modify"
        " these defaults.",
        prompt="What title do you want to give this pipeline?\n",
    ),
    location: str = typer.Option(
        ...,
        help="A label for the location where the pipeline should run.",
        prompt="What label should be used for the location of the pipeline? (E.g., PNNL,"
        " San Francisco, etc.)\n",
    ),
    description: str = typer.Option(
        ...,
        help="A brief description of the pipeline that will be used in the pipeline's"
        " README file and in the metadata produced by the pipeline.",
        prompt="Briefly describe the pipeline\n",
    ),
    use_custom_data_converter: bool = typer.Option(
        False,
        help="Flag to generate boilerplate code to apply custom conversions or other"
        " preprocessing actions to the data before it enters the data pipeline. Use"
        " this if the built-in data converters are not sufficient. To see a complete"
        " list of built-in DataConverters visit"
        " https://tsdat.readthedocs.io/en/latest/autoapi/tsdat/io/converters",
        prompt="Do you want to use a custom DataConverter?\n",
    ),
    use_custom_qc: bool = typer.Option(
        False,
        help="Flag to generate boilerplate code for applying custom quality checks or"
        " corrections to the data. Use this if the built-in QualityCheckers or"
        " QualityHandlers are not sufficient. To see a complete list of "
        " list of built-in QualityCheckers and QualityHandlers visit"
        " https://tsdat.readthedocs.io/en/latest/autoapi/tsdat/qc",
        prompt="Do you want to use a custom QualityChecker or QualityHandler?\n",
    ),
):
    """Pipeline cookiecutter wrapper that adds validation and better dynamic defaults."""

    module = "vap_" + slugify(title, separator="_")
    classname = module.replace("_", " ").title().replace(" ", "")
    location_id = slugify(location, separator="_")

    if not typer.confirm(
        f"'{module}' will be the module name (the folder created under 'pipelines/') Is"
        " this OK?\n",
        default=True,
    ):
        module = validated_prompt(
            "What would you like to rename the module to?\n", valid_module
        )

    if not typer.confirm(
        f"'{classname}' will be the name of your TransformationPipeline class (the python class"
        " containing your custom python code hooks). Is this OK?\n",
        default=True,
    ):
        classname = validated_prompt(
            "What would you like to rename the pipeline class to?\n", valid_classname
        )

    if not typer.confirm(
        f"'{location_id}' will be the short label used to represent the location where"
        " the data are collected. Is this OK?\n",
        default=True,
    ):
        location_id = typer.prompt(
            "What would you like to rename the location identifier to?\n"
        )

    cookiedough: Dict[str, Any] = {
        "vap_name": title,
        "location": location,
        "vap_description": description,
        "use_custom_data_converter": _to_cookiecutter_bool(use_custom_data_converter),
        "use_custom_qc": _to_cookiecutter_bool(use_custom_qc),
        "module": module,
        "classname": classname,
        "location_id": location_id,
    }

    typer.echo(
        "\nGenerating templates/vap cookiecutter with the following answers:\n"
        f" {cookiedough}\n"
    )

    cookiecutter(
        "templates/vap",
        no_input=True,
        output_dir="pipelines/",
        extra_context={**cookiedough},
    )

    output_dir = Path("pipelines") / module
    typer.echo(f"Created new pipeline pipeline in {output_dir.as_posix()}")


@app.callback(invoke_without_command=True)
def default(ctx: typer.Context):
    """Prompts the user to select which command to run if no options are provided."""

    # Skip the callback if the user selected a command
    if ctx.invoked_subcommand is not None:
        return

    from rich.prompt import Prompt

    options: Dict[str, Any] = {
        "ingest": ingest,
        "vap": vap,
    }

    selected = Prompt.ask(
        "Please choose a type of pipeline to create",
        choices=list(options),
        default="ingest",
    )

    typer.run(options[selected])


if __name__ == "__main__":
    app()
