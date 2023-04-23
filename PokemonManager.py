from PokemonDataLoader import PokemonDataLoader
import pandas as pd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class PokemonManager:
    def __init__(self) -> None:
        self.__loader = PokemonDataLoader # create for get pokemon dataframe
        self.__pokemon_data = self.__loader.load_pokemon_data()

    def get_pokemon_data(self): 
        return self.__pokemon_data
    
    def main_type_frequency_g(self): # frequency graph of main type 
        ax = self.__pokemon_data["Type 1"].value_counts().plot.bar()
        ax.set_title("Main type Frequency")
        return ax
    
    def attack_defense_relationship_g(self): # scatterplot of attack and defense
        plt.figure(figsize=(12, 6))
        ax = sns.relplot()
    
    def attack_dis_g(self): # distribution graph of attack
        pass
    
    def defense_dis_g(self): # distribution graph of defense
        pass
    
    def generation_part_to_whole_g(self): # part of whole graph of generation
        pass
    
    
    
    

        

if __name__ == "__main__":
    manager = PokemonManager()
    plot = manager.main_type_frequency_g()
    plt.show()
    