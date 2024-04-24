import tabulate

openblas_target_cpu_archs = {"arm64": ["ARMV8", "CORTEXA53", "FT2000"]}

def generate_target_dir_name(commit_hash, target_arch, benchmark_name):
    return "results_{}_{}_{}".format(
        commit_hash, target_arch,
        benchmark_name if benchmark_name is not None else ""
    )

def tabulate_simplified_results(simplified_results):
    for benchmark in simplified_results:
        result = simplified_results[benchmark]
        means = result["mean"]
        spreads = result["spread"]
        params = result["params"]
        print(benchmark)
        if len(params) == 0:
            print(tabulate.tabulate({"mean": [means], "spread": [spreads]},
                                    headers="keys", tablefmt="pipe"))
        else:
            print(tabulate.tabulate(result, headers="keys", tablefmt="pipe"))
        print()
