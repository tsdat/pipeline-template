import shutil
from typer.testing import CliRunner
from pathlib import Path

from runner import app

runner = CliRunner()


def test_multidispatch():
    # Don't run test if example_pipeline is deleted
    ex_pipeline = Path("pipelines/example_pipeline")

    if ex_pipeline.is_dir():
        # Run pipeline
        input_key = (
            ex_pipeline / "test/data/input/buoy.z06.00.20201201.000000.waves.csv"
        ).as_posix()
        result = runner.invoke(app, ["--multidispatch", input_key])

        # assert pipeline runs successfully
        assert result.exit_code == 0

        # Remove test pipeline storage
        path = Path("storage/root")
        storage_dir = ["data", "ancillary"]
        file_dir = [
            "humboldt.buoy_z05-waves.a1",
            "morro.buoy_z06-waves.a1",
        ]
        for folder in storage_dir:
            for f in file_dir:
                output_dir = path / folder / f
                assert output_dir.is_dir()
                shutil.rmtree(output_dir)
    else:
        assert not ex_pipeline.is_dir()
