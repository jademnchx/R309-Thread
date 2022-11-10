from exo_6 import download_image
from exo_valid_1 import download_image
from exo_valid_1_3 import download_image
import sys 

def main() :
    print("Hello World")
    T = [download_image]
    P = [download_image]
    G = [download_image]
    for i in range(100):
    for i in range(len(T)):
        T[i].start()
    for i in range(len(T)):
        T[i].join()
    
if __name__ == "__main__":
    sys.exit(0)