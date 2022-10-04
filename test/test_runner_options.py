import subprocess


def test_multidispatch():

    input_key = "pipelines/example_pipeline/test/data/input/buoy.z06.00.20201201.000000.waves.csv"
    result = subprocess.run("python runner.py " + input_key + " --multidispatch")

    # assert pipeline runs successfully
    assert result.returncode == 0