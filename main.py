from thread_6_pool import download_image as pool
from thread_9_threadingthread import download_image as thread
from threas_8_multipsocess import download_image as multiprocessing
import sys 
#Thread
def main() :
    print("Hello World")
    T = [pool]
    P = [thread]
    G = [multiprocessing]
    for i in range(100):
        
    for i in range(len(T)):
        T[i].start()
    for i in range(len(T)):
        T[i].join()
    
if __name__ == "__main__":
    sys.exit(0)