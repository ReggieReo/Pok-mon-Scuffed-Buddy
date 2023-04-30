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

    def get_main_type_frequency_g(self):  # frequency graph of main type
        figure = plt.figure(figsize=(12, 5))
        ax = self.__pokemon_data["Type 1"].value_counts().plot.bar()
        ax.set_title("Main type Frequency")
        return figure

    def get_relationship_g(self, type1, type2):  # scatterplot of attack and defense
        figure = plt.figure(figsize=(12, 6))
        ax = sns.scatterplot(
            data=self.__pokemon_data, x=type1, y=type2, hue="Generation"
        )
        figure.suptitle("Scatterplot of attack and defense")
        return figure

    def get_attribute_dis_g(self, attribute):  # distribution graph of attack
        figure = plt.figure(figsize=(12, 6))
        ax = sns.histplot(
            data=self.__pokemon_data[attribute],
        )
        return figure

    def get_generation_part_to_whole_g(self):  # part of whole graph of generation
        # figure = plt.figure(figsize=(12, 6))
        plot = (
            self.__pokemon_data["Generation"]
            .value_counts()
            .sort_index()
            .plot(
                kind="pie",
                y="Generation",
                title="lol",
                autopct="%.2f%%",
                figsize=(12, 6),
                legend=True,
            )
        )
        return plot

    def get_all_type_network_g(self):
        G = nx.DiGraph()
        figure = plt.figure(figsize=(12, 6))
        df = self.__type_data.copy()
        df.set_index("Attacking", inplace=True)
        for label, content in df.items():
            G.add_node(label)
        for label, content in df.items():
            for type2, l in content.items():
                if l != 0:
                    G.add_edge(u_of_edge=label, v_of_edge=type2, weight=l)
        pos = nx.circular_layout(G)
        plot = nx.draw(G, pos=pos, with_labels=True)
        return figure

    def get_one_type_chart_g(self, type: str):
        df = self.__type_data.set_index("Attacking")[type]
        G = nx.DiGraph()
        for node in df.index:
            G.add_node(node)
        for type2, effectiveness in df.items():
            if effectiveness != 0:
                G.add_edge(u_of_edge=type, v_of_edge=type2, weight=effectiveness)
        figure = plt.figure(figsize=(12, 6))
        pos = nx.shell_layout(G)
        plot = nx.draw(G, pos=pos, with_labels=True)
        weight = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(G, pos, edge_labels=weight)
        return figure


if __name__ == "__main__":
    manager = PokemonManager()
    # manager.get_attack_defense_relationship_g()
    # manager.get_main_type_frequency_g()
    # manager.get_attribute_dis_g("Attack")
    # manager.get_generation_part_to_whole_g()
    manager.get_all_type_network_g()
    # manager.get_one_type_chart_g("Normal")
    plt.show()
