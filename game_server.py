import socket
import game_characters
from datetime import datetime

def make_info_message_about_character(name_char,life,magic):
    name=name_char.name
    e_magic=str(name_char.effective_magic)
    e_strike=str(name_char.effective_strike)
    e_defense=str(name_char.effective_defense)
    magic_r=str(name_char.magic_raise)
    strike=str(name_char.strike_power)
    message="Character Name: "+name+'\n'+"Life: "+str(int(life))+'\n'+"Magic: "+str(int(magic))+'\n'+"Effective Magic: "+e_magic+'\n'+"Effective Strike: "+e_strike+'\n'+"Effective Defense: "+e_defense+'\n'+"Magic Raise: "+magic_r+'\n'+"Strike: "+strike
    return message

def sending_character_info(client):
    full_message=""
    for name in characters_name_list:
        message=make_info_message_about_character(name,100,100)+"*"
        full_message+=message
    client.sendall(full_message.encode())

def recving_client_choice(num):
    choice=(clients[num].recv(1024)).decode("utf-8")
    if choice=="end":
        return "the end"
    dic_clients_message[num]=choice

def write_information_in_file(num,life1,magic1,life2,magic2):
    if life1<=0 and life2<=0:
        message="both players lost their life at the same time so the result of the game is tied.\n"
    elif life1<=0 or life2<=0:
        if life1<=0:
            winner_name="client 2"
        else:
            winner_name="client 1"
        message=f"the final winner of the match is {winner_name}\n"
    else:
        message=f"round{num}:"+"\n"+"client 1:"+"\n"+f"life: {life1}"+"\n"+f"magic: {magic1}"+"\n"+"client 2:"+"\n"+f"life: {life2}"+"\n"+f"magic: {magic2}"+"\n"
    file=open("information.txt","a")
    file.write(message)
    file.close()

my_file=open("information.txt","a")
now = datetime.now()
my_file.write(f'match started at: {now}\n')
my_file.close()

Bellatrix=game_characters.magician('Bellatrix Lestrange',80,65,80,45,25)
Draco=game_characters.magician('Draco Malfoy',68,60,60,50,27)
Lord=game_characters.magician('Lord Voldemort',90,50,60,55,15)
Dolores=game_characters.magician('Dolores Umbridge',70,40,40,60,18)
Lucius=game_characters.magician('Lucius Malfoy',70,70,65,50,20)
Peter=game_characters.magician('Peter Pettigrew',50,55,80,65,12)
characters_name_dic={"Bellatrix":Bellatrix,"Draco":Draco,"Lord":Lord,"Dolores":Dolores,"Lucius":Lucius,"Peter":Peter}

main_server= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
main_server.bind(("",8000))
main_server.listen()
clients = []
characters_name_list=[Bellatrix,Draco,Lord,Dolores,Lucius,Peter]

for num in range(2):
    client_soc, addr = main_server.accept()
    clients.append(client_soc)

for client in clients:
    sending_character_info(client)

magic_client0=100
life_client0=100
magic_client1=100
life_client1=100
round_num=1

while True:
    try:
        dic_clients_message=dict()
        for client in range(len(clients)):
            choice=recving_client_choice(client)
            if choice=="the end":
                raise Exception

        list_choice_client0=dic_clients_message[0].split("*")
        list_name_choice_client0=list_choice_client0[0].split(" ")
        list_choice_client1=dic_clients_message[1].split("*")
        list_name_choice_client1=list_choice_client1[0].split(" ")

        class_name_client0=list_name_choice_client0[0]
        move_client0=list_choice_client0[1]
        class_name_client1=list_name_choice_client1[0]
        move_client1=list_choice_client1[1]

        life_client0=life_client0-game_characters.calculate_life1(move_client0,characters_name_dic[class_name_client0],move_client1,characters_name_dic[class_name_client1])
        life_client1=life_client1-game_characters.calculate_life1(move_client1,characters_name_dic[class_name_client1],move_client0,characters_name_dic[class_name_client0])
        magic_client0=magic_client0-game_characters.calculate_magic1(move_client0,characters_name_dic[class_name_client0],move_client1,characters_name_dic[class_name_client1])
        magic_client1=magic_client1-game_characters.calculate_magic1(move_client1,characters_name_dic[class_name_client1],move_client0,characters_name_dic[class_name_client0])
        if life_client1<=0 and life_client0<=0:
            message_client0="you both lost your life at the same time so the result of the game is tied."
            message_client1="you both lost your life at the same time so the result of the game is tied."
        elif life_client1<=0 or life_client0<=0:
            if life_client0<=0:
                message_client0="sorry but you lost this match."
                message_client1="congratulations you have won."
            else:
                message_client0="congratulations you have won."
                message_client1="sorry but you lost this match."
        else:
            message_client0=make_info_message_about_character(characters_name_dic[class_name_client0],life_client0,magic_client0)
            message_client1=make_info_message_about_character(characters_name_dic[class_name_client1],life_client1,magic_client1)

        clients[0].sendall(message_client0.encode())
        clients[1].sendall(message_client1.encode())

        write_information_in_file(round_num,life_client0,magic_client0,life_client1,magic_client1)
        round_num+=1

        if life_client0<=0 or life_client1<=0:
            magic_client0=100
            life_client0=100
            magic_client1=100
            life_client1=100
            round_num=1

    except:
        main_server.close()
        break