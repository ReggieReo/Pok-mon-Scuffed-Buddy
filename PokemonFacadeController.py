import pandas as pd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx
from PokemonManager import PokemonManager


class PokemonFacadeController:
    
    def __init__(self) -> None:
        self.__manager = PokemonManager()

    def get_pokemon_data(self):
        return self.__manager.get_pokemon_data()

    def get_main_type_frequency_g(self, ax):
        return self.__manager.get_main_type_frequency_g(ax)

    def get_relationship_g(self, type1: str, type2: str, ax):
        return self.__manager.get_relationship_g(type1, type2, ax)

    def get_attribute_dis_g(self, attribute: str, ax):
        return self.__manager.get_attribute_dis_g(attribute, ax)

    def get_generation_part_to_whole_g(self, ax):
        return self.__manager.get_generation_part_to_whole_g(ax)

    def get_all_type_network_g(self, ax):
        return self.__manager.get_all_type_network_g(ax)

    def get_one_type_chart_g(self, type: str, ax):
        return self.__manager.get_one_type_chart_g(type, ax)
    
    # both get_hit_effective and is_poke_exist won't work if use dataframe from
    # attribute. Can't be fixed have to create a new data frame
    def get_hit_effective(self, first_name: str, second_name:str):
        poke_df = pd.read_csv("data/pokemon/Pokemon.csv").set_index("Name")
        if not self.is_poke_exist(first_name) or not self.is_poke_exist(second_name):
            return "Not valid pokemon"
        fist_poke = poke_df.loc[first_name.capitalize()]
        second_poke = poke_df.loc[second_name.capitalize()]
        type1 = fist_poke["Type 1"]
        type2 = second_poke["Type 1"]
        return self.__manager.get_hit_effective(type1, type2)
    
    def is_poke_exist(self, name: str):
        poke_df = pd.read_csv("data/pokemon/Pokemon.csv").set_index("Name")
        pokelist = (list(poke_df.index))
        if name not in pokelist:
            return False
        return True
        

if __name__ == "__main__":
    pokemon_controller = PokemonFacadeController()
    print(pokemon_controller.get_hit_effective("Piplup", "Charmander"))
    # pokemon_controller.get_all_type_network_g()
    # # pokemon_controller.get_generation_part_to_whole_g()
    # pokemon_controller.get_one_type_chart_g("Normal")
    # poke = pokemon_controller.get_pokemon_object("pikachu")
    # plt.show()
    # print(type(poke.get_type2()))
    # print(pokemon_controller.get_pokemon_data())
