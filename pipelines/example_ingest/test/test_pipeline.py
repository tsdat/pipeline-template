import xarray as xr
from pathlib import Path
from tsdat import PipelineConfig, assert_close


def test_example_ingest_pipeline():
    config_path = Path("pipelines/example_ingest/config/pipeline.yaml")
    config = PipelineConfig.from_yaml(config_path)
    pipeline = config.instantiate_pipeline()

    test_file = "pipelines/example_ingest/test/data/input/data.csv"
    expected_file = (
        "pipelines/example_ingest/test/data/expected/abc.example.a1.20220424.000000.nc"
    )

    dataset = pipeline.run([test_file])
    expected: xr.Dataset = xr.open_dataset(expected_file)  # type: ignore
    assert_close(dataset, expected, check_fill_value=False)