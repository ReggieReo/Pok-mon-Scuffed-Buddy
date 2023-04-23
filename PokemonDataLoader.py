import pandas as pd

class PokemonDataLoader:
    
    @staticmethod
    def load_pokemon_data():
        pokemon_data = pd.read_csv("data/pokemon/Pokemon.csv")
        return pokemon_data
    


    
if __name__ == "__main__":
    test = PokemonDataLoader()
    data = test.load_pokemon_data()
    print(data)
    
    

