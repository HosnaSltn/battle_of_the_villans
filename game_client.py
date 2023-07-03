import socket
import game_window

def recving_results_from_server(full_character_dic,_client):
    server_message=(client.recv(1024)).decode("utf-8")
    if server_message=="sorry but you lost this match." or server_message=="congratulations you have won." or server_message=="you both lost your life at the same time so the result of the game is tied.":
        game_window.showing_results(full_character_dic,server_message,client)
    else:
        game_window.choose_your_move(server_message,client)

client= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1",8000))

character_info=(client.recv(1024)).decode('utf-8')
info_list=character_info.split("*")

characters_info_dic=dict()
for i in range(6):
    characters_info_dic[i+1]=info_list[i]

game_window.start_window(characters_info_dic,client)
while True:
    try:
        recving_results_from_server(characters_info_dic,client)
    except:
        break