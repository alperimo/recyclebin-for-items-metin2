import gameInfo
import event
import net

	onPressKeyDict[app.DIK_K]	= lambda : self.__PressToGeriDonusum()

	def __ServerCommand_Build(self):
		serverCommandList={
			## New System Plugin ##
			"PythonToLua"			: self.__PythonToLua, # .python to Quest
			"PythonIslem"			: self.__PythonIslem, # .python to Quest
			"LuaToPython"			: self.__LuaToPython, # Quest to .python
			## END - New System Plugin - END ##
		}

	def OpenQuestWindow(self, skin, idx):
		if gameInfo.INPUT == 1:
			return
		self.interface.OpenQuestWindow(skin, idx)


	def __PythonToLua(self, id):
		gameInfo.PYTHONTOLUA = int(id)

	def __PythonIslem(self, PythonIslem):
		if PythonIslem == "PYTHONISLEM":
			net.SendQuestInputStringPacket(gameInfo.PYTHONISLEM)

	def __LuaToPython(self, LuaToPython):
		if LuaToPython.find("#quest_input#") != -1:
			gameInfo.INPUT = 1
		elif LuaToPython.find("#quest_inputbitir#") != -1:
			gameInfo.INPUT = 0

		elif LuaToPython.find("geridonusum_itemler") != -1:
			bol = LuaToPython.split("|")
			if not "slot"+str(gameInfo.GERIDONUSUM_ITEM_SIRA+1) in gameInfo.GERIDONUSUM_ITEMLER.keys():
				gameInfo.GERIDONUSUM_ITEMLER["slot"+str(gameInfo.GERIDONUSUM_ITEM_SIRA+1)]=bol[1]	
				gameInfo.GERIDONUSUM_ITEM_YENILE=1		
				gameInfo.GERIDONUSUM_ITEM_SIRA+=1
		elif LuaToPython.find("geridonusum_gerial") != -1:
			gameInfo.GERIDONUSUM_ITEM_AL=1
			
	def __PressToGeriDonusum(self):
		import uiinventory
		self.geriDonusum=uiinventory.GeriDonusumWindow()
		if gameInfo.GERIDONUSUM_ITEM_ACIK==0:
			self.geriDonusum.Show()
		else:
			gameInfo.GERIDONUSUM_ITEM_YENILE=2