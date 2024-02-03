from random import choice

capital = "Barcelona"

bird = "Pigeons"

flower = "Roses"

song = "El Canto del Barça"

def randomfunfact():
    funfacts = [
        "…is the only city in the world awarded a Royal Gold Medal for architecture by Royal Institute of British Architects "
        "…had no beaches until the 1992 Olympics "
        "…is home to the busiest pedestrian street in Spain "
        "…is older than Rome "
    ]
    
    index = choice ("012")
    
    print(funfacts[int(index)])
    
if __name__ == "__main__":
    randomfunfact()