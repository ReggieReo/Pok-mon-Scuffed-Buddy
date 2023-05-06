import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import ImageTk, Image
from PokemonFacadeController import PokemonFacadeController
from threading import Thread


class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.facade = PokemonFacadeController()
        self.frame = None
        self.create_button_frame()
        self.switch_page(PokemonGraphPage(self))
        self.geometry("1000x750")
        self.title("Pokémon Scuffed Buddy")
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def switch_page(self, page):
        if self.frame is not None:
            self.frame.destroy()
        new_frame = page
        self.frame = new_frame
        self.frame.grid(row=1, sticky="N")

    def create_button_frame(self,):
        self.button_frame = ttk.LabelFrame(self, text="")
        self.button1 = tk.Button(self.button_frame, text="Pokemon Stat",command=lambda: self.switch_page(PokemonStatPage(self)))
        self.button2 = tk.Button(self.button_frame, text="Pokemon Graph", command=lambda: self.switch_page(PokemonGraphPage(self)))
        self.button3 = tk.Button(self.button_frame, text="Pokemon Compare", command=lambda: self.switch_page(PokemonComparePage(self)))
        self.button4 = tk.Button(self.button_frame, text="quit", command=self.destroy)
        self.button1.grid(row=0, column=1, sticky="WE", padx=(10, 10))
        self.button2.grid(row=0, column=0, sticky="WE", padx=(10, 10))
        self.button3.grid(row=0, column=2, sticky="WE", padx=(10, 10))
        self.button4.grid(row=0, column=3, sticky="WE", padx=(10, 10))
        self.button_frame.grid(row=0, sticky="ns")
        
        
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
    def  __init__(self, master: tk.Tk):
        super().__init__(master)
        self.master = master
        self.facade = master.facade
        self.create_frame()

    def create_frame(self):
        """
        create both frame for the page
        """
        self.frame1 = ttk.Frame(self)
        self.frame2 = ttk.Frame(self)
        self.frame3 = ttk.Frame(self)
        self.frame1.grid(row = 0, column=0, sticky="NWSE")
        self.frame2.grid(row = 0, column=1, sticky="NWSE")
        self.frame3.grid(row = 1, column=0, sticky="NS", columnspan=2)
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)
        
        self.frame3.grid_columnconfigure(0, weight=1)
        self.frame3.grid_rowconfigure(0, weight=1)
        
        self.frame1_widget()
        self.frame2_widget() 
        self.frame3_widget()
    
    def frame1_widget(self):
        frame = self.frame1
        self.fig = Figure(figsize=(6,6))
        self.axes = self.fig.add_subplot()
        self.facade.get_relationship_g("Attack", "Defense", self.axes)
        self.casvas = FigureCanvasTkAgg(self.fig, master=frame)
        self.describe = None
        self.number_att = 0
        self.casvas.get_tk_widget().grid()
        self.casvas.draw()
    
    def frame2_widget(self):
        """
        """
        # create tree for selecting graph
        frame = self.frame2
        self.graph_list = ttk.Treeview(frame, columns=("Graph"), show='headings', selectmode='browse', height=32)
        self.graph_list.heading("Graph", text="Graph")
        self.graph_list.column("Graph", width=375)
        self.graph_list.bind("<<TreeviewSelect>>", self.update_plot)
        self.add_selecting_graph()
        self.graph_list.grid(sticky="WENS")
        
    def frame3_widget(self):
        self.corr = tk.Button(self.frame3, text="Descriptive statistics and Correlation", command= lambda: self.static_page(), font="30")
        self.corr.grid(row=0, column=0, sticky="")
        
    def add_selecting_graph(self):
        list = self.graph_list
        # distribution graph
        list.insert(parent="", index="end", values="Distibution\ of\ Attack")
        list.insert(parent="", index="end", values="Distibution\ of\ Defense")
        list.insert(parent="", index="end", values="Distibution\ of\ Hitpoint")
        list.insert(parent="", index="end", values="Distibution\ of\ Special\ Attack")
        list.insert(parent="", index="end", values="Distibution\ of\ Special\ Defends")
        list.insert(parent="", index="end", values="Distibution\ of\ Speed")
        # part to whole graph
        list.insert(parent="", index="end", values="Proportion\ of\ Generation")
        # Network graph
        list.insert(parent="", index="end", values="Network\ Graph\ of\ Type\ Chart")
        list.insert(parent="", index="end", values="Network\ Graph\ of\ Fire\ Type")
        list.insert(parent="", index="end", values="Network\ Graph\ of\ Water\ Type")
        list.insert(parent="", index="end", values="Network\ Graph\ of\ Grass\ Type")
        # relation graph
        list.insert(parent="", index="end", values="Relationship\ between\ Attack\ and\ Defense")
        list.insert(parent="", index="end", values="Relationship\ between\ Special\ Attack\ and\ Special\ Defense")
        list.insert(parent="", index="end", values="Relationship\ between\ Hitpoint\ and\ Speed")
        # bar graph
        list.insert(parent="", index="end", values="Main\ type\ Frequency")
        
        
    def update_plot(self, event):
        self.selected_g = self.graph_list.item(self.graph_list.focus())["values"][0]
        
        if self.selected_g == "Distibution of Attack":
            self.axes.clear()
            self.describe = self.facade.get_attribute_dis_g("Attack", self.axes)
            self.number_att = 1
            self.fig.tight_layout()
            self.casvas.draw()
        elif self.selected_g == "Distibution of Defense":
            self.axes.clear()
            self.describe = self.facade.get_attribute_dis_g("Defense", self.axes)
            self.number_att = 1
            self.casvas.draw()
        elif self.selected_g == "Distibution of Hitpoint":
            self.axes.clear()
            self.describe = self.facade.get_attribute_dis_g("HP", self.axes)
            self.number_att = 1
            self.casvas.draw()
        elif self.selected_g == "Distibution of Special Attack":
            self.axes.clear()
            self.describe = self.facade.get_attribute_dis_g("Sp. Atk", self.axes)
            self.number_att = 1
            self.casvas.draw()
        elif self.selected_g == "Distibution of Special Defends":
            self.axes.clear()
            self.describe = self.facade.get_attribute_dis_g("Sp. Def", self.axes)
            self.number_att = 1
            self.casvas.draw()
        elif self.selected_g == "Distibution of Speed":
            self.axes.clear()
            self.describe = self.facade.get_attribute_dis_g("Speed", self.axes)
            self.number_att = 1
            self.casvas.draw()
            
        elif self.selected_g == "Proportion of Generation":
            self.axes.clear()
            self.facade.get_generation_part_to_whole_g(self.axes)
            self.describe = None
            self.number_att = 0
            self.casvas.draw()
            
        elif self.selected_g == "Network Graph of Type Chart":
            self.axes.clear()
            self.facade.get_all_type_network_g(self.axes)
            self.describe = None  
            self.number_att = 0
            self.casvas.draw()
            self.fig.delaxes(self.axes)
            self.axes = self.fig.add_subplot()

        elif self.selected_g == "Network Graph of Fire Type":
            self.axes.clear()
            self.facade.get_one_type_chart_g("Fire", self.axes)
            self.describe = None
            self.number_att = 0
            self.casvas.draw()
            self.fig.delaxes(self.axes)
            self.axes = self.fig.add_subplot()
        elif self.selected_g == "Network Graph of Water Type":
            self.axes.clear()
            self.facade.get_one_type_chart_g("Water", self.axes)
            self.describe = None
            self.number_att = 0
            self.casvas.draw()
            self.fig.delaxes(self.axes)
            self.axes = self.fig.add_subplot()
        elif self.selected_g == "Network Graph of Grass Type":
            self.axes.clear()
            self.facade.get_one_type_chart_g("Grass", self.axes)
            self.describe = None
            self.number_att = 0
            self.casvas.draw()
            self.fig.delaxes(self.axes)
            self.axes = self.fig.add_subplot()
            
        elif self.selected_g == "Relationship between Attack and Defense":
            self.axes.clear()
            self.describe_1, self.describe_2, self.correlation = self.facade.get_relationship_g("Attack", "Defense", self.axes)
            self.number_att = 2
            self.casvas.draw()
        elif self.selected_g == "Relationship between Special Attack and Special Defense":
            self.axes.clear()
            self.describe_1, self.describe_2, self.correlation = self.facade.get_relationship_g("Sp. Atk", "Sp. Def", self.axes)
            self.number_att = 2
            self.casvas.draw()
        elif self.selected_g == "Relationship between Hitpoint and Speed":
            self.axes.clear()
            self.describe_1, self.describe_2, self.correlation = self.facade.get_relationship_g("HP", "Speed", self.axes)
            self.number_att = 2
            self.casvas.draw()
            
        elif self.selected_g == "Main type Frequency":
            self.axes.clear()
            self.facade.get_main_type_frequency_g(self.axes)
            self.number_att = 0
            self.casvas.draw()
            
    def static_page(self):
        static_window = tk.Toplevel(self)
        close_button = tk.Button(static_window, command=lambda: self.destroy_descriptive_window(static_window), text="Close")
        static_window.bind("<FocusOut>", lambda e: self.destroy_descriptive_window(static_window))
        static_window.geometry("500x500")
        self.corr.configure(state="disabled")
        if self.number_att == 0:
            static_window.grid_columnconfigure(0, weight=1)
            static_window.grid_rowconfigure(0, weight=1)
            label = tk.Label(static_window, text="There are no \ndescriptive statistics and correlation\n of this attrbute.")
            label.grid(row=0, column=0, sticky="NWSE")
            close_button.grid(row=1, column=0)
        if self.number_att == 1:
            static_window.grid_columnconfigure(0, weight=1)
            static_window.grid_rowconfigure(0, weight=1)
            static_window.grid_rowconfigure(1, weight=2)
            static_window.grid_rowconfigure(2, weight=0)
            title = tk.Label(static_window, text=f"Descriptive statistics of {' '.join(self.selected_g.split(' ')[2::]).lower()}")
            label = tk.Label(static_window, text=self.describe)
            title.grid(row=0, column=0, sticky="SN")
            label.grid(row=1, column=0, sticky="N")
            close_button.grid(row=2, column=0)
            
        if self.number_att == 2:
            title = tk.Label(static_window, text=f"Descriptive statistics of {' '.join(self.selected_g.split(' ')[2::]).lower()}")
            des_1 = tk.Label(static_window, text=self.describe_1)
            des_2 = tk.Label(static_window, text=self.describe_2)
            title_2 = tk.Label(static_window, text=f"Correlation of {' '.join(self.selected_g.split(' ')[2::]).lower()}")
            correlation = tk.Label(static_window, text=f"{self.correlation}")
            
            static_window.grid_columnconfigure(0, weight=1)
            static_window.grid_columnconfigure(1, weight=1)
            static_window.grid_rowconfigure(0, weight=1)
            static_window.grid_rowconfigure(1, weight=1)
            static_window.grid_rowconfigure(2, weight=1)
            static_window.grid_rowconfigure(3, weight=1)
            static_window.grid_rowconfigure(4, weight=1)
            
            title.grid(row=0, column=0, columnspan=2, sticky="S")
            des_1.grid(row=1, column=0)
            des_2.grid(row=1, column=1)
            title_2.grid(row=2, column=0, columnspan=2, sticky="S")
            correlation.grid(row=4, column=0, columnspan=2, sticky="N")
            close_button.grid(row=5, column=0, columnspan=2)
            

    def destroy_descriptive_window(self, master: tk.Toplevel):
        self.corr.configure(state="normal")
        master.destroy()
        
        
class PokemonComparePage(tk.Frame):
    def  __init__(self, master):
        super().__init__(master)
        self.lable1 = tk.Label(self, text="PokemonComparePage PlaceHolder").grid()


if __name__ == "__main__":
    app = App()
    app.mainloop()
    # print("lol")