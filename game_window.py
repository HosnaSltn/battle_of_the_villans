import tkinter as tk

def start_window(info_dic,client_soc):
    window=tk.Tk()
    window.title("battle of the villans")
    tk.Label().grid(row=0,column=0,pady=40)
    game_title= tk.Label(text="battle of the villans",font=("AdageDisplayCapsSSi",18)).grid(row=1,column=0,padx=40)
    welcome_label= tk.Label(text="Welcome",font=("Holy Mackerel!",20)).grid(row=2,column=0,pady=5)
    start_button= tk.Button(text="Start",font=("Holy Mackerel!",20),command=lambda :[close_window(window),choose_window(info_dic,client_soc)]).grid(row=3,column=0,pady=50)
    window.mainloop()

def close_window(window):
    window.destroy()

def choose_window(info_dic,client_soc):
    window=tk.Tk()
    window.title("battle of the villans")
    menu= tk.Label(text="Choose your character:",font=("ArcaneBroad",10)).grid(row=0,column=0)
    d=tk.Label(text="(you can see details of each character by clicking over their name)",font=("ArcaneBroad",10)).grid(row=1,column=0)
    name_dic=make_dic_of_names(info_dic)
    character_1= tk.Button(text=name_dic[0],command=lambda :[close_window(window),show_character_info(info_dic,1,client_soc)]).grid(row=2,column=0,pady=5)
    character_2= tk.Button(text=name_dic[1],command=lambda :[close_window(window),show_character_info(info_dic,2,client_soc)]).grid(row=3,column=0,pady=5)
    character_3= tk.Button(text=name_dic[2],command=lambda :[close_window(window),show_character_info(info_dic,3,client_soc)]).grid(row=4,column=0,pady=5)
    character_4= tk.Button(text=name_dic[3],command=lambda :[close_window(window),show_character_info(info_dic,4,client_soc)]).grid(row=5,column=0,pady=5)
    character_5= tk.Button(text=name_dic[4],command=lambda :[close_window(window),show_character_info(info_dic,5,client_soc)]).grid(row=6,column=0,pady=5)
    character_6= tk.Button(text=name_dic[5],command=lambda :[close_window(window),show_character_info(info_dic,6,client_soc)]).grid(row=7,column=0,pady=5)
    exit_button= tk.Button(text="exit",font=("ArcaneBroad",10),command=lambda :[close_window(window),client_exit(client_soc)]).grid(row=8,column=0,pady=10)
    window.mainloop()

def make_dic_of_names(info_dic):
    list_name=[]
    for str_info in info_dic.values():
        name=take_out_the_name(str_info)
        list_name.append(name)
    return list_name

def take_out_the_name(str_info):
    info_list= str_info.split("\n")
    character_name= info_list[0].split(":")
    return character_name[1]

def show_character_info(info_dic,num_character,client_soc):
    window=tk.Tk()
    window.title("battle of the villans")
    character_pic= tk.PhotoImage(file=f"{num_character}.png")
    character_pic_label= tk.Label(image=character_pic).grid(row=0,column=0)
    character_info_label= tk.Label(text=info_dic[num_character],font=("ArcaneBroad",10)).grid(row=1,column=0)
    back_button= tk.Button(text="go back",font=("Holy Mackerel!",10),command=lambda :[close_window(window),choose_window(info_dic,client_soc)]).grid(row=2,column=1,padx=15)
    pick_bottun= tk.Button(text="pick this character",font=("Holy Mackerel!",10),command=lambda :[close_window(window),choose_your_move(info_dic[num_character],client_soc)]).grid(row=2,column=0)
    exit_button= tk.Button(text="exit",font=("Holy Mackerel!",10),command=lambda :[close_window(window),client_exit(client_soc)]).grid(row=2,column=2,padx=20)
    window.mainloop()

def client_exit(client_soc):
    window=tk.Tk()
    window.title("battle of the villans")
    farewell_label= tk.Label(text="Goodbye!",font=("AdageDisplayCapsSSi",20)).grid(padx=200,pady=270)
    server_message=client_soc.sendall("end".encode())
    client_soc.close()
    window.mainloop()

def choose_your_move(character_info,client_soc):
    window=tk.Tk()
    window.title("battle of the villans")
    window.geometry("600x200")
    choose_move_label= tk.Label(text="Choose what move you want to make:\nif you don't have any magic left you can't use magic moves. ",font=("ArcaneBroad",10)).grid(row=1,column=0)
    move_1= tk.Button(text="1.Strike",font=("ArcaneBroad",10),command=lambda :[close_window(window),client_selections ("strike",character_info,client_soc)]).grid(row=2,column=0)
    move_2= tk.Label(text="2.Magic",font=("ArcaneBroad",10)).grid(row=3,column=0)
    spell1= tk.Button(text="Avada Kedavra",font=("ArcaneBroad",10),command=lambda :[close_window(window),client_selections ("avada_kedavra",character_info,client_soc)]).grid(row=4,column=0)
    spell2= tk.Button(text="Stupefy",font=("ArcaneBroad",10),command=lambda :[close_window(window),client_selections ("stupefy",character_info,client_soc)]).grid(row=4,column=1)
    spell3= tk.Button(text="Confringo",font=("ArcaneBroad",10),command=lambda :[close_window(window),client_selections ("confringo",character_info,client_soc)]).grid(row=4,column=2)
    move_3= tk.Button(text="3.Defense",font=("ArcaneBroad",10),command=lambda :[close_window(window),client_selections ("defense",character_info,client_soc)]).grid(row=5,column=0)
    exit_button= tk.Button(text="Exit",font=("ArcaneBroad",10),command=lambda :[close_window(window),client_exit(client_soc)]).grid(row=6,column=0)
    character_name=take_out_the_name(character_info)
    tk.Label(text=character_name,font=("ArcaneBroad",15)).grid(row=0,column=0)
    life,magic=take_out_life_and_magic(character_info)
    life_label=tk.Label(text="Life:",font=("ArcaneBroad",10)).grid(row=1,column=1)
    life_line= tk.Label(text=space(life),bg="blue").grid(row=1,column=2)
    magic_label=tk.Label(text="Magic:",font=("ArcaneBroad",10)).grid(row=2,column=1)
    magic_line= tk.Label(text=space(magic),bg="red").grid(row=2,column=2)
    window.mainloop()

def space(num):
    str=""
    for i in range(int(num)):
        str+=" "
    return str

def take_out_life_and_magic(str_info):
    split_list= str_info.split("\n")
    life_= split_list[1].split(":")
    magic_= split_list[2].split(":")
    life= life_[1][1:]
    magic= magic_[1][1:]
    return life,magic

def client_selections (move_kind,character_info,client_soc):
    character_name=take_out_the_name(character_info)
    client_choice=character_name[1:]+"*"+move_kind
    client_soc.sendall(client_choice.encode())

def showing_results(info_dic,result_str,client_soc):
    window=tk.Tk()
    window.title("battle of the villans")
    result= tk.Label(text=result_str,font=("ArcaneBroad",10)).grid(row=0,column=0)
    tk.Label(text="if you would like to play again click on the another match button or else click on the exit button.",font=("ArcaneBroad",10)).grid(row=1,column=0)
    tk.Button(text="another match",font=("ArcaneBroad",10),command=lambda :[close_window(window),choose_window(info_dic,client_soc)]).grid(row=2,column=1)
    exit_button= tk.Button(text="Exit",font=("ArcaneBroad",10),command=lambda :[close_window(window),client_exit(client_soc)]).grid(row=2,column=2)
    window.mainloop()
