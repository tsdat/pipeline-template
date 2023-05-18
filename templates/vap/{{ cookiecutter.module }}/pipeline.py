import xarray as xr

# import matplotlib.dates as mdates
# import matplotlib.pyplot as plt
from tsdat import TransformationPipeline



# DEVELOPER: Implement your pipeline and update its docstring.
class {{ cookiecutter.classname }}(TransformationPipeline):
    """---------------------------------------------------------------------------------
    This is an example pipeline meant to demonstrate how one might set up a
    pipeline using this template repository.

    ---------------------------------------------------------------------------------"""

    def hook_customize_dataset(self, dataset: xr.Dataset) -> xr.Dataset:
        # DEVELOPER: (Optional) Use this hook to modify the dataset before qc is applied
        return dataset

    def hook_finalize_dataset(self, dataset: xr.Dataset) -> xr.Dataset:
        # DEVELOPER: (Optional) Use this hook to modify the dataset after qc is applied
        # but before it gets saved to the storage area
        return dataset

    def hook_plot_dataset(self, dataset: xr.Dataset):
        # DEVELOPER: (Optional, recommended) Create plots.
        # location = self.dataset_config.attrs.location_id
        # datastream: str = self.dataset_config.attrs.datastream

        # date, time = get_start_date_and_time_str(dataset)

        # plt.style.use("default")  # clear any styles that were set before
        # plt.style.use("shared/styling.mplstyle")

        # with self.storage.uploadable_dir(datastream) as tmp_dir:

        #     fig, ax = plt.subplots()
        #     dataset["example_var"].plot(ax=ax, x="time")  # type: ignore
        #     fig.suptitle(f"Example Variable at {location} on {date} {time}")
        #     plot_file = get_filename(dataset, title="example_plot", extension="png")
        #     fig.savefig(tmp_dir / plot_file)
        #     plt.close(fig)
        # TODO: Better x-axis ticks:
        # Set the x-axis to have ticks spaced by the hour
        # hours = mdates.HourLocator(interval=1)
        # ax.xaxis.set_major_locator(hours)

        # # Set the format of the x-axis tick labels
        # time_format = mdates.DateFormatter('%H:%M')
        # ax.xaxis.set_major_formatter(time_format)
        pass
