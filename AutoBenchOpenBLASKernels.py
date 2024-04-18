import os
import argparse

openblas_target_cpu_archs = {"arm64": ["ARMV8"]}

def run_benchmark(target_arch, commit_hash, dest_dir, benchmark_name=None):
    os.chdir("benchmarks")
    os.environ["OPENBLAS_CORETYPE"] = target_arch
    if benchmark_name is not None:
        os.system("asv run --show-stderr --python=same "
                  "--bench {} --set-commit-hash {}".format(
                      benchmark_name, commit_hash))
    else:
        os.system("asv run --show-stderr --python=same "
                  "--set-commit-hash {}".format(commit_hash))
    target_dir = "{}/results_{}_{}_{}".format(
        dest_dir, commit_hash, target_arch,
        benchmark_name if benchmark_name is not None else ""
    )
    os.system("mkdir -p {}".format(target_dir))
    os.system("cp -r results/* {}/".format(target_dir))
    os.system("rm -rf results/")

def run_benchmarks_for_cpu_archs(target_archs, commit_hash, dest_dir, benchmark_name):
    for target_arch in target_archs:
        run_benchmark(target_arch, commit_hash, dest_dir, benchmark_name)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Parse information needed for benchmarking.')
    parser.add_argument('--set-commit-hash', dest='commit_hash', required=True)
    parser.add_argument('--benchmark-name', dest='benchmark_name', default=None)
    parser.add_argument('--hardware', dest='hardware', required=True)
    parser.add_argument('--dest-dir', dest='dest_dir', required=True)

    args = parser.parse_args()
    run_benchmarks_for_cpu_archs(openblas_target_cpu_archs[args.hardware],
                                 args.commit_hash, args.dest_dir, args.benchmark_name)
