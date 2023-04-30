import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd
from PIL import ImageTk, Image
from PokemonFacadeController import PokemonFacadeController

class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.facade = PokemonFacadeController()
        self.frame = None
        self.create_button_frame()
        self.switch_page(PokemonStatPage(self))
        self.geometry("700x500")
        self.title("Pokémon Scuffed Buddy")

    def switch_page(self, page):
        if self.frame is not None:
            self.frame.destroy()
        new_frame = page
        self.frame = new_frame
        self.frame.grid(row=1, sticky="W")

    def create_button_frame(self):
        self.button_frame = ttk.Frame(self, height=1000, width=1000)
        self.button1 = tk.Button(self.button_frame, text="Pokemon Stat",command=lambda: self.switch_page(PokemonStatPage(self)),width=15)
        self.button2 = tk.Button(self.button_frame, text="Pokemon Graph", command=lambda: self.switch_page(PokemonGraphPage(self)),width=15)
        self.button3 = tk.Button(self.button_frame, text="Pokemon Compare", command=lambda: self.switch_page(PokemonComparePage(self)),width=15)
        self.button1.grid(row=0, column=1)
        self.button2.grid(row=0, column=0)
        self.button3.grid(row=0, column=2)
        self.button_frame.grid(row=0, sticky="EW")
        
class PokemonStatPage(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.mainframe = master
        self.pokemon_df = self.mainframe.facade.get_pokemon_data()
        self.current_pokemon_data_frame = self.pokemon_df[self.pokemon_df["Name"]=="Piplup"].iloc[0]
        self.current_pokemon_name = "Piplub"
        self.create_frame()

    def create_frame(self):
        """
        create both frame for the page
        """
        self.frame1 = ttk.Frame(self)
        self.frame2 = ttk.Frame(self)
        self.frame1.grid(row = 0, column=0,sticky="N")
        self.frame2.grid(row = 0, column=1,sticky="W")
        self.frame1_widget()
        self.frame2_widget()

    def frame1_widget(self):
        """
        create widget for first frame
        """
        frame = self.frame1
        # poke_sprite = ImageTk.PhotoImage(file=self.FILE)
        # poke_sprite_label = tk.Label(frame, image=poke_sprite)
        # poke_sprite_label.grid()
        
        # name_label = tk.Label(frame, text="lol")
        # name_label.grid()
        self.image_path = "data/sprite/393.png"
        self.image = ImageTk.PhotoImage(Image.open(self.image_path))
        self.poke_image_label = tk.Label(frame)
        self.poke_image_label["image"] = self.image
        self.type1 = tk.Label(frame, text=self.current_pokemon_data_frame["Type 1"])
        self.type2 = tk.Label(frame, text=self.current_pokemon_data_frame["Type 2"])
        
        self.poke_image_label.grid(row=0, sticky="EW", columnspan=2)
        self.type1.grid(row=1, column=0)
        self.type2.grid(row=1, column=1)
        
        pass


    def frame2_widget(self):
        """
        create widget for second frame
        """
        frame = self.frame2
        # create tree view for select pokemon
        self.poke_list = ttk.Treeview(frame, columns=("pokedex #", "Name"), show='headings', selectmode='browse', height=20)
        # name the column
        self.poke_list.heading("pokedex #", text="pokedex #")
        self.poke_list.heading("Name", text="Name")
        # add pokemon to tree view
        for tuple, series in self.pokemon_df.iterrows():
            self.poke_list.insert(parent="", index="end",iid=series["#"], values=(series["#"], series["Name"]))
        self.poke_list.bind("<ButtonRelease-1>", self.return_select_treeview)
        self.poke_list.bind("<ButtonRelease-1>", self.change_frame1_info, add="+")
        self.poke_list.grid()

    def return_select_treeview(self, event):
        """
        used for callback event on select
        """
        select_pokemon = self.poke_list.item(self.poke_list.focus())
        select_pokemon_name = select_pokemon["values"][1] 
        self.current_pokemon_data_frame = self.pokemon_df[self.pokemon_df["Name"]==select_pokemon_name].iloc[0]
        self.current_pokemon_name =select_pokemon_name
        
        # for testing if the code work corrently
        # print(self.poke_list.focus())
        # print(self.current_pokemon_name)
        # print(self.current_pokemon_data_frame)
        
    def change_frame1_info(self, event):
        # print(self.current_pokemon_data_frame['#'])
        """
        used for callback event on select
        """
        self.image_path = f"data/sprite/{self.current_pokemon_data_frame['#']}.png"
        self.image = ImageTk.PhotoImage(Image.open(self.image_path))
        self.poke_image_label["image"] = self.image
        
        
        # self.poke_image_label.grid() 
        
        
        

class PokemonGraphPage(tk.Frame):
    def  __init__(self, master):
        super().__init__(master)
        self.label1 = tk.Label(self, text="PokemonGraphPage").grid()

class PokemonComparePage(tk.Frame):
    def  __init__(self, master):
        super().__init__(master)
        self.lable1 = tk.Label(self, text="PokemonComparePage").grid()


if __name__ == "__main__":
    app = App()
    app.mainloop()
    # print("lol")