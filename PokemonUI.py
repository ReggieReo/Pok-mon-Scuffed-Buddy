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
        self.frame.grid(row=1, column=0, ipadx=100)

    def create_button_frame(self):
        self.button_frame = ttk.Frame(self, height=1000, width=1000)
        self.button1 = tk.Button(self.button_frame, text="Pokemon Stat",command=lambda: self.switch_page(PokemonStatPage(self)))
        self.button2 = tk.Button(self.button_frame, text="Pokemon Graph", command=lambda: self.switch_page(PokemonGraphPage(self)))
        self.button3 = tk.Button(self.button_frame, text="Pokemon Compare", command=lambda: self.switch_page(PokemonComparePage(self)))
        self.button1.grid(row=0, column=1, sticky="WE", padx=(10, 10))
        self.button2.grid(row=0, column=0, sticky="WE", padx=(10, 10))
        self.button3.grid(row=0, column=2, sticky="WE", padx=(10, 10))
        self.button_frame.grid(row=0, column=0, sticky="W")
        
        
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
        self.frame1.grid(row = 0, column=0)
        self.frame2.grid(row = 0, column=1)
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
        
        self.type = tk.Label(frame, text=f"{self.current_pokemon_data_frame['Type 1']} {self.current_pokemon_data_frame['Type 2']}")
        
        self.pokedex_num = tk.Label(frame, text="#:")
        self.pokedex_num_val = tk.Label(frame, text=self.current_pokemon_data_frame["#"])
        
        self.name = tk.Label(frame, text="Name:")
        self.name_value = tk.Label(frame, text=self.current_pokemon_data_frame['Name'])
        
        self.total = tk.Label(frame, text="Total:")
        self.total_val = tk.Label(frame, text=self.current_pokemon_data_frame["Total"])
        
        self.hp = tk.Label(frame, text="HP:")
        self.hp_val = tk.Label(frame, text=self.current_pokemon_data_frame["HP"])
        
        self.attack = tk.Label(frame, text="Attack:")
        self.attack_val = tk.Label(frame, text=self.current_pokemon_data_frame["Attack"])
        
        self.defense = tk.Label(frame, text="Defense:")
        self.defense_val = tk.Label(frame, text=self.current_pokemon_data_frame["Defense"])
        
        self.sp_atk = tk.Label(frame, text="Special Attack:")
        self.sp_atk_val = tk.Label(frame, text=self.current_pokemon_data_frame["Sp. Atk"])
        
        self.sp_def = tk.Label(frame, text="Special Defense:")
        self.sp_def_val = tk.Label(frame, text=self.current_pokemon_data_frame["Sp. Def"])
        
        self.speed = tk.Label(frame, text="Speed:")
        self.speed_val = tk.Label(frame, text=self.current_pokemon_data_frame["Speed"])
        
        self.gen = tk.Label(frame, text="Generation:")
        self.gen_val = tk.Label(frame, text=self.current_pokemon_data_frame["Generation"])
        
        self.legen = tk.Label(frame, text="Legendary:")
        self.legen_val = tk.Label(frame, text=self.current_pokemon_data_frame["Legendary"])
        
        #place into program
        self.poke_image_label.grid(row=0, sticky="EW", columnspan=2)
        
        self.type.grid(row=1, column=0, sticky="WE", columnspan=2)
        
        self.pokedex_num.grid(row=2, column=0, sticky="W")
        self.pokedex_num_val.grid(row=2, column=1, sticky="W")
        
        self.name.grid(row=3, column=0, sticky="W")
        self.name_value.grid(row=3, column=1, sticky="W")

        self.total.grid(row=4, column=0, sticky="W")
        self.total_val.grid(row=4, column=1, sticky="W")
        
        self.hp.grid(row=5, column=0, sticky="W")
        self.hp_val.grid(row=5, column=1, sticky="W")
        
        self.attack.grid(row=6, column=0, sticky="W")
        self.attack_val.grid(row=6, column=1, sticky="W")
        
        self.defense.grid(row=7, column=0, sticky="W")
        self.defense_val.grid(row=7, column=1, sticky="W")
        
        self.sp_atk.grid(row=7, column=0, sticky="W")
        self.sp_atk_val.grid(row=7, column=1, sticky="W")
        
        self.sp_def.grid(row=8, column=0, sticky="W", padx=(0,15))
        self.sp_def_val.grid(row=8, column=1, sticky="W")
        
        self.speed.grid(row=9, column=0, sticky="W")
        self.speed_val.grid(row=9, column=1, sticky="W")
        
        self.gen.grid(row=10, column=0, sticky="W")
        self.gen_val.grid(row=10, column=1, sticky="W")
        
        self.legen.grid(row=11, column=0, sticky="W")
        self.legen_val.grid(row=11, column=1, sticky="W")

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
        # chagne selected pokemon info
        self.poke_list.bind("<<TreeviewSelect>>", self.return_select_treeview)
        # change first frame info
        self.poke_list.bind("<<TreeviewSelect>>", self.change_frame1_info, add="+")
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
        frame = self.frame1
        # change image
        self.image_path = f"data/sprite/{self.current_pokemon_data_frame['#']}.png"
        self.image = ImageTk.PhotoImage(Image.open(self.image_path))
        self.poke_image_label["image"] = self.image
        
        # change poke info
        self.type["text"] = f"{self.current_pokemon_data_frame['Type 1']} {self.current_pokemon_data_frame['Type 2']}"
        self.pokedex_num_val["text"] = self.current_pokemon_data_frame["#"]
        self.name_value = tk.Label(frame, text=self.current_pokemon_data_frame['Name']) 
        self.total_val["text"] = self.current_pokemon_data_frame["Total"]
        self.hp_val["text"] = self.current_pokemon_data_frame["HP"]
        self.attack_val["text"] = self.current_pokemon_data_frame["Attack"]
        self.defense_val["text"] = self.current_pokemon_data_frame["Defense"]
        self.sp_atk_val["text"] = self.current_pokemon_data_frame["Sp. Atk"]
        self.sp_def_val["text"] = self.current_pokemon_data_frame["Sp. Def"]
        self.speed_val["text"] = self.current_pokemon_data_frame["Speed"]
        self.gen_val["text"] = self.current_pokemon_data_frame["Generation"]
        self.legen_val["text"] = self.current_pokemon_data_frame["Legendary"]
        
        

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