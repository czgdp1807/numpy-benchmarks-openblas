## About

This repository contains scripts for automatically benchmarking several CPU architectures supported by OpenBLAS simultaneously.

It will also contain scripts for analysing the resulting benchmarking data.

## Steps to use

Use [size_config](https://github.com/czgdp1807/numpy/tree/size_config) from my fork of numpy.

Inside `numpy` project root execute the following steps,

1. `git clean -fdx`
2. `pip install -e . --no-build-isolation`
3. `python ../numpy-benchmarks-openblas/script.py --set-commit-hash=2da02ea321f557c0cfe0ad6d0e7d8a4354c51103 --benchmark-name=bench_linalg.Eindot.time_matmul_a_b --hardware=x86_64 --result-dir=/path/to/dir/where/results/will/be/stored/by/this/script`

In the third step note the `../numpy-benchmarks-openblas/script.py`. It means that `numpy-benchmarks-openblas` is in the same directory as `numpy`. For example, if `numpy` is present in `~/Quansight/` then `numpy-benchmarks-openblas` should also be present in `~/Quansight/`

For graphical representation, pass` --presentation=graph`. The graphs will be saved in `simplified_results/graphs` under the path passed in `--result-dir`. For example, if you pass `--result-dir=~/x/y/z` then the graphs will be saved inside, `~/x/y/z/simplified_results/graphs`.

After running the `script.py` once if you only want to do the visualisation of the benchmarking data, you need to only run the `CompareSimplifiedBenchmarkResults.py` with all the command options as it is. In other words, just replace `script.py` with `CompareSimplifiedBenchmarkResults.py`. That would just only plot graphs or output a table.

For tuning the sizes for different benchmarks, change the values in `bench_sizes.json`. The keys are the name of benchmarks (defined as Python classes in `bench_linalg.py`). The value of benchmark key is a mapping of variable (defined inside the Python classes) to its sizes/dimensions (change these for benchmarking purposes).
