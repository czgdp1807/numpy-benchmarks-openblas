import os
import argparse
import json
import tabulate
from utils import generate_target_dir_name, openblas_target_cpu_archs

def tabulate_results(benchmarkparams2archtimes):
    for benchmark in benchmarkparams2archtimes:
        print(benchmark)
        means, spreads, archs = [], [], []
        for mean, spread, arch in benchmarkparams2archtimes[benchmark]:
            means.append(mean)
            spreads.append(spread)
            archs.append(arch)
        combined = sorted(zip(means, spreads, archs))
        means = [mean for mean, _, _ in combined]
        spreads = [spread for _, spread, _ in combined]
        archs = [arch for _, _, arch in combined]
        ratios = [mean/means[0] for mean in means]
        print(tabulate.tabulate({"arch": archs, "mean": means, "spread": spreads, "perf_ratios": ratios},
                                headers="keys", tablefmt="pipe"))
        print()

def process_simplified_benchmark_results(target_archs, commit_hash, result_dir, benchmark_name, presentation):
    arch2benchdata = []
    for target_arch in target_archs:
        simplified_results_dir = os.path.expanduser("{}/simplified_results".format(result_dir))
        os.chdir(simplified_results_dir)
        filename = "{}/{}.json".format(
            simplified_results_dir,
            generate_target_dir_name(commit_hash, target_arch, benchmark_name)
        )
        with open(filename) as f:
            arch2benchdata.append(json.load(f))

    benchmarks = arch2benchdata[0]["results"].keys()
    benchmarkparams2archtimes = {}
    for benchdata in arch2benchdata:
        benchdata_results = benchdata["results"]
        for benchmark in benchmarks:
            if len(benchdata_results[benchmark]["params"]) > 0:
                for i in range(len(benchdata_results[benchmark]["params"])):
                    param = benchdata_results[benchmark]["params"][i]
                    if (benchmark, param) not in benchmarkparams2archtimes:
                        benchmarkparams2archtimes[(benchmark, param)] = []
                    benchmarkparams2archtimes[(benchmark, param)].append((
                        benchdata_results[benchmark]["mean"][i],
                        benchdata_results[benchmark]["spread"][i],
                        benchdata["arch"])
                    )
            else:
                if benchmark not in benchmarkparams2archtimes:
                    benchmarkparams2archtimes[benchmark] = []
                benchmarkparams2archtimes[benchmark].append((
                    benchdata_results[benchmark]["mean"],
                    benchdata_results[benchmark]["spread"],
                    benchdata["arch"])
                )

    if presentation == "table":
        tabulate_results(benchmarkparams2archtimes)
    else:
        raise ValueError("{} is not supported.".format(presentation))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Parse information needed for benchmarking.')
    parser.add_argument('--set-commit-hash', dest='commit_hash', required=True)
    parser.add_argument('--benchmark-name', dest='benchmark_name', default=None)
    parser.add_argument('--hardware', dest='hardware', required=True)
    parser.add_argument('--result-dir', dest='result_dir', required=True)
    parser.add_argument('--presentation', dest='presentation', required=False, default="table")

    args = parser.parse_args()
    process_simplified_benchmark_results(
        openblas_target_cpu_archs[args.hardware], args.commit_hash, args.result_dir,
        args.benchmark_name, args.presentation
    )
