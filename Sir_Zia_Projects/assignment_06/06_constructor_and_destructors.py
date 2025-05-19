class Logger:
    def __init__(self):
        print("Hello Object Created")   #Constructor
        
    def __del__(self):
        print("Good Bye : object destroyed") # Destructor
        
if __name__ == "__main__":
    log = Logger()
    del log
    