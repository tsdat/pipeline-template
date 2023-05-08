from pathlib import Path

import pytest
import xarray as xr
from tsdat import assert_close, PipelineConfig, TransformationPipeline


# DEVELOPER: Update paths to your configuration(s), test input(s), and expected test
# results files.
# The transformation pipeline will likely depend on the output of an ingestion pipeline
# in order to declare this dependency so the tests can run in the correct order (e.g.,
# for github actions CI/CD), update the line below to point to the correct folder and
# test name
@pytest.mark.dependency(depends=["../../example_pipeline/test/test_pipeline.py"])
def test_{{ cookiecutter.module }}_pipeline():
    # The transformation pipeline will likely depend on the output of an ingestion
    # pipeline. To account for this we first run the ingest to generate input data for
    # the vap, and then run the vap test. Please update the line below to point to the
    #  correct folder / test name
    from pipelines.FOLDER.test.test_pipeline import TEST_NAME

    TEST_NAME()

    config_path = Path("pipelines/{{ cookiecutter.module }}/config/pipeline.yaml")
    config = PipelineConfig.from_yaml(config_path)
    pipeline: TransformationPipeline = config.instantiate_pipeline()  # type: ignore

    # Transformation pipelines require an input of [date.time, date.time] formatted as
    # YYYYMMDD.hhmmss. The start date is inclusive, the end date is exclusive. E.g., the
    # default below would run the pipeline on data from midnight on 2022-04-24 to just
    # before midnight on 2022-04-25:
    run_dates = ["20220424.000000", "20220425.000000"]
    dataset = pipeline.run(run_dates)

    # You will need to create this file after running the data through the pipeline
    # OR: Delete this and perform sanity checks on the input data instead of comparing
    # with an expected output file
    expected_file = "pipelines/{{ cookiecutter.module }}/test/data/expected/abc.example.c1.20220424.000000.nc"
    expected: xr.Dataset = xr.open_dataset(expected_file)  # type: ignore
    assert_close(dataset, expected, check_attrs=False)
