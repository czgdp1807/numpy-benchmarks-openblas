import os
import argparse
import subprocess
import shutil
from utils import generate_target_dir_name, openblas_target_cpu_archs

def run_benchmark(target_arch, commit_hash, dest_dir, benchmark_name=None):
    os.chdir("benchmarks")
    if "OPENBLAS_CORETYPE" in os.environ:
        del os.environ['OPENBLAS_CORETYPE']
    os.environ["OPENBLAS_CORETYPE"] = target_arch
    subprocess.run(["printenv", "OPENBLAS_CORETYPE"])
    if benchmark_name is not None:
        subprocess.run(["asv", "run", "--show-stderr", "--python", "same",
                        "--bench", benchmark_name, "--set-commit-hash",
                        commit_hash])
    else:
        subprocess.run(["asv", "run", "--show-stderr", "--python", "same",
                        "--set-commit-hash", commit_hash])
    target_dir = "{}/{}".format(
        dest_dir, generate_target_dir_name(
            commit_hash, target_arch, benchmark_name)
    )
    os.makedirs(os.path.expanduser(target_dir), exist_ok=True)
    if not os.path.exists("results"):
        raise OSError("results doesn't exist in {}".format(os.getcwd()))
    shutil.copytree("results", os.path.expanduser(target_dir), dirs_exist_ok=True)
    shutil.rmtree("results")
    os.chdir("../")

def run_benchmarks_for_cpu_archs(target_archs, commit_hash, dest_dir, benchmark_name):
    for target_arch in target_archs:
        run_benchmark(target_arch, commit_hash, dest_dir, benchmark_name)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Parse information needed for benchmarking.')
    parser.add_argument('--set-commit-hash', dest='commit_hash', required=True)
    parser.add_argument('--benchmark-name', dest='benchmark_name', default=None)
    parser.add_argument('--hardware', dest='hardware', required=True)
    parser.add_argument('--result-dir', dest='result_dir', required=True)

    args = parser.parse_args()
    run_benchmarks_for_cpu_archs(openblas_target_cpu_archs[args.hardware],
                                 args.commit_hash, args.result_dir, args.benchmark_name)
