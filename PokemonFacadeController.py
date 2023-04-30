import pandas as pd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx
from PokemonManager import PokemonManager
from Pokemon import Pokemon

class PokemonFacadeController:
    
    def __init__(self) -> None:
        self.__manager = PokemonManager()
        
    def get_pokemon_data(self):
        return self.__manager.get_pokemon_data()
    
    def get_main_type_frequency_g(self):
        return self.__manager.get_all_type_network_g()
    
    def get_relationship_g(self, type1: str, type2: str):
        return self.__manager.get_relationship_g(type1=type1, type2=type2)
    
    def get_attribute_dis_g(self, attribute: str):
        return self.__manager.get_attribute_dis_g(attribute)
    
    def get_generation_part_to_whole_g(self):
        return self.__manager.get_generation_part_to_whole_g()
    
    def get_all_type_network_g(self):
        return self.__manager.get_all_type_network_g()
    
    def get_one_type_chart_g(self, type: str):
        return self.__manager.get_one_type_chart_g(type)
    
    def get_pokemon_object(self, name: str):
        df = self.__manager.get_pokemon_data()
        pdf = df[df.Name==name.capitalize()].iloc[0]
        pokemon = Pokemon(name = pdf["Name"], type1= pdf["Type 1"], 
                          type2=pdf["Type 2"], total=pdf["Total"],
                          hp=pdf["HP"], attack=pdf["Attack"], 
                          defense=pdf["Defense"], sp_attack=pdf["Sp. Atk"],
                          sp_defense=pdf["Sp. Def"], speed=pdf["Speed"],
                          gen=pdf["Generation"], legendary=pdf["Legendary"])
        return pokemon
    
    

if __name__ == "__main__":
    pokemon_controller = PokemonFacadeController()
    # pokemon_controller.get_all_type_network_g()
    # pokemon_controller.get_attribute_dis_g("Attack")
    # # pokemon_controller.get_generation_part_to_whole_g()
    # pokemon_controller.get_one_type_chart_g("Normal")
    # poke = pokemon_controller.get_pokemon_object("pikachu")
    # plt.show()
    # print(type(poke.get_type2()))
    print(pokemon_controller.get_pokemon_data())
