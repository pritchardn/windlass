# Experiment 1: Hello World

## Aim 
Determine if Merkle-DAG driven compression successfully discriminates between two conceptually identical yet practically
distinct computational workflows. 

## Hypothesis
We present four hypotheses in this experiment
- RR(G1, G2) - These graphs are a rerun
- ~RT(G1, G2) - These graphs are not a repeat
- RP(G1, G2) - These graphs reproduce the same data
- RPLS(G1, G2) - These graphs are a scientific replication 
- ~RPLC(G1, G2) - These graphs are not a computational replication

In the case of a match the edit distance between two leaf hashes is zero. In the case of a miss the edit distance
between the two hashes is greater than 230 of 256 bytes. 
## Method
- The description of the Windlass DALiuGE extension is separate
- Hash-function (SHA-256)
- Graph 1 `HelloWorldBash.graph`
  - BashShell
    - Command `echo -en 'Hello world > %o0` 
  - File `result1.in`
  - BashShell
    - Command `cp %i0 %o0`
  - File `result1.out`
- Graph 2 `HelloSBash.graph`
  - BashShell
    - Command `echo -en 'world' > %o0`
  - File `result2.in`
  - BashShell
    - Command `echo 'Hello' $(<%i0) > %o0`
  - File `result2.out`
- Comparison
  - There is only one leaf in both graphs and therefore agglomeration is not necessary
```python
def compare(h1, h2):
    distance = 0    
    for i in range(min(len(h1), len(h2))):
        if h1[i] != h2[i]:
            distance+=1   
    return distance 
```

## Results
| Mode | Graph 1 | Graph 2 | ED |
|:------:|:---------:|:---------:|:----:|
| RR   | 8e44a6dd6bdbb741437de588b33f46c47a1ec9b67b952181d759877b132191b3 | 8e44a6dd6bdbb741437de588b33f46c47a1ec9b67b952181d759877b132191b3 |  0  |
| RT   |         |         |    |
| RP   |         |         |    |
| RPLS |         |         |    |
| RPLC |         |         |    |

## Discussion