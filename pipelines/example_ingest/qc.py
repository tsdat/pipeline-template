import numpy as np
import xarray as xr
from numpy.typing import NDArray
from tsdat import QualityChecker, QualityHandler


class CustomQualityChecker(QualityChecker):
    """---------------------------------------------------------------------------------
    Custom Quality Checker

    ---------------------------------------------------------------------------------"""

    def run(self, dataset: xr.Dataset, variable_name: str) -> NDArray[np.bool8]:

        var_data = dataset[variable_name]

        failures: NDArray[np.bool8] = np.zeros_like(var_data, dtype=np.bool8)  # type: ignore

        # DEVELOPER: Add your custom quality checking code here
        raise NotImplementedError

        return failures


class CustomQualityHandler(QualityHandler):
    def run(
        self, dataset: xr.Dataset, variable_name: str, failures: NDArray[np.bool8]
    ) -> xr.Dataset:

        # DEVELOPER: Add custom quality handling code here
        raise NotImplementedError

        return dataset
