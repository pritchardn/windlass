# Experiment 1: Hello World 1

## Aim 
Determine if Merkle-DAG driven compression successfully discriminates between two conceptually identical yet practically
different computational workflows. 

## Hypotheses
We present four hypotheses in this experiment
- RR(G1, G2) - These graphs are a rerun
- !RT(G1, G2) - These graphs are not a repeat
- RP(G1, G2) - These graphs reproduce the same data
- RPLS(G1, G2) - These graphs are a scientific replication 
- !RPLC(G1, G2) - These graphs are not a computational replication

In the case of a match the edit distance between two leaf hashes is zero. In the case of a miss the edit distance
between the two hashes is greater than 230 of 256 bytes. 

## Method
- The description of the Windlass DALiuGE extension is separate
- Hash-function (SHA-256)
- Graph 1 `HelloWorldBash.graph`
  - BashShell
    - Command `echo -en 'Hello world > %o0` 
  - File `result1_1.in`
  - BashShell
    - Command `cp %i0 %o0`
  - File `result1_1.out`
- Graph 2 `HelloSBash.graph`
  - BashShell
    - Command `echo -en 'world' > %o0`
  - File `result1_2.in`
  - BashShell
    - Command `echo 'Hello' $(<%i0) > %o0`
  - File `result1_2.out`
- Comparison
  - Agglomeration is now implemented so we refer to the 'signature' of each workflow run.
```python
def compare(h1, h2):
    distance = abs(len(h1) - len(h2))    
    for i in range(min(len(h1), len(h2))):
        if h1[i] != h2[i]:
            distance+=1   
    return distance 
```

## Results
| Mode | Graph 1 | Graph 2 | ED |
|:------:|:---------:|:---------:|:----:|
| RR   | 94e51251a5bbf63d1b5f56acb396f7740164a0072bbe84cf4f2d52222a0cf636 | 94e51251a5bbf63d1b5f56acb396f7740164a0072bbe84cf4f2d52222a0cf636 |  0  |
| RT   |         |         |    |
| RP   |         |         |    |
| RPLS |         |         |    |
| RPLC |         |         |    |

## Discussion