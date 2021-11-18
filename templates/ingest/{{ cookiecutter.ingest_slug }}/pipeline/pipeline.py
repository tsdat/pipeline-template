import os
import cmocean
import numpy as np
import pandas as pd
import xarray as xr
import matplotlib.pyplot as plt

from typing import Dict
from tsdat import DSUtil
from utils import IngestPipeline, format_time_xticks


# TODO – Developer: Use hooks to add custom functionality to the pipeline including
# plots, as applicable. Remove any unused code.


class Pipeline(IngestPipeline):
    """--------------------------------------------------------------------------------
    {{ cookiecutter.ingest.upper() }} INGESTION PIPELINE

    {{ cookiecutter.description }}

    --------------------------------------------------------------------------------"""

    def hook_customize_raw_datasets(
        self, raw_dataset_mapping: Dict[str, xr.Dataset]
    ) -> Dict[str, xr.Dataset]:
        return raw_dataset_mapping

    def hook_customize_dataset(
        self, dataset: xr.Dataset, raw_mapping: Dict[str, xr.Dataset]
    ) -> xr.Dataset:
        return dataset

    def hook_finalize_dataset(self, dataset: xr.Dataset) -> xr.Dataset:
        return dataset

    def hook_generate_and_persist_plots(self, dataset: xr.Dataset):
        style_file = os.path.join(os.path.dirname(__file__), "styling.mplstyle")

        date = pd.to_datetime(dataset.time.data[0]).strftime("%d-%b-%Y")
        loc = dataset.attrs["location_meaning"]

        with plt.style.context(style_file):

            # Create an example plot with some noise added for fun
            filename = DSUtil.get_plot_filename(dataset, "example_noise", "png")
            with self.storage._tmp.get_temp_filepath(filename) as tmp_path:
                fig, ax = plt.subplots()

                noise = np.random.random(dataset["example_var"].data.shape) - 0.5
                noisy_example = dataset["example_var"] + noise

                dataset["example_var"].plot(
                    ax=ax,
                    x="time",
                    c=cmocean.cm.deep_r(0.75),
                    label="example_var",
                )
                noisy_example.plot(
                    ax=ax,
                    x="time",
                    c=cmocean.cm.deep_r(0.25),
                    label="noisy_example_var",
                )

                fig.suptitle(f"Example variable at {loc} on {date}")
                ax.set_title("")  # Remove bogus title created by xarray
                ax.legend(ncol=2, bbox_to_anchor=(1, -0.05))
                ax.set_ylabel("Example (m)")
                ax.set_xlabel("Time (UTC)")
                format_time_xticks(ax)

                fig.savefig(tmp_path)
                self.storage.save(tmp_path)
                plt.close(fig)
