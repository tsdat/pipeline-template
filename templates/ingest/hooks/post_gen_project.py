import os
import subprocess
from pathlib import Path

PROJECT_DIR = Path.cwd() / "pipelines" / "{{ cookiecutter.__module }}"


def main():
    print("Template created for {{ cookiecutter.ingest_slug }}. Checking selections...")

    if "{{ cookiecutter.use_custom_data_reader }}" == "no":  # type: ignore
        os.remove(PROJECT_DIR / "readers.py")

    if "{{ cookiecutter.use_custom_data_converter }}" == "no":  # type: ignore
        os.remove(PROJECT_DIR / "readers.py")

    if "{{ cookiecutter.use_custom_qc }}" == "no":  # type: ignore
        os.remove(PROJECT_DIR / "qc.py")

    print("Formatting template code...")

    subprocess.run(["black", PROJECT_DIR])

    print(f"Generated {{ cookiecutter.ingest_slug }} in {PROJECT_DIR}")


if __name__ == "__main__":
    main()
