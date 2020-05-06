from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

n = 3
data = np.full(n, rank, int)  # send buffer
buff = np.empty(n, int)             # receive buffer

# Destination and source for messages
tgt = rank + 1
src = rank - 1

if rank == 0:
    print("Isend and Irecv:")

# Message chain using Send and Recv
if rank > 0:
    req_recv = comm.Irecv(buff, source=src)
if rank < size - 1:
    req_send = comm.Isend(data, dest=tgt)
    req_send.Wait()
    print("  Rank %d: sent %d elements." % (rank, len(data)))
if rank > 0:
    req_recv.Wait()
    print("  Rank %d: received an array filled with %ds." % (rank, buff[0]))