import subprocess
import os

def main():
    file = "/Users/christian/Desktop/ML-Blackjack/test.sh"
    oFile = subprocess.Popen(file, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    stdout, stderr = oFile.communicate(input = "100")

    #print(os.getcwd())
    
if __name__ == "__main__":
    main()