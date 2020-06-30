# Explanation
Here we begin to implement the Rerun component of our System.
From a cursory inspection verifying the execution of a drop ready for embedding in a block-DAG should be fairly
straightforward. The logical graph elements will be more difficult since there currently does not exist any structure
other than JSON files that are parsed.

For now I will add a daliuge/reproducible directory to store any extra files. 

An abstractDROP will assemble the atomic pieces of run-time information. Each shall have a repro-flag. 


## Current Issues/Comments/Questions
- My current solution to initialization has a default C
- Current behaviour to change reproducibility level is to reset all reproducibility values. I think this is reasonable
since it avoids having a mismatching reproduciblity level and reproducibility data. I might also consider making it
impossible to change this?
- Should I program with type-hinting. It makes code more readable but is a fairly recent feature used only by editors
- I am not sure how to handle unsupported options. Part of me wants to fit to the Python 'we are adults here' mentality
but on the other hand, it is good practice to prepare for such situations.
- My current 'supported' functionality is based on a single function. It could be possible to simply remove unsupported
flags from the Enum as a cleaner solution?
- Groups are handled in-editor by adding a group ID field, nothing more.
- Moving from LGT to PGT in the pg_generator.make_single_drop function. This is a self-proclaimed dummy function...
- Current behaviour sees reproducibility data be copied when child drops are created in the unrolling process 

## Closed Issues
- We have added separate unroll and partition pgt functions since it is totally reasonable to do these phases separately

## Added Code
- daliuge-common
  - reproducibility
    - constants.py
    - setup.py
- daliuge-runtime
  - dlg
    - drop.py (added functionality)
    - graph_loader.py
    - manager
      - node_manager.py
      - session.py
  - test
    - reproducibility
      - test_drophash.py
- daliuge-translator
  - dlg
    - translator
      - tool_commands.py - (added CLA -R)
      - dlg_submit - added Reproducibility flag and output options
  

## TODO:
- Handling multi-session deployments  

## Testing Needs
- Drop hashing
- lgt_init
- lg_init
- Topological sort algorithm
- Translation to PGT
  - ! MPI nodes
  - ! Grouped nodes
  - Standard nodes
- Per-drop setting vs. global setting 
## Done
- The default level should be inherited from a DALiuGE global setting 
  - An additional DEFAULT constant has been added (for now it is set at RERUN)
  - I am unsure if this is sufficient
- Physical node encryption. A 'hash me' type of system. Perhaps using my MerkleTree Implementation
  - Since I am only interested in execution verification for Rerunning. We only need to look at the flags.
    - This can be defeated much like MPIs flag system.
- Logical graph template -> Block-DAG
- Logical graph -> Block-DAG"
- Logical graph -> Physical-Graph-Template
  - Achieved by adding fields in the LG and LGN classes to include their reprodata
  - pg_generator.unroll now returns the drop_list *and* the LGT reprodata as a final element
  - This is then popped by the partition function.