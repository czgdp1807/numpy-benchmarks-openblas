import os
import argparse
import json
import glob
from utils import generate_target_dir_name, tabulate_simplified_results, openblas_target_cpu_archs

def simplify_benchmark_result(target_arch, commit_hash, result_dir,
                              simplified_results_dir, benchmark_name=None,
                              tabulate=False):
    contents = glob.glob("**/*.json")
    for content in contents:
        if ".json" in content:
            with open(content) as f:
                data = json.load(f)
                if ("commit_hash" not in data or
                    commit_hash != data["commit_hash"]):
                    continue

                result_columns = data["result_columns"]
                params = data["params"]
                results = data["results"]
                simplified_results = {}
                for benchmark in results:
                    q1, q3 = None, None
                    result = dict(zip(result_columns, results[benchmark]))
                    simplified_result = {}
                    if result["result"] is None:
                        simplified_result = {"mean": None, "stats_q_75": None,
                                             "stats_q_25": None, "spread": None,
                                             "params": None}
                        simplified_results[benchmark] = simplified_result
                        continue

                    if len(result["params"]) == 0:
                        simplified_result["mean"] = result["result"][0]
                        q3 = result["stats_q_75"][0]
                        q1 = result["stats_q_25"][0]
                        simplified_result["spread"] = (q3 - q1)/2
                        simplified_result["params"] = []
                    else:
                        simplified_result["params"] = result["params"][0]
                        means = []
                        spreads = []
                        for i in range(len(result["params"][0])):
                            means.append(result["result"][i])
                            q3 = result["stats_q_75"][i]
                            q1 = result["stats_q_25"][i]
                            spreads.append((q3 - q1)/2)
                        simplified_result["mean"] = means
                        simplified_result["spread"] = spreads

                    simplified_results[benchmark] = simplified_result
                simplified_results = {"params": params, "results": simplified_results,
                                      "commit_hash": commit_hash, "benchmark": benchmark_name,
                                      "arch": target_arch}
                if tabulate:
                    print(target_arch)
                    tabulate_simplified_results(simplified_results["results"])
                outfile = open(os.path.expanduser("{}/{}.json".format(
                    simplified_results_dir, generate_target_dir_name(
                    commit_hash, target_arch, benchmark_name))), "w+")
                json.dump(simplified_results, outfile)
                outfile.close()

def simplify_benchmark_results(target_archs, commit_hash, result_dir, benchmark_name, tabulate):
    for target_arch in target_archs:
        simplified_results_dir = "{}/simplified_results".format(result_dir)
        target_dir = os.path.expanduser("{}/{}".format(
            result_dir,
            generate_target_dir_name(commit_hash, target_arch, benchmark_name)
        ))
        os.chdir(target_dir)
        os.system("mkdir -p {}".format(simplified_results_dir))
        simplify_benchmark_result(target_arch, commit_hash, result_dir,
                                  simplified_results_dir, benchmark_name,
                                  tabulate)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Parse information needed for benchmarking.')
    parser.add_argument('--set-commit-hash', dest='commit_hash', required=True)
    parser.add_argument('--benchmark-name', dest='benchmark_name', default=None)
    parser.add_argument('--hardware', dest='hardware', required=True)
    parser.add_argument('--result-dir', dest='result_dir', required=True)
    parser.add_argument('--tabulate', dest='tabulate', required=False, default=False)

    args = parser.parse_args()
    simplify_benchmark_results(openblas_target_cpu_archs[args.hardware],
                               args.commit_hash, args.result_dir,
                               args.benchmark_name, args.tabulate)
