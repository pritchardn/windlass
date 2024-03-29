# Experiment 2: Hello World 2

## Aim 
Determine if Merkle-DAG driven compression successfully discriminates between two conceptually different yet practically
identical computational workflows. 

## Hypotheses
We present four hypotheses in this experiment
- !RR(G1, G2) - These graphs are not a rerun
- !RT(G1, G2) - These graphs are not a repeat
- RP(G1, G2) - These graphs reproduce the same data
- !RPLS(G1, G2) - These graphs are not a scientific replication 
- !RPLC(G1, G2) - These graphs are not a computational replication

In the case of a match the edit distance between two leaf hashes is zero. In the case of a miss the edit distance
between the two hashes is greater than 230 of 256 bytes. 

## Method
- The description of the Windlass DALiuGE extension is separate
- Hash-function (SHA-256)
- Graph 1 `HelloSPython.graph`
  - PythonComponent
    - appClass `` 
  - File `result2_1.in`
  - PythonComponent
    - appClass ``
  - File `result2_1.out`
- Graph 2 `HelloSBash.graph`
  - BashShell
    - Command `echo -en 'world' > %o0`
  - File `result2_2.in`
  - BashShell
    - Command `echo 'Hello' $(<%i0) > %o0`
  - File `result2_2.out`
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
| Mode | Match |
|:------:|:----:|
| RR   | False |
| RT   | False |
| RP   | _False_ |
| RPLS | False |
| RPLC | False |

## Discussion
The unexpected failure to achieve reproduction points out an important part of our scheme.
The exact data representation matters absolutely in this scheme.
Stay tuned for a follow up that adds an extra post-processing step, ensuring reproducibility.