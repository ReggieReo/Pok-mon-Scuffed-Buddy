from PokemonDataLoader import PokemonDataLoader
import pandas as pd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class PokemonManager:
    def __init__(self) -> None:
        self.__loader = PokemonDataLoader
        self.__pokemon_data = self.__loader.load_pokemon_data()
    
    def get_pokemon_data(self):
        return self.__pokemon_data
    
    
    def main_type_frequency_g(self):
        ax = self.__pokemon_data["Type 1"].value_counts().plot.bar()
        ax.set_title("Main type Frequency")
        return ax
    
    def attack_defense_relationship_g(self):
        plt.figure(figsize=(12, 6))
        ax = sns.relplot()
    
    
    

        

if __name__ == "__main__":
    manager = PokemonManager()
    plot = manager.main_type_frequency_g()
    plt.show()
    