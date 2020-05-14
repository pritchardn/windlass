# Explanation

The goal is to run a series of Hello World examples to have a very simple example for explaining the differences between
the 5Rs. 

To run them. The general workflow is to first start the DALiuGE daemon server which listens on port 8000
```
$ dlg daemon
```

We then launch an example with Python.

## Current Thinking
- I do not think anything relating to EAGLE is functional. As such I may need to test things differently
  - Write the graphs manually as drops first
  - Convert this backwards into a JSON graph file 
  - Run this file in the usual fashion.

## TODO:
- `Hello %s`
- `Hello world` - Scattered and Gathered
- Tapping into drop execution to get output printed / written to file (perhaps a new graph)
- A proper write-up

## Done
- `Hello World`