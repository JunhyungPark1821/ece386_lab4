# ece386_lab4


| Stat | Keras | LiteRT |
| -------- | ------- | ------- |
| duration_time (ns) | 13009878540 | 1576031265 |
| user_time (ns) | 12510103010 | 590813796 |
| system_time (ns) | 955558016 | 107537160 |
| cpu_cycles | 31625004024 | 1496717095 |
| cache-misses | 253354708 | 8404318 |
| cache-references | 12006358389 | 451173635 |
| stalled-cycles-backend | 11242520473 | 814494145 |
| L1-dcache-loads | 12005162719 | 455526748 |
| L1-dcache-load-misses | 254041726 | 8788863 |
| l2d_cache_rd | 757540701 | 18930773 |
| l2d_cache_inval | 35945020 | 513631 |
| l3d_cache_rd | 461660374 | 12631207 |
| LLC-loads | 461256024 | 12606124 |
| LLC-load-misses | 174554132 | 5598791 |
| mem_access_rd | 8500914063 | 311240116 |


Compare

Running your .tflite model with 10 images per run vs 40 images per run

Running your .tflite model with LiteRT vs your .keras model with Keras

Discuss the results in your README.md. Make sure you emphasize

Relative model sizes

Relative performance for more vs. fewer images per run, and why

Pipeline stalls waiting for memory

L2 invalidations (meaning something in the L2 cache had to be overwritten)

LLC loads and misses
