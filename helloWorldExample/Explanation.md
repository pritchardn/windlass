# Explanation

The goal is to run a series of Hello World examples to have a very simple example for explaining the differences between
the 5Rs. 

To run them. The general workflow is to first start the DALiuGE daemon server which listens on port 8000
```
$ dlg daemon
```

We then launch an example with Python.

## Current Issues
- Currently, I ensure execution via waiting, which is not ideal but the DropctxWaiter is still a mystery to me. 

## TODO:
- `Hello %s` - Manual Drop Launching
- `Hello world` - Scattered and Gathered, Manual Drop Launching 
- `Hello %s` - Bash script -> Python Script -> File, Manual Drop Launching
- `Hello %s` - Python Script -> Bash Script -> File, Manual Drop Launching
- `Hello %s` - File -> Bash Script -> File, Manual Drop Launching
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