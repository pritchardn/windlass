# Experiment 6
## Aim
Demonstrate that an input data change affects reproducibility hashes even if the output results are identical.

## Hypothesis
We present four hypothesis
  - RR(G1, G2)
  - RT(G1, G2)
  - !RP(G1, G2)
  - !RPLS(G1, G2)
  - !RPLC(G1, G2)
  
The numbers1.in should contain [4,3,2,1] written to file whereas the original file contains [1,2,3,4]

## Results
| Mode | Match |
|:------:|:----:|
| RR   | True |
| RT   | True |
| RP   | False |
| RPLS | False |
| RPLC | False |

As expected. Fantastic.