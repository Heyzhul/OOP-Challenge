# main.py

from pet import Pet

def main():
    my_pet = Pet("Fluffy")

    my_pet.get_status()
    my_pet.eat()
    my_pet.sleep()
    my_pet.play()
    my_pet.train("Sit")
    my_pet.train("Roll Over")
    my_pet.show_tricks()
    my_pet.get_status()

if __name__ == "__main__":
    main()
