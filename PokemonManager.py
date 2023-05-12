import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx
from PokemonDataLoader import PokemonDataLoader


class PokemonManager:
    def __init__(self) -> None:
        self.__loader = PokemonDataLoader  # create for get pokemon dataframe
        self.__pokemon_data = self.__loader.load_pokemon_data()
        self.__type_data = pd.read_csv("data/pokemon/chart.csv")

    def get_pokemon_data(self):
        return self.__pokemon_data

    def get_main_type_frequency_g(self, ax):  # frequency graph of main type
        ax = self.__pokemon_data["Type 1"].value_counts().plot.bar(ax=ax)
        ax.set_title("Main type Frequency")

    def get_relationship_g(self, type1, type2, ax):  # scatterplot of two attibute
        ax = sns.scatterplot(
            data=self.__pokemon_data, x=type1, y=type2, hue="Generation", ax=ax
        )
        des1 = self.__pokemon_data[type1].describe()
        des2 = self.__pokemon_data[type2].describe()
        corr = self.__pokemon_data[type1].corr(self.__pokemon_data[type2])
        ax.set_title(f"Relationship between {type1} and {type2}")
        return des1, des2, corr

    def get_attribute_dis_g(self, attribute, ax):  # distribution graph of attack
        sns.histplot(data=self.__pokemon_data[attribute], ax=ax)
        ax.set_title(f"Distribution of {attribute}")
        ax.set_aspect("auto")
        ax.set_frame_on(True)
        ax.grid(color="grey", linestyle="-", linewidth=1, axis="y", alpha=0.5)
        ax.set_xlabel(attribute)
        ax.set_ylabel("Frequency")
        return self.__pokemon_data[attribute].describe()

    def get_generation_part_to_whole_g(self, ax):  # part of whole graph of generation
        ax.pie(
            x=self.__pokemon_data["Generation"].value_counts().sort_index(),
            autopct="%.2f%%",
            labels=[
                "Generation 1",
                "Generation 2",
                "Generation 3",
                "Generation 4",
                "Generation 5",
            ],
        )
        ax.set_title("Proportion of Generation")
        ax.set_aspect("auto")
        ax.grid(color="r", linestyle="-", linewidth=2)

    def get_all_type_network_g(self, ax):  # all type to all type network
        G = nx.DiGraph()
        df = self.__type_data.copy()
        df.set_index("Attacking", inplace=True)
        for label, content in df.items():
            G.add_node(label)
        for label, content in df.items():
            for type2, l in content.items():
                if l != 0:
                    G.add_edge(u_of_edge=label, v_of_edge=type2, weight=l)
        pos = nx.circular_layout(G)
        nx.draw(G, pos=pos, with_labels=True, ax=ax)
        ax.set_title("Type Chart")

    def get_one_type_chart_g(self, type: str, ax: plt.Axes):  # one type to all network
        poke_type = [
            "Normal",
            "Fire",
            "Water",
            "Electric",
            "Grass",
            "Ice",
            "Fighting",
            "Poison",
            "Ground",
            "Flying",
            "Psychic",
            "Bug",
            "Rock",
            "Ghost",
            "Dragon",
            "Dark",
            "Steel",
            "Fairy",
        ]

        df = self.__type_data.set_index("Attacking")
        G = nx.DiGraph()
        for node in df.index:
            G.add_node(node)
        for effect_type in poke_type:
            G.add_edge(
                u_of_edge=type, v_of_edge=effect_type, weight=df.loc[type, effect_type]
            )
        pos = nx.shell_layout(G)
        nx.draw(G, pos=pos, with_labels=True, ax=ax)
        weight = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(G, pos, edge_labels=weight, ax=ax)
        ax.set_title("Fire type relationship")

    def get_hit_effective(self, type1: str, type2: str):
        type1 = type1.capitalize()
        type2 = type2.capitalize()
        poke_type = [
            "Normal",
            "Fire",
            "Water",
            "Electric",
            "Grass",
            "Ice",
            "Fighting",
            "Poison",
            "Ground",
            "Flying",
            "Psychic",
            "Bug",
            "Rock",
            "Ghost",
            "Dragon",
            "Dark",
            "Steel",
            "Fairy",
        ]

        df = self.__type_data.set_index("Attacking")
        G = nx.DiGraph()
        for node in df.index:
            G.add_node(node)
        for effect_type in poke_type:
            G.add_edge(
                u_of_edge=type1,
                v_of_edge=effect_type,
                weight=df.loc[type1, effect_type],
            )
        path_length = dict(nx.single_source_dijkstra_path_length(G=G, source=type1))
        effectiveness = path_length[type2]
        if type1 == type2:
            effectiveness = self.__type_data.set_index("Attacking").loc[type1, type2]
        if effectiveness == 1.0:
            return "Normal"
        elif effectiveness == 2.0:
            return "Not Very Effective"
        elif effectiveness == 0.5:
            return "Super Effective"
        elif effectiveness == 3.0:
            return "Doesn't Affect"


if __name__ == "__main__":
    manager = PokemonManager()
    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot()
    # x = manager.get_hit_effective(type1="Fire", type2="Water")
    # print(x)
    # manager.get_one_type_chart_g("Electric", ax)
    # manager.get_generation_part_to_whole_g(ax)
    manager.get_all_type_network_g(ax)
    # manager.get_generation_part_to_whole_g(ax)
    # des1, des2, corr = manager.get_relationship_g("Attack", "Speed", ax)
    # print(des1)
    # print(des2)
    # print(corr)
    plt.show()
    # print(des)
