# Explanation

The goal is to run a series of Hello World examples to have a very simple example for explaining the differences between
the 5Rs. 

To run them. The general workflow is to first start the DALiuGE daemon server which listens on port 8000
```
$ dlg daemon
```

We then launch an example with Python.

## Current Issues/Comments/Questions
- Currently, I ensure execution via waiting, which is not ideal but the DropctxWaiter is still a mystery to me. 

## TODO:
- `Hello world` - File -> Bash -> File -> NGAS, Manual Drop Launching, Replicating pre-existing example
- `Hello world` - Scattered and Gathered, Manual Drop Launching 
- `Hello %s` - Bash script -> Python Script -> File, Manual Drop Launching
- `Hello %s` - Python Script -> Bash Script -> File, Manual Drop Launching
- `Hello %s` - DALiuGE Graph Launching
- `Hello world` - Scattered and Gathered, DALiuGE Graph Launching 
- `Hello %s` - Bash script -> Python Script -> File, DALiuGE Graph Launching
- `Hello %s` - Python Script -> Bash Script -> File, DALiuGE Graph Launching
- `Hello %s` - File -> Bash Script -> File, DALiuGE Graph Launching
- Tapping into drop execution to get output printed / written to file (perhaps a new graph)
- A proper write-up

## Done
- `Hello World` - Via DALiuGE Graph Launcher (`daliugebased/helloDaliuge.py`)
- `Hello World` - Via Manual Drop Launching (`dropbased/helloworld.py`)
- `Hello %s` - Manual Drop Launching (InMemory Drops)
- `Hello %s` - Bash script apps, Manual Drop Launching
- `Hello world` - Directly writing to file, Manual Drop Launching. The simplest possible example
- `Hello %s` - File -> Bash Script -> File, Manual Drop Launching

## Resolved Issues/Comments/Questions
- The reliance on kwargs makes use of the system unintuitive. Lots of looking up rather than exploiting IDE tools.
  - This is why we would build an editor. This is probably the most pythonic way to achieve this. 
- I've been using the StreamingOutput -> Memory -> Streaming Input paradigm. Is there a shorter way than this? 
  - Yes, several