import shutil
from typer.testing import CliRunner
from pathlib import Path

from runner import app

runner = CliRunner()


def test_multidispatch():
    # Remove test pipeline storage
    storage_dir = ["data", "ancillary"]
    file_dir = [
        "humboldt.buoy_z05-waves.a1",
        "morro.buoy_z06-waves.a1",
    ]
    path = Path("storage/root")
    for folder in storage_dir:
        for f in file_dir:
            output_dir = path / folder / f
            if output_dir.exists():
                shutil.rmtree(output_dir)

    # Run pipeline
    input_key = "pipelines/example_pipeline/test/data/input/buoy.z06.00.20201201.000000.waves.csv"
    result = runner.invoke(app, ["--multidispatch", input_key])

    # assert pipeline runs successfully
    assert result.exit_code == 0
    for folder in storage_dir:
        for f in file_dir:
            output_dir = path / folder / f
            assert output_dir.is_dir()
