import argparse
import os

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Parse information needed for benchmarking.')
    parser.add_argument('--set-commit-hash', dest='commit_hash', required=True)
    parser.add_argument('--benchmark-name', dest='benchmark_name', default=None)
    parser.add_argument('--hardware', dest='hardware', required=True)
    parser.add_argument('--result-dir', dest='result_dir', required=True)
    parser.add_argument('--presentation', dest='presentation',
                        required=False, default="table")
    parser.add_argument('--script', dest='script', required=False, default=None)

    args = parser.parse_args()
    scripts = [
        "../numpy-benchmarks-openblas/AutoBenchOpenBLASKernels.py",
        "../numpy-benchmarks-openblas/SimplifyASVBenchmarkResults.py",
        "numpy-benchmarks-openblas/CompareSimplifiedBenchmarkResults.py"
    ]

    for script in scripts:
        if args.script is not None and args.script not in script:
            continue
        cmd = "python {}".format(script)
        cmd_args = " --set-commit-hash={} --benchmark-name={} --hardware={} --result-dir={} ".format(
                    args.commit_hash, args.benchmark_name, args.hardware, args.result_dir)
        if (script == "numpy-benchmarks-openblas/CompareSimplifiedBenchmarkResults.py" and
            args.presentation == "graph"):
            os.chdir("..")
            os.system("pip uninstall -y numpy")
            os.system("pip install numpy==1.26.0")
            cmd_args += "--presentation={}".format(args.presentation)
            os.system(cmd + cmd_args)
            os.chdir("numpy")
            os.system("pip install -r requirements/build_requirements.txt")
            os.system("pip install -e . --no-build-isolation")
        else:
            if script == "numpy-benchmarks-openblas/CompareSimplifiedBenchmarkResults.py":
                cmd = "python ../{}".format(script)
            os.system(cmd + cmd_args)
