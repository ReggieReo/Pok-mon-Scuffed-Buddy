class Pokemon:
    
    def __init__(self, name, type1, type2, total, hp, attack,
                defense, sp_attack, sp_defense, speed, 
                gen, legendary) -> None:
        self.__name = name
        self.__type1 = type1
        self.__type2 = type2
        self.__total = total
        self.__hp = hp
        self.__attack = attack
        self.__defense = defense
        self.__sp_attack = sp_attack
        self.__sp_defense = sp_defense
        self.__speed = speed
        self.__gen = gen
        self.__legenday = legendary
        
    def get_name(self):
        return self.__name
    
    def get_type1(self):
        return self.__type1

    def get_type2(self):
        return self.__type2
    
    def get_total(self):
        return self.__total
    
    def get_hp(self):
        return self.__hp
    
    def get_attack(self):
        return self.__attack
    
    def get_defense(self):
        return self.__defense
    
    def get_sp_attack(self):
        return self.__sp_attack
    
    def get_sp_defense(self):
        return self.__sp_defense
    
    def get_speed(self):
        return self.__speed
    
    def get_gen(self):
        return self.__gen
    
    def get_legendary(self):
        return self.__legenday
    
    def __str__(self) -> str:
        return f""" Name: {self.__name}
        {self.__type1}
        {self.__type2}
        {self.__total} 
        {self.__hp}
        {self.__attack}
        {self.__defense}
        {self.__sp_attack}
        {self.__sp_defense}
        {self.__speed}
        {self.__gen}
        {self.__legenday}
    """
    
    