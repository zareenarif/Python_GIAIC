class Counter:
    count = 0
    
    def __init__(self):
        Counter.count +=1
        
    @classmethod 
    def show_count(cls):
        print(f"Total object created : {cls.count}")
        
if __name__ == "__main__":
    object1 =Counter()
    object2 =Counter()
    object3 =Counter()
    Counter.show_count()