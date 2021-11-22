import typer

from typing import List
from pathlib import Path
from enum import Enum
from utils import logger, PipelineDispatcher, set_env


app = typer.Typer()


class Mode(str, Enum):
    aws = "aws"
    local = "local"


@app.command()
def run_pipeline(
    files: List[Path] = typer.Argument(
        ...,
        exists=True,
        file_okay=True,
        dir_okay=False,
        readable=True,
        resolve_path=True,
        help="Path(s) to the file(s) to process",
    ),
):
    """--------------------------------------------------------------------------
    Main entry point to run a registered ingestion pipeline on provided data
    file(s). This script takes path(s) to input file(s), automatically determines
    which ingest to use to process the data, and runs that ingest on the provided
    data.

    Args:

        files (List[Path], optional): The path(s) to the input file(s) to process.

    --------------------------------------------------------------------------"""

    set_env()

    logger.info(f"Found input files: {files}")

    dispatcher = PipelineDispatcher(auto_discover=True)

    logger.debug(f"Discovered ingest modules: \n{dispatcher._cache._modules}")

    success = dispatcher.dispatch(files)

    logger.info(f"Pipeline status: {'success' if success else 'failure'}")


if __name__ == "__main__":
    typer.run(run_pipeline)
