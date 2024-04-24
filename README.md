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

```zsh
(numpy-dev) 19:04:24:~/Quansight/numpy % python ../numpy-benchmarks-openblas/SimplifyASVBenchmarkResults.py --set-commit-hash=fd3a52b57d64ad9fb5dc4cc8bf3fe0a72da98286 --benchmark-name=bench_linalg --hardware=arm64 --result-dir=~/Quansight/numpy_benchmark_results --tabulate=true
ARMV8
bench_linalg.Eindot.time_dot_a_b
|        mean |   spread |
|------------:|---------:|
| 0.000127032 | 2.61e-06 |

bench_linalg.Eindot.time_dot_d_dot_b_c
|       mean |   spread |
|-----------:|---------:|
| 1.1585e-05 | 4.75e-08 |

bench_linalg.Eindot.time_dot_trans_a_at
|        mean |     spread |
|------------:|-----------:|
| 5.36265e-05 | 5.2045e-06 |

bench_linalg.Eindot.time_dot_trans_a_atc
|        mean |    spread |
|------------:|----------:|
| 6.34866e-05 | 3.326e-06 |

bench_linalg.Eindot.time_dot_trans_at_a
|        mean |   spread |
|------------:|---------:|
| 0.000135415 |  5.1e-07 |

bench_linalg.Eindot.time_dot_trans_atc_a
|        mean |    spread |
|------------:|----------:|
| 9.41447e-05 | 2.045e-07 |

bench_linalg.Eindot.time_einsum_i_ij_j
|        mean |    spread |
|------------:|----------:|
| 0.000433848 | 2.705e-06 |

bench_linalg.Eindot.time_einsum_ij_jk_a_b
|       mean |    spread |
|-----------:|----------:|
| 0.00519206 | 7.365e-05 |

bench_linalg.Eindot.time_einsum_ijk_jil_kl
|    mean |    spread |
|--------:|----------:|
| 0.02205 | 0.0001735 |

bench_linalg.Eindot.time_inner_trans_a_a
|        mean |    spread |
|------------:|----------:|
| 4.89733e-05 | 4.904e-06 |

bench_linalg.Eindot.time_inner_trans_a_ac
|        mean |     spread |
|------------:|-----------:|
| 8.43557e-05 | 6.6685e-06 |

bench_linalg.Eindot.time_matmul_a_b
|        mean |    spread |
|------------:|----------:|
| 0.000127457 | 4.815e-06 |

bench_linalg.Eindot.time_matmul_d_matmul_b_c
|        mean |    spread |
|------------:|----------:|
| 1.20714e-05 | 1.025e-07 |

bench_linalg.Eindot.time_matmul_trans_a_at
|        mean |     spread |
|------------:|-----------:|
| 4.91696e-05 | 4.8035e-06 |

bench_linalg.Eindot.time_matmul_trans_a_atc
|        mean |   spread |
|------------:|---------:|
| 6.05044e-05 | 1.56e-07 |

bench_linalg.Eindot.time_matmul_trans_at_a
|        mean |   spread |
|------------:|---------:|
| 0.000101885 | 2.85e-07 |

bench_linalg.Eindot.time_matmul_trans_atc_a
|        mean |   spread |
|------------:|---------:|
| 8.73188e-05 | 8.18e-07 |

bench_linalg.Eindot.time_tensordot_a_b_axes_1_0_0_1
|        mean |    spread |
|------------:|----------:|
| 0.000679363 | 5.895e-06 |

bench_linalg.Einsum.time_einsum_contig_contig
| params                  |        mean |    spread |
|:------------------------|------------:|----------:|
| <class 'numpy.float32'> | 4.72113e-05 | 1.175e-07 |
| <class 'numpy.float64'> | 0.000100592 | 1.6e-07   |

bench_linalg.Einsum.time_einsum_contig_outstride0
| params                  |        mean |    spread |
|:------------------------|------------:|----------:|
| <class 'numpy.float32'> | 3.35476e-05 | 3.85e-07  |
| <class 'numpy.float64'> | 6.02525e-05 | 7.125e-07 |

bench_linalg.Einsum.time_einsum_mul
| params                  |        mean |    spread |
|:------------------------|------------:|----------:|
| <class 'numpy.float32'> | 0.000439823 | 2.7e-05   |
| <class 'numpy.float64'> | 0.000263899 | 2.365e-06 |

bench_linalg.Einsum.time_einsum_multiply
| params                  |        mean |    spread |
|:------------------------|------------:|----------:|
| <class 'numpy.float32'> | 1.61506e-05 | 3.655e-07 |
| <class 'numpy.float64'> | 1.99633e-05 | 1.685e-07 |

bench_linalg.Einsum.time_einsum_noncon_contig_contig
| params                  |        mean |    spread |
|:------------------------|------------:|----------:|
| <class 'numpy.float32'> | 8.32946e-06 | 9.105e-08 |
| <class 'numpy.float64'> | 8.21808e-06 | 7.475e-08 |

bench_linalg.Einsum.time_einsum_noncon_contig_outstride0
| params                  |        mean |    spread |
|:------------------------|------------:|----------:|
| <class 'numpy.float32'> | 6.41034e-06 | 1.395e-08 |
| <class 'numpy.float64'> | 6.51005e-06 | 6.485e-08 |

bench_linalg.Einsum.time_einsum_noncon_mul
| params                  |        mean |     spread |
|:------------------------|------------:|-----------:|
| <class 'numpy.float32'> | 8.92866e-06 | 1.3895e-07 |
| <class 'numpy.float64'> | 8.09395e-06 | 2.82e-08   |

bench_linalg.Einsum.time_einsum_noncon_multiply
| params                  |        mean |    spread |
|:------------------------|------------:|----------:|
| <class 'numpy.float32'> | 1.62053e-05 | 6.8e-08   |
| <class 'numpy.float64'> | 1.99836e-05 | 1.955e-07 |

bench_linalg.Einsum.time_einsum_noncon_outer
| params                  |        mean |   spread |
|:------------------------|------------:|---------:|
| <class 'numpy.float32'> | 0.000536091 | 2.91e-06 |
| <class 'numpy.float64'> | 0.00265263  | 9.47e-05 |

bench_linalg.Einsum.time_einsum_noncon_sum_mul
| params                  |        mean |   spread |
|:------------------------|------------:|---------:|
| <class 'numpy.float32'> | 2.08999e-05 | 2.68e-07 |
| <class 'numpy.float64'> | 1.3323e-05  | 7.6e-08  |

bench_linalg.Einsum.time_einsum_noncon_sum_mul2
| params                  |        mean |    spread |
|:------------------------|------------:|----------:|
| <class 'numpy.float32'> | 2.05439e-05 | 3.33e-07  |
| <class 'numpy.float64'> | 1.32561e-05 | 1.465e-07 |

bench_linalg.Einsum.time_einsum_outer
| params                  |       mean |     spread |
|:------------------------|-----------:|-----------:|
| <class 'numpy.float32'> | 0.00306083 | 5.99e-05   |
| <class 'numpy.float64'> | 0.00665838 | 0.00016355 |

bench_linalg.Einsum.time_einsum_sum_mul
| params                  |        mean |    spread |
|:------------------------|------------:|----------:|
| <class 'numpy.float32'> | 1.49147e-05 | 2.28e-07  |
| <class 'numpy.float64'> | 1.16379e-05 | 1.145e-07 |

bench_linalg.Einsum.time_einsum_sum_mul2
| params                  |        mean |    spread |
|:------------------------|------------:|----------:|
| <class 'numpy.float32'> | 1.49472e-05 | 1.265e-07 |
| <class 'numpy.float64'> | 1.17721e-05 | 8.25e-08  |

bench_linalg.LinAlgTransposeVdot.time_transpose
| params   |        mean |   spread |
|:---------|------------:|---------:|
| (16, 16) | 3.23066e-07 | 2.54e-09 |
| (32, 32) | 3.28386e-07 | 2.64e-09 |
| (64, 64) | 3.23366e-07 | 1.82e-09 |

bench_linalg.LinAlgTransposeVdot.time_vdot
| params   |        mean |    spread |
|:---------|------------:|----------:|
| (16, 16) | 5.13215e-07 | 7.76e-09  |
| (32, 32) | 9.35687e-07 | 9.915e-09 |
| (64, 64) | 5.16996e-07 | 5.77e-09  |

bench_linalg.Linalg.time_det
| params       |        mean |      spread |
|:-------------|------------:|------------:|
| 'int16'      | 4.09088e-05 | 1.7e-07     |
| 'int32'      | 4.05766e-05 | 6.1e-08     |
| 'complex64'  | 0.000220689 | 9.5e-07     |
| 'int64'      | 0.000130261 | 8.89105e-05 |
| 'float32'    | 4.11208e-05 | 1.1e-07     |
| 'float64'    | 0.000130335 | 8.94795e-05 |
| 'complex128' | 4.11316e-05 | 2.76e-07    |

bench_linalg.Linalg.time_pinv
| params       |        mean |     spread |
|:-------------|------------:|-----------:|
| 'int16'      | 0.00183497  | 0.00089168 |
| 'int32'      | 0.0017369   | 0.00081767 |
| 'complex64'  | 0.000949759 | 6.045e-06  |
| 'int64'      | 0.000951337 | 6.355e-06  |
| 'float32'    | 0.000950004 | 5.305e-06  |
| 'float64'    | 0.000959481 | 1.41e-05   |
| 'complex128' | 0.000938078 | 5.095e-06  |

bench_linalg.Linalg.time_svd
| params       |        mean |      spread |
|:-------------|------------:|------------:|
| 'int16'      | 0.000920566 | 9.765e-06   |
| 'int32'      | 0.0018577   | 0.00095652  |
| 'complex64'  | 0.000914955 | 1.6275e-05  |
| 'int64'      | 0.000929979 | 9.455e-06   |
| 'float32'    | 0.00188807  | 0.000959465 |
| 'float64'    | 0.000918418 | 5.945e-06   |
| 'complex128' | 0.000920646 | 1.2075e-05  |

bench_linalg.LinalgNorm.time_norm
| params       |        mean |     spread |
|:-------------|------------:|-----------:|
| 'int16'      | 7.16217e-06 | 3.6475e-07 |
| 'float16'    | 2.22543e-05 | 9.65e-08   |
| 'int32'      | 6.86726e-06 | 4.565e-08  |
| 'float32'    | 4.44147e-06 | 1.94e-08   |
| 'int64'      | 7.31443e-06 | 7.115e-08  |
| 'float64'    | 5.67427e-06 | 4.07e-08   |
| 'complex64'  | 1.00761e-05 | 1.3755e-07 |
| 'complex128' | 1.22716e-05 | 5.2e-08    |

bench_linalg.LinalgSmallArrays.time_det_small_array
|        mean |   spread |
|------------:|---------:|
| 1.55722e-06 | 6.35e-09 |

bench_linalg.LinalgSmallArrays.time_norm_small_array
|        mean |   spread |
|------------:|---------:|
| 9.30947e-07 |  6.8e-09 |

bench_linalg.Lstsq.time_numpy_linalg_lstsq_a__b_float64
|        mean |    spread |
|------------:|----------:|
| 0.000840373 | 2.135e-06 |
```
