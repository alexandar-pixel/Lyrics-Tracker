#! python3

import sys
import os
import spotipy
import spotipy.util as util
import lyricsgenius
import json
from json.decoder import JSONDecodeError
import webbrowser
import urllib.request
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import Image
from appJar import gui

putanja = ""

os.environ["PYTHONIOENCODING"] = "utf-8" #Deklarisem UTF-8 codec jer pythonov automatski codec ne moze nekad da dekodira tekst sa Geniusa

#Uziamnje korisnickog imena, ako korisnicko ime nije vec uvedeno automatski uzima moje
if len(sys.argv) > 1:
    username = sys.argv[1]
else: 
    username = '04jtk7i35d3c5u9m5728c46mm'

scopes = 'user-read-private user-read-playback-state user-modify-playback-state user-read-currently-playing '

#User ID: 04jtk7i35d3c5u9m5728c46mm

#Brisanje kes memorije i autentacija
try:
    token = util.prompt_for_user_token(username,scope = scopes,client_id='8343db87971f4c538222f3599ab9245f',client_secret='716e7d50760640a28f1cd61e8340abe8',redirect_uri='http://www.google.rs/')
except:
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username,scope = scopes,client_id='8343db87971f4c538222f3599ab9245f',client_secret='716e7d50760640a28f1cd61e8340abe8',redirect_uri='http://www.google.rs/')

#Genius API objekat
genius = lyricsgenius.Genius("3zwyKeI25QzVoqrxVaYD8j-_JZGL6iB6yPYNPZKxpcsY7crFNhlxRiTO0SjBHf5Z")

def uzmiTekst(pesma, umetnik):
    print("\n")
    tekst = genius.search_song(pesma, umetnik)
    with open('G:\coding, matura etc\coding\Rest of proggraming\Python\Lyric tracker\Tekst.txt', 'w') as f: #POSTO NE MOGU DA NADJEM DOKUMENTACIJU song.title za ime pesme
        f.write(tekst.title + " - " + tekst.artist + "\n")                                                  #                                      song.artist za ime umetnika  
        f.write("\n")                                                                                       #                                      song.lyrics za tekst pesme 
        f.write(tekst.lyrics + "\n")
        os.startfile('G:\coding, matura etc\coding\Rest of proggraming\Python\Lyric tracker\Tekst.txt')

    with open('G:\coding, matura etc\coding\Rest of proggraming\Python\Lyric tracker\Lista Pesama.txt', 'a') as f:
        f.write(tekst.title + " - " + tekst.artist + "\n")

    #print(tekst.lyrics)
    #print(tekst)
    #print(pesma)

def dl_img(url, putanja, ime):

    root = Tk()
    root.withdraw()
    root.attributes("-topmost", True)

    putanja = filedialog.askdirectory()
    putanjaCela = os.path.abspath(putanja + "/" + ime + '.jpg')  #os.path.abspath daje celu putanju automatski i resava vecinu errora vezani za putanju
    urllib.request.urlretrieve(url, putanjaCela)

    print("Download complete at:", putanjaCela)
    print("Open picture? y/n")

    odluka = input()

    if odluka == "y":
        img = Image.open(putanjaCela)
        img.show()

    if odluka == "n":
        pass
    
    with open("G:\coding, matura etc\coding\Rest of proggraming\Python\Lyric tracker\Lista Albumskih Ilustracija.txt", 'a') as f:
        f.write(pesmaInfo['item']['album']['images'][0]['url'] + " " + pesma + " - " + umetnik + "\n")

def uzmiSliku(pesma, umetnik):
    global albumIme
    print("Download image? y/n")
    if input() == "y":
        url = pesmaInfo['item']['album']['images'][0]['url']
        print("Do you want to rename the image? y/n")

        if input() == "y":
            ime = input()
        else:
            ime = albumIme

        putanja = 'G:\coding, matura etc\coding\Rest of proggraming\Python\Lyric tracker\slike'
        
        dl_img(url, putanja, ime)
        

    else:
        print("Otvara se")

        webbrowser.open(pesmaInfo['item']['album']['images'][0]['url'])

        with open("G:\coding, matura etc\coding\Rest of proggraming\Python\Lyric tracker\Lista Albumskih Ilustracija.txt", 'a') as f:
            f.write(pesmaInfo['item']['album']['images'][0]['url'] + " " + pesma + " - " + umetnik + "\n")


def manualno():

    print("1 for lyrics")
    print("2 for cover art")

    odluka = input() #Iz nekog razloga mora ovako da se radi sa inputom jer ako stavim samo input() onda mora vise puta da se klikne enter

    if odluka == "1":
        global pesma
        global umetnik
        print("Input the name of the song: ")
        pesma = input()
        print("Input the artist (If you don't know leave blank): ")
        umetnik = input()
        uzmiTekst(pesma, umetnik)

    if odluka == "2":
        global url
        global putanja
        global ime

        putanja = "slike/"

        print("Input name of album and artist: ")
        ime = input()
        albumInfo = sp.search(ime, limit=1, offset=0, type='album', market=None)
        #print(json.dumps(albumInfo, sort_keys = True, indent = 4))
        ime = albumInfo['albums']['items'][0]['name']
        print(ime)
        url = albumInfo['albums']['items'][0]['images'][0]['url']
        print(url)
        dl_img(url, putanja, ime)

def pustiPesmu():
    print("\n")
    print("DISCLAIMER: PREMIUM REQUIERD")
    print("\n")
    try:
        print("Input the name of the song and artist: ")
        ime = input()
        pesme = []
        pesma = sp.search(ime, limit=1, offset=0, type='track', market=None)
        pesme.append([pesma['tracks']['items'][0]['name']])
        #print(json.dumps(pesma, sort_keys = True, indent = 4))
        
        sp.start_playback(uredjajiID[0], None, pesme)
    except:
        print("\n")
        print("You don't have premium :(")
        print("\n")

while True:  #Mnoge stvari su ovde jer moraju da se azuriraju sa Spotifajevim serverom
    
    
    sp = spotipy.Spotify(auth = token) #Spotify objekat

    #Uzimanje potrebih objekata/podataka
    user = sp.current_user() #Korisnik
    uredjaji = sp.devices() #Uredjaji
    uredjajiID = [uredjaji['devices'][0]['id']]
    #print(json.dumps(uredjaji, sort_keys = True, indent = 4))
    pesmaInfo = sp.current_user_playing_track() #Pesma
    #print(json.dumps(pesmaInfo, sort_keys = True, indent = 4))

    ERRORpostoji = False

    try:                                  
        pesma = pesmaInfo['item']['name'] #Koristim try/except zato sto se posle nekog vremena Spotify diskonektuje i to pravi error sa API-em zato upozoravam korisnika
    except:                               # da osvezi Spotify
        ERRORpostoji = True
    if ERRORpostoji == False:
        for i in pesma: #Kada pesma ima '-' to cesto zbuni Geniusev API a i Python zato kada ima '-' u imenu pesme samo obrsem sve nakon '-'
            if i == "-":
                pesma = pesma[:pesma.find("-")-1]
                ERRORpostoji = False
                break

        umetnik = pesmaInfo['item']['album']['artists'][0]['name'] #Umetnik
        #print(json.dumps(pesmaInfo, sort_keys = True, indent = 4))
        albumIme = pesmaInfo['item']['album']['name']
        displayName = user['display_name'] #Ime korisnika u Spotify-u

        print("\n")
        print(f"@@@@@ Currently playing: {pesma} - {umetnik} @@@@")
        print("\n")
        print("1 for lyrics of current song playing")
        print("2 for cover art of current song playing")
        print("3 to play a song")
        print("m for manual input")
        print("r for refresh")
        print("0 to exit")

        odluka = input()

        if odluka == "1":
            uzmiTekst(pesma, umetnik)
        if odluka == "2":
            uzmiSliku(pesma, umetnik)
        if odluka == "0":
            sys.exit()
        if odluka == "3":
            pustiPesmu()
        if odluka == "r":
            pass
        if odluka == "m":
            manualno()
        
    else:
        print("\n")
        print("There was an error please refresh Spotify\n")
        break
