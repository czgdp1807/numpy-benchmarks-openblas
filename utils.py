def generate_target_dir_name(commit_hash, target_arch, benchmark_name):
    return "results_{}_{}_{}".format(
        commit_hash, target_arch,
        benchmark_name if benchmark_name is not None else ""
    )
