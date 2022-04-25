import xarray as xr
from tsdat import DataReader


class CustomDataReader(DataReader):
    """---------------------------------------------------------------------------------
    Data reader that can read from *xyz* formatted-data files.

    ---------------------------------------------------------------------------------"""

    # DEVELOPER: Implement the read function update the classname/docstring as needed.

    def read(self, input_key: str) -> xr.Dataset:
        raise NotImplementedError
        return xr.Dataset()
