import xarray as xr
from tsdat import IngestPipeline, FileHandler, S3Path
from tsdat.qc import QualityManagement
from typing import Union, List, Dict


class IngestPipelineUtils(IngestPipeline):

    def run_plots(self, files: Union[List[S3Path], List[str]]):
        """----------------------------------------------------------------------------
        Runs the `IngestPipelineUtils.hook_generate_and_persist_plots()` function on the
        provided file or list of files. This is useful for re-running plots without the
        need to also reprocess the data.

        Args:
            files (Union[List[S3Path], str]): The file(s) to read in and produce plots
            for. Note that these files will be processed independent of one another.

        ----------------------------------------------------------------------------"""
        for _file in files:
            with self.storage.tmp.fetch(_file) as tmp_file:
                ds = FileHandler.read(tmp_file)
                self.hook_generate_and_persist_plots(ds)
