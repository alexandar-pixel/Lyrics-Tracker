# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 13 2019)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

from PIL import Image
from tkinter import *		 #Sve tri tinker biblioteke su neophode za .askdirectory()
from tkinter import filedialog
import tkinter as tk     
import wx
import wx.xrc
import wx.richtext
import sys
import os
import spotipy
import spotipy.util as util
import lyricsgenius
import json
from json.decoder import JSONDecodeError
import urllib.request
import threading
import time

username = '04jtk7i35d3c5u9m5728c46mm'

scopes = 'user-read-private user-read-playback-state user-modify-playback-state user-read-currently-playing '

#User ID: 04jtk7i35d3c5u9m5728c46mm

#Brisanje kes memorije i autentacija
try:
    token = util.prompt_for_user_token(username,scope = scopes,client_id='8343db87971f4c538222f3599ab9245f',client_secret='716e7d50760640a28f1cd61e8340abe8',redirect_uri='http://www.google.com/')
except:
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username,scope = scopes,client_id='8343db87971f4c538222f3599ab9245f',client_secret='716e7d50760640a28f1cd61e8340abe8',redirect_uri='http://www.google.com/')

#Genius API objekat
genius = lyricsgenius.Genius("xQP_kEpP9ekBfB8w_JQ9gHqKZmmr7ShwqMkWsc6WtsNxyBQVvJCBWoM6sXCfUWH9")

def uzmiTekst(pesma, umetnik, kutija):
	tekst = genius.search_song(pesma, artist = umetnik)
	kutija.SetValue("")
	kutija.AppendText(tekst.title + " - " + tekst.artist + "\n")
	kutija.AppendText("\n" + tekst.lyrics)
	print(threading.active_count())

def uzmiSliku(pesma, kutija, stikla, bul):
	#print(json.dumps(pesma, sort_keys = True, indent = 4))
	try:
		if bul == True:
			url = pesma['item']['album']['images'][0]['url']
			ime = pesma['item']['album']['name']
		
		else:
			url = pesma['tracks']['items'][0]['album']['images'][0]['url']
			ime = pesma['tracks']['items'][0]['album']['name']
	except:
		ime = "."
		wx.MessageBox("An error occured. \nPlease check your spelling and your connection to Spotify.", 'Error', wx.OK | wx.ICON_ERROR)
	
	if ime != ".":
		for i in ime:
			if i == "?" or i == "/" or i == "*" or i == ">" or i == "<" or i == "|" :
				ime = ime.replace(i,"")
	
	print(ime)

	if stikla.GetValue() == True:
		root = Tk()
		root.withdraw()
		root.attributes("-topmost", True)

		putanja = filedialog.askdirectory()
		putanjaCela = os.path.abspath(putanja + "/" + ime + '.jpg')  #os.path.abspath daje celu putanju automatski i resava vecinu errora vezani za putanju
		print(putanjaCela)
		urllib.request.urlretrieve(url, putanjaCela)

		img = wx.Image(putanjaCela, type=wx.BITMAP_TYPE_ANY , index=-1)

	else:
		putanja = os.getenv('APPDATA')
		print(putanja)
		putanjaCela = os.path.abspath(putanja + "/" + ime + '.jpg')  #os.path.abspath daje celu putanju automatski i resava vecinu errora vezani za putanju
		print(putanjaCela)
		urllib.request.urlretrieve(url, putanjaCela)

		img = wx.Image(putanjaCela, type=wx.BITMAP_TYPE_ANY, index=-1)
		os.remove(putanjaCela)

	print(type(img))

	kutija.SetValue("")
	kutija.AddImage(img)
	kutija.AppendText("") #Ovo dodajem da bi se richText azurirao, ako se ne azurira ne prikazuje se slika
	print(threading.active_count())


threadLista = []

###########################################################################
## Class frameMain
###########################################################################

class frameMain ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Lyrics Tracker", pos = wx.DefaultPosition, size = wx.Size( 700,780 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizerMainFrameN = wx.BoxSizer( wx.VERTICAL )

		bSizerMainFrame = wx.BoxSizer( wx.VERTICAL )

		self.m_panelMain = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 700,780 ), wx.TAB_TRAVERSAL )
		bSizerPanelN1 = wx.BoxSizer( wx.VERTICAL )

		bSizerPanelN2 = wx.BoxSizer( wx.VERTICAL )

		bSizer12 = wx.BoxSizer( wx.HORIZONTAL )

		bSizerPanel1 = wx.BoxSizer( wx.HORIZONTAL )

		self.buttonGetCurrentLyrics = wx.Button( self.m_panelMain, wx.ID_ANY, u"Get Current Lyrics", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerPanel1.Add( self.buttonGetCurrentLyrics, 0, wx.ALL, 5 )

		self.buttonGetCurrentCoverArt = wx.Button( self.m_panelMain, wx.ID_ANY, u"Get Current Cover Art", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerPanel1.Add( self.buttonGetCurrentCoverArt, 0, wx.ALL, 5 )

		self.checkBoxDownload = wx.CheckBox( self.m_panelMain, wx.ID_ANY, u"Download Cover Art", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerPanel1.Add( self.checkBoxDownload, 0, wx.TOP|wx.LEFT, 12 )


		bSizer12.Add( bSizerPanel1, 0, 0, 0 )


		bSizerPanelN2.Add( bSizer12, 0, 0, 0 )

		bSizerPanel2 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_textCtrlSongName = wx.TextCtrl( self.m_panelMain, wx.ID_ANY, u"Enter Song Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerPanel2.Add( self.m_textCtrlSongName, 0, wx.ALL, 5 )
		self.m_textCtrlSongName.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )

		self.m_textCtrlArtistName = wx.TextCtrl( self.m_panelMain, wx.ID_ANY, u"Enter Artist Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerPanel2.Add( self.m_textCtrlArtistName, 0, wx.ALL, 5 )
		self.m_textCtrlArtistName.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )

		self.buttonGetLyrics = wx.Button( self.m_panelMain, wx.ID_ANY, u"Get Lyrics", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerPanel2.Add( self.buttonGetLyrics, 0, wx.ALL, 5 )

		self.buttonGetCoverArt = wx.Button( self.m_panelMain, wx.ID_ANY, u"Get Cover Art", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerPanel2.Add( self.buttonGetCoverArt, 0, wx.ALL, 5 )


		bSizerPanelN2.Add( bSizerPanel2, 0, wx.ALL, 0 )

		bSizerPanel3 = wx.BoxSizer( wx.VERTICAL )

		self.m_richTextLyrics = wx.richtext.RichTextCtrl( self.m_panelMain, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		bSizerPanel3.Add( self.m_richTextLyrics, 1, wx.EXPAND |wx.ALL, 5 )


		bSizerPanelN2.Add( bSizerPanel3, 1, wx.ALL|wx.EXPAND, 0 )


		bSizerPanelN1.Add( bSizerPanelN2, 1, wx.EXPAND, 0 )


		self.m_panelMain.SetSizer( bSizerPanelN1 )
		self.m_panelMain.Layout()
		bSizerMainFrame.Add( self.m_panelMain, 1, wx.EXPAND |wx.ALL, 0 )


		bSizerMainFrameN.Add( bSizerMainFrame, 1, wx.ALL|wx.EXPAND, 0 )


		self.SetSizer( bSizerMainFrameN )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.buttonGetCurrentLyrics.Bind( wx.EVT_BUTTON, self.buttonGetCurrentLyricsOnButtonClick )
		self.buttonGetCurrentCoverArt.Bind( wx.EVT_BUTTON, self.buttonGetCurrentCoverArtOnButtonClick )
		self.m_textCtrlSongName.Bind( wx.EVT_SET_FOCUS, self.m_textCtrlSongNameOnSetFocus )
		self.m_textCtrlArtistName.Bind( wx.EVT_SET_FOCUS, self.m_textCtrlArtistNameOnSetFocus )
		self.buttonGetLyrics.Bind( wx.EVT_BUTTON, self.buttonGetLyricsOnButtonClick )
		self.buttonGetCoverArt.Bind( wx.EVT_BUTTON, self.buttonGetCoverArtOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def buttonGetCurrentLyricsOnButtonClick( self, event ):
		sp = spotipy.Spotify(auth = token) #Spotify objekat

		#Uzimanje potrebih objekata/podataka
		user = sp.current_user() #Korisnik
		#uredjaji = sp.devices() #Uredjaji
		#uredjajiID = [uredjaji['devices'][0]['id']]
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

			t1 = threading.Thread(target = uzmiTekst, name = "uzmiTekst", args = (pesma, umetnik, self.m_richTextLyrics))
			t1.start()
			#uzmiTekst(pesma, umetnik, self.m_richTextLyrics)
		
		else:
			wx.MessageBox("An error occured while connecting to Spotify's servers. \nPlease refresh Spotify.", 'Error', wx.OK | wx.ICON_ERROR)

	def buttonGetCurrentCoverArtOnButtonClick( self, event ):
		currentCoverArt = True

		sp = spotipy.Spotify(auth = token) #Spotify objekat

		pesma = sp.current_user_playing_track()

		t2 = threading.Thread(target = uzmiSliku, name = "uzmiSliku", args = (pesma, self.m_richTextLyrics, self.checkBoxDownload, currentCoverArt))
		t2.start()
		#uzmiSliku(pesma, self.m_richTextLyrics, self.checkBoxDownload, currentCoverArt)
		#event.Skip()

	def m_textCtrlSongNameOnSetFocus( self, event ):
		self.m_textCtrlSongName.ForegroundColour = "Window Text"
		if self.m_textCtrlSongName.GetValue() == "Enter Song Name":
			self.m_textCtrlSongName.SetValue("")

	def m_textCtrlArtistNameOnSetFocus( self, event ):
		self.m_textCtrlArtistName.ForegroundColour = "Window Text"
		if self.m_textCtrlArtistName.GetValue() == "Enter Artist Name":
			self.m_textCtrlArtistName.SetValue("")

	def buttonGetLyricsOnButtonClick( self, event ):
		pesma = self.m_textCtrlSongName.GetValue()
		umetnik = self.m_textCtrlArtistName.GetValue()
		print(pesma)
		print(umetnik)

		t1 = threading.Thread(target = uzmiTekst, name = "uzmiTekst", args = (pesma, umetnik, self.m_richTextLyrics))
		t1.start()
		#uzmiTekst(pesma, umetnik, self.m_richTextLyrics)
		#event.Skip()

	def buttonGetCoverArtOnButtonClick( self, event ):
		currentCoverArt = False
		#print("debuging", self.m_textCtrlSongName.GetValue())
		sp = spotipy.Spotify(auth = token) #Spotify objekat

		if self.m_textCtrlSongName.GetValue() == "Enter Song Name":
			pesma = "."
		else:
			pesma = self.m_textCtrlSongName.GetValue()
		
		if self.m_textCtrlArtistName.GetValue() == "Enter Artist Name":
			umetnik = "."
		else:
			umetnik = self.m_textCtrlArtistName.GetValue()
		
		if pesma == "." and umetnik == ".":
			pesma = ""
			umetnik = ""

		pesma = pesma + " " + umetnik
		pesma = sp.search(pesma, limit=1, offset=0, type='track', market=None)

		t2 = threading.Thread(target = uzmiSliku, name = "uzmiSliku", args = (pesma, self.m_richTextLyrics, self.checkBoxDownload, currentCoverArt))
		t2.start()
		#uzmiSliku(pesma, self.m_richTextLyrics, self.checkBoxDownload, currentCoverArt)

		#print(json.dumps(pesmaInfo, sort_keys = True, indent = 4))


class MainApp(wx.App):
	def OnInit(self):
		mainFrame = frameMain(None)
		mainFrame.Show(True)
		return True

if __name__ == '__main__':
	app = MainApp()
	app.MainLoop()
