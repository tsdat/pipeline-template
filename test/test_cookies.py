import pytest

import shutil
from typer.testing import CliRunner
from pathlib import Path

from templates.generate import app

runner = CliRunner()


def test_generate_ingest_pipeline():

    output_dir = Path("pipelines") / "ingest_testing"
    if output_dir.exists():
        shutil.rmtree(output_dir)

    result = runner.invoke(
        app,
        [
            "ingest",
            "--ingest-title",
            "Ingest Testing",
            "--ingest-location",
            "PNNL",
            "--ingest-description",
            "Testing typer wrapper over cookiecutter ingest pipeline template.",
            "--no-use-custom-data-reader",
            "--no-use-custom-data-converter",
            "--no-use-custom-qc",
        ],
        input="\n".join(
            [
                "y",  # Okay to module name
                "y",  # Okay to classname
                "y",  # Okay to location id
            ]
        ),
    )

    assert result.exit_code == 0
    assert output_dir.is_dir()

    # Run pytest on the output dir
    exit_code = pytest.main(output_dir)
    assert exit_code.name == "OK"

    shutil.rmtree(output_dir)
