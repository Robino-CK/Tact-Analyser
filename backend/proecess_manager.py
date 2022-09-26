from asyncio import run_coroutine_threadsafe


# Python program to illustrate the concept
# of threading
# importing the threading module
import threading

from recorder import start_recorder 
from takt import play_song
def print_cube(num):
    """
    function to print cube of given num
    """
    print("Cube: {}".format(num * num * num))
  
if __name__ == "__main__":

    # creating thread
    t1 = threading.Thread(target=start_recorder,)
    t2 = threading.Thread(target=play_song)
  
    #t2 = threading.Thread(target=play_tone, args=(10,))
  
    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()
  
    # wait until thread 1 is completely executed
    t1.join()
    # wait until thread 2 is completely executed
    t2.join()
  
    # both threads completely executed
    print("Done!")