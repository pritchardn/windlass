# Explanation
Here we begin to implement the Rerun component of our System.
From a cursory inspection verifying the execution of a drop ready for embedding in a block-DAG should be fairly
straightforward. The logical graph elements will be more difficult since there currently does not exist any structure
other than JSON files that are parsed.

For now I will add a daliuge/reproducible directory to store any extra files. 

An abstractDROP will assemble the atomic pieces of run-time information. Each shall have a reppro-flag. 


## Current Issues/Comments/Questions


## TODO:
- Physical node encryption. A 'hash me' type of system. Perhaps using my MerkleTree Implementation
  - Since I am only interested in execution verification for Rerunning. We only need to look at the flags.
    - This can be defeated much like MPIs flag system. 
- Logical graph template -> Block-DAG
- Logical graph -> Block-DAG"
- Logical graph -> Physical-Graph-Template -> Block-DAG
- PGT -> PG -> Block-DAG (based on per-drop hashing).
- The limitations from check-summing are present and will need to be worked around.
- The default level should be inherited from a DALiuGE global setting 

## Done