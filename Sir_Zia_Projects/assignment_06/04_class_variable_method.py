class Bank:
    bank_name = "Zar Bank" #class variable
    
    @classmethod
    def change_bank_name(cls, name): #class method
        cls.bank_name = name
        
if __name__ == "__main__":
    user1 = Bank()
    user2 = Bank()
    
    print("Befor changing bank name:")
    print(f"User1's bank name :{user1.bank_name}")
    print(f"User1's bank name :{user2.bank_name}")
    
    Bank.change_bank_name("RF Bank")
    
    print("\nAfter changing bank name :")
    print(f"User1's bank name :{user1.bank_name}")
    print(f"User1's bank name :{user2.bank_name}")