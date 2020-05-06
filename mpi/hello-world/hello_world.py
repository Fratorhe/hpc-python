from mpi4py import MPI

comm = MPI.COMM_WORLD # this is the communicator

size = comm.Get_size() # gets the total number of processes 
rank = comm.Get_rank() # gets the name of the process

print("I am rank %d in group of %d processes" % (rank, size))
