import argparse
import tabulate

def clean_string(str):
    return str.replace(" ", "").replace("\t", "").rstrip("\n")

def read_file(file_path):
    file = open(file_path)
    lines = file.readlines()
    machine_info = lines[0]
    data = {}

    i = 1
    while i < len(lines):
        bench = clean_string(lines[i])
        data[bench] = {}
        i += 3
        while i < len(lines) and clean_string(lines[i]) != "":
            kernel_data = clean_string(lines[i]).split("|")
            kernel = kernel_data[1]
            data[bench][kernel] = {}
            data[bench][kernel]["mean"] = float(kernel_data[2])
            data[bench][kernel]["spread"] = float(kernel_data[3])
            data[bench][kernel]["perf_ratio"] = float(kernel_data[4])
            i += 1
        i += 1

    return data, machine_info

def compare_results(file1, file2, threshold):
    dict1, machine_info1 = read_file(file1)
    dict2, machine_info2 = read_file(file2)
    print("Machine info for file {} is {}".format(file1, machine_info1))
    print("Machine infor for file {} is {}".format(file2, machine_info2))
    for bench in dict1:
        archs = []
        means = []
        spreads = []
        ratios = []
        for kernel in dict1[bench]:
            mean1 = dict1[bench][kernel]["mean"]
            spread1 = dict1[bench][kernel]["spread"]
            perf_ratio1 = dict1[bench][kernel]["perf_ratio"]
            mean2 = dict2[bench][kernel]["mean"]
            spread2 = dict2[bench][kernel]["spread"]
            perf_ratio2 = dict2[bench][kernel]["perf_ratio"]
            if abs(mean2 - mean1)/mean1 > threshold:
                archs.append(kernel)
                means.append((mean1, mean2))
                spreads.append((spread1, spread2))
                ratios.append((perf_ratio1, perf_ratio2))

        if( len(archs) > 0 ):
            print(bench)
            print(tabulate.tabulate({"arch": archs, "mean": means, "spread": spreads, "perf_ratios": ratios},
                                    headers="keys", tablefmt="pipe"))
            print()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Parse information needed for comparing benchmarking results')
    parser.add_argument('--file1', dest='file1', required=True)
    parser.add_argument('--file2', dest='file2', required=True)
    parser.add_argument('--threshold', dest='threshold', default=0.1, type=float)

    args = parser.parse_args()
    compare_results(args.file1, args.file2, args.threshold)
