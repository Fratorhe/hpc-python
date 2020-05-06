from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

message_to_pass = {'rank':rank}
if rank == 0: 
    # si eres proc0, envia a 1 este mensaje.
    comm.send(message_to_pass, dest=1)
    # si eres proc0, recibe de 1 el mensaje que 1 te envia.
    msg = comm.recv(source=1)
    print(msg)
elif rank == 1:
    comm.send(message_to_pass, dest=0)
    msg = comm.recv(source=0)
    print(msg)

# with numpy:
# construct a NumPy array which is initialized to the rank of process. 
# Send and receive the array using Send and Recv and 
# after receiving print out the rank of process together with the first element of the received array.
if rank == 0: 
    # create the np array 
    a = np.array([1.14,2.5,5.0], float)
    # si eres proc0, envia a 1 este mensaje.
    comm.Send(a, dest=1)

elif rank == 1:
    b = np.empty(3, float)
    comm.Recv(b, source=0)
    print(b)