from pipelines.{{ cookiecutter.ingest_slug }} import CustomPipeline
from utils import expand, set_env


# TODO – Developer: Update path to data and/or configuration files as needed.
if __name__ == "__main__":
    set_env()
    pipeline = CustomPipeline(
        expand("config/pipeline_config_{{ cookiecutter.ingest_slug }}.yml", __file__),
        expand("config/storage_config_{{ cookiecutter.ingest_slug }}.yml", __file__),
    )
    pipeline.run(
        expand("tests/data/input/data.csv", __file__)
    )
