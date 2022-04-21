import xarray as xr
from tsdat.pipeline.ingest import IngestPipeline


class CustomPipeline(IngestPipeline):
    """--------------------------------------------------------------------------------
    EXAMPLE INGEST INGESTION PIPELINE

    This is an example ingest meant to demonstrate how one might set up an ingestion
    pipeline using this template repository. It should be deleted before this
    repository or any of its ingests are used in a production environment.

    --------------------------------------------------------------------------------"""

    def hook_customize_dataset(self, dataset: xr.Dataset) -> xr.Dataset:
        return dataset

    def hook_finalize_dataset(self, dataset: xr.Dataset) -> xr.Dataset:
        return dataset

    def hook_plot_dataset(self, dataset: xr.Dataset):
        # DEVELOPER: Add plots
        ...
