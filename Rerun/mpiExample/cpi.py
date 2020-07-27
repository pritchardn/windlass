#!/usr/bin/env python3
from mpi4py import MPI
import numpy
import sys
import os

out = './mpi_result_py.out'
comm = MPI.Comm.Get_parent()
size = comm.Get_size()
rank = comm.Get_rank()
print("Hello from rank %d" % rank)
N = numpy.array(0, dtype='i')
comm.Bcast([N, MPI.INT], root=0)
h = 1.0 / N
s = 0.0
for i in range(rank, N, size):
    x = h*(i+0.5)
    s += 4.0 / (1.0 + x**2)
PI = numpy.array(s*h, dtype='d')
comm.Reduce([PI, MPI.DOUBLE], None, op=MPI.SUM, root=0)
if rank == 0:

    fp = open(out)
    fp.write(str(PI))
    fp.close()
comm.Disconnect()
sys.exit(0)
