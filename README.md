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

```zsh
(numpy-dev) 11:59:55:~/Quansight/numpy % python ../numpy-benchmarks-openblas/CompareSimplifiedBenchmarkResults.py --set-commit-hash=fd3a52b57d64ad9fb5dc4cc8bf3fe0a72da98286 --benchmark-name=bench_linalg --hardware=arm64 --result-dir=~/Quansight/numpy_benchmark_results
bench_linalg.Eindot.time_dot_a_b
| arch          |        mean |     spread |   perf_ratios |
|:--------------|------------:|-----------:|--------------:|
| FT2000        | 0.000126383 | 1.985e-06  |       1       |
| ARMV8         | 0.000126519 | 1.775e-06  |       1.00108 |
| CORTEXX2      | 0.000127241 | 1.535e-06  |       1.00679 |
| NEOVERSEV1    | 0.000128012 | 4.06e-06   |       1.0129  |
| CORTEXA53     | 0.000129011 | 4.395e-06  |       1.0208  |
| FALKOR        | 0.000129234 | 4.155e-06  |       1.02256 |
| VORTEX        | 0.000129351 | 1.275e-06  |       1.02348 |
| CORTEXX1      | 0.000129417 | 2.98e-06   |       1.02401 |
| ARMV8SVE      | 0.000129449 | 6.48e-06   |       1.02427 |
| CORTEXA73     | 0.000129482 | 4.11e-06   |       1.02452 |
| CORTEXA72     | 0.000129848 | 6.115e-06  |       1.02742 |
| A64FX         | 0.000130168 | 3.615e-06  |       1.02995 |
| THUNDERX      | 0.00013017  | 3.115e-06  |       1.02997 |
| CORTEXA510    | 0.000130261 | 6.115e-06  |       1.03069 |
| CORTEXA57     | 0.000130721 | 6.805e-06  |       1.03433 |
| EMAG8180      | 0.000130804 | 1.805e-06  |       1.03499 |
| CORTEXA710    | 0.000131255 | 4.585e-06  |       1.03855 |
| THUNDERX2T99  | 0.00013219  | 5.21e-06   |       1.04595 |
| CORTEXA76     | 0.00013363  | 7.1e-06    |       1.05735 |
| TSV110        | 0.000134783 | 6.95e-06   |       1.06646 |
| THUNDERX3T110 | 0.00013498  | 4.365e-06  |       1.06803 |
| NEOVERSEN2    | 0.000137062 | 6.015e-06  |       1.0845  |
| CORTEXA55     | 0.00013783  | 4.505e-06  |       1.09058 |
| NEOVERSEN1    | 0.000139126 | 1.2945e-05 |       1.10083 |

bench_linalg.Eindot.time_dot_d_dot_b_c
| arch          |        mean |    spread |   perf_ratios |
|:--------------|------------:|----------:|--------------:|
| ARMV8         | 1.143e-05   | 8.75e-08  |       1       |
| NEOVERSEN2    | 1.14565e-05 | 2.7e-08   |       1.00232 |
| CORTEXX1      | 1.14724e-05 | 7.55e-08  |       1.00371 |
| CORTEXA53     | 1.14946e-05 | 5.9e-08   |       1.00566 |
| CORTEXA710    | 1.14992e-05 | 1.005e-07 |       1.00606 |
| THUNDERX3T110 | 1.15006e-05 | 1.255e-07 |       1.00618 |
| CORTEXA76     | 1.15123e-05 | 7.2e-08   |       1.0072  |
| NEOVERSEV1    | 1.15244e-05 | 9.25e-08  |       1.00826 |
| THUNDERX2T99  | 1.15309e-05 | 5e-08     |       1.00883 |
| CORTEXA57     | 1.15385e-05 | 8.55e-08  |       1.00949 |
| THUNDERX      | 1.15493e-05 | 3.85e-08  |       1.01044 |
| A64FX         | 1.15762e-05 | 4.65e-08  |       1.01279 |
| CORTEXA73     | 1.15813e-05 | 8.7e-08   |       1.01324 |
| CORTEXA72     | 1.15885e-05 | 8.85e-08  |       1.01387 |
| VORTEX        | 1.15905e-05 | 6.1e-08   |       1.01404 |
| ARMV8SVE      | 1.15917e-05 | 1.035e-07 |       1.01414 |
| FT2000        | 1.15939e-05 | 1.065e-07 |       1.01434 |
| FALKOR        | 1.15948e-05 | 7.15e-08  |       1.01442 |
| CORTEXA55     | 1.15995e-05 | 4.7e-08   |       1.01483 |
| CORTEXX2      | 1.16019e-05 | 1.02e-07  |       1.01504 |
| EMAG8180      | 1.1605e-05  | 6.95e-08  |       1.01531 |
| NEOVERSEN1    | 1.16431e-05 | 9.25e-08  |       1.01864 |
| CORTEXA510    | 1.16533e-05 | 6.65e-08  |       1.01954 |
| TSV110        | 1.17019e-05 | 1.06e-07  |       1.02379 |

bench_linalg.Eindot.time_dot_trans_a_at
| arch          |        mean |     spread |   perf_ratios |
|:--------------|------------:|-----------:|--------------:|
| FT2000        | 4.84195e-05 | 6.1475e-06 |       1       |
| EMAG8180      | 4.87134e-05 | 3.6535e-06 |       1.00607 |
| FALKOR        | 4.87207e-05 | 3.5615e-06 |       1.00622 |
| CORTEXA710    | 4.87281e-05 | 3.49e-06   |       1.00637 |
| CORTEXX2      | 4.87313e-05 | 3.668e-06  |       1.00644 |
| NEOVERSEV1    | 4.87479e-05 | 4.793e-06  |       1.00678 |
| A64FX         | 4.87884e-05 | 3.759e-06  |       1.00762 |
| CORTEXA53     | 4.881e-05   | 4.744e-06  |       1.00806 |
| CORTEXA57     | 4.88101e-05 | 5.882e-06  |       1.00807 |
| VORTEX        | 4.88223e-05 | 3.8485e-06 |       1.00832 |
| NEOVERSEN2    | 4.88542e-05 | 4.719e-06  |       1.00898 |
| CORTEXA510    | 4.89062e-05 | 5.042e-06  |       1.01005 |
| THUNDERX      | 4.90482e-05 | 4.114e-06  |       1.01298 |
| THUNDERX3T110 | 4.97052e-05 | 4.0585e-06 |       1.02655 |
| CORTEXX1      | 5.01721e-05 | 6.515e-06  |       1.0362  |
| CORTEXA55     | 5.03763e-05 | 4.2025e-06 |       1.04041 |
| CORTEXA76     | 5.2469e-05  | 4.7015e-06 |       1.08363 |
| CORTEXA72     | 5.34437e-05 | 4.8975e-06 |       1.10376 |
| ARMV8         | 5.38171e-05 | 5.3825e-06 |       1.11147 |
| ARMV8SVE      | 5.41702e-05 | 6.163e-06  |       1.11877 |
| CORTEXA73     | 5.52596e-05 | 6.5275e-06 |       1.14127 |
| TSV110        | 5.68936e-05 | 2.8575e-06 |       1.17501 |
| THUNDERX2T99  | 5.85284e-05 | 5.1455e-06 |       1.20878 |
| NEOVERSEN1    | 5.85324e-05 | 5.437e-06  |       1.20886 |

bench_linalg.Eindot.time_dot_trans_a_atc
| arch          |        mean |     spread |   perf_ratios |
|:--------------|------------:|-----------:|--------------:|
| CORTEXX2      | 6.11591e-05 | 2.115e-07  |       1       |
| FALKOR        | 6.12421e-05 | 9.45e-08   |       1.00136 |
| EMAG8180      | 6.13264e-05 | 2.265e-07  |       1.00274 |
| NEOVERSEN1    | 6.14112e-05 | 1.07e-07   |       1.00412 |
| CORTEXA72     | 6.14177e-05 | 1.77e-07   |       1.00423 |
| A64FX         | 6.14271e-05 | 1.64e-07   |       1.00438 |
| THUNDERX2T99  | 6.1443e-05  | 3.45e-07   |       1.00464 |
| ARMV8         | 6.14469e-05 | 2.81e-07   |       1.00471 |
| VORTEX        | 6.14717e-05 | 2.515e-07  |       1.00511 |
| ARMV8SVE      | 6.15092e-05 | 1.01e-07   |       1.00573 |
| TSV110        | 6.15263e-05 | 1.0755e-06 |       1.006   |
| CORTEXA53     | 6.15409e-05 | 2.565e-07  |       1.00624 |
| NEOVERSEV1    | 6.15612e-05 | 8.75e-08   |       1.00657 |
| FT2000        | 6.15697e-05 | 2.26e-07   |       1.00671 |
| CORTEXA57     | 6.15774e-05 | 2.825e-07  |       1.00684 |
| CORTEXA710    | 6.15779e-05 | 5.015e-07  |       1.00685 |
| THUNDERX      | 6.16109e-05 | 2.51e-07   |       1.00739 |
| NEOVERSEN2    | 6.1621e-05  | 2.45e-07   |       1.00755 |
| THUNDERX3T110 | 6.17886e-05 | 8.19e-07   |       1.01029 |
| CORTEXA55     | 6.17908e-05 | 2.525e-07  |       1.01033 |
| CORTEXA76     | 6.20655e-05 | 1.0825e-06 |       1.01482 |
| CORTEXA510    | 6.24135e-05 | 2.4525e-06 |       1.02051 |
| CORTEXA73     | 6.29174e-05 | 1.4295e-06 |       1.02875 |
| CORTEXX1      | 7.24757e-05 | 1.0258e-05 |       1.18503 |

bench_linalg.Eindot.time_dot_trans_at_a
| arch          |        mean |    spread |   perf_ratios |
|:--------------|------------:|----------:|--------------:|
| ARMV8         | 0.000135008 | 4e-07     |       1       |
| NEOVERSEN2    | 0.000135017 | 3.05e-07  |       1.00007 |
| CORTEXX1      | 0.000135226 | 1.25e-06  |       1.00162 |
| CORTEXX2      | 0.000135234 | 4.95e-07  |       1.00167 |
| THUNDERX2T99  | 0.000135501 | 6.3e-07   |       1.00366 |
| NEOVERSEN1    | 0.000135535 | 2.95e-07  |       1.00391 |
| CORTEXA72     | 0.000135597 | 7.7e-07   |       1.00436 |
| CORTEXA53     | 0.000135621 | 8.05e-07  |       1.00454 |
| THUNDERX3T110 | 0.000135639 | 5.95e-07  |       1.00467 |
| FT2000        | 0.000135652 | 4.95e-07  |       1.00477 |
| CORTEXA510    | 0.000135665 | 3.75e-07  |       1.00487 |
| TSV110        | 0.000135728 | 8.3e-07   |       1.00533 |
| ARMV8SVE      | 0.000135771 | 6.65e-07  |       1.00565 |
| CORTEXA55     | 0.000135845 | 7.8e-07   |       1.0062  |
| CORTEXA710    | 0.000135853 | 1.105e-06 |       1.00626 |
| THUNDERX      | 0.000135889 | 5.3e-07   |       1.00653 |
| CORTEXA57     | 0.000135902 | 5.95e-07  |       1.00663 |
| A64FX         | 0.000135963 | 6.3e-07   |       1.00707 |
| EMAG8180      | 0.000136066 | 7.3e-07   |       1.00784 |
| NEOVERSEV1    | 0.000136097 | 4.65e-07  |       1.00806 |
| VORTEX        | 0.000136319 | 1.315e-06 |       1.00971 |
| FALKOR        | 0.00013644  | 6.2e-07   |       1.01061 |
| CORTEXA73     | 0.000137106 | 1.985e-06 |       1.01554 |
| CORTEXA76     | 0.000137914 | 1.395e-06 |       1.02152 |

bench_linalg.Eindot.time_dot_trans_atc_a
| arch          |        mean |     spread |   perf_ratios |
|:--------------|------------:|-----------:|--------------:|
| CORTEXA710    | 9.38967e-05 | 2.22e-07   |       1       |
| NEOVERSEV1    | 9.42142e-05 | 6.94e-07   |       1.00338 |
| CORTEXX2      | 9.42234e-05 | 6.635e-07  |       1.00348 |
| CORTEXX1      | 9.42841e-05 | 1.501e-06  |       1.00413 |
| NEOVERSEN2    | 9.4321e-05  | 1.3595e-06 |       1.00452 |
| EMAG8180      | 9.44321e-05 | 1.058e-06  |       1.0057  |
| CORTEXA53     | 9.44917e-05 | 9.115e-07  |       1.00634 |
| FT2000        | 9.45327e-05 | 1.1245e-06 |       1.00677 |
| A64FX         | 9.4608e-05  | 1.056e-06  |       1.00757 |
| CORTEXA55     | 9.47074e-05 | 1.501e-06  |       1.00863 |
| FALKOR        | 9.48969e-05 | 7.74e-07   |       1.01065 |
| CORTEXA57     | 9.51051e-05 | 8.495e-07  |       1.01287 |
| TSV110        | 9.51402e-05 | 2.4045e-06 |       1.01324 |
| VORTEX        | 9.52496e-05 | 1.092e-06  |       1.01441 |
| ARMV8SVE      | 9.53757e-05 | 1.8395e-06 |       1.01575 |
| THUNDERX      | 9.55042e-05 | 1.2325e-06 |       1.01712 |
| THUNDERX2T99  | 9.55902e-05 | 1.182e-06  |       1.01803 |
| CORTEXA510    | 9.57051e-05 | 1.313e-06  |       1.01926 |
| ARMV8         | 9.57144e-05 | 1.696e-06  |       1.01936 |
| THUNDERX3T110 | 9.57191e-05 | 1.1075e-06 |       1.01941 |
| CORTEXA73     | 9.5775e-05  | 1.375e-06  |       1.02    |
| CORTEXA76     | 9.67852e-05 | 1.8615e-06 |       1.03076 |
| CORTEXA72     | 9.71303e-05 | 2.385e-06  |       1.03444 |
| NEOVERSEN1    | 9.88317e-05 | 4.6345e-06 |       1.05256 |

bench_linalg.Eindot.time_einsum_i_ij_j
| arch          |        mean |    spread |   perf_ratios |
|:--------------|------------:|----------:|--------------:|
| ARMV8         | 0.000436666 | 1.745e-06 |       1       |
| NEOVERSEN2    | 0.000445718 | 5.2e-07   |       1.02073 |
| CORTEXA73     | 0.000446043 | 3.12e-06  |       1.02148 |
| ARMV8SVE      | 0.000446129 | 1.165e-06 |       1.02167 |
| CORTEXX2      | 0.000446334 | 1.54e-06  |       1.02214 |
| FT2000        | 0.000446458 | 2.53e-06  |       1.02243 |
| EMAG8180      | 0.000446711 | 1.15e-06  |       1.023   |
| VORTEX        | 0.000446841 | 1.89e-06  |       1.0233  |
| CORTEXA53     | 0.00044708  | 1.705e-06 |       1.02385 |
| CORTEXA72     | 0.000447447 | 4.14e-06  |       1.02469 |
| NEOVERSEN1    | 0.000447468 | 1.61e-06  |       1.02474 |
| CORTEXA510    | 0.000447757 | 1.62e-06  |       1.0254  |
| NEOVERSEV1    | 0.000447845 | 2.11e-06  |       1.0256  |
| FALKOR        | 0.000447895 | 8.2e-07   |       1.02572 |
| CORTEXX1      | 0.000448181 | 2.47e-06  |       1.02637 |
| A64FX         | 0.000448409 | 2.115e-06 |       1.02689 |
| CORTEXA57     | 0.000448579 | 1.5e-06   |       1.02728 |
| THUNDERX      | 0.000448688 | 2.095e-06 |       1.02753 |
| CORTEXA710    | 0.000448913 | 1.315e-06 |       1.02805 |
| CORTEXA55     | 0.000449168 | 2.19e-06  |       1.02863 |
| THUNDERX2T99  | 0.000449273 | 1.76e-06  |       1.02887 |
| CORTEXA76     | 0.000452648 | 2.255e-06 |       1.0366  |
| THUNDERX3T110 | 0.000454591 | 5.435e-06 |       1.04105 |
| TSV110        | 0.00045712  | 9.3e-06   |       1.04684 |

bench_linalg.Eindot.time_einsum_ij_jk_a_b
| arch          |       mean |    spread |   perf_ratios |
|:--------------|-----------:|----------:|--------------:|
| ARMV8         | 0.00520908 | 6.81e-05  |       1       |
| CORTEXX1      | 0.00525007 | 1.3e-05   |       1.00787 |
| CORTEXX2      | 0.00525154 | 6.6e-06   |       1.00815 |
| NEOVERSEV1    | 0.00525265 | 7.55e-06  |       1.00836 |
| CORTEXA710    | 0.00525535 | 8.45e-06  |       1.00888 |
| NEOVERSEN2    | 0.00525673 | 1.15e-05  |       1.00915 |
| CORTEXA73     | 0.00525923 | 1.34e-05  |       1.00963 |
| THUNDERX2T99  | 0.00526306 | 7.05e-06  |       1.01036 |
| VORTEX        | 0.00526367 | 1.475e-05 |       1.01048 |
| THUNDERX      | 0.00526618 | 1.295e-05 |       1.01096 |
| NEOVERSEN1    | 0.00526779 | 6.05e-06  |       1.01127 |
| TSV110        | 0.00526794 | 1.295e-05 |       1.0113  |
| CORTEXA510    | 0.00526857 | 1.245e-05 |       1.01142 |
| FT2000        | 0.00526889 | 1.545e-05 |       1.01148 |
| ARMV8SVE      | 0.00526918 | 1.395e-05 |       1.01154 |
| A64FX         | 0.00527367 | 1.215e-05 |       1.0124  |
| CORTEXA57     | 0.00527541 | 1.81e-05  |       1.01273 |
| CORTEXA53     | 0.00527767 | 1.35e-05  |       1.01317 |
| CORTEXA72     | 0.00527946 | 1.415e-05 |       1.01351 |
| EMAG8180      | 0.00528309 | 1.4e-05   |       1.01421 |
| FALKOR        | 0.00528753 | 3.105e-05 |       1.01506 |
| CORTEXA76     | 0.00528915 | 2.28e-05  |       1.01537 |
| THUNDERX3T110 | 0.00529267 | 2.05e-05  |       1.01605 |
| CORTEXA55     | 0.00529273 | 1.1e-05   |       1.01606 |

bench_linalg.Eindot.time_einsum_ijk_jil_kl
| arch          |      mean |    spread |   perf_ratios |
|:--------------|----------:|----------:|--------------:|
| ARMV8         | 0.0220866 | 5.4e-05   |       1       |
| CORTEXA710    | 0.0223956 | 0.000194  |       1.01399 |
| VORTEX        | 0.022411  | 0.0001325 |       1.01469 |
| EMAG8180      | 0.0224584 | 6.9e-05   |       1.01683 |
| NEOVERSEV1    | 0.0224914 | 0.000144  |       1.01833 |
| CORTEXX1      | 0.0224922 | 0.0003485 |       1.01837 |
| FALKOR        | 0.0225033 | 0.0002525 |       1.01886 |
| CORTEXA53     | 0.0225067 | 5.75e-05  |       1.01902 |
| CORTEXA510    | 0.0225424 | 0.000118  |       1.02063 |
| CORTEXX2      | 0.0225518 | 0.0001615 |       1.02106 |
| CORTEXA72     | 0.0225622 | 0.000332  |       1.02153 |
| CORTEXA73     | 0.022571  | 0.000142  |       1.02193 |
| ARMV8SVE      | 0.0226161 | 0.0001125 |       1.02397 |
| NEOVERSEN2    | 0.022623  | 4.65e-05  |       1.02429 |
| THUNDERX2T99  | 0.022653  | 0.000224  |       1.02564 |
| CORTEXA76     | 0.0226827 | 0.0003775 |       1.02699 |
| A64FX         | 0.0227236 | 0.0003785 |       1.02884 |
| CORTEXA55     | 0.0227621 | 0.0005415 |       1.03058 |
| THUNDERX      | 0.0227676 | 0.000271  |       1.03083 |
| CORTEXA57     | 0.0227694 | 7.15e-05  |       1.03091 |
| NEOVERSEN1    | 0.0228064 | 9.6e-05   |       1.03259 |
| THUNDERX3T110 | 0.0228919 | 0.000153  |       1.03646 |
| FT2000        | 0.0231016 | 0.0004115 |       1.04595 |
| TSV110        | 0.0231017 | 0.0002895 |       1.04596 |

bench_linalg.Eindot.time_inner_trans_a_a
| arch          |        mean |     spread |   perf_ratios |
|:--------------|------------:|-----------:|--------------:|
| FT2000        | 4.85183e-05 | 4.9755e-06 |       1       |
| ARMV8SVE      | 4.87302e-05 | 3.8725e-06 |       1.00437 |
| ARMV8         | 4.87851e-05 | 3.6085e-06 |       1.0055  |
| CORTEXX2      | 4.88882e-05 | 3.5185e-06 |       1.00762 |
| A64FX         | 4.89334e-05 | 1.325e-07  |       1.00856 |
| CORTEXA53     | 4.89501e-05 | 5.153e-06  |       1.0089  |
| NEOVERSEN2    | 4.8973e-05  | 6.864e-06  |       1.00937 |
| CORTEXA73     | 4.90158e-05 | 5.3775e-06 |       1.01026 |
| CORTEXA76     | 4.90197e-05 | 5.235e-06  |       1.01034 |
| EMAG8180      | 4.90301e-05 | 5.2225e-06 |       1.01055 |
| CORTEXA510    | 4.90517e-05 | 4.8265e-06 |       1.01099 |
| VORTEX        | 4.91492e-05 | 5.3865e-06 |       1.01301 |
| CORTEXX1      | 4.92166e-05 | 3.85e-06   |       1.01439 |
| THUNDERX2T99  | 4.92387e-05 | 5.355e-06  |       1.01485 |
| CORTEXA57     | 4.94666e-05 | 5.141e-06  |       1.01955 |
| TSV110        | 4.98379e-05 | 3.694e-06  |       1.0272  |
| NEOVERSEN1    | 5.15113e-05 | 4.5455e-06 |       1.06169 |
| FALKOR        | 5.25329e-05 | 4.913e-06  |       1.08275 |
| CORTEXA710    | 5.34638e-05 | 4.7995e-06 |       1.10193 |
| CORTEXA72     | 5.57742e-05 | 4.7765e-06 |       1.14955 |
| NEOVERSEV1    | 5.86786e-05 | 5.9425e-06 |       1.20941 |
| THUNDERX      | 5.93714e-05 | 5.685e-06  |       1.22369 |
| CORTEXA55     | 5.99564e-05 | 4.9895e-06 |       1.23575 |
| THUNDERX3T110 | 6.31634e-05 | 7.3175e-06 |       1.30185 |

bench_linalg.Eindot.time_inner_trans_a_ac
| arch          |        mean |     spread |   perf_ratios |
|:--------------|------------:|-----------:|--------------:|
| CORTEXX1      | 7.13865e-05 | 3.055e-07  |       1       |
| CORTEXX2      | 7.14692e-05 | 6.4445e-06 |       1.00116 |
| CORTEXA710    | 7.15984e-05 | 6.5515e-06 |       1.00297 |
| THUNDERX2T99  | 7.15988e-05 | 2.87e-07   |       1.00297 |
| CORTEXA73     | 7.17396e-05 | 4.874e-06  |       1.00495 |
| VORTEX        | 7.19176e-05 | 7.769e-06  |       1.00744 |
| CORTEXA53     | 7.29803e-05 | 6.5475e-06 |       1.02233 |
| CORTEXA510    | 7.95924e-05 | 7.638e-06  |       1.11495 |
| ARMV8         | 8.07374e-05 | 8.1185e-06 |       1.13099 |
| CORTEXA55     | 8.24468e-05 | 8.3475e-06 |       1.15494 |
| NEOVERSEN2    | 8.44559e-05 | 8.8415e-06 |       1.18308 |
| CORTEXA72     | 8.46296e-05 | 8.049e-06  |       1.18551 |
| CORTEXA57     | 8.50215e-05 | 7.1595e-06 |       1.191   |
| NEOVERSEV1    | 8.51258e-05 | 8.3835e-06 |       1.19246 |
| EMAG8180      | 8.51499e-05 | 7.2895e-06 |       1.1928  |
| FALKOR        | 8.54514e-05 | 8.1445e-06 |       1.19702 |
| ARMV8SVE      | 8.55007e-05 | 9.3215e-06 |       1.19771 |
| A64FX         | 8.56989e-05 | 7.352e-06  |       1.20049 |
| FT2000        | 8.57475e-05 | 6.451e-06  |       1.20117 |
| THUNDERX      | 8.60879e-05 | 8.124e-06  |       1.20594 |
| NEOVERSEN1    | 8.62441e-05 | 3.508e-06  |       1.20813 |
| CORTEXA76     | 8.64354e-05 | 5.431e-06  |       1.21081 |
| THUNDERX3T110 | 8.66937e-05 | 6.252e-06  |       1.21443 |
| TSV110        | 0.000101198 | 2.0208e-05 |       1.41761 |

bench_linalg.Eindot.time_matmul_a_b
| arch          |        mean |    spread |   perf_ratios |
|:--------------|------------:|----------:|--------------:|
| A64FX         | 0.000117898 | 6.15e-06  |       1       |
| CORTEXA72     | 0.000118213 | 2.595e-06 |       1.00267 |
| NEOVERSEV1    | 0.000118407 | 2.025e-06 |       1.00432 |
| CORTEXX2      | 0.000118729 | 5.885e-06 |       1.00704 |
| THUNDERX3T110 | 0.000119233 | 1.27e-06  |       1.01132 |
| CORTEXA76     | 0.000119384 | 6.265e-06 |       1.0126  |
| VORTEX        | 0.000119522 | 3.4e-06   |       1.01377 |
| CORTEXA57     | 0.000119713 | 2.605e-06 |       1.01539 |
| FALKOR        | 0.000119759 | 2.8e-06   |       1.01578 |
| CORTEXA55     | 0.000120122 | 3.185e-06 |       1.01886 |
| CORTEXA73     | 0.000120352 | 1.84e-06  |       1.02081 |
| ARMV8SVE      | 0.000120505 | 1.535e-06 |       1.0221  |
| NEOVERSEN2    | 0.000120512 | 2.71e-06  |       1.02217 |
| CORTEXA510    | 0.000120861 | 2.515e-06 |       1.02513 |
| NEOVERSEN1    | 0.000121208 | 5.235e-06 |       1.02807 |
| THUNDERX      | 0.000121328 | 2.875e-06 |       1.02909 |
| CORTEXX1      | 0.000121652 | 3.415e-06 |       1.03183 |
| THUNDERX2T99  | 0.000121776 | 3.34e-06  |       1.03289 |
| CORTEXA710    | 0.000122672 | 3.58e-06  |       1.04049 |
| ARMV8         | 0.000123005 | 1.885e-06 |       1.04331 |
| CORTEXA53     | 0.000123903 | 3.33e-06  |       1.05093 |
| EMAG8180      | 0.00012652  | 3.48e-06  |       1.07312 |
| TSV110        | 0.000126763 | 1.135e-06 |       1.07519 |
| FT2000        | 0.000127643 | 5.58e-06  |       1.08265 |

bench_linalg.Eindot.time_matmul_d_matmul_b_c
| arch          |        mean |    spread |   perf_ratios |
|:--------------|------------:|----------:|--------------:|
| CORTEXA53     | 1.19041e-05 | 3.8e-08   |       1       |
| ARMV8         | 1.19143e-05 | 6.25e-08  |       1.00086 |
| CORTEXX2      | 1.19148e-05 | 5.3e-08   |       1.0009  |
| NEOVERSEV1    | 1.19209e-05 | 5.3e-08   |       1.00141 |
| ARMV8SVE      | 1.19289e-05 | 7.85e-08  |       1.00209 |
| CORTEXA510    | 1.19894e-05 | 8.6e-08   |       1.00716 |
| NEOVERSEN2    | 1.19963e-05 | 6.7e-08   |       1.00775 |
| A64FX         | 1.19992e-05 | 6.35e-08  |       1.00799 |
| THUNDERX2T99  | 1.20011e-05 | 1.095e-07 |       1.00815 |
| CORTEXA55     | 1.20146e-05 | 8.45e-08  |       1.00928 |
| VORTEX        | 1.20283e-05 | 8.05e-08  |       1.01044 |
| NEOVERSEN1    | 1.20313e-05 | 5.7e-08   |       1.01069 |
| CORTEXX1      | 1.20356e-05 | 7.25e-08  |       1.01105 |
| FT2000        | 1.20425e-05 | 7.25e-08  |       1.01163 |
| EMAG8180      | 1.20444e-05 | 7.65e-08  |       1.01179 |
| CORTEXA710    | 1.20564e-05 | 1.13e-07  |       1.0128  |
| THUNDERX3T110 | 1.20577e-05 | 9.9e-08   |       1.01291 |
| CORTEXA73     | 1.20632e-05 | 1.95e-07  |       1.01337 |
| CORTEXA76     | 1.20723e-05 | 6.15e-08  |       1.01413 |
| THUNDERX      | 1.20726e-05 | 8.25e-08  |       1.01415 |
| FALKOR        | 1.20728e-05 | 1.04e-07  |       1.01417 |
| TSV110        | 1.21128e-05 | 7.4e-08   |       1.01754 |
| CORTEXA72     | 1.2116e-05  | 1.48e-07  |       1.0178  |
| CORTEXA57     | 1.2141e-05  | 1.615e-07 |       1.0199  |

bench_linalg.Eindot.time_matmul_trans_a_at
| arch          |        mean |     spread |   perf_ratios |
|:--------------|------------:|-----------:|--------------:|
| NEOVERSEV1    | 4.37416e-05 | 1.27e-07   |       1       |
| NEOVERSEN2    | 4.37755e-05 | 5.0395e-06 |       1.00077 |
| CORTEXX2      | 4.37929e-05 | 3.4125e-06 |       1.00117 |
| FT2000        | 4.38555e-05 | 3.4245e-06 |       1.0026  |
| EMAG8180      | 4.3901e-05  | 3.533e-06  |       1.00364 |
| ARMV8SVE      | 4.39064e-05 | 5.373e-06  |       1.00377 |
| CORTEXA710    | 4.39429e-05 | 5.5545e-06 |       1.0046  |
| A64FX         | 4.39679e-05 | 3.6235e-06 |       1.00517 |
| THUNDERX3T110 | 4.40395e-05 | 4.961e-06  |       1.00681 |
| VORTEX        | 4.40415e-05 | 5.4005e-06 |       1.00686 |
| CORTEXA53     | 4.40481e-05 | 4.74e-06   |       1.00701 |
| THUNDERX      | 4.40963e-05 | 4.7875e-06 |       1.00811 |
| ARMV8         | 4.42227e-05 | 4.9355e-06 |       1.011   |
| CORTEXA73     | 4.42266e-05 | 5.585e-06  |       1.01109 |
| CORTEXA510    | 4.44399e-05 | 5.0925e-06 |       1.01596 |
| CORTEXA57     | 4.49692e-05 | 5.442e-06  |       1.02806 |
| CORTEXX1      | 4.73808e-05 | 5.6475e-06 |       1.0832  |
| FALKOR        | 4.86205e-05 | 4.8335e-06 |       1.11154 |
| CORTEXA72     | 4.86219e-05 | 6.554e-06  |       1.11157 |
| TSV110        | 4.86533e-05 | 6.8015e-06 |       1.11229 |
| THUNDERX2T99  | 4.86892e-05 | 6.9625e-06 |       1.11311 |
| CORTEXA76     | 4.95638e-05 | 6.8885e-06 |       1.1331  |
| CORTEXA55     | 5.36009e-05 | 7.0505e-06 |       1.2254  |
| NEOVERSEN1    | 5.36565e-05 | 4.59e-06   |       1.22667 |

bench_linalg.Eindot.time_matmul_trans_a_atc
| arch          |        mean |     spread |   perf_ratios |
|:--------------|------------:|-----------:|--------------:|
| CORTEXX2      | 6.00692e-05 | 1.455e-07  |       1       |
| FT2000        | 6.01938e-05 | 2.44e-07   |       1.00207 |
| CORTEXA73     | 6.02592e-05 | 2.32e-07   |       1.00316 |
| A64FX         | 6.02892e-05 | 2.265e-07  |       1.00366 |
| FALKOR        | 6.03249e-05 | 1.905e-07  |       1.00426 |
| NEOVERSEV1    | 6.03326e-05 | 1.41e-07   |       1.00438 |
| ARMV8         | 6.03809e-05 | 2.195e-07  |       1.00519 |
| NEOVERSEN1    | 6.0436e-05  | 1.675e-07  |       1.00611 |
| ARMV8SVE      | 6.04385e-05 | 8.35e-08   |       1.00615 |
| CORTEXX1      | 6.04555e-05 | 7.755e-07  |       1.00643 |
| CORTEXA53     | 6.04803e-05 | 1.15e-07   |       1.00684 |
| NEOVERSEN2    | 6.04914e-05 | 9.8e-08    |       1.00703 |
| EMAG8180      | 6.05097e-05 | 2.485e-07  |       1.00733 |
| THUNDERX2T99  | 6.05573e-05 | 1.321e-06  |       1.00813 |
| THUNDERX      | 6.05633e-05 | 2.935e-07  |       1.00822 |
| CORTEXA72     | 6.05683e-05 | 1.405e-07  |       1.00831 |
| CORTEXA57     | 6.06379e-05 | 1.57e-07   |       1.00947 |
| VORTEX        | 6.06526e-05 | 1.995e-07  |       1.00971 |
| CORTEXA710    | 6.07203e-05 | 1.6e-07    |       1.01084 |
| TSV110        | 6.07934e-05 | 3.585e-07  |       1.01205 |
| CORTEXA510    | 6.07947e-05 | 1.757e-06  |       1.01208 |
| THUNDERX3T110 | 6.0845e-05  | 7.25e-07   |       1.01291 |
| CORTEXA55     | 6.12533e-05 | 1.354e-06  |       1.01971 |
| CORTEXA76     | 6.171e-05   | 5.3095e-06 |       1.02731 |

bench_linalg.Eindot.time_matmul_trans_at_a
| arch          |        mean |    spread |   perf_ratios |
|:--------------|------------:|----------:|--------------:|
| CORTEXX1      | 0.000101661 | 4.05e-07  |       1       |
| ARMV8SVE      | 0.000101733 | 4.85e-07  |       1.00071 |
| CORTEXA73     | 0.000101773 | 3.8e-07   |       1.0011  |
| CORTEXX2      | 0.000101796 | 5.6e-07   |       1.00133 |
| A64FX         | 0.000101858 | 2.85e-07  |       1.00194 |
| NEOVERSEV1    | 0.000101861 | 3.7e-07   |       1.00197 |
| FT2000        | 0.000101916 | 3.75e-07  |       1.00251 |
| NEOVERSEN2    | 0.000102001 | 3.2e-07   |       1.00334 |
| CORTEXA72     | 0.000102042 | 2.9e-07   |       1.00375 |
| NEOVERSEN1    | 0.000102048 | 2.5e-07   |       1.00381 |
| FALKOR        | 0.000102051 | 3.6e-07   |       1.00384 |
| THUNDERX2T99  | 0.000102063 | 4.1e-07   |       1.00396 |
| CORTEXA510    | 0.000102084 | 2.5e-07   |       1.00416 |
| VORTEX        | 0.000102091 | 2.45e-07  |       1.00423 |
| CORTEXA76     | 0.000102101 | 1.55e-07  |       1.00433 |
| CORTEXA53     | 0.000102126 | 4.2e-07   |       1.00457 |
| THUNDERX3T110 | 0.000102167 | 2.65e-07  |       1.00498 |
| CORTEXA710    | 0.000102193 | 3.5e-07   |       1.00524 |
| ARMV8         | 0.00010224  | 3.35e-07  |       1.00569 |
| THUNDERX      | 0.000102352 | 3.1e-07   |       1.0068  |
| EMAG8180      | 0.000102362 | 3.7e-07   |       1.0069  |
| CORTEXA57     | 0.000102704 | 4e-07     |       1.01027 |
| TSV110        | 0.000102803 | 7.75e-07  |       1.01124 |
| CORTEXA55     | 0.000109122 | 8.195e-06 |       1.07339 |

bench_linalg.Eindot.time_matmul_trans_atc_a
| arch          |        mean |     spread |   perf_ratios |
|:--------------|------------:|-----------:|--------------:|
| NEOVERSEV1    | 8.61255e-05 | 6.17e-07   |       1       |
| CORTEXA53     | 8.65067e-05 | 4.755e-07  |       1.00443 |
| ARMV8SVE      | 8.65087e-05 | 3.805e-07  |       1.00445 |
| CORTEXA73     | 8.6514e-05  | 4.235e-07  |       1.00451 |
| THUNDERX      | 8.65452e-05 | 6.905e-07  |       1.00487 |
| VORTEX        | 8.6561e-05  | 3.335e-07  |       1.00506 |
| A64FX         | 8.6603e-05  | 3.31e-07   |       1.00554 |
| CORTEXA57     | 8.66181e-05 | 1.044e-06  |       1.00572 |
| CORTEXA76     | 8.67026e-05 | 1.91e-07   |       1.0067  |
| CORTEXA72     | 8.69022e-05 | 1.3725e-06 |       1.00902 |
| FT2000        | 8.69173e-05 | 7.54e-07   |       1.00919 |
| THUNDERX2T99  | 8.69811e-05 | 4.48e-07   |       1.00993 |
| NEOVERSEN2    | 8.70317e-05 | 7.97e-07   |       1.01052 |
| CORTEXA55     | 8.70754e-05 | 7.675e-07  |       1.01103 |
| CORTEXX2      | 8.70764e-05 | 4.63e-07   |       1.01104 |
| CORTEXX1      | 8.71937e-05 | 6.34e-07   |       1.0124  |
| NEOVERSEN1    | 8.72232e-05 | 7.685e-07  |       1.01274 |
| THUNDERX3T110 | 8.73527e-05 | 6.31e-07   |       1.01425 |
| CORTEXA710    | 8.73535e-05 | 5.605e-07  |       1.01426 |
| EMAG8180      | 8.74165e-05 | 1.7535e-06 |       1.01499 |
| FALKOR        | 8.74564e-05 | 3.44e-07   |       1.01545 |
| ARMV8         | 8.7557e-05  | 6.365e-07  |       1.01662 |
| CORTEXA510    | 8.8457e-05  | 1.885e-06  |       1.02707 |
| TSV110        | 8.94023e-05 | 2.507e-06  |       1.03805 |

bench_linalg.Eindot.time_tensordot_a_b_axes_1_0_0_1
| arch          |        mean |     spread |   perf_ratios |
|:--------------|------------:|-----------:|--------------:|
| CORTEXA73     | 0.000663928 | 2.03e-06   |       1       |
| CORTEXX2      | 0.000664305 | 1.77e-06   |       1.00057 |
| FT2000        | 0.000665888 | 5.14e-06   |       1.00295 |
| CORTEXA53     | 0.000666949 | 3.24e-06   |       1.00455 |
| NEOVERSEV1    | 0.000667378 | 7.91e-06   |       1.0052  |
| CORTEXX1      | 0.000671192 | 5.14e-06   |       1.01094 |
| NEOVERSEN2    | 0.00067126  | 1.42e-05   |       1.01104 |
| CORTEXA710    | 0.000673017 | 6.49e-06   |       1.01369 |
| CORTEXA72     | 0.000677547 | 1.3385e-05 |       1.02051 |
| NEOVERSEN1    | 0.000677582 | 8.62e-06   |       1.02056 |
| ARMV8SVE      | 0.000681647 | 4.705e-06  |       1.02669 |
| A64FX         | 0.000681701 | 2.835e-06  |       1.02677 |
| FALKOR        | 0.000685465 | 7.505e-06  |       1.03244 |
| CORTEXA55     | 0.000685501 | 3.93e-06   |       1.03249 |
| THUNDERX2T99  | 0.000686194 | 6.965e-06  |       1.03354 |
| VORTEX        | 0.000686982 | 3.485e-06  |       1.03472 |
| THUNDERX      | 0.000687109 | 2.815e-06  |       1.03491 |
| CORTEXA57     | 0.000688921 | 2.236e-05  |       1.03764 |
| ARMV8         | 0.000691663 | 1.7565e-05 |       1.04177 |
| EMAG8180      | 0.000693309 | 1.5155e-05 |       1.04425 |
| CORTEXA510    | 0.000694443 | 3.831e-05  |       1.04596 |
| TSV110        | 0.000697681 | 1.3505e-05 |       1.05084 |
| THUNDERX3T110 | 0.000724382 | 2.4895e-05 |       1.09105 |
| CORTEXA76     | 0.000735522 | 7.5375e-05 |       1.10783 |

('bench_linalg.Einsum.time_einsum_contig_contig', "<class 'numpy.float32'>")
| arch          |        mean |     spread |   perf_ratios |
|:--------------|------------:|-----------:|--------------:|
| ARMV8         | 4.74991e-05 | 1.0275e-06 |       1       |
| CORTEXA53     | 4.7555e-05  | 7.91e-07   |       1.00118 |
| CORTEXA73     | 4.80428e-05 | 1.75e-08   |       1.01145 |
| CORTEXX2      | 4.81308e-05 | 5.445e-07  |       1.0133  |
| CORTEXX1      | 4.81319e-05 | 1.375e-07  |       1.01332 |
| TSV110        | 4.82806e-05 | 1.83e-07   |       1.01645 |
| FT2000        | 4.82947e-05 | 4.65e-08   |       1.01675 |
| CORTEXA710    | 4.83132e-05 | 1.155e-07  |       1.01714 |
| NEOVERSEV1    | 4.8318e-05  | 9.3e-08    |       1.01724 |
| NEOVERSEN1    | 4.83201e-05 | 4.8e-08    |       1.01728 |
| VORTEX        | 4.83226e-05 | 1.5e-07    |       1.01734 |
| NEOVERSEN2    | 4.83381e-05 | 6.45e-08   |       1.01766 |
| EMAG8180      | 4.8361e-05  | 3.695e-07  |       1.01814 |
| FALKOR        | 4.83889e-05 | 1.935e-07  |       1.01873 |
| THUNDERX2T99  | 4.84054e-05 | 5.31e-07   |       1.01908 |
| A64FX         | 4.84071e-05 | 1.445e-07  |       1.01911 |
| CORTEXA57     | 4.8435e-05  | 1.42e-07   |       1.0197  |
| CORTEXA55     | 4.84593e-05 | 1.405e-07  |       1.02022 |
| ARMV8SVE      | 4.85208e-05 | 4.6e-08    |       1.02151 |
| THUNDERX      | 4.85216e-05 | 1.69e-07   |       1.02152 |
| CORTEXA76     | 4.85536e-05 | 1.605e-07  |       1.0222  |
| CORTEXA510    | 4.86463e-05 | 3.2e-07    |       1.02415 |
| CORTEXA72     | 4.86569e-05 | 7.45e-07   |       1.02437 |
| THUNDERX3T110 | 4.88726e-05 | 2.395e-07  |       1.02892 |

('bench_linalg.Einsum.time_einsum_contig_contig', "<class 'numpy.float64'>")
| arch          |        mean |    spread |   perf_ratios |
|:--------------|------------:|----------:|--------------:|
| ARMV8SVE      | 0.000100295 | 3.1e-07   |       1       |
| CORTEXA53     | 0.000100472 | 1.8e-07   |       1.00176 |
| THUNDERX2T99  | 0.000100643 | 2e-07     |       1.00347 |
| A64FX         | 0.000100699 | 3.15e-07  |       1.00403 |
| ARMV8         | 0.000100717 | 2.3e-07   |       1.0042  |
| FT2000        | 0.000100781 | 3.7e-07   |       1.00484 |
| VORTEX        | 0.000100972 | 8.35e-07  |       1.00675 |
| CORTEXA55     | 0.000101398 | 8.9e-07   |       1.01099 |
| CORTEXA73     | 0.000101536 | 1.325e-06 |       1.01238 |
| EMAG8180      | 0.000101704 | 1.545e-06 |       1.01405 |
| NEOVERSEV1    | 0.000101727 | 1.595e-06 |       1.01428 |
| THUNDERX      | 0.000102002 | 1.545e-06 |       1.01702 |
| NEOVERSEN2    | 0.000102054 | 1.16e-06  |       1.01754 |
| TSV110        | 0.000102725 | 8.9e-07   |       1.02423 |
| CORTEXX1      | 0.000103195 | 2.05e-07  |       1.02891 |
| CORTEXA72     | 0.0001033   | 5.4e-07   |       1.02996 |
| CORTEXA510    | 0.000103337 | 3.55e-07  |       1.03033 |
| CORTEXA57     | 0.000103349 | 3.85e-07  |       1.03045 |
| FALKOR        | 0.000103355 | 5.75e-07  |       1.03051 |
| THUNDERX3T110 | 0.000103507 | 1.9e-07   |       1.03202 |
| CORTEXA710    | 0.000103605 | 3.6e-07   |       1.033   |
| CORTEXA76     | 0.000103615 | 4.25e-07  |       1.0331  |
| NEOVERSEN1    | 0.000103631 | 1.75e-07  |       1.03326 |
| CORTEXX2      | 0.000103665 | 5.3e-07   |       1.0336  |

('bench_linalg.Einsum.time_einsum_contig_outstride0', "<class 'numpy.float32'>")
| arch          |        mean |    spread |   perf_ratios |
|:--------------|------------:|----------:|--------------:|
| ARMV8         | 3.38728e-05 | 3.575e-07 |       1       |
| CORTEXX2      | 3.396e-05   | 1.35e-08  |       1.00258 |
| CORTEXX1      | 3.39945e-05 | 2.65e-08  |       1.0036  |
| CORTEXA73     | 3.40011e-05 | 4.3e-08   |       1.00379 |
| CORTEXA710    | 3.40283e-05 | 8.95e-08  |       1.00459 |
| NEOVERSEN2    | 3.40576e-05 | 5.15e-08  |       1.00546 |
| CORTEXA76     | 3.4059e-05  | 9.75e-08  |       1.0055  |
| FT2000        | 3.41028e-05 | 1.17e-07  |       1.00679 |
| EMAG8180      | 3.41795e-05 | 1.29e-07  |       1.00905 |
| ARMV8SVE      | 3.41941e-05 | 9.25e-08  |       1.00949 |
| THUNDERX3T110 | 3.41971e-05 | 8.95e-08  |       1.00957 |
| NEOVERSEV1    | 3.41993e-05 | 7.4e-08   |       1.00964 |
| VORTEX        | 3.42185e-05 | 1.71e-07  |       1.01021 |
| NEOVERSEN1    | 3.42306e-05 | 6.85e-08  |       1.01056 |
| CORTEXA53     | 3.4233e-05  | 6.85e-08  |       1.01064 |
| CORTEXA510    | 3.42339e-05 | 1.105e-07 |       1.01066 |
| THUNDERX      | 3.4238e-05  | 1.285e-07 |       1.01078 |
| A64FX         | 3.43102e-05 | 5e-08     |       1.01291 |
| THUNDERX2T99  | 3.43294e-05 | 8e-08     |       1.01348 |
| TSV110        | 3.43536e-05 | 9.1e-08   |       1.01419 |
| FALKOR        | 3.43741e-05 | 2.57e-07  |       1.0148  |
| CORTEXA55     | 3.44461e-05 | 1.415e-07 |       1.01693 |
| CORTEXA57     | 3.45094e-05 | 8.65e-08  |       1.0188  |
| CORTEXA72     | 3.45266e-05 | 3.75e-07  |       1.0193  |

('bench_linalg.Einsum.time_einsum_contig_outstride0', "<class 'numpy.float64'>")
| arch          |        mean |    spread |   perf_ratios |
|:--------------|------------:|----------:|--------------:|
| ARMV8         | 5.94558e-05 | 2.21e-07  |       1       |
| FT2000        | 6.05623e-05 | 5.05e-08  |       1.01861 |
| CORTEXA73     | 6.06142e-05 | 5.9e-08   |       1.01948 |
| CORTEXX2      | 6.06804e-05 | 1.93e-07  |       1.0206  |
| CORTEXA57     | 6.06841e-05 | 2.14e-07  |       1.02066 |
| NEOVERSEN2    | 6.07554e-05 | 2.52e-07  |       1.02186 |
| CORTEXA710    | 6.08187e-05 | 1.56e-07  |       1.02292 |
| CORTEXX1      | 6.08347e-05 | 1.31e-07  |       1.02319 |
| NEOVERSEV1    | 6.085e-05   | 9.5e-08   |       1.02345 |
| THUNDERX2T99  | 6.0861e-05  | 1.485e-07 |       1.02363 |
| CORTEXA72     | 6.08644e-05 | 3.33e-07  |       1.02369 |
| EMAG8180      | 6.08729e-05 | 2.26e-07  |       1.02383 |
| FALKOR        | 6.09225e-05 | 1.96e-07  |       1.02467 |
| TSV110        | 6.09402e-05 | 1.93e-07  |       1.02497 |
| ARMV8SVE      | 6.09426e-05 | 8.2e-08   |       1.02501 |
| CORTEXA53     | 6.10108e-05 | 1.435e-07 |       1.02615 |
| CORTEXA55     | 6.10769e-05 | 1.375e-07 |       1.02726 |
| A64FX         | 6.109e-05   | 2.89e-07  |       1.02749 |
| NEOVERSEN1    | 6.1115e-05  | 1.79e-07  |       1.02791 |
| THUNDERX      | 6.11827e-05 | 1.025e-07 |       1.02904 |
| VORTEX        | 6.1202e-05  | 2.365e-07 |       1.02937 |
| THUNDERX3T110 | 6.13667e-05 | 5.245e-07 |       1.03214 |
| CORTEXA510    | 6.17183e-05 | 9.88e-07  |       1.03805 |
| CORTEXA76     | 6.1993e-05  | 7.385e-07 |       1.04267 |

('bench_linalg.Einsum.time_einsum_mul', "<class 'numpy.float32'>")
| arch          |        mean |     spread |   perf_ratios |
|:--------------|------------:|-----------:|--------------:|
| ARMV8         | 0.000412587 | 3.795e-06  |       1       |
| NEOVERSEN2    | 0.000420261 | 1.71e-06   |       1.0186  |
| CORTEXA73     | 0.000421881 | 4.85e-06   |       1.02253 |
| CORTEXX1      | 0.000422508 | 5.65e-06   |       1.02405 |
| CORTEXA710    | 0.000425945 | 2.19e-06   |       1.03238 |
| FT2000        | 0.000426873 | 4.29e-06   |       1.03463 |
| NEOVERSEN1    | 0.000427212 | 5.245e-06  |       1.03545 |
| EMAG8180      | 0.000427458 | 1.11e-05   |       1.03604 |
| CORTEXA53     | 0.000428286 | 4.04e-06   |       1.03805 |
| NEOVERSEV1    | 0.00042883  | 3.045e-06  |       1.03937 |
| THUNDERX2T99  | 0.000429367 | 9.71e-06   |       1.04067 |
| ARMV8SVE      | 0.000430369 | 4.295e-06  |       1.0431  |
| CORTEXA76     | 0.000431287 | 3.91e-06   |       1.04533 |
| CORTEXX2      | 0.000432259 | 1.003e-05  |       1.04768 |
| A64FX         | 0.00043334  | 5.045e-06  |       1.0503  |
| CORTEXA57     | 0.000435081 | 8.665e-06  |       1.05452 |
| CORTEXA510    | 0.000438944 | 8.365e-06  |       1.06388 |
| VORTEX        | 0.000439161 | 9.55e-06   |       1.06441 |
| THUNDERX      | 0.000441843 | 1.6255e-05 |       1.07091 |
| CORTEXA72     | 0.00044572  | 3.0285e-05 |       1.08031 |
| THUNDERX3T110 | 0.000450418 | 6.53e-06   |       1.09169 |
| TSV110        | 0.000452689 | 3.3905e-05 |       1.0972  |
| FALKOR        | 0.000458617 | 2.561e-05  |       1.11157 |
| CORTEXA55     | 0.000462567 | 1.7005e-05 |       1.12114 |

('bench_linalg.Einsum.time_einsum_mul', "<class 'numpy.float64'>")
| arch          |        mean |     spread |   perf_ratios |
|:--------------|------------:|-----------:|--------------:|
| ARMV8         | 0.000262073 | 4.615e-06  |       1       |
| NEOVERSEV1    | 0.000264914 | 4.335e-06  |       1.01084 |
| CORTEXA73     | 0.000266016 | 2.51e-06   |       1.01505 |
| CORTEXX1      | 0.000266163 | 3.57e-06   |       1.01561 |
| CORTEXA710    | 0.000266499 | 2.315e-06  |       1.01689 |
| NEOVERSEN2    | 0.00026676  | 2.425e-06  |       1.01789 |
| FT2000        | 0.000267059 | 4.61e-06   |       1.01903 |
| CORTEXA53     | 0.00026802  | 6.58e-06   |       1.02269 |
| NEOVERSEN1    | 0.000270507 | 2.86e-06   |       1.03218 |
| CORTEXA72     | 0.000270541 | 1.0455e-05 |       1.03231 |
| CORTEXA57     | 0.000271524 | 6.64e-06   |       1.03607 |
| EMAG8180      | 0.000272166 | 6.415e-06  |       1.03851 |
| THUNDERX      | 0.000272801 | 4.25e-06   |       1.04094 |
| THUNDERX3T110 | 0.000272863 | 3.335e-06  |       1.04117 |
| VORTEX        | 0.000275848 | 7.36e-06   |       1.05256 |
| TSV110        | 0.000276397 | 1.833e-05  |       1.05466 |
| ARMV8SVE      | 0.000276557 | 3.935e-06  |       1.05527 |
| CORTEXX2      | 0.000279229 | 9.355e-06  |       1.06546 |
| THUNDERX2T99  | 0.000279474 | 4.425e-06  |       1.0664  |
| A64FX         | 0.000281268 | 5.205e-06  |       1.07324 |
| CORTEXA55     | 0.000281366 | 1.237e-05  |       1.07362 |
| CORTEXA510    | 0.000299732 | 1.318e-05  |       1.1437  |
| CORTEXA76     | 0.000299831 | 1.7535e-05 |       1.14407 |
| FALKOR        | 0.000318227 | 2.2125e-05 |       1.21427 |

('bench_linalg.Einsum.time_einsum_multiply', "<class 'numpy.float32'>")
| arch          |        mean |    spread |   perf_ratios |
|:--------------|------------:|----------:|--------------:|
| ARMV8         | 1.60385e-05 | 2.85e-07  |       1       |
| CORTEXX1      | 1.61571e-05 | 5.2e-08   |       1.0074  |
| CORTEXA53     | 1.61584e-05 | 2.2e-08   |       1.00748 |
| CORTEXX2      | 1.61869e-05 | 2.15e-08  |       1.00926 |
| EMAG8180      | 1.61907e-05 | 4.65e-08  |       1.00949 |
| NEOVERSEV1    | 1.62207e-05 | 1.43e-07  |       1.01136 |
| ARMV8SVE      | 1.62278e-05 | 5.35e-08  |       1.0118  |
| FT2000        | 1.62345e-05 | 7.7e-08   |       1.01222 |
| CORTEXA72     | 1.62346e-05 | 1.52e-07  |       1.01223 |
| THUNDERX2T99  | 1.62507e-05 | 4.95e-08  |       1.01323 |
| NEOVERSEN2    | 1.62601e-05 | 2e-08     |       1.01382 |
| CORTEXA76     | 1.62768e-05 | 7.65e-08  |       1.01486 |
| CORTEXA73     | 1.63003e-05 | 7.55e-08  |       1.01633 |
| THUNDERX      | 1.63129e-05 | 6.55e-08  |       1.01711 |
| NEOVERSEN1    | 1.6337e-05  | 8.65e-08  |       1.01862 |
| CORTEXA710    | 1.63385e-05 | 4.65e-08  |       1.01871 |
| THUNDERX3T110 | 1.63751e-05 | 2.75e-08  |       1.02099 |
| CORTEXA510    | 1.63796e-05 | 2.025e-07 |       1.02127 |
| VORTEX        | 1.63919e-05 | 4.6e-08   |       1.02204 |
| CORTEXA55     | 1.64091e-05 | 6.2e-08   |       1.02311 |
| A64FX         | 1.64106e-05 | 4.45e-08  |       1.0232  |
| CORTEXA57     | 1.64166e-05 | 1.185e-07 |       1.02358 |
| TSV110        | 1.6501e-05  | 8.2e-08   |       1.02884 |
| FALKOR        | 1.65507e-05 | 2.79e-07  |       1.03194 |

('bench_linalg.Einsum.time_einsum_multiply', "<class 'numpy.float64'>")
| arch          |        mean |    spread |   perf_ratios |
|:--------------|------------:|----------:|--------------:|
| NEOVERSEV1    | 2.01512e-05 | 8.55e-08  |       1       |
| CORTEXA710    | 2.01529e-05 | 1.005e-07 |       1.00008 |
| NEOVERSEN2    | 2.01702e-05 | 2.65e-08  |       1.00094 |
| FT2000        | 2.01731e-05 | 1.9e-08   |       1.00108 |
| NEOVERSEN1    | 2.01752e-05 | 4.05e-08  |       1.00119 |
| CORTEXA72     | 2.0197e-05  | 9.2e-08   |       1.00227 |
| CORTEXX1      | 2.02357e-05 | 4.1e-08   |       1.0042  |
| TSV110        | 2.02405e-05 | 1.175e-07 |       1.00443 |
| CORTEXX2      | 2.02455e-05 | 5.95e-08  |       1.00468 |
| CORTEXA73     | 2.02461e-05 | 1.075e-07 |       1.00471 |
| ARMV8SVE      | 2.02511e-05 | 5.5e-08   |       1.00496 |
| CORTEXA53     | 2.02541e-05 | 3.5e-08   |       1.00511 |
| ARMV8         | 2.02745e-05 | 2.705e-07 |       1.00612 |
| THUNDERX2T99  | 2.02761e-05 | 1.08e-07  |       1.0062  |
| THUNDERX      | 2.03098e-05 | 2.435e-07 |       1.00787 |
| EMAG8180      | 2.03111e-05 | 1.185e-07 |       1.00793 |
| A64FX         | 2.03442e-05 | 6.3e-08   |       1.00958 |
| CORTEXA76     | 2.03632e-05 | 1.75e-08  |       1.01052 |
| VORTEX        | 2.0368e-05  | 4.8e-08   |       1.01076 |
| THUNDERX3T110 | 2.03789e-05 | 7e-08     |       1.0113  |
| FALKOR        | 2.04025e-05 | 1.615e-07 |       1.01247 |
| CORTEXA55     | 2.04451e-05 | 1.425e-07 |       1.01459 |
| CORTEXA510    | 2.05437e-05 | 1.01e-07  |       1.01948 |
| CORTEXA57     | 2.06022e-05 | 3.465e-07 |       1.02238 |

('bench_linalg.Einsum.time_einsum_noncon_contig_contig', "<class 'numpy.float32'>")
| arch          |        mean |     spread |   perf_ratios |
|:--------------|------------:|-----------:|--------------:|
| NEOVERSEN2    | 8.03244e-06 | 5.31e-08   |       1       |
| ARMV8         | 8.07068e-06 | 1.354e-07  |       1.00476 |
| FT2000        | 8.09021e-06 | 1.31e-08   |       1.00719 |
| CORTEXA510    | 8.10069e-06 | 4.55e-08   |       1.0085  |
| CORTEXA72     | 8.10267e-06 | 1.24e-08   |       1.00874 |
| CORTEXA55     | 8.11856e-06 | 7.575e-08  |       1.01072 |
| THUNDERX2T99  | 8.13378e-06 | 2.5e-08    |       1.01262 |
| THUNDERX      | 8.13619e-06 | 4.16e-08   |       1.01292 |
| CORTEXX2      | 8.15707e-06 | 1.2185e-07 |       1.01552 |
| CORTEXA73     | 8.1623e-06  | 1.069e-07  |       1.01617 |
| ARMV8SVE      | 8.1667e-06  | 5.385e-08  |       1.01671 |
| CORTEXA710    | 8.1706e-06  | 1.322e-07  |       1.0172  |
| CORTEXA57     | 8.18221e-06 | 6.95e-08   |       1.01865 |
| CORTEXA53     | 8.21407e-06 | 1.393e-07  |       1.02261 |
| CORTEXX1      | 8.21517e-06 | 1.922e-07  |       1.02275 |
| THUNDERX3T110 | 8.21605e-06 | 1.1105e-07 |       1.02286 |
| A64FX         | 8.246e-06   | 1.328e-07  |       1.02659 |
| EMAG8180      | 8.24729e-06 | 1.619e-07  |       1.02675 |
| NEOVERSEN1    | 8.25161e-06 | 1.926e-07  |       1.02729 |
| NEOVERSEV1    | 8.25875e-06 | 1.269e-07  |       1.02817 |
| VORTEX        | 8.29593e-06 | 7.41e-08   |       1.0328  |
| TSV110        | 8.35399e-06 | 3.76e-08   |       1.04003 |
| CORTEXA76     | 8.36403e-06 | 5.85e-08   |       1.04128 |
| FALKOR        | 8.3747e-06  | 3.775e-08  |       1.04261 |

('bench_linalg.Einsum.time_einsum_noncon_contig_contig', "<class 'numpy.float64'>")
| arch          |        mean |     spread |   perf_ratios |
|:--------------|------------:|-----------:|--------------:|
| ARMV8         | 8.11628e-06 | 1.27e-07   |       1       |
| CORTEXX2      | 8.14389e-06 | 3.61e-08   |       1.0034  |
| NEOVERSEN2    | 8.15394e-06 | 2.335e-08  |       1.00464 |
| TSV110        | 8.18887e-06 | 2.95e-08   |       1.00894 |
| EMAG8180      | 8.23413e-06 | 8.98e-08   |       1.01452 |
| FALKOR        | 8.27957e-06 | 1.182e-07  |       1.02012 |
| FT2000        | 8.28907e-06 | 1.767e-07  |       1.02129 |
| CORTEXA710    | 8.29305e-06 | 1.266e-07  |       1.02178 |
| CORTEXA510    | 8.29769e-06 | 6.865e-08  |       1.02235 |
| NEOVERSEV1    | 8.32157e-06 | 1.2525e-07 |       1.02529 |
| VORTEX        | 8.32984e-06 | 1.572e-07  |       1.02631 |
| A64FX         | 8.34539e-06 | 1.086e-07  |       1.02823 |
| CORTEXA73     | 8.34781e-06 | 1.012e-07  |       1.02853 |
| THUNDERX      | 8.34968e-06 | 1.8125e-07 |       1.02876 |
| THUNDERX3T110 | 8.36004e-06 | 9.705e-08  |       1.03003 |
| NEOVERSEN1    | 8.36211e-06 | 1.361e-07  |       1.03029 |
| CORTEXA53     | 8.36916e-06 | 1.2625e-07 |       1.03116 |
| CORTEXA57     | 8.37774e-06 | 2.8055e-07 |       1.03221 |
| CORTEXA55     | 8.41207e-06 | 1.475e-08  |       1.03644 |
| CORTEXA76     | 8.43839e-06 | 8.065e-08  |       1.03969 |
| CORTEXA72     | 8.47933e-06 | 2.17e-08   |       1.04473 |
| CORTEXX1      | 8.48954e-06 | 4.425e-08  |       1.04599 |
| ARMV8SVE      | 8.50018e-06 | 2.315e-08  |       1.0473  |
| THUNDERX2T99  | 8.56013e-06 | 1.37e-07   |       1.05469 |

('bench_linalg.Einsum.time_einsum_noncon_contig_outstride0', "<class 'numpy.float32'>")
| arch          |        mean |    spread |   perf_ratios |
|:--------------|------------:|----------:|--------------:|
| NEOVERSEN2    | 6.32979e-06 | 1.19e-08  |       1       |
| ARMV8         | 6.34917e-06 | 1.045e-07 |       1.00306 |
| CORTEXX2      | 6.37099e-06 | 3.95e-09  |       1.00651 |
| CORTEXA710    | 6.39218e-06 | 5.9e-08   |       1.00986 |
| FALKOR        | 6.39277e-06 | 4.49e-08  |       1.00995 |
| THUNDERX2T99  | 6.39418e-06 | 2.975e-08 |       1.01017 |
| A64FX         | 6.39506e-06 | 2.915e-08 |       1.01031 |
| EMAG8180      | 6.39547e-06 | 7.505e-08 |       1.01038 |
| NEOVERSEN1    | 6.40552e-06 | 2.72e-08  |       1.01196 |
| CORTEXA73     | 6.41358e-06 | 8.5e-09   |       1.01324 |
| THUNDERX3T110 | 6.41745e-06 | 2.67e-08  |       1.01385 |
| ARMV8SVE      | 6.41762e-06 | 2.795e-08 |       1.01388 |
| THUNDERX      | 6.41974e-06 | 1.655e-08 |       1.01421 |
| CORTEXA72     | 6.42354e-06 | 3.46e-08  |       1.01481 |
| VORTEX        | 6.42555e-06 | 6.16e-08  |       1.01513 |
| NEOVERSEV1    | 6.42574e-06 | 1.535e-08 |       1.01516 |
| CORTEXA55     | 6.43136e-06 | 1.475e-08 |       1.01605 |
| FT2000        | 6.43417e-06 | 2.615e-08 |       1.01649 |
| CORTEXA53     | 6.43573e-06 | 9.95e-09  |       1.01674 |
| CORTEXX1      | 6.43608e-06 | 9.9e-09   |       1.01679 |
| TSV110        | 6.45466e-06 | 3.29e-08  |       1.01973 |
| CORTEXA76     | 6.4985e-06  | 1.115e-08 |       1.02665 |
| CORTEXA57     | 6.5044e-06  | 4.2e-08   |       1.02759 |
| CORTEXA510    | 6.50579e-06 | 6.74e-08  |       1.02781 |

('bench_linalg.Einsum.time_einsum_noncon_contig_outstride0', "<class 'numpy.float64'>")
| arch          |        mean |     spread |   perf_ratios |
|:--------------|------------:|-----------:|--------------:|
| NEOVERSEN1    | 6.47655e-06 | 1.91e-08   |       1       |
| CORTEXX2      | 6.48619e-06 | 1.58e-08   |       1.00149 |
| NEOVERSEV1    | 6.49172e-06 | 3.4e-08    |       1.00234 |
| ARMV8SVE      | 6.49455e-06 | 5.2e-08    |       1.00278 |
| ARMV8         | 6.49728e-06 | 9.475e-08  |       1.0032  |
| CORTEXA710    | 6.49889e-06 | 1.925e-08  |       1.00345 |
| CORTEXX1      | 6.50231e-06 | 1.615e-08  |       1.00398 |
| THUNDERX2T99  | 6.50468e-06 | 2.115e-08  |       1.00434 |
| VORTEX        | 6.50726e-06 | 2.535e-08  |       1.00474 |
| CORTEXA55     | 6.5123e-06  | 1.245e-08  |       1.00552 |
| NEOVERSEN2    | 6.51367e-06 | 1.4e-08    |       1.00573 |
| THUNDERX      | 6.51987e-06 | 1.795e-08  |       1.00669 |
| THUNDERX3T110 | 6.52309e-06 | 2.44e-08   |       1.00719 |
| CORTEXA53     | 6.52354e-06 | 1.975e-08  |       1.00726 |
| FT2000        | 6.53607e-06 | 3.72e-08   |       1.00919 |
| TSV110        | 6.54312e-06 | 2.165e-08  |       1.01028 |
| CORTEXA73     | 6.54549e-06 | 5.38e-08   |       1.01064 |
| A64FX         | 6.5464e-06  | 3.005e-08  |       1.01078 |
| CORTEXA72     | 6.54695e-06 | 3.295e-08  |       1.01087 |
| CORTEXA510    | 6.56175e-06 | 1.3775e-07 |       1.01316 |
| CORTEXA76     | 6.5669e-06  | 2.17e-08   |       1.01395 |
| FALKOR        | 6.58312e-06 | 5.27e-08   |       1.01646 |
| CORTEXA57     | 6.59437e-06 | 4.525e-08  |       1.01819 |
| EMAG8180      | 6.59741e-06 | 4.625e-08  |       1.01866 |

('bench_linalg.Einsum.time_einsum_noncon_mul', "<class 'numpy.float32'>")
| arch          |        mean |     spread |   perf_ratios |
|:--------------|------------:|-----------:|--------------:|
| CORTEXX1      | 8.88984e-06 | 6.055e-08  |       1       |
| NEOVERSEV1    | 8.93037e-06 | 5.39e-08   |       1.00456 |
| ARMV8         | 8.93388e-06 | 5.66e-08   |       1.00495 |
| CORTEXX2      | 8.94217e-06 | 2.11e-08   |       1.00589 |
| CORTEXA73     | 8.95801e-06 | 4.52e-08   |       1.00767 |
| FT2000        | 8.96947e-06 | 2.835e-08  |       1.00896 |
| ARMV8SVE      | 9.00146e-06 | 3.605e-08  |       1.01256 |
| THUNDERX2T99  | 9.00439e-06 | 4.475e-08  |       1.01288 |
| TSV110        | 9.00862e-06 | 5.145e-08  |       1.01336 |
| CORTEXA72     | 9.01095e-06 | 1.84e-08   |       1.01362 |
| NEOVERSEN1    | 9.01378e-06 | 2.455e-08  |       1.01394 |
| NEOVERSEN2    | 9.01415e-06 | 2.395e-08  |       1.01398 |
| FALKOR        | 9.01474e-06 | 1.66e-08   |       1.01405 |
| CORTEXA710    | 9.01601e-06 | 7.705e-08  |       1.01419 |
| A64FX         | 9.02046e-06 | 3.715e-08  |       1.01469 |
| CORTEXA76     | 9.02868e-06 | 6.74e-08   |       1.01562 |
| EMAG8180      | 9.03128e-06 | 1.192e-07  |       1.01591 |
| CORTEXA53     | 9.03612e-06 | 3.75e-08   |       1.01645 |
| THUNDERX      | 9.05105e-06 | 3.18e-08   |       1.01813 |
| THUNDERX3T110 | 9.05363e-06 | 2.04e-08   |       1.01842 |
| VORTEX        | 9.07293e-06 | 2.95e-08   |       1.0206  |
| CORTEXA510    | 9.0735e-06  | 1.0385e-07 |       1.02066 |
| CORTEXA57     | 9.07911e-06 | 1.788e-07  |       1.02129 |
| CORTEXA55     | 9.11095e-06 | 1.0205e-07 |       1.02487 |

('bench_linalg.Einsum.time_einsum_noncon_mul', "<class 'numpy.float64'>")
| arch          |        mean |     spread |   perf_ratios |
|:--------------|------------:|-----------:|--------------:|
| ARMV8         | 8.09189e-06 | 1.1025e-07 |       1       |
| NEOVERSEV1    | 8.10235e-06 | 2.96e-08   |       1.00129 |
| THUNDERX2T99  | 8.1238e-06  | 2.565e-08  |       1.00394 |
| CORTEXA72     | 8.12726e-06 | 4.905e-08  |       1.00437 |
| THUNDERX      | 8.1311e-06  | 2.07e-08   |       1.00485 |
| NEOVERSEN1    | 8.13195e-06 | 3.695e-08  |       1.00495 |
| NEOVERSEN2    | 8.14552e-06 | 1.735e-08  |       1.00663 |
| CORTEXA55     | 8.15807e-06 | 4.865e-08  |       1.00818 |
| A64FX         | 8.16975e-06 | 3.75e-08   |       1.00962 |
| CORTEXX2      | 8.18206e-06 | 3.32e-08   |       1.01114 |
| EMAG8180      | 8.19849e-06 | 7.02e-08   |       1.01317 |
| FALKOR        | 8.20153e-06 | 5.04e-08   |       1.01355 |
| ARMV8SVE      | 8.20355e-06 | 3.105e-08  |       1.0138  |
| CORTEXA73     | 8.20412e-06 | 6.29e-08   |       1.01387 |
| CORTEXA710    | 8.21136e-06 | 2.975e-08  |       1.01476 |
| CORTEXA53     | 8.21714e-06 | 3.045e-08  |       1.01548 |
| CORTEXA76     | 8.21992e-06 | 1.93e-08   |       1.01582 |
| FT2000        | 8.22847e-06 | 4.785e-08  |       1.01688 |
| THUNDERX3T110 | 8.23588e-06 | 5.495e-08  |       1.01779 |
| CORTEXX1      | 8.24373e-06 | 5.755e-08  |       1.01876 |
| CORTEXA57     | 8.25779e-06 | 5.145e-08  |       1.0205  |
| VORTEX        | 8.2671e-06  | 3.07e-08   |       1.02165 |
| TSV110        | 8.31439e-06 | 8.255e-08  |       1.0275  |
| CORTEXA510    | 8.32163e-06 | 6.97e-08   |       1.02839 |

('bench_linalg.Einsum.time_einsum_noncon_multiply', "<class 'numpy.float32'>")
| arch          |        mean |    spread |   perf_ratios |
|:--------------|------------:|----------:|--------------:|
| CORTEXA710    | 1.60951e-05 | 6.8e-08   |       1       |
| CORTEXA72     | 1.60971e-05 | 5.4e-08   |       1.00012 |
| NEOVERSEN2    | 1.61249e-05 | 4.05e-08  |       1.00185 |
| CORTEXX2      | 1.61838e-05 | 5.85e-08  |       1.00551 |
| FT2000        | 1.6209e-05  | 1.105e-07 |       1.00707 |
| CORTEXA73     | 1.62124e-05 | 1.24e-07  |       1.00729 |
| CORTEXX1      | 1.62145e-05 | 4.1e-08   |       1.00742 |
| CORTEXA55     | 1.62155e-05 | 1.03e-07  |       1.00748 |
| NEOVERSEV1    | 1.62198e-05 | 2e-08     |       1.00775 |
| EMAG8180      | 1.6224e-05  | 3.7e-08   |       1.00801 |
| THUNDERX2T99  | 1.62251e-05 | 1.075e-07 |       1.00808 |
| CORTEXA57     | 1.6254e-05  | 4.2e-08   |       1.00987 |
| NEOVERSEN1    | 1.62629e-05 | 6.5e-08   |       1.01042 |
| A64FX         | 1.62666e-05 | 7.4e-08   |       1.01066 |
| CORTEXA53     | 1.62906e-05 | 1.135e-07 |       1.01215 |
| CORTEXA76     | 1.62957e-05 | 1.43e-07  |       1.01246 |
| VORTEX        | 1.63059e-05 | 6.8e-08   |       1.0131  |
| THUNDERX3T110 | 1.63151e-05 | 2.7e-08   |       1.01367 |
| THUNDERX      | 1.63162e-05 | 3.15e-08  |       1.01374 |
| ARMV8         | 1.63237e-05 | 2.355e-07 |       1.0142  |
| ARMV8SVE      | 1.63241e-05 | 5.25e-08  |       1.01423 |
| TSV110        | 1.63297e-05 | 6.4e-08   |       1.01458 |
| CORTEXA510    | 1.64386e-05 | 1.67e-07  |       1.02134 |
| FALKOR        | 1.65843e-05 | 1.005e-07 |       1.03039 |

('bench_linalg.Einsum.time_einsum_noncon_multiply', "<class 'numpy.float64'>")
| arch          |        mean |    spread |   perf_ratios |
|:--------------|------------:|----------:|--------------:|
| ARMV8         | 2.00333e-05 | 1.805e-07 |       1       |
| NEOVERSEN2    | 2.01289e-05 | 4e-08     |       1.00477 |
| NEOVERSEV1    | 2.01718e-05 | 2.85e-08  |       1.00691 |
| CORTEXA710    | 2.01766e-05 | 4.75e-08  |       1.00715 |
| THUNDERX3T110 | 2.01799e-05 | 8.35e-08  |       1.00732 |
| NEOVERSEN1    | 2.01915e-05 | 5.3e-08   |       1.0079  |
| CORTEXA73     | 2.02272e-05 | 1.36e-07  |       1.00968 |
| CORTEXX1      | 2.02349e-05 | 2.15e-08  |       1.01006 |
| EMAG8180      | 2.02358e-05 | 6.6e-08   |       1.01011 |
| CORTEXX2      | 2.02454e-05 | 4.65e-08  |       1.01058 |
| FT2000        | 2.02513e-05 | 4.6e-08   |       1.01088 |
| CORTEXA72     | 2.02587e-05 | 8.4e-08   |       1.01125 |
| CORTEXA55     | 2.02683e-05 | 4e-08     |       1.01173 |
| THUNDERX      | 2.02724e-05 | 6.45e-08  |       1.01193 |
| ARMV8SVE      | 2.02793e-05 | 1.51e-07  |       1.01228 |
| CORTEXA53     | 2.02925e-05 | 1.36e-07  |       1.01294 |
| THUNDERX2T99  | 2.02977e-05 | 6.25e-08  |       1.0132  |
| CORTEXA57     | 2.02981e-05 | 4.8e-08   |       1.01322 |
| CORTEXA510    | 2.03078e-05 | 5.6e-08   |       1.0137  |
| VORTEX        | 2.03107e-05 | 5.85e-08  |       1.01385 |
| A64FX         | 2.03442e-05 | 7.75e-08  |       1.01552 |
| CORTEXA76     | 2.03645e-05 | 4.65e-08  |       1.01653 |
| TSV110        | 2.0377e-05  | 9.7e-08   |       1.01716 |
| FALKOR        | 2.04466e-05 | 1.235e-07 |       1.02063 |

('bench_linalg.Einsum.time_einsum_noncon_outer', "<class 'numpy.float32'>")
| arch          |        mean |     spread |   perf_ratios |
|:--------------|------------:|-----------:|--------------:|
| ARMV8         | 0.000527724 | 4.74e-06   |       1       |
| CORTEXA710    | 0.000532448 | 7.35e-07   |       1.00895 |
| CORTEXX2      | 0.000533203 | 5.25e-07   |       1.01038 |
| CORTEXA55     | 0.000533658 | 1.12e-06   |       1.01124 |
| CORTEXX1      | 0.000534059 | 8.1e-07    |       1.012   |
| A64FX         | 0.000534242 | 2.495e-06  |       1.01235 |
| CORTEXA72     | 0.000534251 | 1.44e-06   |       1.01237 |
| NEOVERSEV1    | 0.00053434  | 7.3e-07    |       1.01254 |
| EMAG8180      | 0.000534497 | 1.51e-06   |       1.01283 |
| NEOVERSEN2    | 0.000534716 | 1.72e-06   |       1.01325 |
| FALKOR        | 0.000535484 | 2.23e-06   |       1.0147  |
| NEOVERSEN1    | 0.000535594 | 2.5e-07    |       1.01491 |
| ARMV8SVE      | 0.000535842 | 1.92e-06   |       1.01538 |
| VORTEX        | 0.000535872 | 1.485e-06  |       1.01544 |
| THUNDERX      | 0.000536161 | 1.1e-06    |       1.01599 |
| CORTEXA73     | 0.000536386 | 4.48e-06   |       1.01641 |
| CORTEXA53     | 0.000536704 | 1.15e-06   |       1.01702 |
| THUNDERX3T110 | 0.000537609 | 1.435e-06  |       1.01873 |
| FT2000        | 0.00053769  | 1.97e-06   |       1.01888 |
| CORTEXA76     | 0.000537927 | 3.01e-06   |       1.01933 |
| THUNDERX2T99  | 0.000538234 | 5.17e-06   |       1.01991 |
| CORTEXA510    | 0.000538857 | 2.297e-05  |       1.0211  |
| CORTEXA57     | 0.000542216 | 3.1635e-05 |       1.02746 |
| TSV110        | 0.000545469 | 1.0155e-05 |       1.03363 |

('bench_linalg.Einsum.time_einsum_noncon_outer', "<class 'numpy.float64'>")
| arch          |       mean |     spread |   perf_ratios |
|:--------------|-----------:|-----------:|--------------:|
| ARMV8         | 0.00245095 | 1.295e-05  |       1       |
| CORTEXX2      | 0.00246146 | 1.655e-05  |       1.00429 |
| NEOVERSEV1    | 0.00246283 | 1.02e-05   |       1.00485 |
| NEOVERSEN2    | 0.00246798 | 1.08e-05   |       1.00695 |
| EMAG8180      | 0.00247183 | 2.815e-05  |       1.00852 |
| FT2000        | 0.00247881 | 6.885e-05  |       1.01137 |
| CORTEXA53     | 0.00248151 | 3.225e-05  |       1.01247 |
| CORTEXX1      | 0.00248874 | 1.41e-05   |       1.01542 |
| CORTEXA710    | 0.0025106  | 1.17e-05   |       1.02434 |
| CORTEXA55     | 0.00253253 | 3.37e-05   |       1.03329 |
| CORTEXA72     | 0.00253426 | 0.00012805 |       1.03399 |
| CORTEXA73     | 0.0025423  | 7.76e-05   |       1.03727 |
| A64FX         | 0.00254568 | 4.855e-05  |       1.03865 |
| CORTEXA76     | 0.00255932 | 4.35e-05   |       1.04422 |
| THUNDERX2T99  | 0.00256212 | 2.865e-05  |       1.04536 |
| NEOVERSEN1    | 0.00256545 | 4.865e-05  |       1.04672 |
| ARMV8SVE      | 0.00257022 | 5.005e-05  |       1.04866 |
| VORTEX        | 0.00258128 | 2.78e-05   |       1.05318 |
| FALKOR        | 0.00260334 | 2.64e-05   |       1.06218 |
| CORTEXA57     | 0.00261243 | 0.0001319  |       1.06588 |
| TSV110        | 0.00264514 | 5.495e-05  |       1.07923 |
| THUNDERX      | 0.00265222 | 5.125e-05  |       1.08212 |
| THUNDERX3T110 | 0.00269258 | 9.895e-05  |       1.09859 |
| CORTEXA510    | 0.00302937 | 0.00048745 |       1.236   |

('bench_linalg.Einsum.time_einsum_noncon_sum_mul', "<class 'numpy.float32'>")
| arch          |        mean |    spread |   perf_ratios |
|:--------------|------------:|----------:|--------------:|
| FT2000        | 2.06054e-05 | 1.85e-08  |       1       |
| FALKOR        | 2.06204e-05 | 4.35e-08  |       1.00072 |
| CORTEXA710    | 2.06356e-05 | 5.75e-08  |       1.00147 |
| CORTEXX1      | 2.06526e-05 | 2.8e-08   |       1.00229 |
| ARMV8         | 2.06585e-05 | 3.535e-07 |       1.00257 |
| CORTEXA73     | 2.06627e-05 | 3.5e-08   |       1.00278 |
| NEOVERSEN1    | 2.06642e-05 | 7.9e-08   |       1.00285 |
| EMAG8180      | 2.06647e-05 | 1.62e-07  |       1.00288 |
| NEOVERSEN2    | 2.06782e-05 | 3.5e-08   |       1.00353 |
| NEOVERSEV1    | 2.06971e-05 | 3e-08     |       1.00445 |
| THUNDERX2T99  | 2.07182e-05 | 8.05e-08  |       1.00547 |
| ARMV8SVE      | 2.07311e-05 | 1.95e-08  |       1.0061  |
| A64FX         | 2.07374e-05 | 1.09e-07  |       1.0064  |
| CORTEXX2      | 2.07376e-05 | 6.45e-08  |       1.00641 |
| CORTEXA72     | 2.07607e-05 | 5.45e-08  |       1.00753 |
| CORTEXA55     | 2.07699e-05 | 8.1e-08   |       1.00798 |
| THUNDERX3T110 | 2.07722e-05 | 3.105e-07 |       1.00809 |
| TSV110        | 2.07749e-05 | 8e-08     |       1.00822 |
| CORTEXA510    | 2.07753e-05 | 1.185e-07 |       1.00825 |
| VORTEX        | 2.08052e-05 | 9.15e-08  |       1.00969 |
| CORTEXA57     | 2.08218e-05 | 6.395e-07 |       1.0105  |
| THUNDERX      | 2.08466e-05 | 5.45e-08  |       1.01171 |
| CORTEXA76     | 2.08749e-05 | 9.85e-08  |       1.01308 |
| CORTEXA53     | 2.11792e-05 | 4.85e-07  |       1.02785 |

('bench_linalg.Einsum.time_einsum_noncon_sum_mul', "<class 'numpy.float64'>")
| arch          |        mean |    spread |   perf_ratios |
|:--------------|------------:|----------:|--------------:|
| ARMV8         | 1.33346e-05 | 7.55e-08  |       1       |
| CORTEXX2      | 1.33559e-05 | 5e-08     |       1.0016  |
| FT2000        | 1.33819e-05 | 9.55e-08  |       1.00355 |
| VORTEX        | 1.33997e-05 | 3.15e-08  |       1.00489 |
| THUNDERX3T110 | 1.34081e-05 | 4.15e-08  |       1.00552 |
| THUNDERX      | 1.34186e-05 | 3.8e-08   |       1.0063  |
| A64FX         | 1.34273e-05 | 5.1e-08   |       1.00695 |
| ARMV8SVE      | 1.34481e-05 | 4.4e-08   |       1.00851 |
| CORTEXA710    | 1.3449e-05  | 2.6e-08   |       1.00858 |
| CORTEXX1      | 1.34504e-05 | 5.25e-08  |       1.00868 |
| NEOVERSEN2    | 1.34512e-05 | 5.1e-08   |       1.00875 |
| THUNDERX2T99  | 1.34545e-05 | 3.55e-08  |       1.00899 |
| FALKOR        | 1.3456e-05  | 2.4e-08   |       1.0091  |
| NEOVERSEV1    | 1.34699e-05 | 7.35e-08  |       1.01015 |
| NEOVERSEN1    | 1.34874e-05 | 6.75e-08  |       1.01146 |
| TSV110        | 1.3491e-05  | 3.95e-08  |       1.01173 |
| CORTEXA72     | 1.34946e-05 | 2.05e-07  |       1.012   |
| CORTEXA55     | 1.35021e-05 | 7.35e-08  |       1.01256 |
| CORTEXA73     | 1.35086e-05 | 1.435e-07 |       1.01305 |
| CORTEXA510    | 1.35157e-05 | 2.01e-07  |       1.01358 |
| EMAG8180      | 1.35452e-05 | 1.385e-07 |       1.01579 |
| CORTEXA53     | 1.35531e-05 | 7.5e-08   |       1.01638 |
| CORTEXA76     | 1.35671e-05 | 3.35e-08  |       1.01744 |
| CORTEXA57     | 1.37824e-05 | 1.155e-07 |       1.03358 |

('bench_linalg.Einsum.time_einsum_noncon_sum_mul2', "<class 'numpy.float32'>")
| arch          |        mean |     spread |   perf_ratios |
|:--------------|------------:|-----------:|--------------:|
| NEOVERSEV1    | 2.0639e-05  | 2.75e-08   |       1       |
| CORTEXX1      | 2.0673e-05  | 2.7e-08    |       1.00165 |
| CORTEXA73     | 2.06914e-05 | 6.95e-08   |       1.00254 |
| CORTEXA55     | 2.0709e-05  | 2.355e-07  |       1.00339 |
| CORTEXX2      | 2.07304e-05 | 1.05e-08   |       1.00443 |
| CORTEXA53     | 2.07498e-05 | 5.15e-08   |       1.00537 |
| THUNDERX2T99  | 2.07745e-05 | 7e-08      |       1.00657 |
| NEOVERSEN1    | 2.07819e-05 | 4.785e-07  |       1.00693 |
| THUNDERX3T110 | 2.07836e-05 | 4.15e-08   |       1.00701 |
| NEOVERSEN2    | 2.08107e-05 | 3.6e-08    |       1.00832 |
| VORTEX        | 2.08119e-05 | 5.15e-08   |       1.00838 |
| FT2000        | 2.08215e-05 | 9.15e-08   |       1.00884 |
| CORTEXA72     | 2.08347e-05 | 1.25e-07   |       1.00949 |
| THUNDERX      | 2.08402e-05 | 8.4e-08    |       1.00975 |
| ARMV8SVE      | 2.08529e-05 | 7.05e-08   |       1.01037 |
| CORTEXA510    | 2.08549e-05 | 9.3e-08    |       1.01046 |
| ARMV8         | 2.08608e-05 | 9.665e-07  |       1.01075 |
| CORTEXA76     | 2.08825e-05 | 1.065e-07  |       1.0118  |
| A64FX         | 2.08882e-05 | 4.6e-08    |       1.01208 |
| EMAG8180      | 2.09789e-05 | 5.77e-07   |       1.01647 |
| CORTEXA710    | 2.10197e-05 | 6.235e-07  |       1.01845 |
| FALKOR        | 2.11288e-05 | 2.975e-07  |       1.02373 |
| TSV110        | 2.1137e-05  | 3.7e-07    |       1.02413 |
| CORTEXA57     | 2.14e-05    | 1.0985e-06 |       1.03687 |

('bench_linalg.Einsum.time_einsum_noncon_sum_mul2', "<class 'numpy.float64'>")
| arch          |        mean |    spread |   perf_ratios |
|:--------------|------------:|----------:|--------------:|
| ARMV8         | 1.32878e-05 | 2.495e-07 |       1       |
| CORTEXA76     | 1.33111e-05 | 7e-08     |       1.00176 |
| CORTEXA72     | 1.3342e-05  | 6.45e-08  |       1.00408 |
| CORTEXX2      | 1.33747e-05 | 6.2e-08   |       1.00655 |
| CORTEXA510    | 1.33947e-05 | 5.6e-08   |       1.00805 |
| FT2000        | 1.34045e-05 | 2.75e-08  |       1.00878 |
| CORTEXA73     | 1.34047e-05 | 1.07e-07  |       1.0088  |
| CORTEXX1      | 1.34244e-05 | 3e-08     |       1.01028 |
| THUNDERX2T99  | 1.34244e-05 | 5.65e-08  |       1.01028 |
| NEOVERSEN2    | 1.34263e-05 | 2.75e-08  |       1.01043 |
| NEOVERSEV1    | 1.34582e-05 | 6e-08     |       1.01283 |
| CORTEXA710    | 1.34666e-05 | 5.8e-08   |       1.01346 |
| CORTEXA55     | 1.34675e-05 | 2.25e-08  |       1.01353 |
| TSV110        | 1.34736e-05 | 1.055e-07 |       1.01399 |
| CORTEXA57     | 1.34809e-05 | 8.25e-08  |       1.01454 |
| CORTEXA53     | 1.34917e-05 | 1.56e-07  |       1.01535 |
| VORTEX        | 1.34932e-05 | 5.35e-08  |       1.01546 |
| THUNDERX      | 1.35214e-05 | 7e-08     |       1.01758 |
| THUNDERX3T110 | 1.35255e-05 | 4.75e-08  |       1.01789 |
| ARMV8SVE      | 1.35374e-05 | 1.395e-07 |       1.01879 |
| A64FX         | 1.35611e-05 | 3.45e-08  |       1.02057 |
| EMAG8180      | 1.35617e-05 | 7.15e-08  |       1.02061 |
| NEOVERSEN1    | 1.35748e-05 | 3.95e-08  |       1.0216  |
| FALKOR        | 1.36411e-05 | 1.605e-07 |       1.02659 |

('bench_linalg.Einsum.time_einsum_outer', "<class 'numpy.float32'>")
| arch          |       mean |     spread |   perf_ratios |
|:--------------|-----------:|-----------:|--------------:|
| CORTEXX2      | 0.00287019 | 2.015e-05  |       1       |
| ARMV8         | 0.00288292 | 3.66e-05   |       1.00443 |
| NEOVERSEN2    | 0.00289289 | 2.465e-05  |       1.00791 |
| CORTEXX1      | 0.00290973 | 1.945e-05  |       1.01377 |
| EMAG8180      | 0.00293855 | 4.38e-05   |       1.02382 |
| NEOVERSEV1    | 0.00294714 | 4.825e-05  |       1.02681 |
| CORTEXA710    | 0.00299081 | 5.015e-05  |       1.04202 |
| NEOVERSEN1    | 0.0029929  | 4.94e-05   |       1.04275 |
| CORTEXA53     | 0.00300887 | 5.735e-05  |       1.04832 |
| CORTEXA72     | 0.00301256 | 6.95e-05   |       1.0496  |
| A64FX         | 0.00301968 | 6.135e-05  |       1.05208 |
| TSV110        | 0.00303921 | 3.825e-05  |       1.05889 |
| ARMV8SVE      | 0.00304444 | 5.475e-05  |       1.06071 |
| CORTEXA55     | 0.00304478 | 0.00017695 |       1.06083 |
| VORTEX        | 0.00305158 | 5.595e-05  |       1.0632  |
| CORTEXA510    | 0.00308997 | 0.00013655 |       1.07657 |
| FALKOR        | 0.00311498 | 5.935e-05  |       1.08529 |
| CORTEXA76     | 0.0031437  | 9.36e-05   |       1.09529 |
| THUNDERX2T99  | 0.00314528 | 5.32e-05   |       1.09584 |
| THUNDERX      | 0.00316061 | 4.19e-05   |       1.10119 |
| FT2000        | 0.00326764 | 0.00036715 |       1.13847 |
| THUNDERX3T110 | 0.00329334 | 0.00019545 |       1.14743 |
| CORTEXA73     | 0.00343975 | 0.00049715 |       1.19844 |
| CORTEXA57     | 0.0034653  | 0.00039445 |       1.20734 |

('bench_linalg.Einsum.time_einsum_outer', "<class 'numpy.float64'>")
| arch          |       mean |     spread |   perf_ratios |
|:--------------|-----------:|-----------:|--------------:|
| ARMV8         | 0.00630827 | 5.65e-05   |       1       |
| CORTEXX1      | 0.00633208 | 2.95e-05   |       1.00377 |
| CORTEXX2      | 0.00635308 | 4.785e-05  |       1.0071  |
| NEOVERSEN2    | 0.006373   | 3.555e-05  |       1.01026 |
| TSV110        | 0.00638752 | 8.235e-05  |       1.01256 |
| EMAG8180      | 0.00640465 | 0.0001386  |       1.01528 |
| NEOVERSEV1    | 0.00643771 | 4.275e-05  |       1.02052 |
| CORTEXA710    | 0.00645407 | 6.635e-05  |       1.02311 |
| CORTEXA72     | 0.00646265 | 5.975e-05  |       1.02447 |
| CORTEXA53     | 0.00647474 | 0.0001359  |       1.02639 |
| NEOVERSEN1    | 0.00649991 | 8.35e-05   |       1.03038 |
| FT2000        | 0.00650659 | 0.0006217  |       1.03144 |
| CORTEXA55     | 0.00651925 | 0.00015385 |       1.03344 |
| A64FX         | 0.00653831 | 6.495e-05  |       1.03647 |
| ARMV8SVE      | 0.00657569 | 0.00011545 |       1.04239 |
| THUNDERX2T99  | 0.00657936 | 0.00019485 |       1.04297 |
| FALKOR        | 0.00660552 | 5.175e-05  |       1.04712 |
| CORTEXA510    | 0.00661344 | 7.615e-05  |       1.04838 |
| THUNDERX3T110 | 0.00664615 | 0.00014755 |       1.05356 |
| THUNDERX      | 0.00668431 | 0.0001016  |       1.05961 |
| VORTEX        | 0.00671497 | 0.0002564  |       1.06447 |
| CORTEXA76     | 0.00677537 | 0.00011925 |       1.07405 |
| CORTEXA57     | 0.00677694 | 0.00018335 |       1.07429 |
| CORTEXA73     | 0.00680543 | 0.00100135 |       1.07881 |

('bench_linalg.Einsum.time_einsum_sum_mul', "<class 'numpy.float32'>")
| arch          |        mean |    spread |   perf_ratios |
|:--------------|------------:|----------:|--------------:|
| ARMV8         | 1.48031e-05 | 2.425e-07 |       1       |
| CORTEXX2      | 1.48255e-05 | 2.45e-08  |       1.00151 |
| EMAG8180      | 1.48432e-05 | 1.95e-08  |       1.00271 |
| CORTEXA53     | 1.48562e-05 | 2.5e-08   |       1.00358 |
| TSV110        | 1.48616e-05 | 4.55e-08  |       1.00395 |
| CORTEXX1      | 1.48856e-05 | 9.95e-08  |       1.00557 |
| FT2000        | 1.48879e-05 | 1.075e-07 |       1.00572 |
| NEOVERSEV1    | 1.48907e-05 | 1.7e-08   |       1.00592 |
| CORTEXA73     | 1.49118e-05 | 6.2e-08   |       1.00734 |
| CORTEXA72     | 1.49176e-05 | 2.4e-08   |       1.00773 |
| CORTEXA55     | 1.49212e-05 | 1.7e-07   |       1.00798 |
| NEOVERSEN1    | 1.49217e-05 | 1.33e-07  |       1.00801 |
| CORTEXA710    | 1.49226e-05 | 7.55e-08  |       1.00807 |
| NEOVERSEN2    | 1.49314e-05 | 2.65e-08  |       1.00866 |
| CORTEXA76     | 1.49418e-05 | 4.05e-08  |       1.00937 |
| THUNDERX3T110 | 1.49455e-05 | 6.35e-08  |       1.00962 |
| THUNDERX2T99  | 1.49706e-05 | 4.7e-08   |       1.01132 |
| A64FX         | 1.49876e-05 | 3.95e-08  |       1.01246 |
| CORTEXA510    | 1.50058e-05 | 1.04e-07  |       1.01369 |
| THUNDERX      | 1.50228e-05 | 3.43e-07  |       1.01484 |
| ARMV8SVE      | 1.50414e-05 | 3.95e-08  |       1.01609 |
| VORTEX        | 1.50666e-05 | 1.27e-07  |       1.0178  |
| CORTEXA57     | 1.50891e-05 | 2.25e-08  |       1.01932 |
| FALKOR        | 1.51081e-05 | 7.15e-08  |       1.0206  |

('bench_linalg.Einsum.time_einsum_sum_mul', "<class 'numpy.float64'>")
| arch          |        mean |   spread |   perf_ratios |
|:--------------|------------:|---------:|--------------:|
| ARMV8         | 1.15924e-05 | 2.65e-07 |       1       |
| ARMV8SVE      | 1.17091e-05 | 4.75e-08 |       1.01007 |
| CORTEXA73     | 1.17117e-05 | 9.4e-08  |       1.01029 |
| CORTEXA55     | 1.17214e-05 | 3.85e-08 |       1.01113 |
| CORTEXX2      | 1.1726e-05  | 2.25e-08 |       1.01153 |
| TSV110        | 1.17363e-05 | 8.1e-08  |       1.01242 |
| NEOVERSEN1    | 1.17404e-05 | 2.55e-08 |       1.01276 |
| CORTEXX1      | 1.17455e-05 | 3.5e-08  |       1.01321 |
| CORTEXA710    | 1.17458e-05 | 1.25e-08 |       1.01323 |
| THUNDERX3T110 | 1.17464e-05 | 7.05e-08 |       1.01328 |
| EMAG8180      | 1.17466e-05 | 8.7e-08  |       1.0133  |
| FT2000        | 1.1754e-05  | 7.6e-08  |       1.01394 |
| NEOVERSEV1    | 1.17546e-05 | 4.6e-08  |       1.01399 |
| CORTEXA72     | 1.17593e-05 | 7.85e-08 |       1.0144  |
| THUNDERX      | 1.17654e-05 | 4.65e-08 |       1.01493 |
| FALKOR        | 1.17834e-05 | 4.05e-08 |       1.01647 |
| VORTEX        | 1.17874e-05 | 5.05e-08 |       1.01682 |
| CORTEXA76     | 1.17947e-05 | 2.65e-08 |       1.01745 |
| NEOVERSEN2    | 1.17977e-05 | 5.2e-08  |       1.01771 |
| CORTEXA57     | 1.18176e-05 | 6.25e-08 |       1.01943 |
| THUNDERX2T99  | 1.182e-05   | 4.55e-08 |       1.01963 |
| A64FX         | 1.18634e-05 | 5.55e-08 |       1.02338 |
| CORTEXA53     | 1.19178e-05 | 8.6e-08  |       1.02807 |
| CORTEXA510    | 1.19824e-05 | 3.25e-08 |       1.03365 |

('bench_linalg.Einsum.time_einsum_sum_mul2', "<class 'numpy.float32'>")
| arch          |        mean |    spread |   perf_ratios |
|:--------------|------------:|----------:|--------------:|
| ARMV8         | 1.48545e-05 | 1.28e-07  |       1       |
| CORTEXA72     | 1.48716e-05 | 1.55e-08  |       1.00115 |
| NEOVERSEV1    | 1.48786e-05 | 1.7e-08   |       1.00162 |
| CORTEXX1      | 1.49107e-05 | 3.8e-08   |       1.00378 |
| FT2000        | 1.49268e-05 | 1.9e-08   |       1.00487 |
| CORTEXX2      | 1.4933e-05  | 3.4e-08   |       1.00529 |
| CORTEXA710    | 1.49549e-05 | 2.15e-08  |       1.00676 |
| CORTEXA55     | 1.49564e-05 | 5.85e-08  |       1.00686 |
| NEOVERSEN2    | 1.49579e-05 | 1.46e-07  |       1.00696 |
| NEOVERSEN1    | 1.49747e-05 | 5.95e-08  |       1.00809 |
| CORTEXA57     | 1.4975e-05  | 8.45e-08  |       1.00811 |
| FALKOR        | 1.49772e-05 | 6.05e-08  |       1.00826 |
| TSV110        | 1.49783e-05 | 1.7e-08   |       1.00833 |
| CORTEXA510    | 1.49903e-05 | 6.5e-08   |       1.00914 |
| CORTEXA76     | 1.50002e-05 | 5.95e-08  |       1.00981 |
| CORTEXA53     | 1.50058e-05 | 7.9e-08   |       1.01019 |
| CORTEXA73     | 1.50289e-05 | 9.6e-08   |       1.01174 |
| EMAG8180      | 1.50431e-05 | 2.155e-07 |       1.0127  |
| THUNDERX      | 1.50441e-05 | 2.85e-08  |       1.01276 |
| VORTEX        | 1.50696e-05 | 5.05e-08  |       1.01448 |
| ARMV8SVE      | 1.50749e-05 | 6.55e-08  |       1.01483 |
| A64FX         | 1.50837e-05 | 4.6e-08   |       1.01543 |
| THUNDERX2T99  | 1.50907e-05 | 6.71e-07  |       1.0159  |
| THUNDERX3T110 | 1.5092e-05  | 5.15e-08  |       1.01599 |

('bench_linalg.Einsum.time_einsum_sum_mul2', "<class 'numpy.float64'>")
| arch          |        mean |    spread |   perf_ratios |
|:--------------|------------:|----------:|--------------:|
| NEOVERSEV1    | 1.16237e-05 | 4.85e-08  |       1       |
| ARMV8         | 1.16389e-05 | 1.4e-08   |       1.00131 |
| CORTEXA72     | 1.17046e-05 | 4.3e-08   |       1.00696 |
| NEOVERSEN2    | 1.17157e-05 | 3.55e-08  |       1.00791 |
| CORTEXA73     | 1.17213e-05 | 1.4e-07   |       1.0084  |
| CORTEXA710    | 1.17309e-05 | 4.95e-08  |       1.00922 |
| CORTEXA510    | 1.17344e-05 | 5.2e-08   |       1.00952 |
| THUNDERX3T110 | 1.17409e-05 | 3.3e-08   |       1.01008 |
| NEOVERSEN1    | 1.17477e-05 | 3.9e-08   |       1.01066 |
| CORTEXX2      | 1.17601e-05 | 3.15e-08  |       1.01174 |
| FT2000        | 1.17882e-05 | 1.02e-07  |       1.01415 |
| THUNDERX      | 1.17902e-05 | 2.65e-08  |       1.01433 |
| CORTEXX1      | 1.18085e-05 | 4.55e-08  |       1.0159  |
| EMAG8180      | 1.18142e-05 | 4.2e-08   |       1.01639 |
| CORTEXA53     | 1.1816e-05  | 7.65e-08  |       1.01654 |
| THUNDERX2T99  | 1.18162e-05 | 1.75e-08  |       1.01656 |
| A64FX         | 1.18227e-05 | 1.115e-07 |       1.01712 |
| CORTEXA55     | 1.18227e-05 | 1.1e-08   |       1.01712 |
| CORTEXA76     | 1.18371e-05 | 1.49e-07  |       1.01836 |
| ARMV8SVE      | 1.18643e-05 | 5.85e-08  |       1.0207  |
| VORTEX        | 1.18708e-05 | 3.95e-08  |       1.02126 |
| FALKOR        | 1.18868e-05 | 1.265e-07 |       1.02264 |
| CORTEXA57     | 1.18911e-05 | 8.2e-08   |       1.023   |
| TSV110        | 1.19676e-05 | 5.65e-08  |       1.02959 |

('bench_linalg.LinAlgTransposeVdot.time_transpose', '(16, 16)')
| arch          |        mean |     spread |   perf_ratios |
|:--------------|------------:|-----------:|--------------:|
| ARMV8         | 3.21331e-07 | 5.665e-09  |       1       |
| CORTEXX1      | 3.23313e-07 | 6.85e-10   |       1.00617 |
| CORTEXA510    | 3.2367e-07  | 1.3e-09    |       1.00728 |
| CORTEXA72     | 3.23728e-07 | 5.1e-10    |       1.00746 |
| CORTEXA76     | 3.24005e-07 | 9.4e-10    |       1.00832 |
| CORTEXX2      | 3.24169e-07 | 1.55e-09   |       1.00883 |
| NEOVERSEV1    | 3.24323e-07 | 8.55e-10   |       1.00931 |
| FALKOR        | 3.25003e-07 | 1.265e-09  |       1.01143 |
| EMAG8180      | 3.25378e-07 | 1.41e-09   |       1.0126  |
| TSV110        | 3.2562e-07  | 5.4e-10    |       1.01335 |
| CORTEXA73     | 3.25729e-07 | 1.6e-10    |       1.01369 |
| CORTEXA55     | 3.25937e-07 | 3.095e-09  |       1.01433 |
| NEOVERSEN1    | 3.2656e-07  | 7.05e-10   |       1.01627 |
| A64FX         | 3.26987e-07 | 1.275e-09  |       1.0176  |
| CORTEXA53     | 3.27132e-07 | 1.325e-09  |       1.01805 |
| VORTEX        | 3.27242e-07 | 1.75e-09   |       1.0184  |
| THUNDERX      | 3.27377e-07 | 1.6e-09    |       1.01881 |
| THUNDERX3T110 | 3.28397e-07 | 1.24e-09   |       1.02199 |
| CORTEXA710    | 3.28428e-07 | 8e-10      |       1.02208 |
| THUNDERX2T99  | 3.29295e-07 | 3.74e-09   |       1.02478 |
| FT2000        | 3.31038e-07 | 8.245e-09  |       1.03021 |
| NEOVERSEN2    | 3.31687e-07 | 7.22e-09   |       1.03223 |
| ARMV8SVE      | 3.36464e-07 | 1.1695e-08 |       1.04709 |
| CORTEXA57     | 3.36978e-07 | 5.92e-09   |       1.04869 |

('bench_linalg.LinAlgTransposeVdot.time_transpose', '(32, 32)')
| arch          |        mean |    spread |   perf_ratios |
|:--------------|------------:|----------:|--------------:|
| ARMV8         | 3.20996e-07 | 5.425e-09 |       1       |
| NEOVERSEN1    | 3.23397e-07 | 1.86e-09  |       1.00748 |
| CORTEXA710    | 3.2356e-07  | 2.125e-09 |       1.00799 |
| TSV110        | 3.23794e-07 | 5.3e-10   |       1.00872 |
| THUNDERX      | 3.24073e-07 | 1.975e-09 |       1.00958 |
| CORTEXX1      | 3.24092e-07 | 2.02e-09  |       1.00965 |
| NEOVERSEN2    | 3.24241e-07 | 1.825e-09 |       1.01011 |
| CORTEXA72     | 3.24528e-07 | 1.3e-10   |       1.011   |
| CORTEXA53     | 3.24989e-07 | 1.515e-09 |       1.01244 |
| CORTEXX2      | 3.25169e-07 | 6.75e-10  |       1.013   |
| FALKOR        | 3.25263e-07 | 1.725e-09 |       1.01329 |
| CORTEXA73     | 3.2565e-07  | 2.335e-09 |       1.0145  |
| ARMV8SVE      | 3.25726e-07 | 1.615e-09 |       1.01474 |
| NEOVERSEV1    | 3.25943e-07 | 3.985e-09 |       1.01541 |
| EMAG8180      | 3.26573e-07 | 1.775e-09 |       1.01737 |
| CORTEXA76     | 3.26858e-07 | 1.505e-09 |       1.01826 |
| A64FX         | 3.27616e-07 | 1.325e-09 |       1.02062 |
| CORTEXA55     | 3.27928e-07 | 1.34e-09  |       1.02159 |
| THUNDERX2T99  | 3.28344e-07 | 2.13e-09  |       1.02289 |
| THUNDERX3T110 | 3.29396e-07 | 2.1e-09   |       1.02617 |
| CORTEXA510    | 3.29546e-07 | 5.925e-09 |       1.02663 |
| VORTEX        | 3.30036e-07 | 2.25e-09  |       1.02816 |
| CORTEXA57     | 3.30956e-07 | 1.43e-09  |       1.03103 |
| FT2000        | 3.34911e-07 | 1.006e-08 |       1.04335 |

('bench_linalg.LinAlgTransposeVdot.time_transpose', '(64, 64)')
| arch          |        mean |    spread |   perf_ratios |
|:--------------|------------:|----------:|--------------:|
| ARMV8         | 3.2247e-07  | 4.855e-09 |       1       |
| CORTEXX1      | 3.23361e-07 | 5.15e-10  |       1.00276 |
| NEOVERSEN2    | 3.23672e-07 | 1.25e-10  |       1.00373 |
| CORTEXA72     | 3.24193e-07 | 2.4e-10   |       1.00534 |
| CORTEXX2      | 3.24495e-07 | 6.5e-10   |       1.00628 |
| NEOVERSEV1    | 3.24786e-07 | 7e-10     |       1.00718 |
| CORTEXA73     | 3.2491e-07  | 6.5e-10   |       1.00756 |
| A64FX         | 3.25203e-07 | 9.5e-10   |       1.00847 |
| FALKOR        | 3.25722e-07 | 1.35e-09  |       1.01008 |
| CORTEXA710    | 3.26095e-07 | 5.55e-09  |       1.01124 |
| CORTEXA510    | 3.26277e-07 | 1.385e-09 |       1.0118  |
| THUNDERX3T110 | 3.26334e-07 | 8.95e-10  |       1.01198 |
| CORTEXA55     | 3.26382e-07 | 7.2e-10   |       1.01213 |
| CORTEXA53     | 3.26403e-07 | 1.515e-09 |       1.01219 |
| EMAG8180      | 3.26909e-07 | 2.2e-09   |       1.01376 |
| CORTEXA76     | 3.2697e-07  | 1.495e-09 |       1.01395 |
| NEOVERSEN1    | 3.28081e-07 | 1.62e-09  |       1.0174  |
| CORTEXA57     | 3.30239e-07 | 2.135e-09 |       1.02409 |
| FT2000        | 3.31394e-07 | 6.18e-09  |       1.02767 |
| TSV110        | 3.32227e-07 | 8.43e-09  |       1.03026 |
| THUNDERX2T99  | 3.32903e-07 | 6.275e-09 |       1.03235 |
| VORTEX        | 3.3628e-07  | 9.105e-09 |       1.04283 |
| ARMV8SVE      | 3.37057e-07 | 7.585e-09 |       1.04523 |
| THUNDERX      | 3.40358e-07 | 1.41e-09  |       1.05547 |

('bench_linalg.LinAlgTransposeVdot.time_vdot', '(16, 16)')
| arch          |        mean |    spread |   perf_ratios |
|:--------------|------------:|----------:|--------------:|
| ARMV8         | 5.13669e-07 | 4.25e-09  |       1       |
| CORTEXA73     | 5.14406e-07 | 1.905e-09 |       1.00144 |
| NEOVERSEN2    | 5.14446e-07 | 1.76e-09  |       1.00151 |
| CORTEXA55     | 5.15344e-07 | 1.185e-09 |       1.00326 |
| CORTEXX2      | 5.1556e-07  | 1.455e-09 |       1.00368 |
| CORTEXX1      | 5.17552e-07 | 1.035e-09 |       1.00756 |
| CORTEXA53     | 5.17661e-07 | 1.8e-09   |       1.00777 |
| NEOVERSEN1    | 5.18005e-07 | 2.23e-09  |       1.00844 |
| VORTEX        | 5.18048e-07 | 2.435e-09 |       1.00853 |
| FALKOR        | 5.18211e-07 | 3.05e-09  |       1.00884 |
| ARMV8SVE      | 5.18363e-07 | 2.35e-09  |       1.00914 |
| THUNDERX3T110 | 5.18698e-07 | 2.27e-09  |       1.00979 |
| CORTEXA510    | 5.18821e-07 | 1.43e-09  |       1.01003 |
| A64FX         | 5.19078e-07 | 1.515e-09 |       1.01053 |
| TSV110        | 5.19363e-07 | 1.8e-09   |       1.01109 |
| NEOVERSEV1    | 5.19467e-07 | 1.585e-09 |       1.01129 |
| CORTEXA710    | 5.19625e-07 | 2.905e-09 |       1.01159 |
| THUNDERX      | 5.19689e-07 | 8.9e-10   |       1.01172 |
| CORTEXA57     | 5.19708e-07 | 6.945e-09 |       1.01176 |
| FT2000        | 5.20124e-07 | 1.47e-09  |       1.01257 |
| THUNDERX2T99  | 5.20141e-07 | 1.885e-09 |       1.0126  |
| EMAG8180      | 5.20307e-07 | 4.605e-09 |       1.01292 |
| CORTEXA72     | 5.23251e-07 | 6.44e-09  |       1.01866 |
| CORTEXA76     | 5.24019e-07 | 4.165e-09 |       1.02015 |

('bench_linalg.LinAlgTransposeVdot.time_vdot', '(32, 32)')
| arch          |        mean |    spread |   perf_ratios |
|:--------------|------------:|----------:|--------------:|
| ARMV8         | 9.36343e-07 | 3.555e-09 |       1       |
| CORTEXA55     | 9.54962e-07 | 1.765e-09 |       1.01989 |
| NEOVERSEV1    | 9.55634e-07 | 2.93e-09  |       1.0206  |
| CORTEXX1      | 9.55712e-07 | 3.785e-09 |       1.02069 |
| CORTEXA73     | 9.56104e-07 | 2.34e-09  |       1.0211  |
| CORTEXA72     | 9.57689e-07 | 3.835e-09 |       1.0228  |
| NEOVERSEN1    | 9.57767e-07 | 2.175e-09 |       1.02288 |
| NEOVERSEN2    | 9.58561e-07 | 5.605e-09 |       1.02373 |
| FALKOR        | 9.59727e-07 | 4.725e-09 |       1.02497 |
| ARMV8SVE      | 9.59989e-07 | 5.74e-09  |       1.02525 |
| CORTEXA76     | 9.60494e-07 | 3.83e-09  |       1.02579 |
| EMAG8180      | 9.60939e-07 | 1.55e-09  |       1.02627 |
| CORTEXA57     | 9.62455e-07 | 3.295e-09 |       1.02789 |
| CORTEXX2      | 9.62572e-07 | 3.755e-09 |       1.02801 |
| THUNDERX2T99  | 9.62634e-07 | 3.315e-09 |       1.02808 |
| VORTEX        | 9.63256e-07 | 3.125e-09 |       1.02874 |
| CORTEXA510    | 9.63771e-07 | 4.83e-09  |       1.02929 |
| THUNDERX      | 9.65075e-07 | 4.01e-09  |       1.03069 |
| THUNDERX3T110 | 9.66017e-07 | 2.25e-09  |       1.03169 |
| A64FX         | 9.66184e-07 | 3.77e-09  |       1.03187 |
| CORTEXA710    | 9.66434e-07 | 9.69e-09  |       1.03214 |
| TSV110        | 9.69214e-07 | 3.935e-09 |       1.03511 |
| FT2000        | 9.70437e-07 | 9.5e-09   |       1.03641 |
| CORTEXA53     | 9.70903e-07 | 3.69e-09  |       1.03691 |

('bench_linalg.LinAlgTransposeVdot.time_vdot', '(64, 64)')
| arch          |        mean |     spread |   perf_ratios |
|:--------------|------------:|-----------:|--------------:|
| CORTEXA55     | 5.15595e-07 | 1.275e-09  |       1       |
| CORTEXX2      | 5.15845e-07 | 1.42e-09   |       1.00048 |
| NEOVERSEN1    | 5.16985e-07 | 1.67e-09   |       1.00269 |
| CORTEXX1      | 5.17154e-07 | 2.43e-09   |       1.00302 |
| ARMV8         | 5.17497e-07 | 2.03e-09   |       1.00369 |
| FALKOR        | 5.18119e-07 | 1.67e-09   |       1.00489 |
| CORTEXA76     | 5.18245e-07 | 1.23e-09   |       1.00514 |
| ARMV8SVE      | 5.18846e-07 | 1.025e-09  |       1.00631 |
| NEOVERSEV1    | 5.19546e-07 | 6.36e-09   |       1.00766 |
| CORTEXA53     | 5.19961e-07 | 1.285e-09  |       1.00847 |
| NEOVERSEN2    | 5.20361e-07 | 4.405e-09  |       1.00924 |
| THUNDERX3T110 | 5.20671e-07 | 2.045e-09  |       1.00984 |
| CORTEXA72     | 5.20689e-07 | 2.855e-09  |       1.00988 |
| THUNDERX2T99  | 5.20889e-07 | 1.6e-09    |       1.01027 |
| VORTEX        | 5.20948e-07 | 1.495e-09  |       1.01038 |
| A64FX         | 5.21269e-07 | 1.95e-09   |       1.011   |
| EMAG8180      | 5.21299e-07 | 2.67e-09   |       1.01106 |
| CORTEXA57     | 5.21318e-07 | 1.29e-09   |       1.0111  |
| THUNDERX      | 5.22445e-07 | 2.515e-09  |       1.01328 |
| TSV110        | 5.23288e-07 | 1.465e-09  |       1.01492 |
| CORTEXA73     | 5.25065e-07 | 8.88e-09   |       1.01837 |
| CORTEXA710    | 5.25067e-07 | 6.535e-09  |       1.01837 |
| CORTEXA510    | 5.25154e-07 | 4.16e-09   |       1.01854 |
| FT2000        | 5.35609e-07 | 1.1665e-08 |       1.03882 |

('bench_linalg.Linalg.time_det', "'float32'")
| arch          |        mean |      spread |   perf_ratios |
|:--------------|------------:|------------:|--------------:|
| NEOVERSEN2    | 3.72291e-05 | 8.25e-08    |       1       |
| NEOVERSEN1    | 3.88369e-05 | 1.5855e-06  |       1.04319 |
| VORTEX        | 3.89605e-05 | 1.562e-06   |       1.04651 |
| CORTEXA76     | 3.89979e-05 | 1.8465e-06  |       1.04751 |
| THUNDERX2T99  | 4.06961e-05 | 1.19e-07    |       1.09313 |
| CORTEXA55     | 4.07162e-05 | 7.8e-08     |       1.09367 |
| CORTEXA73     | 4.07597e-05 | 1.18e-07    |       1.09484 |
| EMAG8180      | 4.07828e-05 | 1.35e-07    |       1.09545 |
| CORTEXX2      | 4.08297e-05 | 3.28e-07    |       1.09671 |
| CORTEXX1      | 4.09425e-05 | 2.345e-07   |       1.09975 |
| ARMV8SVE      | 0.000127968 | 8.71965e-05 |       3.4373  |
| NEOVERSEV1    | 0.000128139 | 9.07175e-05 |       3.44192 |
| CORTEXA57     | 0.000128376 | 9.0371e-05  |       3.44827 |
| THUNDERX      | 0.000128411 | 8.73425e-05 |       3.44921 |
| CORTEXA72     | 0.000128516 | 8.7129e-05  |       3.45202 |
| ARMV8         | 0.000128756 | 8.6531e-05  |       3.45847 |
| TSV110        | 0.000129357 | 9.01695e-05 |       3.47462 |
| CORTEXA710    | 0.000129534 | 8.87675e-05 |       3.47938 |
| CORTEXA510    | 0.000130043 | 8.96295e-05 |       3.49305 |
| FALKOR        | 0.000130053 | 8.93895e-05 |       3.49331 |
| THUNDERX3T110 | 0.000130207 | 9.0401e-05  |       3.49744 |
| A64FX         | 0.000130704 | 8.9233e-05  |       3.51079 |
| CORTEXA53     | 0.000130855 | 9.22525e-05 |       3.51485 |
| FT2000        | 0.000218766 | 1.87e-06    |       5.8762  |

('bench_linalg.Linalg.time_det', "'complex128'")
| arch          |        mean |      spread |   perf_ratios |
|:--------------|------------:|------------:|--------------:|
| CORTEXA55     | 3.91256e-05 | 1.742e-06   |       1       |
| THUNDERX2T99  | 3.95905e-05 | 2.121e-06   |       1.01188 |
| CORTEXA73     | 4.03781e-05 | 2.077e-06   |       1.03201 |
| CORTEXA72     | 4.04527e-05 | 1.385e-07   |       1.03392 |
| CORTEXA510    | 4.05705e-05 | 1.255e-07   |       1.03693 |
| ARMV8         | 4.06008e-05 | 3.39e-07    |       1.03771 |
| THUNDERX      | 4.06673e-05 | 1.37e-07    |       1.0394  |
| TSV110        | 4.08915e-05 | 3.695e-07   |       1.04514 |
| FALKOR        | 4.08997e-05 | 3.905e-07   |       1.04534 |
| EMAG8180      | 4.09718e-05 | 2.145e-07   |       1.04719 |
| CORTEXX1      | 0.000127703 | 8.73805e-05 |       3.26392 |
| NEOVERSEN2    | 0.000127964 | 8.7119e-05  |       3.27059 |
| FT2000        | 0.000128283 | 8.77425e-05 |       3.27874 |
| VORTEX        | 0.000128888 | 9.1662e-05  |       3.2942  |
| CORTEXA57     | 0.000129629 | 8.9344e-05  |       3.31315 |
| CORTEXX2      | 0.000129671 | 8.95815e-05 |       3.31422 |
| CORTEXA53     | 0.00012995  | 9.03055e-05 |       3.32137 |
| NEOVERSEN1    | 0.000129996 | 8.9095e-05  |       3.32252 |
| ARMV8SVE      | 0.000129996 | 8.92825e-05 |       3.32253 |
| THUNDERX3T110 | 0.000131103 | 8.78455e-05 |       3.35083 |
| CORTEXA76     | 0.000134697 | 9.39035e-05 |       3.4427  |
| CORTEXA710    | 0.00021877  | 2.685e-06   |       5.59149 |
| A64FX         | 0.000220219 | 7.15e-07    |       5.62852 |
| NEOVERSEV1    | 0.000223852 | 8.735e-06   |       5.72137 |

('bench_linalg.Linalg.time_det', "'int16'")
| arch          |        mean |      spread |   perf_ratios |
|:--------------|------------:|------------:|--------------:|
| CORTEXX1      | 3.8786e-05  | 1.646e-06   |       1       |
| THUNDERX3T110 | 3.8867e-05  | 1.7935e-06  |       1.00209 |
| CORTEXA53     | 3.89187e-05 | 1.619e-06   |       1.00342 |
| EMAG8180      | 3.91036e-05 | 1.723e-06   |       1.00819 |
| NEOVERSEN1    | 3.94571e-05 | 1.9125e-06  |       1.0173  |
| TSV110        | 3.97733e-05 | 1.668e-06   |       1.02545 |
| CORTEXA72     | 4.05192e-05 | 8.5e-08     |       1.04469 |
| CORTEXA510    | 4.06005e-05 | 1.865e-07   |       1.04678 |
| FT2000        | 4.07028e-05 | 1.74e-07    |       1.04942 |
| THUNDERX      | 4.08854e-05 | 1.51e-07    |       1.05413 |
| THUNDERX2T99  | 4.0957e-05  | 3.7e-07     |       1.05597 |
| CORTEXA57     | 4.13264e-05 | 1.3865e-06  |       1.0655  |
| NEOVERSEV1    | 0.000126266 | 8.90655e-05 |       3.25546 |
| ARMV8         | 0.000127512 | 8.7595e-05  |       3.28757 |
| CORTEXA55     | 0.000127994 | 8.7083e-05  |       3.3     |
| ARMV8SVE      | 0.000128159 | 8.73735e-05 |       3.30426 |
| CORTEXA76     | 0.000128211 | 8.80325e-05 |       3.3056  |
| NEOVERSEN2    | 0.000128289 | 9.0673e-05  |       3.30761 |
| CORTEXA710    | 0.000128598 | 8.71745e-05 |       3.31559 |
| A64FX         | 0.000128796 | 9.1408e-05  |       3.32067 |
| CORTEXX2      | 0.000129769 | 8.9487e-05  |       3.34577 |
| VORTEX        | 0.000130183 | 8.91885e-05 |       3.35644 |
| CORTEXA73     | 0.000130961 | 8.955e-05   |       3.37651 |
| FALKOR        | 0.000216693 | 6.05e-07    |       5.58689 |

('bench_linalg.Linalg.time_det', "'int32'")
| arch          |        mean |      spread |   perf_ratios |
|:--------------|------------:|------------:|--------------:|
| CORTEXA710    | 3.89528e-05 | 1.665e-06   |       1       |
| FALKOR        | 3.90723e-05 | 1.603e-06   |       1.00307 |
| TSV110        | 3.93448e-05 | 1.9545e-06  |       1.01006 |
| CORTEXA72     | 4.03581e-05 | 2.2e-08     |       1.03608 |
| CORTEXX1      | 4.04784e-05 | 6.65e-08    |       1.03916 |
| EMAG8180      | 4.0645e-05  | 2.395e-07   |       1.04344 |
| CORTEXA57     | 4.06602e-05 | 8.95e-08    |       1.04383 |
| ARMV8         | 4.08409e-05 | 1.455e-07   |       1.04847 |
| CORTEXX2      | 4.09148e-05 | 4.855e-07   |       1.05037 |
| CORTEXA510    | 4.10104e-05 | 1.62e-07    |       1.05282 |
| CORTEXA55     | 4.10336e-05 | 2.405e-07   |       1.05342 |
| CORTEXA76     | 4.17016e-05 | 3.02e-07    |       1.07057 |
| ARMV8SVE      | 0.000126422 | 8.9627e-05  |       3.24551 |
| FT2000        | 0.000126943 | 8.96765e-05 |       3.25888 |
| NEOVERSEN2    | 0.000128121 | 8.75635e-05 |       3.28914 |
| THUNDERX      | 0.000128188 | 8.79635e-05 |       3.29085 |
| CORTEXA53     | 0.000129419 | 8.90165e-05 |       3.32245 |
| THUNDERX2T99  | 0.000130458 | 8.9435e-05  |       3.34913 |
| A64FX         | 0.000130486 | 8.9668e-05  |       3.34985 |
| VORTEX        | 0.000130742 | 8.96435e-05 |       3.35641 |
| NEOVERSEV1    | 0.000132147 | 9.16e-05    |       3.39248 |
| NEOVERSEN1    | 0.000216902 | 1.68e-06    |       5.56832 |
| CORTEXA73     | 0.000218973 | 1.135e-06   |       5.62149 |
| THUNDERX3T110 | 0.000220378 | 5.65e-07    |       5.65755 |

('bench_linalg.Linalg.time_det', "'float64'")
| arch          |        mean |      spread |   perf_ratios |
|:--------------|------------:|------------:|--------------:|
| VORTEX        | 3.91458e-05 | 1.6135e-06  |       1       |
| EMAG8180      | 3.91743e-05 | 1.6605e-06  |       1.00073 |
| FALKOR        | 3.91978e-05 | 2.2525e-06  |       1.00133 |
| THUNDERX3T110 | 3.93834e-05 | 1.8905e-06  |       1.00607 |
| CORTEXA57     | 3.96094e-05 | 1.0775e-06  |       1.01184 |
| ARMV8         | 4.04322e-05 | 5.25e-08    |       1.03286 |
| THUNDERX2T99  | 4.06091e-05 | 1.585e-07   |       1.03738 |
| CORTEXA55     | 4.07332e-05 | 1.715e-07   |       1.04055 |
| NEOVERSEN1    | 4.09647e-05 | 2.44e-07    |       1.04646 |
| THUNDERX      | 4.10673e-05 | 3.085e-07   |       1.04908 |
| FT2000        | 4.19986e-05 | 1.58e-07    |       1.07287 |
| CORTEXA72     | 0.000127579 | 8.71995e-05 |       3.25906 |
| CORTEXX1      | 0.000128021 | 9.0355e-05  |       3.27037 |
| A64FX         | 0.000128036 | 9.09975e-05 |       3.27076 |
| CORTEXA76     | 0.000128444 | 8.8434e-05  |       3.28116 |
| NEOVERSEN2    | 0.000129247 | 8.8269e-05  |       3.30169 |
| ARMV8SVE      | 0.000130086 | 8.8706e-05  |       3.32311 |
| CORTEXA53     | 0.000130421 | 8.94985e-05 |       3.33167 |
| CORTEXA710    | 0.000130485 | 8.92615e-05 |       3.3333  |
| TSV110        | 0.000131572 | 9.42805e-05 |       3.36106 |
| NEOVERSEV1    | 0.000131583 | 8.8335e-05  |       3.36134 |
| CORTEXX2      | 0.000216696 | 1.865e-06   |       5.53561 |
| CORTEXA510    | 0.000219397 | 1.235e-06   |       5.6046  |
| CORTEXA73     | 0.000220829 | 3.315e-06   |       5.64118 |

('bench_linalg.Linalg.time_det', "'complex64'")
| arch          |        mean |      spread |   perf_ratios |
|:--------------|------------:|------------:|--------------:|
| CORTEXA76     | 3.89966e-05 | 1.4775e-06  |       1       |
| CORTEXX2      | 3.93004e-05 | 2.1725e-06  |       1.00779 |
| CORTEXA73     | 3.93443e-05 | 1.8285e-06  |       1.00892 |
| CORTEXA53     | 4.0519e-05  | 2.45e-07    |       1.03904 |
| ARMV8SVE      | 4.0527e-05  | 1.37e-07    |       1.03924 |
| THUNDERX      | 4.06525e-05 | 8.1e-08     |       1.04246 |
| THUNDERX2T99  | 4.07699e-05 | 2.26e-07    |       1.04547 |
| EMAG8180      | 4.0783e-05  | 1.76e-07    |       1.04581 |
| ARMV8         | 4.08138e-05 | 3.075e-07   |       1.0466  |
| CORTEXA510    | 4.08712e-05 | 4.22e-07    |       1.04807 |
| CORTEXA710    | 4.0971e-05  | 3.83e-07    |       1.05063 |
| A64FX         | 4.13723e-05 | 1.285e-07   |       1.06092 |
| NEOVERSEN1    | 0.000127551 | 8.7589e-05  |       3.27083 |
| CORTEXA57     | 0.000127738 | 9.0884e-05  |       3.2756  |
| CORTEXA72     | 0.000127822 | 8.6871e-05  |       3.27777 |
| CORTEXA55     | 0.000128031 | 9.061e-05   |       3.28312 |
| CORTEXX1      | 0.000128114 | 8.7804e-05  |       3.28525 |
| TSV110        | 0.000128456 | 9.22335e-05 |       3.29403 |
| THUNDERX3T110 | 0.00012858  | 8.77315e-05 |       3.2972  |
| NEOVERSEV1    | 0.000128615 | 8.8334e-05  |       3.29809 |
| VORTEX        | 0.000128654 | 8.74765e-05 |       3.29911 |
| NEOVERSEN2    | 0.000129811 | 8.7561e-05  |       3.32877 |
| FT2000        | 0.000129974 | 8.937e-05   |       3.33294 |
| FALKOR        | 0.000130522 | 8.9596e-05  |       3.34701 |

('bench_linalg.Linalg.time_det', "'int64'")
| arch          |        mean |      spread |   perf_ratios |
|:--------------|------------:|------------:|--------------:|
| NEOVERSEV1    | 3.91424e-05 | 2.192e-06   |       1       |
| ARMV8         | 4.04261e-05 | 1.03e-07    |       1.0328  |
| ARMV8SVE      | 4.07329e-05 | 5.85e-08    |       1.04063 |
| NEOVERSEN2    | 4.07653e-05 | 3.275e-07   |       1.04146 |
| TSV110        | 4.0817e-05  | 4.605e-07   |       1.04278 |
| CORTEXA55     | 4.08724e-05 | 1.51e-07    |       1.0442  |
| FT2000        | 4.08965e-05 | 2.48e-07    |       1.04481 |
| THUNDERX      | 4.09481e-05 | 2.235e-07   |       1.04613 |
| CORTEXA710    | 4.0961e-05  | 1.185e-07   |       1.04646 |
| NEOVERSEN1    | 4.09646e-05 | 3.89e-07    |       1.04655 |
| CORTEXA73     | 4.11784e-05 | 2.14e-07    |       1.05202 |
| CORTEXA53     | 4.12241e-05 | 1.115e-07   |       1.05318 |
| CORTEXA72     | 0.00012794  | 9.1127e-05  |       3.26858 |
| A64FX         | 0.000128385 | 8.7915e-05  |       3.27996 |
| THUNDERX2T99  | 0.000128699 | 8.809e-05   |       3.28797 |
| THUNDERX3T110 | 0.000129682 | 9.0013e-05  |       3.31309 |
| CORTEXX1      | 0.000130006 | 8.89975e-05 |       3.32135 |
| CORTEXA510    | 0.000130087 | 8.86285e-05 |       3.32344 |
| EMAG8180      | 0.00013032  | 8.88545e-05 |       3.32938 |
| CORTEXX2      | 0.000130574 | 8.88205e-05 |       3.33587 |
| CORTEXA57     | 0.00013078  | 9.08135e-05 |       3.34115 |
| FALKOR        | 0.000132548 | 8.77195e-05 |       3.38629 |
| VORTEX        | 0.000216467 | 9.8e-07     |       5.53026 |
| CORTEXA76     | 0.000217788 | 1.255e-06   |       5.56399 |

('bench_linalg.Linalg.time_pinv', "'float32'")
| arch          |        mean |      spread |   perf_ratios |
|:--------------|------------:|------------:|--------------:|
| CORTEXA72     | 0.000951669 | 1.165e-06   |       1       |
| NEOVERSEV1    | 0.000953833 | 2.2e-06     |       1.00227 |
| THUNDERX2T99  | 0.000954278 | 3.65e-06    |       1.00274 |
| ARMV8         | 0.000955417 | 1.6525e-05  |       1.00394 |
| CORTEXX2      | 0.000955525 | 6.85e-06    |       1.00405 |
| CORTEXA55     | 0.000956384 | 7.18e-06    |       1.00496 |
| A64FX         | 0.000958176 | 5.13e-06    |       1.00684 |
| CORTEXA510    | 0.000959422 | 2.96e-06    |       1.00815 |
| CORTEXA73     | 0.000961369 | 1.1125e-05  |       1.01019 |
| TSV110        | 0.000964275 | 8.155e-06   |       1.01325 |
| EMAG8180      | 0.000969326 | 1.3815e-05  |       1.01855 |
| CORTEXA76     | 0.00171458  | 0.00082746  |       1.80166 |
| CORTEXX1      | 0.00173217  | 0.00080584  |       1.82014 |
| CORTEXA710    | 0.00174192  | 0.000790075 |       1.83039 |
| FT2000        | 0.00174833  | 0.000808235 |       1.83712 |
| ARMV8SVE      | 0.00175704  | 0.00083948  |       1.84627 |
| CORTEXA53     | 0.00176302  | 0.00078175  |       1.85255 |
| THUNDERX3T110 | 0.00176347  | 0.000826925 |       1.85303 |
| VORTEX        | 0.00178078  | 0.000832005 |       1.87121 |
| THUNDERX      | 0.00178532  | 0.00084356  |       1.87599 |
| FALKOR        | 0.00179227  | 0.00083047  |       1.88329 |
| NEOVERSEN1    | 0.00259802  | 2.63e-05    |       2.72996 |
| NEOVERSEN2    | 0.00261055  | 4.555e-05   |       2.74313 |
| CORTEXA57     | 0.00264019  | 3.945e-05   |       2.77428 |

('bench_linalg.Linalg.time_pinv', "'complex128'")
| arch          |        mean |      spread |   perf_ratios |
|:--------------|------------:|------------:|--------------:|
| CORTEXX1      | 0.000952629 | 1.305e-06   |       1       |
| NEOVERSEV1    | 0.000953172 | 4.695e-06   |       1.00057 |
| CORTEXA72     | 0.000953381 | 2.45e-06    |       1.00079 |
| CORTEXA76     | 0.000953777 | 1.805e-06   |       1.0012  |
| FT2000        | 0.000954621 | 2.9e-06     |       1.00209 |
| ARMV8SVE      | 0.00095479  | 2.685e-06   |       1.00227 |
| FALKOR        | 0.000955172 | 3.135e-06   |       1.00267 |
| THUNDERX3T110 | 0.000958661 | 2.195e-06   |       1.00633 |
| CORTEXA55     | 0.000959602 | 7.2e-06     |       1.00732 |
| CORTEXX2      | 0.000967816 | 8.77e-06    |       1.01594 |
| NEOVERSEN1    | 0.00169505  | 0.000842445 |       1.77934 |
| ARMV8         | 0.00173771  | 0.000819195 |       1.82412 |
| THUNDERX2T99  | 0.00174426  | 0.00080446  |       1.831   |
| CORTEXA710    | 0.00176292  | 0.00083219  |       1.85059 |
| VORTEX        | 0.00176298  | 0.000822345 |       1.85065 |
| CORTEXA510    | 0.00176685  | 0.00082216  |       1.85471 |
| NEOVERSEN2    | 0.00176699  | 0.000826355 |       1.85486 |
| CORTEXA53     | 0.0017727   | 0.000835215 |       1.86085 |
| CORTEXA73     | 0.0017811   | 0.00084959  |       1.86967 |
| CORTEXA57     | 0.00178772  | 0.00085328  |       1.87662 |
| EMAG8180      | 0.00179459  | 0.00085414  |       1.88383 |
| A64FX         | 0.00260207  | 3.76e-05    |       2.73146 |
| TSV110        | 0.0026372   | 3.24e-05    |       2.76834 |
| THUNDERX      | 0.00266897  | 5.05e-05    |       2.80169 |

('bench_linalg.Linalg.time_pinv', "'int16'")
| arch          |        mean |      spread |   perf_ratios |
|:--------------|------------:|------------:|--------------:|
| ARMV8         | 0.000937235 | 4.035e-06   |       1       |
| NEOVERSEN1    | 0.000952989 | 1.77e-06    |       1.01681 |
| EMAG8180      | 0.000953034 | 1.335e-06   |       1.01686 |
| CORTEXA72     | 0.000953453 | 4.79e-06    |       1.0173  |
| ARMV8SVE      | 0.000953712 | 1.815e-06   |       1.01758 |
| CORTEXA57     | 0.000956305 | 2.77e-06    |       1.02035 |
| CORTEXA710    | 0.000956841 | 3.71e-06    |       1.02092 |
| CORTEXX1      | 0.000959593 | 3.215e-06   |       1.02386 |
| VORTEX        | 0.000962375 | 1.739e-05   |       1.02682 |
| NEOVERSEV1    | 0.000966288 | 2.178e-05   |       1.031   |
| TSV110        | 0.00096958  | 2.3175e-05  |       1.03451 |
| CORTEXA55     | 0.00172872  | 0.000838065 |       1.84449 |
| CORTEXA510    | 0.0017315   | 0.00078818  |       1.84746 |
| A64FX         | 0.00173543  | 0.00079504  |       1.85165 |
| THUNDERX      | 0.00174601  | 0.00079074  |       1.86293 |
| THUNDERX3T110 | 0.00174912  | 0.000832125 |       1.86626 |
| FALKOR        | 0.00175291  | 0.000846965 |       1.8703  |
| FT2000        | 0.00175697  | 0.00081899  |       1.87463 |
| CORTEXX2      | 0.00177767  | 0.00084406  |       1.89672 |
| CORTEXA73     | 0.00178251  | 0.000829785 |       1.90188 |
| CORTEXA76     | 0.00178912  | 0.000807485 |       1.90893 |
| CORTEXA53     | 0.00180215  | 0.0008157   |       1.92283 |
| THUNDERX2T99  | 0.00257625  | 3.15e-05    |       2.74878 |
| NEOVERSEN2    | 0.00259253  | 4.31e-05    |       2.76615 |

('bench_linalg.Linalg.time_pinv', "'int32'")
| arch          |        mean |      spread |   perf_ratios |
|:--------------|------------:|------------:|--------------:|
| NEOVERSEN1    | 0.000953062 | 2.605e-06   |       1       |
| CORTEXA55     | 0.000953206 | 1.755e-06   |       1.00015 |
| CORTEXX2      | 0.000953578 | 1.7295e-05  |       1.00054 |
| A64FX         | 0.000954858 | 6.515e-06   |       1.00188 |
| TSV110        | 0.000959434 | 6.15e-06    |       1.00669 |
| CORTEXA57     | 0.000960805 | 8.155e-06   |       1.00812 |
| FT2000        | 0.00096165  | 3.745e-06   |       1.00901 |
| CORTEXA76     | 0.000961674 | 5.275e-06   |       1.00904 |
| FALKOR        | 0.00173577  | 0.00079737  |       1.82126 |
| NEOVERSEV1    | 0.00174013  | 0.000806405 |       1.82583 |
| THUNDERX2T99  | 0.00175131  | 0.0008772   |       1.83756 |
| CORTEXX1      | 0.0017515   | 0.000835485 |       1.83776 |
| CORTEXA510    | 0.00175396  | 0.000817005 |       1.84034 |
| EMAG8180      | 0.0017575   | 0.00082325  |       1.84406 |
| ARMV8         | 0.00176191  | 0.000855005 |       1.84868 |
| THUNDERX3T110 | 0.0017677   | 0.00081731  |       1.85476 |
| CORTEXA53     | 0.00176801  | 0.000817415 |       1.85508 |
| VORTEX        | 0.00176891  | 0.0008265   |       1.85603 |
| CORTEXA72     | 0.0017716   | 0.00083541  |       1.85885 |
| NEOVERSEN2    | 0.00177337  | 0.000834885 |       1.8607  |
| CORTEXA710    | 0.00178454  | 0.000856445 |       1.87243 |
| THUNDERX      | 0.00178898  | 0.000833945 |       1.87708 |
| ARMV8SVE      | 0.00180154  | 0.00084621  |       1.89026 |
| CORTEXA73     | 0.00265417  | 6.53e-05    |       2.78488 |

('bench_linalg.Linalg.time_pinv', "'float64'")
| arch          |        mean |      spread |   perf_ratios |
|:--------------|------------:|------------:|--------------:|
| TSV110        | 0.000951875 | 6.85e-06    |       1       |
| NEOVERSEN1    | 0.00095218  | 3.695e-06   |       1.00032 |
| CORTEXA55     | 0.000953445 | 3.465e-06   |       1.00165 |
| ARMV8         | 0.000955894 | 5.43e-06    |       1.00422 |
| CORTEXA73     | 0.000955979 | 1.785e-06   |       1.00431 |
| CORTEXX1      | 0.000956786 | 1.62e-06    |       1.00516 |
| THUNDERX2T99  | 0.000957517 | 1.875e-06   |       1.00593 |
| THUNDERX      | 0.000957723 | 2.735e-06   |       1.00614 |
| FALKOR        | 0.000960371 | 7.44e-06    |       1.00893 |
| CORTEXA76     | 0.000963985 | 4.01e-06    |       1.01272 |
| CORTEXA53     | 0.000964328 | 9.585e-06   |       1.01308 |
| CORTEXX2      | 0.000964434 | 8.62e-06    |       1.01319 |
| NEOVERSEV1    | 0.000981159 | 2.5845e-05  |       1.03076 |
| VORTEX        | 0.00173342  | 0.000793725 |       1.82106 |
| CORTEXA72     | 0.00173856  | 0.000814025 |       1.82646 |
| NEOVERSEN2    | 0.00174152  | 0.00078799  |       1.82956 |
| A64FX         | 0.00174895  | 0.000815745 |       1.83738 |
| THUNDERX3T110 | 0.00175367  | 0.00083513  |       1.84234 |
| ARMV8SVE      | 0.00176126  | 0.0008409   |       1.85031 |
| CORTEXA510    | 0.00177461  | 0.00085445  |       1.86434 |
| CORTEXA57     | 0.00178784  | 0.000825885 |       1.87822 |
| FT2000        | 0.00179908  | 0.00084654  |       1.89004 |
| EMAG8180      | 0.0025579   | 3.355e-05   |       2.68722 |
| CORTEXA710    | 0.00260811  | 3.48e-05    |       2.73998 |

('bench_linalg.Linalg.time_pinv', "'complex64'")
| arch          |        mean |      spread |   perf_ratios |
|:--------------|------------:|------------:|--------------:|
| ARMV8         | 0.000946614 | 1.321e-05   |       1       |
| NEOVERSEN2    | 0.000954131 | 5.19e-06    |       1.00794 |
| NEOVERSEN1    | 0.000954225 | 3.515e-06   |       1.00804 |
| CORTEXA710    | 0.000954852 | 3.755e-06   |       1.0087  |
| TSV110        | 0.000955756 | 2.485e-06   |       1.00966 |
| NEOVERSEV1    | 0.000957447 | 5.965e-06   |       1.01144 |
| THUNDERX2T99  | 0.000957875 | 2.32e-06    |       1.0119  |
| THUNDERX      | 0.000958953 | 2.935e-06   |       1.01303 |
| CORTEXA73     | 0.000960218 | 9.54e-06    |       1.01437 |
| VORTEX        | 0.000961602 | 3.485e-06   |       1.01583 |
| CORTEXA76     | 0.00096189  | 1.0355e-05  |       1.01614 |
| A64FX         | 0.000964953 | 5.77e-06    |       1.01937 |
| CORTEXA53     | 0.000972451 | 3.412e-05   |       1.02729 |
| THUNDERX3T110 | 0.00171579  | 0.000804385 |       1.81255 |
| ARMV8SVE      | 0.00174049  | 0.00082705  |       1.83865 |
| CORTEXA55     | 0.00175963  | 0.00083964  |       1.85887 |
| EMAG8180      | 0.00175985  | 0.00081122  |       1.8591  |
| CORTEXA510    | 0.00176735  | 0.000808865 |       1.86702 |
| CORTEXA57     | 0.00176879  | 0.0008454   |       1.86855 |
| FALKOR        | 0.00177631  | 0.000844325 |       1.87649 |
| CORTEXX2      | 0.00178946  | 0.000794815 |       1.89038 |
| FT2000        | 0.00179205  | 0.000849965 |       1.89311 |
| CORTEXA72     | 0.00179447  | 0.0008345   |       1.89567 |
| CORTEXX1      | 0.0025661   | 4.02e-05    |       2.71083 |

('bench_linalg.Linalg.time_pinv', "'int64'")
| arch          |        mean |      spread |   perf_ratios |
|:--------------|------------:|------------:|--------------:|
| ARMV8         | 0.000946778 | 2.425e-06   |       1       |
| CORTEXA72     | 0.000951589 | 1.99e-06    |       1.00508 |
| CORTEXX2      | 0.000951741 | 1.049e-05   |       1.00524 |
| ARMV8SVE      | 0.000953975 | 2.79e-06    |       1.0076  |
| CORTEXA710    | 0.000955646 | 3.65e-06    |       1.00937 |
| TSV110        | 0.000956303 | 4.155e-06   |       1.01006 |
| VORTEX        | 0.000957754 | 5.345e-06   |       1.01159 |
| CORTEXA510    | 0.000958947 | 4.635e-06   |       1.01285 |
| FT2000        | 0.000959242 | 1.26e-06    |       1.01316 |
| FALKOR        | 0.000960602 | 3.915e-06   |       1.0146  |
| THUNDERX2T99  | 0.00173909  | 0.000808855 |       1.83685 |
| CORTEXA53     | 0.00175298  | 0.000800475 |       1.85152 |
| CORTEXA55     | 0.00176231  | 0.000843925 |       1.86138 |
| NEOVERSEN1    | 0.00176545  | 0.000818925 |       1.86469 |
| NEOVERSEV1    | 0.00176619  | 0.000818495 |       1.86547 |
| THUNDERX3T110 | 0.00177246  | 0.00083495  |       1.8721  |
| CORTEXX1      | 0.00177624  | 0.000816375 |       1.87609 |
| THUNDERX      | 0.00177884  | 0.000820675 |       1.87883 |
| CORTEXA76     | 0.00178957  | 0.000851585 |       1.89017 |
| CORTEXA57     | 0.00179766  | 0.000834205 |       1.89871 |
| NEOVERSEN2    | 0.00180249  | 0.00086268  |       1.90381 |
| EMAG8180      | 0.00263462  | 3.045e-05   |       2.78273 |
| CORTEXA73     | 0.00264117  | 3.965e-05   |       2.78964 |
| A64FX         | 0.00264977  | 6.22e-05    |       2.79872 |

('bench_linalg.Linalg.time_svd', "'float32'")
| arch          |        mean |      spread |   perf_ratios |
|:--------------|------------:|------------:|--------------:|
| ARMV8         | 0.000906137 | 9.44e-06    |       1       |
| ARMV8SVE      | 0.000922023 | 4.105e-06   |       1.01753 |
| CORTEXA73     | 0.00092242  | 1.33e-06    |       1.01797 |
| CORTEXA76     | 0.00092504  | 2.65e-06    |       1.02086 |
| CORTEXA510    | 0.000925604 | 5.24e-06    |       1.02148 |
| CORTEXA55     | 0.000927316 | 4.515e-06   |       1.02337 |
| FALKOR        | 0.000927847 | 3.045e-06   |       1.02396 |
| THUNDERX3T110 | 0.000927894 | 2.025e-06   |       1.02401 |
| CORTEXA710    | 0.000929794 | 2.295e-06   |       1.02611 |
| NEOVERSEN1    | 0.000930347 | 4.31e-06    |       1.02672 |
| THUNDERX      | 0.000930352 | 6.935e-06   |       1.02672 |
| CORTEXA53     | 0.000931841 | 1.79e-06    |       1.02837 |
| FT2000        | 0.000935682 | 2.18e-06    |       1.03261 |
| THUNDERX2T99  | 0.000936042 | 2.82e-06    |       1.033   |
| A64FX         | 0.000938064 | 9.51e-06    |       1.03523 |
| EMAG8180      | 0.000940362 | 2.065e-06   |       1.03777 |
| CORTEXA57     | 0.000957229 | 2.835e-06   |       1.05638 |
| CORTEXA72     | 0.00181517  | 0.00091971  |       2.0032  |
| CORTEXX1      | 0.0018227   | 0.000897485 |       2.0115  |
| NEOVERSEN2    | 0.0018243   | 0.00089588  |       2.01328 |
| NEOVERSEV1    | 0.00184165  | 0.0009127   |       2.03242 |
| CORTEXX2      | 0.00184822  | 0.00092895  |       2.03966 |
| VORTEX        | 0.00185978  | 0.000970105 |       2.05242 |
| TSV110        | 0.00192217  | 0.00111077  |       2.12128 |

('bench_linalg.Linalg.time_svd', "'complex128'")
| arch          |        mean |      spread |   perf_ratios |
|:--------------|------------:|------------:|--------------:|
| ARMV8         | 0.000912944 | 9.63e-06    |       1       |
| VORTEX        | 0.000921708 | 3.305e-06   |       1.0096  |
| CORTEXX1      | 0.000923189 | 2.96e-06    |       1.01122 |
| ARMV8SVE      | 0.000923367 | 3.785e-06   |       1.01142 |
| CORTEXA73     | 0.000925977 | 1.81e-06    |       1.01428 |
| TSV110        | 0.000927506 | 4.575e-06   |       1.01595 |
| NEOVERSEN1    | 0.00093061  | 3.835e-06   |       1.01935 |
| CORTEXA510    | 0.00093133  | 5.385e-06   |       1.02014 |
| THUNDERX3T110 | 0.000931917 | 3.38e-06    |       1.02078 |
| CORTEXA76     | 0.000934297 | 5.54e-06    |       1.02339 |
| CORTEXX2      | 0.000934877 | 8.64e-06    |       1.02402 |
| CORTEXA57     | 0.000935292 | 5.82e-06    |       1.02448 |
| A64FX         | 0.00093583  | 4.51e-06    |       1.02507 |
| EMAG8180      | 0.00181457  | 0.0009165   |       1.98761 |
| NEOVERSEV1    | 0.00182082  | 0.000911595 |       1.99445 |
| FALKOR        | 0.00182534  | 0.000916435 |       1.9994  |
| CORTEXA53     | 0.0018275   | 0.00090814  |       2.00177 |
| CORTEXA710    | 0.00183167  | 0.000912695 |       2.00634 |
| FT2000        | 0.00186209  | 0.00097474  |       2.03965 |
| NEOVERSEN2    | 0.00186334  | 0.00093121  |       2.04103 |
| THUNDERX2T99  | 0.00188129  | 0.000984835 |       2.06069 |
| THUNDERX      | 0.00189272  | 0.00099697  |       2.0732  |
| CORTEXA55     | 0.00190085  | 0.00099472  |       2.08211 |
| CORTEXA72     | 0.00282509  | 9.885e-05   |       3.09449 |

('bench_linalg.Linalg.time_svd', "'int16'")
| arch          |        mean |      spread |   perf_ratios |
|:--------------|------------:|------------:|--------------:|
| CORTEXX2      | 0.000922884 | 4.015e-06   |       1       |
| THUNDERX2T99  | 0.000926686 | 2.56e-06    |       1.00412 |
| THUNDERX      | 0.000928714 | 5.25e-06    |       1.00632 |
| FALKOR        | 0.000928947 | 3.1e-06     |       1.00657 |
| CORTEXA510    | 0.000929403 | 2.72e-06    |       1.00706 |
| CORTEXA76     | 0.000930759 | 2.025e-06   |       1.00853 |
| NEOVERSEN2    | 0.00093971  | 6.8e-07     |       1.01823 |
| THUNDERX3T110 | 0.000939977 | 1.4e-05     |       1.01852 |
| CORTEXA73     | 0.000941782 | 1.1055e-05  |       1.02048 |
| CORTEXA55     | 0.000956119 | 2.47e-05    |       1.03601 |
| ARMV8         | 0.00182148  | 0.000939755 |       1.97368 |
| CORTEXA710    | 0.00184505  | 0.00095866  |       1.99922 |
| NEOVERSEV1    | 0.00185093  | 0.00092564  |       2.00559 |
| CORTEXA72     | 0.00185272  | 0.000941585 |       2.00753 |
| FT2000        | 0.00186413  | 0.0009976   |       2.0199  |
| ARMV8SVE      | 0.00187153  | 0.000995415 |       2.02791 |
| NEOVERSEN1    | 0.0018729   | 0.00100148  |       2.02939 |
| CORTEXA53     | 0.00188238  | 0.00099761  |       2.03966 |
| EMAG8180      | 0.00190358  | 0.000999905 |       2.06264 |
| A64FX         | 0.00191349  | 0.00100209  |       2.07338 |
| CORTEXA57     | 0.00192179  | 0.00100471  |       2.08238 |
| TSV110        | 0.00265922  | 0.0002655   |       2.88143 |
| CORTEXX1      | 0.00278056  | 5.835e-05   |       3.0129  |
| VORTEX        | 0.00279417  | 8.46e-05    |       3.02765 |

('bench_linalg.Linalg.time_svd', "'int32'")
| arch          |        mean |      spread |   perf_ratios |
|:--------------|------------:|------------:|--------------:|
| ARMV8SVE      | 0.000920462 | 2.575e-06   |       1       |
| CORTEXA73     | 0.000920485 | 4.425e-06   |       1.00003 |
| NEOVERSEN1    | 0.000923205 | 3.775e-06   |       1.00298 |
| THUNDERX2T99  | 0.000924557 | 2.98e-06    |       1.00445 |
| THUNDERX3T110 | 0.000925324 | 3.285e-06   |       1.00528 |
| CORTEXX1      | 0.000926341 | 4.225e-06   |       1.00639 |
| FT2000        | 0.000926926 | 3.2e-06     |       1.00702 |
| A64FX         | 0.000927972 | 2.61e-06    |       1.00816 |
| VORTEX        | 0.000929879 | 5.375e-06   |       1.01023 |
| FALKOR        | 0.000930027 | 5.215e-06   |       1.01039 |
| THUNDERX      | 0.000930555 | 4.335e-06   |       1.01097 |
| CORTEXA53     | 0.000934771 | 5.935e-06   |       1.01555 |
| NEOVERSEV1    | 0.00181037  | 0.000906245 |       1.9668  |
| CORTEXA55     | 0.00181685  | 0.00089566  |       1.97384 |
| ARMV8         | 0.00182759  | 0.00091476  |       1.98551 |
| CORTEXA57     | 0.00185627  | 0.000981195 |       2.01667 |
| NEOVERSEN2    | 0.00186047  | 0.00094793  |       2.02124 |
| CORTEXA510    | 0.00187205  | 0.000994605 |       2.03381 |
| CORTEXA76     | 0.0018756   | 0.00096101  |       2.03768 |
| EMAG8180      | 0.00188308  | 0.00098082  |       2.0458  |
| TSV110        | 0.00189575  | 0.0010214   |       2.05956 |
| CORTEXX2      | 0.00190495  | 0.000966905 |       2.06956 |
| CORTEXA710    | 0.00191892  | 0.00101272  |       2.08473 |
| CORTEXA72     | 0.00285984  | 5.18e-05    |       3.10696 |

('bench_linalg.Linalg.time_svd', "'float64'")
| arch          |        mean |      spread |   perf_ratios |
|:--------------|------------:|------------:|--------------:|
| CORTEXA72     | 0.000921148 | 1.36e-06    |       1       |
| ARMV8         | 0.000922439 | 9.305e-06   |       1.0014  |
| CORTEXA510    | 0.000925047 | 3.18e-06    |       1.00423 |
| NEOVERSEN1    | 0.000926845 | 1.755e-06   |       1.00618 |
| ARMV8SVE      | 0.000927903 | 6.805e-06   |       1.00733 |
| THUNDERX      | 0.000930009 | 4.11e-06    |       1.00962 |
| NEOVERSEN2    | 0.000939263 | 6.15e-06    |       1.01967 |
| A64FX         | 0.000939951 | 1.099e-05   |       1.02041 |
| FALKOR        | 0.000980038 | 6.499e-05   |       1.06393 |
| THUNDERX3T110 | 0.00178335  | 0.000950905 |       1.93601 |
| CORTEXX2      | 0.00179398  | 0.0008814   |       1.94754 |
| TSV110        | 0.00182039  | 0.000911955 |       1.97622 |
| FT2000        | 0.00182207  | 0.000935035 |       1.97805 |
| VORTEX        | 0.00182436  | 0.00091451  |       1.98053 |
| NEOVERSEV1    | 0.00184145  | 0.00093032  |       1.99908 |
| CORTEXA76     | 0.00184723  | 0.00089918  |       2.00536 |
| THUNDERX2T99  | 0.00184804  | 0.000942945 |       2.00624 |
| CORTEXA710    | 0.00189561  | 0.00097456  |       2.05788 |
| CORTEXA73     | 0.00189706  | 0.00099368  |       2.05945 |
| EMAG8180      | 0.00193484  | 0.00100597  |       2.10047 |
| CORTEXA57     | 0.00194316  | 0.00098958  |       2.10949 |
| CORTEXA53     | 0.00285453  | 4.555e-05   |       3.09888 |
| CORTEXA55     | 0.00287331  | 5.4e-05     |       3.11927 |
| CORTEXX1      | 0.00288361  | 4.565e-05   |       3.13045 |

('bench_linalg.Linalg.time_svd', "'complex64'")
| arch          |        mean |      spread |   perf_ratios |
|:--------------|------------:|------------:|--------------:|
| CORTEXA73     | 0.000922142 | 2.44e-06    |       1       |
| EMAG8180      | 0.000924116 | 1.54e-06    |       1.00214 |
| CORTEXA72     | 0.000924884 | 2.06e-06    |       1.00297 |
| THUNDERX3T110 | 0.000926089 | 2.35e-06    |       1.00428 |
| FT2000        | 0.000926367 | 4.095e-06   |       1.00458 |
| NEOVERSEN2    | 0.000926904 | 8.51e-06    |       1.00516 |
| TSV110        | 0.000928066 | 4.725e-06   |       1.00642 |
| ARMV8SVE      | 0.000930411 | 1.495e-06   |       1.00897 |
| CORTEXA76     | 0.000931778 | 1.341e-05   |       1.01045 |
| CORTEXX1      | 0.000932292 | 2.31e-06    |       1.01101 |
| CORTEXA53     | 0.000936958 | 3.62e-06    |       1.01607 |
| A64FX         | 0.000939769 | 1.3495e-05  |       1.01912 |
| ARMV8         | 0.00179177  | 0.0009378   |       1.94305 |
| CORTEXA55     | 0.00182905  | 0.000919105 |       1.98348 |
| FALKOR        | 0.00184629  | 0.000948495 |       2.00218 |
| CORTEXX2      | 0.00184993  | 0.000938955 |       2.00612 |
| VORTEX        | 0.00186363  | 0.000973535 |       2.02098 |
| CORTEXA510    | 0.00187077  | 0.000979505 |       2.02872 |
| NEOVERSEN1    | 0.00188035  | 0.000991335 |       2.03912 |
| THUNDERX      | 0.00188436  | 0.00097085  |       2.04346 |
| CORTEXA710    | 0.00189109  | 0.00100241  |       2.05076 |
| NEOVERSEV1    | 0.00190136  | 0.00100565  |       2.06189 |
| THUNDERX2T99  | 0.00194158  | 0.00103442  |       2.10551 |
| CORTEXA57     | 0.00292523  | 0.0001183   |       3.17221 |

('bench_linalg.Linalg.time_svd', "'int64'")
| arch          |        mean |      spread |   perf_ratios |
|:--------------|------------:|------------:|--------------:|
| NEOVERSEV1    | 0.000924161 | 1.195e-06   |       1       |
| CORTEXA53     | 0.000924227 | 2.385e-06   |       1.00007 |
| FALKOR        | 0.000925102 | 3.975e-06   |       1.00102 |
| EMAG8180      | 0.000926936 | 5.6e-06     |       1.003   |
| THUNDERX3T110 | 0.000928652 | 5.005e-06   |       1.00486 |
| FT2000        | 0.000928981 | 4.415e-06   |       1.00522 |
| THUNDERX2T99  | 0.000929509 | 3.53e-06    |       1.00579 |
| THUNDERX      | 0.000929538 | 3.215e-06   |       1.00582 |
| CORTEXA55     | 0.000930729 | 2.29e-06    |       1.00711 |
| NEOVERSEN1    | 0.000933072 | 1.0905e-05  |       1.00964 |
| NEOVERSEN2    | 0.000934534 | 8.165e-06   |       1.01122 |
| CORTEXX1      | 0.000937881 | 5.735e-06   |       1.01485 |
| TSV110        | 0.000940362 | 1.783e-05   |       1.01753 |
| VORTEX        | 0.000941655 | 1.2875e-05  |       1.01893 |
| CORTEXA710    | 0.000943174 | 2.0075e-05  |       1.02057 |
| ARMV8         | 0.00181207  | 0.00091994  |       1.96077 |
| ARMV8SVE      | 0.00183002  | 0.000923455 |       1.9802  |
| CORTEXA72     | 0.0018691   | 0.00100329  |       2.02248 |
| CORTEXA57     | 0.00187461  | 0.0009502   |       2.02845 |
| CORTEXX2      | 0.00188483  | 0.00098563  |       2.03951 |
| CORTEXA76     | 0.00189832  | 0.00100172  |       2.0541  |
| A64FX         | 0.00191697  | 0.00100927  |       2.07429 |
| CORTEXA510    | 0.00287903  | 8.74e-05    |       3.11529 |
| CORTEXA73     | 0.00288268  | 5.26e-05    |       3.11924 |

('bench_linalg.LinalgNorm.time_norm', "'int16'")
| arch          |        mean |     spread |   perf_ratios |
|:--------------|------------:|-----------:|--------------:|
| CORTEXX2      | 6.75383e-06 | 1.6225e-07 |       1       |
| CORTEXA72     | 6.8169e-06  | 5.12e-08   |       1.00934 |
| NEOVERSEN1    | 6.89174e-06 | 2.111e-07  |       1.02042 |
| NEOVERSEV1    | 6.93325e-06 | 1.753e-07  |       1.02657 |
| ARMV8SVE      | 6.93596e-06 | 2.887e-07  |       1.02697 |
| ARMV8         | 6.93795e-06 | 2.117e-07  |       1.02726 |
| CORTEXX1      | 6.94222e-06 | 2.4805e-07 |       1.02789 |
| CORTEXA710    | 6.96828e-06 | 3.8945e-07 |       1.03175 |
| CORTEXA57     | 6.99536e-06 | 1.344e-07  |       1.03576 |
| CORTEXA53     | 7.15328e-06 | 2.6405e-07 |       1.05914 |
| A64FX         | 7.17898e-06 | 1.313e-07  |       1.06295 |
| CORTEXA510    | 7.20875e-06 | 2.7005e-07 |       1.06736 |
| FALKOR        | 7.27506e-06 | 3.4895e-07 |       1.07718 |
| TSV110        | 7.28095e-06 | 2.767e-07  |       1.07805 |
| CORTEXA76     | 7.29804e-06 | 2.994e-07  |       1.08058 |
| THUNDERX2T99  | 7.33251e-06 | 1.6405e-07 |       1.08568 |
| THUNDERX3T110 | 7.33984e-06 | 1.641e-07  |       1.08677 |
| CORTEXA73     | 7.35106e-06 | 1.4395e-07 |       1.08843 |
| NEOVERSEN2    | 7.36348e-06 | 3.5145e-07 |       1.09027 |
| VORTEX        | 7.38254e-06 | 1.986e-07  |       1.09309 |
| EMAG8180      | 7.40484e-06 | 3.525e-07  |       1.09639 |
| FT2000        | 7.42904e-06 | 2.4685e-07 |       1.09997 |
| THUNDERX      | 7.46718e-06 | 2.083e-07  |       1.10562 |
| CORTEXA55     | 7.64403e-06 | 2.651e-07  |       1.13181 |

('bench_linalg.LinalgNorm.time_norm', "'float16'")
| arch          |        mean |    spread |   perf_ratios |
|:--------------|------------:|----------:|--------------:|
| ARMV8         | 2.20597e-05 | 2.85e-08  |       1       |
| CORTEXA55     | 2.25663e-05 | 1.95e-07  |       1.02297 |
| CORTEXX1      | 2.26462e-05 | 2.62e-07  |       1.02659 |
| EMAG8180      | 2.26577e-05 | 2.35e-08  |       1.02711 |
| NEOVERSEV1    | 2.26652e-05 | 4.85e-08  |       1.02745 |
| CORTEXX2      | 2.26704e-05 | 7e-09     |       1.02768 |
| CORTEXA710    | 2.26741e-05 | 8.5e-09   |       1.02785 |
| CORTEXA72     | 2.26795e-05 | 5.5e-09   |       1.0281  |
| CORTEXA57     | 2.26896e-05 | 2.9e-08   |       1.02855 |
| FALKOR        | 2.26987e-05 | 7.45e-08  |       1.02897 |
| NEOVERSEN1    | 2.27249e-05 | 4.55e-08  |       1.03015 |
| CORTEXA76     | 2.27286e-05 | 3.15e-08  |       1.03032 |
| FT2000        | 2.27431e-05 | 5.8e-08   |       1.03098 |
| ARMV8SVE      | 2.275e-05   | 5.9e-08   |       1.03129 |
| NEOVERSEN2    | 2.27643e-05 | 9.65e-08  |       1.03194 |
| TSV110        | 2.27869e-05 | 1.04e-07  |       1.03297 |
| CORTEXA73     | 2.28145e-05 | 7.05e-08  |       1.03422 |
| CORTEXA510    | 2.28284e-05 | 9.7e-08   |       1.03485 |
| VORTEX        | 2.28656e-05 | 4.9e-08   |       1.03654 |
| THUNDERX      | 2.28659e-05 | 5.05e-08  |       1.03655 |
| A64FX         | 2.28704e-05 | 4.1e-08   |       1.03675 |
| THUNDERX2T99  | 2.28848e-05 | 8.9e-08   |       1.0374  |
| THUNDERX3T110 | 2.29223e-05 | 5.55e-08  |       1.0391  |
| CORTEXA53     | 2.32803e-05 | 5.775e-07 |       1.05533 |

('bench_linalg.LinalgNorm.time_norm', "'int32'")
| arch          |        mean |     spread |   perf_ratios |
|:--------------|------------:|-----------:|--------------:|
| ARMV8         | 6.69848e-06 | 4.015e-08  |       1       |
| CORTEXA710    | 6.74426e-06 | 7.31e-08   |       1.00683 |
| NEOVERSEN1    | 6.75924e-06 | 7.67e-08   |       1.00907 |
| ARMV8SVE      | 6.7684e-06  | 1.2685e-07 |       1.01044 |
| CORTEXX1      | 6.77381e-06 | 1.465e-08  |       1.01125 |
| EMAG8180      | 6.78153e-06 | 1.895e-08  |       1.0124  |
| FT2000        | 6.80055e-06 | 4.535e-08  |       1.01524 |
| CORTEXX2      | 6.81178e-06 | 1.3285e-07 |       1.01692 |
| NEOVERSEV1    | 6.81415e-06 | 6.07e-08   |       1.01727 |
| CORTEXA55     | 6.81445e-06 | 7.91e-08   |       1.01731 |
| TSV110        | 6.81944e-06 | 5.59e-08   |       1.01806 |
| CORTEXA72     | 6.82288e-06 | 5.25e-08   |       1.01857 |
| CORTEXA73     | 6.82904e-06 | 8.83e-08   |       1.01949 |
| CORTEXA53     | 6.83065e-06 | 7.815e-08  |       1.01973 |
| FALKOR        | 6.84247e-06 | 2.015e-08  |       1.0215  |
| CORTEXA510    | 6.84438e-06 | 5.53e-08   |       1.02178 |
| NEOVERSEN2    | 6.84667e-06 | 5.675e-08  |       1.02212 |
| A64FX         | 6.86138e-06 | 4.515e-08  |       1.02432 |
| THUNDERX2T99  | 6.87592e-06 | 7.935e-08  |       1.02649 |
| THUNDERX      | 6.9134e-06  | 5.605e-08  |       1.03209 |
| CORTEXA57     | 6.92037e-06 | 9.015e-08  |       1.03313 |
| CORTEXA76     | 6.92709e-06 | 5.37e-08   |       1.03413 |
| VORTEX        | 6.94273e-06 | 6.295e-08  |       1.03646 |
| THUNDERX3T110 | 6.94551e-06 | 5.905e-08  |       1.03688 |

('bench_linalg.LinalgNorm.time_norm', "'float32'")
| arch          |        mean |    spread |   perf_ratios |
|:--------------|------------:|----------:|--------------:|
| ARMV8         | 4.45625e-06 | 1.98e-08  |       1       |
| CORTEXX2      | 4.49915e-06 | 1.31e-08  |       1.00963 |
| NEOVERSEN1    | 4.50414e-06 | 1.575e-08 |       1.01075 |
| CORTEXA55     | 4.50515e-06 | 1.135e-08 |       1.01097 |
| EMAG8180      | 4.50618e-06 | 8.25e-09  |       1.01121 |
| CORTEXA73     | 4.51075e-06 | 3.795e-08 |       1.01223 |
| NEOVERSEV1    | 4.51102e-06 | 5.45e-09  |       1.01229 |
| CORTEXX1      | 4.51392e-06 | 2.985e-08 |       1.01294 |
| CORTEXA53     | 4.51761e-06 | 7.15e-09  |       1.01377 |
| FALKOR        | 4.52178e-06 | 1.72e-08  |       1.01471 |
| CORTEXA72     | 4.52469e-06 | 6e-09     |       1.01536 |
| THUNDERX      | 4.52595e-06 | 1.88e-08  |       1.01564 |
| CORTEXA57     | 4.52673e-06 | 1.45e-08  |       1.01582 |
| TSV110        | 4.52858e-06 | 2.335e-08 |       1.01623 |
| A64FX         | 4.52899e-06 | 2.78e-08  |       1.01632 |
| THUNDERX2T99  | 4.52952e-06 | 2.145e-08 |       1.01644 |
| CORTEXA510    | 4.5341e-06  | 1.37e-08  |       1.01747 |
| ARMV8SVE      | 4.53469e-06 | 2.375e-08 |       1.0176  |
| FT2000        | 4.53908e-06 | 2.105e-08 |       1.01859 |
| VORTEX        | 4.54163e-06 | 1.73e-08  |       1.01916 |
| NEOVERSEN2    | 4.54647e-06 | 1.43e-08  |       1.02025 |
| CORTEXA76     | 4.55038e-06 | 3.71e-08  |       1.02112 |
| CORTEXA710    | 4.55317e-06 | 1.945e-08 |       1.02175 |
| THUNDERX3T110 | 4.5649e-06  | 1.665e-08 |       1.02438 |

('bench_linalg.LinalgNorm.time_norm', "'int64'")
| arch          |        mean |    spread |   perf_ratios |
|:--------------|------------:|----------:|--------------:|
| ARMV8         | 7.30532e-06 | 9.09e-08  |       1       |
| CORTEXA510    | 7.34098e-06 | 1.03e-08  |       1.00488 |
| CORTEXA72     | 7.34688e-06 | 2.795e-08 |       1.00569 |
| CORTEXX1      | 7.36485e-06 | 1.305e-08 |       1.00815 |
| CORTEXX2      | 7.3757e-06  | 8.8e-09   |       1.00963 |
| NEOVERSEN1    | 7.38649e-06 | 4.24e-08  |       1.01111 |
| A64FX         | 7.3882e-06  | 1.094e-07 |       1.01135 |
| CORTEXA73     | 7.39823e-06 | 7.705e-08 |       1.01272 |
| ARMV8SVE      | 7.40181e-06 | 4.49e-08  |       1.01321 |
| NEOVERSEV1    | 7.4067e-06  | 4.77e-08  |       1.01388 |
| FT2000        | 7.40756e-06 | 6.275e-08 |       1.014   |
| EMAG8180      | 7.4187e-06  | 9.45e-09  |       1.01552 |
| CORTEXA55     | 7.41955e-06 | 7.655e-08 |       1.01564 |
| NEOVERSEN2    | 7.43142e-06 | 5.365e-08 |       1.01726 |
| THUNDERX3T110 | 7.44094e-06 | 3.98e-08  |       1.01857 |
| THUNDERX2T99  | 7.44379e-06 | 3.375e-08 |       1.01895 |
| CORTEXA76     | 7.44666e-06 | 4.125e-08 |       1.01935 |
| THUNDERX      | 7.45297e-06 | 1.567e-07 |       1.02021 |
| FALKOR        | 7.45323e-06 | 4.685e-08 |       1.02025 |
| VORTEX        | 7.45622e-06 | 4.505e-08 |       1.02066 |
| CORTEXA710    | 7.46956e-06 | 4.335e-08 |       1.02248 |
| CORTEXA57     | 7.48772e-06 | 3.38e-08  |       1.02497 |
| CORTEXA53     | 7.51004e-06 | 6.845e-08 |       1.02802 |
| TSV110        | 7.53352e-06 | 9.49e-08  |       1.03124 |

('bench_linalg.LinalgNorm.time_norm', "'float64'")
| arch          |        mean |    spread |   perf_ratios |
|:--------------|------------:|----------:|--------------:|
| ARMV8         | 5.66901e-06 | 5.775e-08 |       1       |
| CORTEXX1      | 5.71191e-06 | 1.89e-08  |       1.00757 |
| CORTEXX2      | 5.7139e-06  | 7.55e-09  |       1.00792 |
| CORTEXA55     | 5.71481e-06 | 2.085e-08 |       1.00808 |
| ARMV8SVE      | 5.73138e-06 | 4.25e-08  |       1.011   |
| CORTEXA72     | 5.73146e-06 | 7.35e-09  |       1.01102 |
| EMAG8180      | 5.73254e-06 | 2.675e-08 |       1.01121 |
| NEOVERSEV1    | 5.73319e-06 | 1.705e-08 |       1.01132 |
| CORTEXA73     | 5.73777e-06 | 4.085e-08 |       1.01213 |
| CORTEXA57     | 5.74368e-06 | 8.7e-09   |       1.01317 |
| FT2000        | 5.75563e-06 | 3.065e-08 |       1.01528 |
| CORTEXA76     | 5.75646e-06 | 1.725e-08 |       1.01543 |
| THUNDERX      | 5.76034e-06 | 2.125e-08 |       1.01611 |
| NEOVERSEN1    | 5.7623e-06  | 8.25e-09  |       1.01646 |
| FALKOR        | 5.76874e-06 | 1.71e-08  |       1.01759 |
| TSV110        | 5.77641e-06 | 7.35e-08  |       1.01895 |
| A64FX         | 5.77911e-06 | 2.075e-08 |       1.01942 |
| THUNDERX2T99  | 5.78782e-06 | 3.345e-08 |       1.02096 |
| THUNDERX3T110 | 5.7893e-06  | 1.01e-08  |       1.02122 |
| CORTEXA710    | 5.79112e-06 | 1.285e-08 |       1.02154 |
| VORTEX        | 5.79271e-06 | 2.635e-08 |       1.02182 |
| NEOVERSEN2    | 5.79658e-06 | 7.97e-08  |       1.0225  |
| CORTEXA510    | 5.838e-06   | 7.91e-08  |       1.02981 |
| CORTEXA53     | 5.87239e-06 | 2.72e-08  |       1.03588 |

('bench_linalg.LinalgNorm.time_norm', "'complex64'")
| arch          |        mean |    spread |   perf_ratios |
|:--------------|------------:|----------:|--------------:|
| ARMV8         | 1.0134e-05  | 1.38e-07  |       1       |
| ARMV8SVE      | 1.01768e-05 | 3.2e-08   |       1.00422 |
| EMAG8180      | 1.01826e-05 | 4.65e-08  |       1.00479 |
| CORTEXA57     | 1.01831e-05 | 2.1e-08   |       1.00484 |
| NEOVERSEV1    | 1.01872e-05 | 2.1e-08   |       1.00525 |
| CORTEXX1      | 1.0188e-05  | 1.65e-08  |       1.00533 |
| CORTEXA72     | 1.01893e-05 | 2.5e-08   |       1.00545 |
| CORTEXX2      | 1.01911e-05 | 4.1e-08   |       1.00563 |
| NEOVERSEN1    | 1.02019e-05 | 5.7e-08   |       1.0067  |
| CORTEXA55     | 1.02057e-05 | 3.1e-08   |       1.00707 |
| TSV110        | 1.0237e-05  | 7.5e-08   |       1.01016 |
| THUNDERX      | 1.024e-05   | 5.95e-08  |       1.01045 |
| A64FX         | 1.024e-05   | 1e-08     |       1.01046 |
| FT2000        | 1.02529e-05 | 2.45e-08  |       1.01172 |
| CORTEXA710    | 1.02571e-05 | 4.15e-08  |       1.01215 |
| THUNDERX2T99  | 1.02608e-05 | 4.45e-08  |       1.01251 |
| VORTEX        | 1.02612e-05 | 3.9e-08   |       1.01255 |
| THUNDERX3T110 | 1.02674e-05 | 3.95e-08  |       1.01316 |
| CORTEXA510    | 1.02743e-05 | 3.3e-08   |       1.01385 |
| FALKOR        | 1.02794e-05 | 6.55e-08  |       1.01435 |
| CORTEXA73     | 1.02828e-05 | 4.3e-08   |       1.01468 |
| NEOVERSEN2    | 1.02939e-05 | 5.25e-08  |       1.01577 |
| CORTEXA76     | 1.03678e-05 | 1.415e-07 |       1.02306 |
| CORTEXA53     | 1.03972e-05 | 2.725e-07 |       1.02597 |

('bench_linalg.LinalgNorm.time_norm', "'complex128'")
| arch          |        mean |    spread |   perf_ratios |
|:--------------|------------:|----------:|--------------:|
| CORTEXX1      | 1.21517e-05 | 2.65e-08  |       1       |
| ARMV8         | 1.21689e-05 | 2.25e-08  |       1.00142 |
| CORTEXA72     | 1.217e-05   | 2.95e-08  |       1.0015  |
| NEOVERSEV1    | 1.21716e-05 | 2.7e-08   |       1.00164 |
| NEOVERSEN1    | 1.21831e-05 | 3.2e-08   |       1.00259 |
| CORTEXA57     | 1.21845e-05 | 4.9e-08   |       1.0027  |
| ARMV8SVE      | 1.22287e-05 | 1.95e-08  |       1.00634 |
| FALKOR        | 1.22302e-05 | 4.9e-08   |       1.00646 |
| CORTEXA73     | 1.22344e-05 | 4.15e-08  |       1.00681 |
| THUNDERX      | 1.22507e-05 | 7.05e-08  |       1.00814 |
| FT2000        | 1.22631e-05 | 6.8e-08   |       1.00917 |
| THUNDERX3T110 | 1.22638e-05 | 3.1e-08   |       1.00923 |
| VORTEX        | 1.22639e-05 | 3.25e-08  |       1.00924 |
| NEOVERSEN2    | 1.22736e-05 | 2e-08     |       1.01004 |
| CORTEXA55     | 1.2274e-05  | 1.55e-07  |       1.01007 |
| CORTEXA510    | 1.22762e-05 | 9.4e-08   |       1.01025 |
| THUNDERX2T99  | 1.22793e-05 | 2.45e-08  |       1.0105  |
| A64FX         | 1.2281e-05  | 4.95e-08  |       1.01064 |
| EMAG8180      | 1.22842e-05 | 6.15e-08  |       1.01091 |
| CORTEXX2      | 1.22881e-05 | 1.575e-07 |       1.01123 |
| CORTEXA710    | 1.22951e-05 | 3.95e-08  |       1.0118  |
| CORTEXA53     | 1.23841e-05 | 1.23e-07  |       1.01912 |
| TSV110        | 1.24548e-05 | 2.345e-07 |       1.02495 |
| CORTEXA76     | 1.25089e-05 | 1.705e-07 |       1.0294  |

bench_linalg.LinalgSmallArrays.time_det_small_array
| arch          |        mean |    spread |   perf_ratios |
|:--------------|------------:|----------:|--------------:|
| CORTEXX2      | 1.54799e-06 | 1.66e-08  |       1       |
| NEOVERSEN2    | 1.5485e-06  | 1.495e-08 |       1.00033 |
| CORTEXA73     | 1.55044e-06 | 6.15e-09  |       1.00158 |
| NEOVERSEN1    | 1.55116e-06 | 1.35e-08  |       1.00205 |
| FT2000        | 1.55162e-06 | 2.6e-09   |       1.00235 |
| CORTEXX1      | 1.55172e-06 | 5.3e-09   |       1.00241 |
| NEOVERSEV1    | 1.55319e-06 | 1e-08     |       1.00336 |
| EMAG8180      | 1.55451e-06 | 5.25e-09  |       1.00421 |
| ARMV8SVE      | 1.55511e-06 | 1.525e-08 |       1.0046  |
| THUNDERX      | 1.55671e-06 | 8.25e-09  |       1.00563 |
| CORTEXA57     | 1.55743e-06 | 6.75e-09  |       1.0061  |
| A64FX         | 1.55945e-06 | 1.05e-08  |       1.0074  |
| FALKOR        | 1.55964e-06 | 4.1e-09   |       1.00753 |
| THUNDERX3T110 | 1.56342e-06 | 6.3e-09   |       1.00997 |
| CORTEXA510    | 1.56395e-06 | 5.6e-09   |       1.01032 |
| CORTEXA72     | 1.56476e-06 | 3.8e-09   |       1.01084 |
| VORTEX        | 1.56604e-06 | 1.795e-08 |       1.01166 |
| TSV110        | 1.57224e-06 | 4.45e-09  |       1.01566 |
| ARMV8         | 1.57355e-06 | 4.5e-09   |       1.01652 |
| CORTEXA55     | 1.57708e-06 | 4.05e-09  |       1.01879 |
| CORTEXA53     | 1.57811e-06 | 1.46e-08  |       1.01946 |
| THUNDERX2T99  | 1.57906e-06 | 1.215e-08 |       1.02007 |
| CORTEXA710    | 1.58081e-06 | 8.25e-09  |       1.02121 |
| CORTEXA76     | 1.58085e-06 | 5.6e-09   |       1.02123 |

bench_linalg.LinalgSmallArrays.time_norm_small_array
| arch          |        mean |    spread |   perf_ratios |
|:--------------|------------:|----------:|--------------:|
| CORTEXX1      | 9.21718e-07 | 3.845e-09 |       1       |
| CORTEXA72     | 9.23256e-07 | 5.175e-09 |       1.00167 |
| ARMV8         | 9.24686e-07 | 4.02e-09  |       1.00322 |
| CORTEXX2      | 9.26841e-07 | 4.77e-09  |       1.00556 |
| TSV110        | 9.28102e-07 | 3.605e-09 |       1.00693 |
| CORTEXA53     | 9.28504e-07 | 7.645e-09 |       1.00736 |
| CORTEXA710    | 9.29901e-07 | 9.605e-09 |       1.00888 |
| NEOVERSEV1    | 9.29915e-07 | 7.24e-09  |       1.00889 |
| ARMV8SVE      | 9.30263e-07 | 4.62e-09  |       1.00927 |
| NEOVERSEN1    | 9.30612e-07 | 3.675e-09 |       1.00965 |
| A64FX         | 9.30623e-07 | 4.865e-09 |       1.00966 |
| THUNDERX2T99  | 9.32492e-07 | 6e-09     |       1.01169 |
| FALKOR        | 9.3275e-07  | 5.63e-09  |       1.01197 |
| EMAG8180      | 9.33648e-07 | 4.235e-09 |       1.01294 |
| CORTEXA73     | 9.35017e-07 | 5.425e-09 |       1.01443 |
| CORTEXA55     | 9.35205e-07 | 8.28e-09  |       1.01463 |
| FT2000        | 9.35278e-07 | 5.235e-09 |       1.01471 |
| THUNDERX3T110 | 9.35585e-07 | 7.32e-09  |       1.01505 |
| THUNDERX      | 9.3603e-07  | 8.27e-09  |       1.01553 |
| CORTEXA510    | 9.36775e-07 | 8.705e-09 |       1.01634 |
| VORTEX        | 9.3728e-07  | 7.185e-09 |       1.01688 |
| NEOVERSEN2    | 9.38905e-07 | 6.015e-09 |       1.01865 |
| CORTEXA57     | 9.4789e-07  | 5.48e-09  |       1.0284  |
| CORTEXA76     | 9.47924e-07 | 3.64e-09  |       1.02843 |

bench_linalg.Lstsq.time_numpy_linalg_lstsq_a__b_float64
| arch          |        mean |     spread |   perf_ratios |
|:--------------|------------:|-----------:|--------------:|
| CORTEXX2      | 0.000833401 | 3.05e-07   |       1       |
| NEOVERSEV1    | 0.000834172 | 1.54e-06   |       1.00092 |
| EMAG8180      | 0.000834487 | 3.815e-06  |       1.0013  |
| NEOVERSEN2    | 0.00083453  | 2.54e-06   |       1.00135 |
| CORTEXA72     | 0.000834872 | 9.85e-07   |       1.00176 |
| CORTEXA710    | 0.000835578 | 3.925e-06  |       1.00261 |
| ARMV8SVE      | 0.000835649 | 2.135e-06  |       1.0027  |
| CORTEXX1      | 0.000836181 | 3.31e-06   |       1.00334 |
| CORTEXA73     | 0.000836977 | 4.085e-06  |       1.00429 |
| NEOVERSEN1    | 0.000838029 | 2.305e-06  |       1.00555 |
| FALKOR        | 0.000838365 | 5.065e-06  |       1.00596 |
| CORTEXA55     | 0.000838811 | 3.205e-06  |       1.00649 |
| CORTEXA53     | 0.000839269 | 2.88e-06   |       1.00704 |
| THUNDERX      | 0.000839826 | 1.295e-06  |       1.00771 |
| FT2000        | 0.000839852 | 2.285e-06  |       1.00774 |
| THUNDERX3T110 | 0.000839898 | 1.77e-06   |       1.0078  |
| ARMV8         | 0.000839929 | 4.475e-06  |       1.00783 |
| VORTEX        | 0.000841189 | 2.355e-06  |       1.00935 |
| TSV110        | 0.000842962 | 8.035e-06  |       1.01147 |
| CORTEXA57     | 0.000843106 | 1.54e-06   |       1.01164 |
| A64FX         | 0.000843658 | 4.315e-06  |       1.01231 |
| THUNDERX2T99  | 0.000844297 | 5.465e-06  |       1.01307 |
| CORTEXA510    | 0.000849663 | 1.7195e-05 |       1.01951 |
| CORTEXA76     | 0.000868326 | 1.141e-05  |       1.04191 |
```
