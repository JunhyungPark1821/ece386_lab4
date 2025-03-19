# ece386_lab4

| Stat | Keras | LiteRT | Difference (Keras - LiteRT) |
| -------- | ------- | ------- | ------- |
| model size (MB) | 26.3 | 2.387 | 23. 913 |
| duration_time (ns) | 13009878540 | 1576031265 | 11433847275 |
| user_time (ns) | 12510103010 | 590813796 | 11919289214 |
| system_time (ns) | 955558016 | 107537160 | 848020856 |
| cpu_cycles | 31625004024 | 1496717095 | 30128286929 |
| cache-misses | 253354708 | 8404318 | 244950390 |
| cache-references | 12006358389 | 451173635 | 11555184754 |
| stalled-cycles-backend | 11242520473 | 814494145 | 10428026328 |
| L1-dcache-loads | 12005162719 | 455526748 | 11549635971 |
| L1-dcache-load-misses | 254041726 | 8788863 | 245252863 |
| l2d_cache_rd | 757540701 | 18930773 | 738609928 |
| l2d_cache_inval | 35945020 | 513631 | 35431389 |
| l3d_cache_rd | 461660374 | 12631207 | 449029167 |
| LLC-loads | 461256024 | 12606124 | 448649900 |
| LLC-load-misses | 174554132 | 5598791 | 168955341 |
| mem_access_rd | 8500914063 | 311240116 | 8189673947 |


First, the model size of the litert model is significantly smaller than the keras model. The difference is 23.913 MB between keras model and litert model. The model size affects the time and cycles necessary for making predictions. The duration time, user time, system time, and cpu cycles for the keras model are significantly higher than the litert model. Additionally, the keras model has higher cache misses than litert model as well, which explains higher time and cycles required with the keras model having to find data in a higher level memory than caches. Furthermore, keras model made more loads and misses to the L1, L2, and L3 caches as well. Finally, keras model caused more stalled cycles in the backend waiting for memory. Overall, keras model would be able to process fewer images per run compared to the litert model. However, the result of the prediction based on the keras model was more accurate than the litert model based on the user experience.
