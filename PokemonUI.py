import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import ImageTk, Image
from PokemonFacadeController import PokemonFacadeController
class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.facade = PokemonFacadeController()
        self.frame = None
        self.create_button_frame()
        self.switch_page(PokemonGraphPage(self))
        self.geometry("1000x750")
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
        self.button4 = tk.Button(self.button_frame, text="quit", command=self.destroy)
        self.button1.grid(row=0, column=1, sticky="WE", padx=(10, 10))
        self.button2.grid(row=0, column=0, sticky="WE", padx=(10, 10))
        self.button3.grid(row=0, column=2, sticky="WE", padx=(10, 10))
        self.button4.grid(row=0, column=3, sticky="WE", padx=(10, 10))
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
        self.frame1.grid(row = 0, column=0, padx=(50, 50), sticky="W")
        self.frame2.grid(row = 0, column=1,sticky="E")
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
        self.image = ImageTk.PhotoImage(Image.open(self.image_path).resize((192, 192)))
        self.poke_image_label = tk.Label(frame)
        self.poke_image_label["image"] = self.image
        
        self.type = tk.Label(frame, text=f"{self.current_pokemon_data_frame['Type 1']} {self.current_pokemon_data_frame['Type 2']}", font=('Helvetica bold', 26))
        
        self.pokedex_num = tk.Label(frame, text="#:", font=('Helvetica', 14))
        self.pokedex_num_val = tk.Label(frame, text=self.current_pokemon_data_frame["#"], font=('Helvetica', 14))
        
        self.name = tk.Label(frame, text="Name:", font=('Helvetica', 14))
        self.name_value = tk.Label(frame, text=self.current_pokemon_data_frame['Name'], font=('Helvetica', 14))
        
        self.total = tk.Label(frame, text="Total:", font=('Helvetica', 14))
        self.total_val = tk.Label(frame, text=self.current_pokemon_data_frame["Total"], font=('Helvetica', 14))
        
        self.hp = tk.Label(frame, text="HP:", font=('Helvetica', 14))
        self.hp_val = tk.Label(frame, text=self.current_pokemon_data_frame["HP"], font=('Helvetica', 14))
        
        self.attack = tk.Label(frame, text="Attack:", font=('Helvetica', 14))
        self.attack_val = tk.Label(frame, text=self.current_pokemon_data_frame["Attack"], font=('Helvetica', 14))
        
        self.defense = tk.Label(frame, text="Defense:", font=('Helvetica', 14))
        self.defense_val = tk.Label(frame, text=self.current_pokemon_data_frame["Defense"], font=('Helvetica', 14))
        
        self.sp_atk = tk.Label(frame, text="Special Attack:", font=('Helvetica', 14))
        self.sp_atk_val = tk.Label(frame, text=self.current_pokemon_data_frame["Sp. Atk"], font=('Helvetica', 14))
        
        self.sp_def = tk.Label(frame, text="Special Defense:", font=('Helvetica', 14))
        self.sp_def_val = tk.Label(frame, text=self.current_pokemon_data_frame["Sp. Def"], font=('Helvetica', 14))
        
        self.speed = tk.Label(frame, text="Speed:", font=('Helvetica', 14))
        self.speed_val = tk.Label(frame, text=self.current_pokemon_data_frame["Speed"], font=('Helvetica', 14))
        
        self.gen = tk.Label(frame, text="Generation:", font=('Helvetica', 14))
        self.gen_val = tk.Label(frame, text=self.current_pokemon_data_frame["Generation"], font=('Helvetica', 14))
        
        self.legen = tk.Label(frame, text="Legendary:", font=('Helvetica', 14))
        self.legen_val = tk.Label(frame, text=self.current_pokemon_data_frame["Legendary"], font=('Helvetica', 14))
        
        #place into program
        self.poke_image_label.grid(row=0, sticky="EW", columnspan=2)
        
        self.type.grid(row=1, column=0, sticky="EW", columnspan=2)
        
        self.pokedex_num.grid(row=2, column=0, sticky="W")
        self.pokedex_num_val.grid(row=2, column=1, sticky="E")
        
        self.name.grid(row=3, column=0, sticky="W")
        self.name_value.grid(row=3, column=1, sticky="E")

        self.total.grid(row=4, column=0, sticky="W")
        self.total_val.grid(row=4, column=1, sticky="E")
        
        self.hp.grid(row=5, column=0, sticky="W")
        self.hp_val.grid(row=5, column=1, sticky="E")
        
        self.attack.grid(row=6, column=0, sticky="W")
        self.attack_val.grid(row=6, column=1, sticky="E")
        
        self.defense.grid(row=7, column=0, sticky="W")
        self.defense_val.grid(row=7, column=1, sticky="E")
        
        self.sp_atk.grid(row=7, column=0, sticky="W")
        self.sp_atk_val.grid(row=7, column=1, sticky="E")
        
        self.sp_def.grid(row=8, column=0, sticky="W")
        self.sp_def_val.grid(row=8, column=1, sticky="E")
        
        self.speed.grid(row=9, column=0, sticky="W")
        self.speed_val.grid(row=9, column=1, sticky="E")
        
        self.gen.grid(row=10, column=0, sticky="W")
        self.gen_val.grid(row=10, column=1, sticky="E")
        
        self.legen.grid(row=11, column=0, sticky="W")
        self.legen_val.grid(row=11, column=1, sticky="E")

    def frame2_widget(self):
        """
        create widget for second frame
        """
        frame = self.frame2
        # create tree view for select pokemon
        self.poke_list = ttk.Treeview(frame, columns=("pokedex #", "Name"), show='headings', selectmode='browse', height=35)
        # name the column
        self.poke_list.heading("pokedex #", text="pokedex #")
        self.poke_list.column("pokedex #", width=75)
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
        self.image = ImageTk.PhotoImage(Image.open(self.image_path).resize((192, 192)))
        self.poke_image_label["image"] = self.image
        
        # change poke info
        self.type["text"] = f"{self.current_pokemon_data_frame['Type 1']} {self.current_pokemon_data_frame['Type 2']}"
        self.pokedex_num_val["text"] = self.current_pokemon_data_frame["#"]
        self.name_value["text"] = self.current_pokemon_data_frame['Name']
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
        self.facade = master.facade
        self.create_frame()

    def create_frame(self):
        """
        create both frame for the page
        """
        self.frame1 = ttk.Frame(self)
        self.frame2 = ttk.Frame(self)
        self.frame1.grid(row = 0, column=0, sticky="N")
        self.frame2.grid(row = 0, column=1, sticky="N")
        self.frame1_widget()
        self.frame2_widget() 
    
    def frame1_widget(self):
        frame = self.frame1
        self.fig = Figure(figsize=(6,6))
        self.axes = self.fig.add_subplot()
        self.facade.get_relationship_g("Attack", "Defense", self.axes)
        self.casvas = FigureCanvasTkAgg(self.fig, master=frame)
        self.casvas.get_tk_widget().grid()
        self.casvas.draw()
    
    def frame2_widget(self):
        """
        """
        # create tree for selecting graph
        frame = self.frame2
        self.graph_list = ttk.Treeview(frame, columns=("Graph"), show='headings', selectmode='browse', height=35)
        self.graph_list.heading("Graph", text="Graph")
        self.graph_list.column("Graph", width=375)
        self.graph_list.bind("<<TreeviewSelect>>",self.update_plot)
        self.add_selecting_graph()
        self.graph_list.pack()
        
    def add_selecting_graph(self):
        list = self.graph_list
        list.insert(parent="", index="end", values="Distibution\ of\ Attack")
        list.insert(parent="", index="end", values="Distibution\ of\ Defense")
        list.insert(parent="", index="end", values="Distibution\ of\ Hitpoint")
        list.insert(parent="", index="end", values="Distibution\ of\ Special Attack")
        list.insert(parent="", index="end", values="Distibution\ of\ Special Defens")
        list.insert(parent="", index="end", values="Distibution\ of\ Speed")
        list.insert(parent="", index="end", values="Network\ Graph\ of\ Type\ Chart")
        list.insert(parent="", index="end", values="Network\ Graph\ of\ Fire\ Type")
        list.insert(parent="", index="end", values="Network\ Graph\ of\ Water\ Type")
        list.insert(parent="", index="end", values="Network\ Graph\ of\ Grass\ Type")
        list.insert(parent="", index="end", values="Relationship\ between\ Attack\ and\ Defense")
        list.insert(parent="", index="end", values="Relationship\ between\ Special\ Attack\ and\ Special\ Defense")
        list.insert(parent="", index="end", values="Relationship\ between\ Hitpoint\ and\ Speed")
        
        
    def update_plot(self, event):
        pass

class PokemonComparePage(tk.Frame):
    def  __init__(self, master):
        super().__init__(master)
        self.lable1 = tk.Label(self, text="PokemonComparePage").grid()


if __name__ == "__main__":
    app = App()
    app.mainloop()
    # print("lol")