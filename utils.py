import tabulate

openblas_target_cpu_archs = {"arm64": [
"ARMV8",
"CORTEXA53",
"CORTEXA57",
"CORTEXA72",
"CORTEXA73",
"CORTEXA76",
"CORTEXA510",
"CORTEXA710",
"CORTEXX1",
"CORTEXX2",
"NEOVERSEN1",
"NEOVERSEV1",
"NEOVERSEN2",
"CORTEXA55",
"EMAG8180",
"FALKOR",
"THUNDERX",
"THUNDERX2T99",
"TSV110",
"THUNDERX3T110",
"VORTEX",
"A64FX",
"ARMV8SVE",
"FT2000"
],

"x86_64": ["P2",
"KATMAI",
"COPPERMINE",
"NORTHWOOD",
"PRESCOTT",
"BANIAS",
"YONAH",
"CORE2",
"PENRYN",
"DUNNINGTON",
"NEHALEM",
"SANDYBRIDGE",
"HASWELL",
"SKYLAKEX",
"ATOM",
"COOPERLAKE",
"SAPPHIRERAPIDS"]}

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
