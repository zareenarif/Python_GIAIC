def convert():
    user_input = float(input("Enter Temperature in Farenhite :"))
    degree_calsius = (user_input - 32) * 5.0/9.0
    print(f"Temperature {user_input} F = {degree_calsius : .2f} C")
    
    
if __name__ == "__main__":
    convert()