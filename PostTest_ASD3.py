import pwinput
import time
import sys
import os
os.system('cls')

def login():
    print('''\n
    =====================
    |     L O G I N     |
    =====================''')
    uname = str.lower(input("Masukkan username : "))
    username = uname.capitalize()
    if username == "Sani" :
        pin = int(pwinput.pwinput("Masukkan PIN : "))
        if pin == 123 :
            time.sleep(1)
            os.system('cls')
            menu()
        else:
            print("Silahkan masukkan PIN yang sesuai!")
            time.sleep(1)
            os.system('cls')
            login()
    else:
        print("Silahkan masukkan username yang sesuai!")
        time.sleep(1)
        os.system('cls')
        login()

def menu():
    pilih = str(input('''
    =================================
    |            Welcome            |
    |           DRAKOR.ID           |
    =================================
    |>>>>> Silahkan pilih opsi <<<<<|
    |                               |
    |   1. Drakor Favorit           |
    |   2. Drakor On Going          |
    |   3. History Tontonan         |
    |   4. Log Out                  |
    |                               |
    =================================
Silahkan pilih opsi (1/2/3/4): '''))
    if pilih == '1':
        time.sleep(1)
        os.system('cls')
        drakor_fav()
    elif pilih == '2':
        time.sleep(1)
        os.system('cls')
        drakor_OnGoing()
    elif pilih == '3':
        time.sleep(1)
        os.system('cls')
        history()
    elif pilih == '4':
        time.sleep(1)
        os.system('cls')
        LogOut()
    else:
        print("Masukkan pilihan opsi yang benar")
        time.sleep(1)
        os.system('cls')
        menu()

def drakor_fav():
    class drakor_fav:
        def __init__(self, nama, genre, tahun_rilis):
            self.name = nama
            self.genree = genre
            self.tahun = tahun_rilis

    drakor_favv1 = drakor_fav("Twenty-Five Twenty-One", "Roman, Coming-of-age", 2022)
    drakor_favv2 = drakor_fav("All Of Us Are Dead", "Zombie apocalypse, Horor", 2022)

    print('''
    =====================================
    | List Drama Korea Ter-Favorit 2022 |
    =====================================''')
    print("Judul       : ",drakor_favv1.name)
    print("Genre       : ",drakor_favv1.genree)
    print("Tahun Rilis : ",drakor_favv1.tahun)
    print("=========================================")
    print("Judul       : ",drakor_favv2.name)
    print("Genre       : ",drakor_favv2.genree)
    print("Tahun Rilis : ",drakor_favv2.tahun)
    print("=========================================")
    print(input("Klik enter untuk kembali"))
    time.sleep(1)
    os.system('cls')
    menu()

def drakor_OnGoing():
    class drakor_OnGoing:
        def __init__(self, nama, genre, tanggal_liris_eps_selanjutnya):
            self.name = nama
            self.genree = genre
            self.tanggal = tanggal_liris_eps_selanjutnya

    drakor_OnGoingg1 = drakor_OnGoing("Taxi Driver 2", "Action, Thriller", "24 Maret 2023")
    drakor_OnGoingg2 = drakor_OnGoing("Delivery Man", "Roman", "22 Maret 2023")

    print('''
    ==================================
    | List Drama Korea On Going 2023 |
    ==================================''')
    print("Judul               : ",drakor_OnGoingg1.name)
    print("Genre               : ",drakor_OnGoingg1.genree)
    print("Episode Selanjutnya : ",drakor_OnGoingg1.tanggal)
    print("===========================================")
    print("Judul               : ",drakor_OnGoingg2.name)
    print("Genre               : ",drakor_OnGoingg2.genree)
    print("Episode Selanjutnya : ",drakor_OnGoingg2.tanggal)
    print("===========================================")
    print(input("Klik enter untuk kembali"))
    time.sleep(1)
    os.system('cls')
    menu()

def history():
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

    class LinkedList:
        def __init__(self):
            self.head = None

        #menambahkan data di awal
        def prepend(self, node):
            node.next = self.head
            self.head = node

        def print_all(self):
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next


    list = LinkedList()

    print('''
    ==================================
    |        Histori Tontonan        |
    ==================================''')
    list.prepend(Node("The Devil Judge"))
    list.prepend(Node("Dark Hole"))
    list.prepend(Node("Vincenzo"))
    list.prepend(Node("Mouse"))
    list.prepend(Node("Start-UP"))

    list.print_all()
    print("======================================")
    print(input("Klik enter untuk kembali"))
    time.sleep(1)
    os.system('cls')
    menu()

def LogOut():
    os.system('cls')
    sys.exit()

login()