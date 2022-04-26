import xarray as xr
import matplotlib.pyplot as plt
from tsdat import IngestPipeline, get_start_date_and_time_str, get_filename
from utils import format_time_xticks


class ExamplePipeline(IngestPipeline):
    """---------------------------------------------------------------------------------
    This is an example ingestion pipeline meant to demonstrate how one might set up a
    pipeline using this template repository.

    ---------------------------------------------------------------------------------"""

    def hook_plot_dataset(self, dataset: xr.Dataset):
        location = self.dataset_config.attrs.location_id
        datastream: str = self.dataset_config.attrs.datastream

        date, time = get_start_date_and_time_str(dataset)

        plt.style.use("default")  # clear any styles that were set before
        plt.style.use("shared/styling.mplstyle")

        with self.storage.uploadable_dir(datastream) as tmp_dir:

            fig, ax = plt.subplots()
            dataset["example_var"].plot(ax=ax, x="time")  # type: ignore
            fig.suptitle(f"Example Variable at {location} on {date} {time}")
            format_time_xticks(ax)
            plot_file = get_filename(dataset, title="example_plot", extension="png")
            fig.savefig(tmp_dir / plot_file)
            plt.close(fig)
