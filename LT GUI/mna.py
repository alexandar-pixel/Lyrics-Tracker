# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 13 2019)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

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
import webbrowser
import urllib.request
import tkinter as tk           #Sve tri tinker biblioteke su neophode za .askdirectory()
from tkinter import filedialog
from tkinter import *
from PIL import Image

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
genius = lyricsgenius.Genius("3zwyKeI25QzVoqrxVaYD8j-_JZGL6iB6yPYNPZKxpcsY7crFNhlxRiTO0SjBHf5Z")

###########################################################################
## Class frameMain
###########################################################################

class frameMain ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"wxPython learning", pos = wx.DefaultPosition, size = wx.Size( 900,900 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizerMainFrameN = wx.BoxSizer( wx.VERTICAL )

		bSizerMainFrame = wx.BoxSizer( wx.VERTICAL )

		self.m_panelMain = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 900,900 ), wx.TAB_TRAVERSAL )
		bSizerPanelN1 = wx.BoxSizer( wx.VERTICAL )

		bSizerPanelN2 = wx.BoxSizer( wx.VERTICAL )

		bSizerPanel1 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_textCtrl6 = wx.TextCtrl( self.m_panelMain, wx.ID_ANY, u"TEMP", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerPanel1.Add( self.m_textCtrl6, 0, wx.ALL, 5 )

		self.m_textCtrl5 = wx.TextCtrl( self.m_panelMain, wx.ID_ANY, u"TEMP", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerPanel1.Add( self.m_textCtrl5, 0, wx.ALL, 5 )

		self.m_button2 = wx.Button( self.m_panelMain, wx.ID_ANY, u"TEMP", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerPanel1.Add( self.m_button2, 0, wx.ALL, 5 )


		bSizerPanelN2.Add( bSizerPanel1, 0, wx.ALL, 0 )

		bSizerPanel2 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_textCtrlSongName = wx.TextCtrl( self.m_panelMain, wx.ID_ANY, u"Enter Song Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerPanel2.Add( self.m_textCtrlSongName, 0, wx.ALL, 5 )

		self.m_textCtrlArtistName = wx.TextCtrl( self.m_panelMain, wx.ID_ANY, u"Enter Artist Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerPanel2.Add( self.m_textCtrlArtistName, 0, wx.ALL, 5 )

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
		bSizerPanelN1.Fit( self.m_panelMain )
		bSizerMainFrame.Add( self.m_panelMain, 1, wx.EXPAND |wx.ALL, 0 )


		bSizerMainFrameN.Add( bSizerMainFrame, 1, wx.ALL|wx.EXPAND, 0 )


		self.SetSizer( bSizerMainFrameN )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.buttonGetLyrics.Bind( wx.EVT_BUTTON, self.buttonGetLyricsOnButtonClick )
		self.buttonGetCoverArt.Bind( wx.EVT_BUTTON, self.buttonGetCoverArtOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def buttonGetLyricsOnButtonClick( self, event ):
            
		pesma = self.m_textCtrlSongName.GetValue()
		umetnik = self.m_textCtrlArtistName.GetValue()
		print(pesma)
		print(umetnik)
		tekst = genius.search_song(pesma, umetnik)
		self.m_richTextLyrics.AppendText(tekst.title + " - " + tekst.artist + "\n")
		self.m_richTextLyrics.AppendText("\n" + tekst.lyrics)
		#event.Skip()

	def buttonGetCoverArtOnButtonClick( self, event ):
		sp = spotipy.Spotify(auth = token) #Spotify objekat

		# Uzimanje potrebih objekata/podataka
		# user = sp.current_user() #Korisnik
		# uredjaji = sp.devices() #Uredjaji
		# uredjajiID = [uredjaji['devices'][0]['id']]
		#print(json.dumps(uredjaji, sort_keys = True, indent = 4))
		# pesmaInfo = sp.current_user_playing_track() #Pesma
		#print(json.dumps(pesmaInfo, sort_keys = True, indent = 4))

		# ERRORpostoji = False

		# try:                                  
		# 	pesma = pesmaInfo['item']['name'] #Koristim try/except zato sto se posle nekog vremena Spotify diskonektuje i to pravi error sa API-em zato upozoravam korisnika
		# except:                               # da osvezi Spotify
		# 	ERRORpostoji = True

		# if ERRORpostoji == False:
		# 	for i in pesma: #Kada pesma ima '-' to cesto zbuni Geniusev API a i Python zato kada ima '-' u imenu pesme samo obrsem sve nakon '-'
		# 		if i == "-":
		# 			pesma = pesma[:pesma.find("-")-1]
		# 			ERRORpostoji = False
		# 			break
            
		pesma = self.m_textCtrlSongName.GetValue()
		umetnik = self.m_textCtrlArtistName.GetValue()

		pesmaInfo = sp.search(pesma, limit=1, offset=0, type='track', market=None)
		print(json.dumps(pesmaInfo, sort_keys = True, indent = 4))

		ime = pesmaInfo['tracks']['items'][0]['name']
		url = pesmaInfo['tracks']['items'][0]['album']['images'][0]['url']
		print(url)

		print(pesma)
		print(umetnik)

		root = Tk()
		root.withdraw()
		root.attributes("-topmost", True)

		putanja = filedialog.askdirectory()
		putanjaCela = os.path.abspath(putanja + "/" + ime + '.jpg')  #os.path.abspath daje celu putanju automatski i resava vecinu errora vezani za putanju
		print(putanjaCela)
		urllib.request.urlretrieve(url, putanjaCela)

		img = wx.Image(putanjaCela, type=wx.BITMAP_TYPE_ANY , index=-1)
		print(type(img))

		self.m_richTextLyrics.AddImage(img)
		self.m_richTextLyrics.AppendText("") #Ovo dodajem da bi se richText azurirao, ako se ne azurira ne prikazuje se slika

		#event.Skip()

class MainApp(wx.App):
	def OnInit(self):
		mainFrame = frameMain(None)
		mainFrame.Show(True)
		return True

if __name__ == '__main__':
	app = MainApp()
	app.MainLoop()
