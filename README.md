## About

This repository contains scripts for automatically benchmarking several CPU architectures supported by OpenBLAS simultaneously.

It will also contain scripts for analysing the resulting benchmarking data.

## Sample Usages

```zsh
(numpy-dev) 0:41:55:~/Quansight/numpy % python ../numpy-benchmarks-openblas/AutoBenchOpenBLASKernels.py --set-commit-hash=fd3a52b57d64ad9fb5dc4cc8bf3fe0a72da98286 --benchmark-name=bench_linalg.LinAlgTransposeVdot.time_vdot --hardware=arm64 --dest-dir=~/Quansight/numpy_benchmark_results
Couldn't load asv.plugins._mamba_helpers because
No module named 'libmambapy'
· Discovering benchmarks
· Running 1 total benchmarks (1 commits * 1 environments * 1 benchmarks)
[ 0.00%] · For numpy commit fd3a52b5 <main>:
[ 0.00%] ·· Building for existing-py_Users_czgdp1807_mambaforge_envs_numpy-dev_bin_python3.1
[ 0.00%] ·· Benchmarking existing-py_Users_czgdp1807_mambaforge_envs_numpy-dev_bin_python3.1
[50.00%] ··· Running (bench_linalg.LinAlgTransposeVdot.time_vdot--).
[100.00%] ··· bench_linalg.LinAlgTransposeVdot.time_vdot                               ok
[100.00%] ··· ========== ============ =============
                shape      npdtypes
              ---------- ------------ -------------
               (16, 16)     int16        505±2ns
               (16, 16)    float16       934±4ns
               (16, 16)     int32       506±0.8ns
               (16, 16)    float32       431±1ns
               (16, 16)     int64        503±1ns
               (16, 16)    float64       440±2ns
               (16, 16)   complex64      479±2ns
               (16, 16)   complex128     483±4ns
               (32, 32)     int16        783±4ns
               (32, 32)    float16     2.51±0.01μs
               (32, 32)     int32        778±6ns
               (32, 32)    float32       506±4ns
               (32, 32)     int64        781±4ns
               (32, 32)    float64       796±6ns
               (32, 32)   complex64      728±4ns
               (32, 32)   complex128     737±3ns
               (64, 64)     int16      1.77±0.01μs
               (64, 64)    float16     8.65±0.01μs
               (64, 64)     int32        1.78±0μs
               (64, 64)    float32       826±2ns
               (64, 64)     int64        1.77±0μs
               (64, 64)    float64       885±2ns
               (64, 64)   complex64      1.61±0μs
               (64, 64)   complex128   1.85±0.01μs
              ========== ============ =============

[100.00%] ···· For parameters: (16, 16), 'int16'
               NumPy CPU features: NEON NEON_FP16 NEON_VFPV4 ASIMD ASIMDHP* ASIMDFHM?

               For parameters: (16, 16), 'float16'
               NumPy CPU features: NEON NEON_FP16 NEON_VFPV4 ASIMD ASIMDHP* ASIMDFHM?

               For parameters: (16, 16), 'int32'
               NumPy CPU features: NEON NEON_FP16 NEON_VFPV4 ASIMD ASIMDHP* ASIMDFHM?

               For parameters: (16, 16), 'float32'
               NumPy CPU features: NEON NEON_FP16 NEON_VFPV4 ASIMD ASIMDHP* ASIMDFHM?

               For parameters: (16, 16), 'int64'
               NumPy CPU features: NEON NEON_FP16 NEON_VFPV4 ASIMD ASIMDHP* ASIMDFHM?

               For parameters: (16, 16), 'float64'
               NumPy CPU features: NEON NEON_FP16 NEON_VFPV4 ASIMD ASIMDHP* ASIMDFHM?

               For parameters: (16, 16), 'complex64'
               NumPy CPU features: NEON NEON_FP16 NEON_VFPV4 ASIMD ASIMDHP* ASIMDFHM?

               For parameters: (16, 16), 'complex128'
               NumPy CPU features: NEON NEON_FP16 NEON_VFPV4 ASIMD ASIMDHP* ASIMDFHM?

               For parameters: (32, 32), 'int16'
               NumPy CPU features: NEON NEON_FP16 NEON_VFPV4 ASIMD ASIMDHP* ASIMDFHM?

               For parameters: (32, 32), 'float16'
               NumPy CPU features: NEON NEON_FP16 NEON_VFPV4 ASIMD ASIMDHP* ASIMDFHM?

               For parameters: (32, 32), 'int32'
               NumPy CPU features: NEON NEON_FP16 NEON_VFPV4 ASIMD ASIMDHP* ASIMDFHM?

               For parameters: (32, 32), 'float32'
               NumPy CPU features: NEON NEON_FP16 NEON_VFPV4 ASIMD ASIMDHP* ASIMDFHM?

               For parameters: (32, 32), 'int64'
               NumPy CPU features: NEON NEON_FP16 NEON_VFPV4 ASIMD ASIMDHP* ASIMDFHM?

               For parameters: (32, 32), 'float64'
               NumPy CPU features: NEON NEON_FP16 NEON_VFPV4 ASIMD ASIMDHP* ASIMDFHM?

               For parameters: (32, 32), 'complex64'
               NumPy CPU features: NEON NEON_FP16 NEON_VFPV4 ASIMD ASIMDHP* ASIMDFHM?

               For parameters: (32, 32), 'complex128'
               NumPy CPU features: NEON NEON_FP16 NEON_VFPV4 ASIMD ASIMDHP* ASIMDFHM?

               For parameters: (64, 64), 'int16'
               NumPy CPU features: NEON NEON_FP16 NEON_VFPV4 ASIMD ASIMDHP* ASIMDFHM?

               For parameters: (64, 64), 'float16'
               NumPy CPU features: NEON NEON_FP16 NEON_VFPV4 ASIMD ASIMDHP* ASIMDFHM?

               For parameters: (64, 64), 'int32'
               NumPy CPU features: NEON NEON_FP16 NEON_VFPV4 ASIMD ASIMDHP* ASIMDFHM?

               For parameters: (64, 64), 'float32'
               NumPy CPU features: NEON NEON_FP16 NEON_VFPV4 ASIMD ASIMDHP* ASIMDFHM?

               For parameters: (64, 64), 'int64'
               NumPy CPU features: NEON NEON_FP16 NEON_VFPV4 ASIMD ASIMDHP* ASIMDFHM?

               For parameters: (64, 64), 'float64'
               NumPy CPU features: NEON NEON_FP16 NEON_VFPV4 ASIMD ASIMDHP* ASIMDFHM?

               For parameters: (64, 64), 'complex64'
               NumPy CPU features: NEON NEON_FP16 NEON_VFPV4 ASIMD ASIMDHP* ASIMDFHM?

               For parameters: (64, 64), 'complex128'
               NumPy CPU features: NEON NEON_FP16 NEON_VFPV4 ASIMD ASIMDHP* ASIMDFHM?
```
