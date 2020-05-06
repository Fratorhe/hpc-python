from mpi4py import MPI
import numpy as np
from sys import stdout
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank() # current task
size = comm.Get_size() # total number (ntasks)


n = 3
a = np.full(n, rank, int)
b = np.empty(n, int)

# Message chain using Send and Recv
tgt = rank + 1
src = rank - 1
if rank == 0:
    comm.Send(a, dest=tgt)
    print("  Rank %d: sent %d elements to rank %d." % (rank, len(a), tgt))
else:
    comm.Recv(b, source=src)
    print("  Rank %d: received an array filled with %ds." % (rank, b[0]))
    if rank < size - 1:
        comm.Send(a, dest=tgt)
        print("  Rank %d: sent %d elements." % (rank, len(b)))

# ... wait for every rank to finish ...
stdout.flush()
comm.barrier()

time.sleep(1)

if rank == 0:
    print("")
    print("Sendrecv (in the middle of the chain):")

# Message chain using Sendrecv when sending *and* receiving
tgt = rank + 1
src = rank - 1

if rank == 0:          # start of chain; only send
    comm.Send(a, dest=tgt)
    print("  Rank %d: sent %d elements to rank %d." % (rank, len(a), tgt))
elif rank == size - 1: # end of chain; only receive
    comm.Recv(b, source=src)
    print("  Rank %d: received a message from rank %d." % (rank, src))
    print("  Rank %d: received an array filled with %ds." % (rank, b[0]))
else:                  # middle of chain; send and receive
    comm.Sendrecv(a, dest=tgt, recvbuf=b, source=src)
    print("  Rank %d: sent %d elements to rank %d." % (rank, len(a), tgt))
    print("  Rank %d: received a message from rank %d." % (rank, src))
    print("  Rank %d: received an array filled with %ds." % (rank, b[0]))

# ... wait for every rank to finish ...
stdout.flush()
comm.barrier()

time.sleep(1)

if rank == 0:
    print("")
    print("Sendrecv (cyclically):")

# Simplified version cyclically
tgt = rank + 1
src = rank - 1
if tgt >= size:
    tgt = 0
if src < 0:
    src = rank-1

# use the same MPI call to do all communication
comm.Sendrecv(a, dest=tgt, recvbuf=b, source=src)
print("  Rank %d: sent %d elements to rank %d." % (rank, len(a), tgt))
print("  Rank %d: received a message from rank %d." % (rank, src))
print("  Rank %d: received an array filled with %ds." % (rank, b[0]))