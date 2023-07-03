import random

class magician:
    def __init__(self,name,effective_magic,effective_strike,effective_defense,magic_raise,strike_power):
        self.life=100
        self.magic=100
        self.avada_kedavra=35
        self.stupefy=22
        self.confringo=15
        self.name=name
        self.effective_magic=effective_magic
        self.effective_strike=effective_strike
        self.effective_defense=effective_defense
        self.magic_raise=magic_raise
        self.strike_power=strike_power

def random_selection(num):
    list=[0,1]
    list_1=random.choices(list,[100-num,num])
    return list_1[0]

def calculate_life1(move1,class_name1,move2,class_name2):
    damage=0
    if move1=="defense":
        possibility1=random_selection(class_name1.effective_defense)
        if possibility1==0:
            if move2=="strike":
                possibility2=random_selection(class_name2.effective_strike)
                if possibility2==1:
                    damage= class_name2.strike_power
            elif move2=="avada_kedavra":
                possibility2=random_selection(class_name2.effective_magic)
                if possibility2==1:
                    damage= class_name2.avada_kedavra
            elif move2=="stupefy":
                possibility2=random_selection(class_name2.effective_magic)
                if possibility2==1:
                    damage=class_name2.stupefy
            elif move2=="confringo":
                possibility2=random_selection(class_name2.effective_magic)
                if possibility2==1:
                    damage=class_name2.confringo
    elif move2=="strike":
        possibility1=random_selection(class_name1.effective_strike)
        if possibility1==1:
            damage= class_name2.strike_power
    elif move2=="avada_kedavra":
        possibility1=random_selection(class_name1.effective_magic)
        if possibility1==1:
            damage= class_name2.avada_kedavra
    elif move2=="stupefy":
        possibility1=random_selection(class_name1.effective_magic)
        if possibility1==1:
            damage= class_name2.stupefy
    elif move2=="confringo":
        possibility1=random_selection(class_name1.effective_magic)
        if possibility1==1:
            damage= class_name2.confringo
    return damage

def calculate_magic1(move1,class_name1,move2,class_name2):
    decrease=0
    if move1=="avada_kedavra" and calculate_life1(move1,class_name1,move2,class_name2)!=0:
        decrease= class_name1.avada_kedavra-(class_name1.avada_kedavra*(class_name1.magic_raise/100))
    elif move1=="stupefy" and calculate_life1(move1,class_name1,move2,class_name2)!=0:
        decrease= class_name1.stupefy-(class_name1.stupefy*(class_name1.magic_raise/100))
    elif move1=="confringo" and calculate_life1(move1,class_name1,move2,class_name2)!=0:
        decrease= class_name1.confringo-(class_name1.confringo*(class_name1.magic_raise/100))
    elif move1=="avada_kedavra" and calculate_life1(move1,class_name1,move2,class_name2)==0:
        decrease=class_name1.avada_kedavra
    elif move1=="stupefy" and calculate_life1(move1,class_name1,move2,class_name2)==0:
        decrease=class_name1.stupefy
    elif move1=="confringo" and calculate_life1(move1,class_name1,move2,class_name2)==0:
        decrease=class_name1.confringo
    return decrease