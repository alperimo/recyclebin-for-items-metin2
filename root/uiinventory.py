import gameInfo
import uiToolTip

class GeriDonusumWindow(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.sayfaTEXT=0
		self.slotSIRA=1
		self.timeOPEN=0
		self.time=0
		toolTip = uiToolTip.ItemToolTip()
		self.toolTip = toolTip

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Show(self):
		self.panelTEMIZLE()
		self.time=app.GetTime()+0.10000
		self.timeREFRESH=0
		self.timeOPEN=1
		self.sayfaTEXT=1
		self.slotSIRA=1
		gameInfo.GERIDONUSUM_ITEM_ACIK=1
		self.__LoadWindow()
		self.SetCenterPosition()
		ui.ScriptWindow.Show(self)
		
	def panelTEMIZLE(self):
		gameInfo.GERIDONUSUM_ITEMLER={}
		gameInfo.GERIDONUSUM_ITEM_AL=0
		gameInfo.GERIDONUSUM_ITEM_SIRA=0
		gameInfo.GERIDONUSUM_ITEM_YENILE=0
		self.sayfaTEXT=1
		self.timeREFRESH=0

	def Close(self):
		snd.PlaySound("sound/ui/click.wav")
		self.panelTEMIZLE()
		gameInfo.GERIDONUSUM_ITEM_ACIK=0
		self.Hide()

	def __LoadWindow(self):
		try:			
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uiscript/geridonusumdialog.py")
			
			self.ileriButton = self.GetChild("ileriButton")
			self.geriButton = self.GetChild("geriButton")
			
			self.itemSlot={
				"slot1":self.GetChild("ItemSlot1"),"slot2":self.GetChild("ItemSlot2"),"slot3":self.GetChild("ItemSlot3"),"slot4":self.GetChild("ItemSlot4"),"slot5":self.GetChild("ItemSlot5"),
				"slot6":self.GetChild("ItemSlot6"),"slot7":self.GetChild("ItemSlot7"),"slot8":self.GetChild("ItemSlot8"),"slot9":self.GetChild("ItemSlot9"),"slot10":self.GetChild("ItemSlot10"),
				"slot11":self.GetChild("ItemSlot11"),"slot12":self.GetChild("ItemSlot12"),"slot13":self.GetChild("ItemSlot13"),"slot14":self.GetChild("ItemSlot14"),
			}
			
			self.itemSlotOverInEvents={
				"slot1":self.OverInItem1,"slot2":self.OverInItem2,"slot3":self.OverInItem3,"slot4":self.OverInItem4,"slot5":self.OverInItem5,"slot6":self.OverInItem6,
				"slot7":self.OverInItem7,"slot8":self.OverInItem8,"slot9":self.OverInItem9,"slot10":self.OverInItem10,"slot11":self.OverInItem11,"slot12":self.OverInItem12,
				"slot13":self.OverInItem13,"slot14":self.OverInItem14,
			}
			
			self.itemSlotButtonEvents={
				"slot1":self.geriAL1,"slot2":self.geriAL2,"slot3":self.geriAL3,"slot4":self.geriAL4,"slot5":self.geriAL5,"slot6":self.geriAL6,
				"slot7":self.geriAL7,"slot8":self.geriAL8,"slot9":self.geriAL9,"slot10":self.geriAL10,"slot11":self.geriAL11,"slot12":self.geriAL12,
				"slot13":self.geriAL13,"slot14":self.geriAL14,
			}
			
		except:
			import exception
			exception.Abort("GeriDonusumDialog.LoadWindow.LoadObject")
			
		for i in xrange(1,15):
			self.itemSlot["slot"+str(i)].SetOverOutItemEvent(ui.__mem_func__(self.OverOutItem))
			self.itemSlot["slot"+str(i)].SetUnselectItemSlotEvent(ui.__mem_func__(self.itemSlotButtonEvents["slot"+str(i)]))
			self.itemSlot["slot"+str(i)].SetOverInItemEvent(ui.__mem_func__(self.itemSlotOverInEvents["slot"+str(i)]))
		
		self.GetChild("TitleBar").SetCloseEvent(ui.__mem_func__(self.Close))
		self.ileriButton.SetEvent(ui.__mem_func__(self.sayfaDegistir),1,"+")
		self.geriButton.SetEvent(ui.__mem_func__(self.sayfaDegistir),1,"-")
		
	def slotTEMIZLE(self):
		for i in xrange(1,15):
			self.itemSlot["slot"+str(i)].ClearSlot(0)
		
	def sayfaDegistir(self,value,gelen):
		itemSLOT=1
		self.slotSIRA=1
		
		self.slotTEMIZLE()
		
		if gelen=="+":
			sayfaYENI=self.sayfaTEXT+1		
			
			for i in xrange(self.sayfaTEXT*14+1,sayfaYENI*14+1):
				if "slot"+str(i) in gameInfo.GERIDONUSUM_ITEMLER.keys():
					self.itemEKLE(i,"yenile")
				itemSLOT+=1
					
			self.sayfaTEXT+=1
			
			self.geriButton.SetUp()
			self.geriButton.Enable()
		else:
			sayfaESKI=self.sayfaTEXT-2
			sayfaYENI=self.sayfaTEXT-1
			
			for i in xrange(sayfaESKI*14+1,sayfaYENI*14+1):
				if "slot"+str(i) in gameInfo.GERIDONUSUM_ITEMLER.keys():
					self.itemEKLE(i,"yenile")
				itemSLOT+=1
					
			self.sayfaTEXT-=1
			
		self.timeREFRESH=0
		
	def itemEKLE(self, gelen, durum=""):
		if durum=="yenile":
			self.itemSlot["slot"+str(self.slotSIRA)].ClearSlot(0)
			if int(gameInfo.GERIDONUSUM_ITEMLER["slot"+str(gelen)].split("#")[2]) == 1:
				self.itemSlot["slot"+str(self.slotSIRA)].SetItemSlot(0,int(gameInfo.GERIDONUSUM_ITEMLER["slot"+str(gelen)].split("#")[1]), 0)
			else:
				self.itemSlot["slot"+str(self.slotSIRA)].SetItemSlot(0,int(gameInfo.GERIDONUSUM_ITEMLER["slot"+str(gelen)].split("#")[1]), int(gameInfo.GERIDONUSUM_ITEMLER["slot"+str(gelen)].split("#")[2]))
			self.itemSlot["slot"+str(self.slotSIRA)].RefreshSlot()
			self.slotSIRA+=1
			return
		
		self.itemSlot["slot"+str(gelen)].ClearSlot(0)
		if int(gameInfo.GERIDONUSUM_ITEMLER["slot"+str(gelen)].split("#")[2]) == 1:
			self.itemSlot["slot"+str(gelen)].SetItemSlot(0,int(gameInfo.GERIDONUSUM_ITEMLER["slot"+str(gelen)].split("#")[1]), 0)
		else:
			self.itemSlot["slot"+str(gelen)].SetItemSlot(0,int(gameInfo.GERIDONUSUM_ITEMLER["slot"+str(gelen)].split("#")[1]), int(gameInfo.GERIDONUSUM_ITEMLER["slot"+str(gelen)].split("#")[2]))
		self.itemSlot["slot"+str(gelen)].RefreshSlot()
		
	def geriAL(self, slotNumber, gelen):
		sayfaYENI=self.sayfaTEXT-1
		gelen = sayfaYENI*14+gelen
		itemVnum=int(gameInfo.GERIDONUSUM_ITEMLER["slot"+str(gelen)].split("#")[1])
		itemNumber=int(gameInfo.GERIDONUSUM_ITEMLER["slot"+str(gelen)].split("#")[26])
		item.SelectItem(itemVnum)
		
		questionText = str(item.GetItemName()) + " adlý eþyayý geri almak istiyor musun? 3.000.000 Yang"
		itemDropQuestionDialog = uiCommon.QuestionDialog()
		itemDropQuestionDialog.SetText(questionText)
		itemDropQuestionDialog.SetAcceptEvent(lambda arg=TRUE: self.geriALbutton(arg,itemNumber))
		itemDropQuestionDialog.SetCancelEvent(lambda arg=FALSE: self.geriALbutton(arg,itemNumber))
		itemDropQuestionDialog.Open()
		self.itemDropQuestionDialog = itemDropQuestionDialog	
			
	def geriALbutton(self, answer, slotNumber):
		if answer:
			if player.GetElk() < 3000000:
				self.popupDialog=uiCommon.PopupDialog()
				self.popupDialog.SetText(locale.SHOP_NOT_ENOUGH_MONEY)
				self.popupDialog.Open()
			else:
				gameInfo.PYTHONISLEM="geridonusum_gerial#"+str(slotNumber)
				event.QuestButtonClick(gameInfo.PYTHONTOLUA)
		
		self.itemDropQuestionDialog.Close()
		self.itemDropQuestionDialog = None
		
	def OverInItem(self, slotNumber, gelen):
		sayfaYENI=self.sayfaTEXT-1
		gelen = sayfaYENI*14+gelen
		self.toolTip.ClearToolTip()
		self.toolTip.Show()
		if "slot"+str(gelen) in gameInfo.GERIDONUSUM_ITEMLER.keys():
			slotIndex = gameInfo.GERIDONUSUM_ITEMLER["slot"+str(gelen)].split("#")
	
			itemVnum = player.GetItemIndex(int(slotIndex[1]))
			itemCount = player.GetItemCount(int(slotIndex[2]))

			items = gameInfo.GERIDONUSUM_ITEMLER["slot"+str(gelen)].split("#")

			metinAttr = [int(items[4]),int(items[5]),int(items[6]),int(items[7]),int(items[8]),int(items[9])]
			slotAttr =  [(int(items[10]),int(items[11])),(int(items[12]),int(items[13])),(int(items[14]),int(items[15])),(int(items[16]),int(items[17])),(int(items[18]),int(items[19])),(int(items[20]),int(items[21])),(int(items[22]),int(items[23]))]
	
			self.toolTip.AddRefineItemData(int(slotIndex[1]), metinAttr, slotAttr)
			
	def geriAL1(self): self.geriAL(0,1)
	def geriAL2(self): self.geriAL(0,2)	
	def geriAL3(self): self.geriAL(0,3)	
	def geriAL4(self): self.geriAL(0,4)
	def geriAL5(self): self.geriAL(0,5)
	def geriAL6(self): self.geriAL(0,6)
	def geriAL7(self): self.geriAL(0,7)
	def geriAL8(self): self.geriAL(0,8)
	def geriAL9(self): self.geriAL(0,9)
	def geriAL10(self): self.geriAL(0,10)
	def geriAL11(self): self.geriAL(0,11)
	def geriAL12(self): self.geriAL(0,12)
	def geriAL13(self): self.geriAL(0,13)
	def geriAL14(self): self.geriAL(0,14)	
	def OverInItem1(self): self.OverInItem(0,1)
	def OverInItem2(self): self.OverInItem(0,2)	
	def OverInItem3(self): self.OverInItem(0,3)	
	def OverInItem4(self): self.OverInItem(0,4)
	def OverInItem5(self): self.OverInItem(0,5)
	def OverInItem6(self): self.OverInItem(0,6)
	def OverInItem7(self): self.OverInItem(0,7)
	def OverInItem8(self): self.OverInItem(0,8)
	def OverInItem9(self): self.OverInItem(0,9)
	def OverInItem10(self): self.OverInItem(0,10)
	def OverInItem11(self): self.OverInItem(0,11)
	def OverInItem12(self): self.OverInItem(0,12)
	def OverInItem13(self): self.OverInItem(0,13)
	def OverInItem14(self): self.OverInItem(0,14)
	def OverOutItem(self): self.toolTip.Hide()
	
	def OnPressEscapeKey(self): 
		self.Close()
		return TRUE
		
	def OnUpdate(self):
		if self.timeOPEN==1:
			if self.time < app.GetTime():
				gameInfo.PYTHONISLEM="geridonusum_itemlerial"
				event.QuestButtonClick(gameInfo.PYTHONTOLUA)
				self.timeOPEN=0
				
		if gameInfo.GERIDONUSUM_ITEM_AL==1:
			self.panelTEMIZLE()
			self.slotTEMIZLE()
			gameInfo.PYTHONISLEM="geridonusum_itemlerial"
			event.QuestButtonClick(gameInfo.PYTHONTOLUA)
			gameInfo.GERIDONUSUM_ITEM_AL=0
				
		if gameInfo.GERIDONUSUM_ITEM_YENILE==1:
			for i in xrange(1,15):
				if "slot"+str(i) in gameInfo.GERIDONUSUM_ITEMLER.keys():
					self.itemEKLE(i)
			gameInfo.GERIDONUSUM_ITEM_YENILE=0
			
		if gameInfo.GERIDONUSUM_ITEM_YENILE==2:
			self.Close()
			gameInfo.GERIDONUSUM_ITEM_YENILE=0
			
		self.GetChild("sayfaSlotValue").SetText(str(self.sayfaTEXT))
		
		if "slot"+str(self.sayfaTEXT*14+1) in gameInfo.GERIDONUSUM_ITEMLER.keys():
			if self.timeREFRESH==0:
				self.ileriButton.SetUp()
				self.ileriButton.Enable()
				self.timeREFRESH=1
		else:
			self.ileriButton.Down()
			self.ileriButton.Disable()
			
		if self.sayfaTEXT==1:
			self.geriButton.Down()
			self.geriButton.Disable()
			
			
class InventoryWindow
	...
	
			self.GetChild("topluSILbutton").SetEvent(ui.__mem_func__(self.SilEmptySlotTOPLU))
			self.topluSILKONTROL()
			
	#fonksiyonaEKLE#
	def RefreshBagSlotWindow(self):
		if gameInfo.TOPLU_SIL_DURUM==1:
			for refresh in xrange(player.INVENTORY_PAGE_SIZE):
				slotNumber = self.__InventoryLocalSlotPosToGlobalSlotPos(refresh)
				if int(slotNumber) in gameInfo.TOPLU_SIL_LIST:
					itemVnum=getItemVNum(slotNumber)
					item.SelectItem(int(itemVnum))
					(itemWidth, itemHeight) = item.GetItemSize()
					self.wndItem.SetCoverButton(refresh, str(gameInfo.CONFIG_YOL)+"satilamaz_"+str(itemHeight)+".tga", str(gameInfo.CONFIG_YOL)+"satilamaz_"+str(itemHeight)+".tga", str(gameInfo.CONFIG_YOL)+"satilamaz_"+str(itemHeight)+".tga", "d:/ymir work/ui/public/slot_cover_button_04.sub", 1, 0)
					self.wndItem.EnableSlot(refresh)
				else:
					self.wndItem.SetCoverButton(refresh,"d:/ymir work/ui/game/quest/slot_button_01.sub","d:/ymir work/ui/game/quest/slot_button_01.sub","d:/ymir work/ui/game/quest/slot_button_01.sub",str(gameInfo.CONFIG_YOL)+"slot_disabled.tga", FALSE, FALSE)
					self.wndItem.EnableSlot(refresh)		
		else:
			for refresh in xrange(player.INVENTORY_PAGE_SIZE):
				slotNumber = self.__InventoryLocalSlotPosToGlobalSlotPos(refresh)
				self.wndItem.SetCoverButton(refresh,"d:/ymir work/ui/game/quest/slot_button_01.sub","d:/ymir work/ui/game/quest/slot_button_01.sub","d:/ymir work/ui/game/quest/slot_button_01.sub",str(gameInfo.CONFIG_YOL)+"slot_disabled.tga", FALSE, FALSE)
				self.wndItem.EnableSlot(refresh)
	
	def UseItemSlot(self, slotIndex):
		if gameInfo.TOPLU_SIL_DURUM==1 and gameInfo.TOPLU_SIL_CAN==0:
			
			mouseModule.mouseController.DeattachObject()
			self.OverOutItem()
			
			gameInfo.TOPLU_SIL_TIME=app.GetTime()+0.10
			gameInfo.TOPLU_SIL_CAN=1
			
			slotIndex2 = self.__InventoryLocalSlotPosToGlobalSlotPos(slotIndex)
		
			if player.IsEquipmentSlot(slotIndex2):
				chat.AppendChat(chat.CHAT_TYPE_INFO,"<System>: Giyilen itemi silemezsin.")
				return
				
			if len(gameInfo.TOPLU_SIL_LIST) >= 15:
				chat.AppendChat(chat.CHAT_TYPE_INFO,"<System>: Tek seferde en fazla 15 item silebilirsin.")
				return
				
			if int(slotIndex2) in gameInfo.TOPLU_SIL_LIST:
				self.wndItem.SetCoverButton(slotIndex,"d:/ymir work/ui/game/quest/slot_button_01.sub","d:/ymir work/ui/game/quest/slot_button_01.sub","d:/ymir work/ui/game/quest/slot_button_01.sub",str(gameInfo.CONFIG_YOL)+"slot_disabled.tga", FALSE, FALSE)
				#self.wndItem.EnableSlot(slotIndex)
				gameInfo.TOPLU_SIL_LIST.remove(int(slotIndex2))
				return
				
			gameInfo.TOPLU_SIL_LIST.append(int(slotIndex2))
				
			itemVnum=player.GetItemIndex(slotIndex2)
			item.SelectItem(int(itemVnum))
			(itemWidth, itemHeight) = item.GetItemSize()
			self.wndItem.SetCoverButton(slotIndex, str(gameInfo.CONFIG_YOL)+"satilamaz_"+str(itemHeight)+".tga", str(gameInfo.CONFIG_YOL)+"satilamaz_"+str(itemHeight)+".tga", str(gameInfo.CONFIG_YOL)+"satilamaz_"+str(itemHeight)+".tga", "d:/ymir work/ui/public/slot_cover_button_04.sub", 1, 0)
			#self.wndItem.EnableSlot(slotIndex)
			
			self.RefreshItemSlot()
			return
		
		if gameInfo.TOPLU_SIL_DURUM==1:
			return
	
	def OnUpdate(self):
		if gameInfo.TOPLU_SIL_CAN==1:
			if gameInfo.TOPLU_SIL_TIME < app.GetTime():
				gameInfo.TOPLU_SIL_CAN=0
	
	#yeniOLARAK#
	def topluSILKONTROL(self):
		if gameInfo.TOPLU_SIL_DURUM==1:
			self.GetChild("topluSILbutton").SetUpVisual(str(gameInfo.CONFIG_YOL)+"toplusil_onay.tga")
			self.GetChild("topluSILbutton").SetOverVisual(str(gameInfo.CONFIG_YOL)+"toplusil_onay2.tga")
			self.GetChild("topluSILbutton").SetDownVisual(str(gameInfo.CONFIG_YOL)+"toplusil_onay2.tga")
		else:
			self.GetChild("topluSILbutton").SetUpVisual(str(gameInfo.CONFIG_YOL)+"toplusil.tga")
			self.GetChild("topluSILbutton").SetOverVisual(str(gameInfo.CONFIG_YOL)+"toplusil2.tga")
			self.GetChild("topluSILbutton").SetDownVisual(str(gameInfo.CONFIG_YOL)+"toplusil2.tga")
		
	def SilEmptySlotTOPLU(self):
		if gameInfo.TOPLU_SIL_DURUM==0:
			chat.AppendChat(chat.CHAT_TYPE_INFO,"<System>: Silmek istediðiniz eþyaya sað týklayýn.")
			gameInfo.TOPLU_SIL_DURUM=1
			gameInfo.TOPLU_SIL_LIST=[]
			gameInfo.TOPLU_SIL_CAN=0
			self.topluSILKONTROL()
		else:
			if len(gameInfo.TOPLU_SIL_LIST)==0:
				chat.AppendChat(chat.CHAT_TYPE_INFO,"<System>: Silmek için bir item seçmedin.")
				gameInfo.TOPLU_SIL_LIST=[]
				gameInfo.TOPLU_SIL_DURUM=0
				gameInfo.TOPLU_SIL_CAN=0
				self.topluSILKONTROL()
				self.RefreshItemSlot()
				return
			
			questionText = str(len(gameInfo.TOPLU_SIL_LIST)) + " adet eþyayý silmek istiyor musun?"
			itemDropQuestionDialog = uiCommon.QuestionDialog()
			itemDropQuestionDialog.SetText(questionText)
			itemDropQuestionDialog.SetAcceptEvent(lambda arg=TRUE: self.SilItemTOPLU(arg))
			itemDropQuestionDialog.SetCancelEvent(lambda arg=FALSE: self.SilItemTOPLU(arg))
			itemDropQuestionDialog.Open()
			self.itemDropQuestionDialog = itemDropQuestionDialog	
			
	def SilItemTOPLU(self, answer):
		if answer:
			silITEM=""
			for i in xrange(0,len(gameInfo.TOPLU_SIL_LIST)):
				silITEM+="#"+str(gameInfo.TOPLU_SIL_LIST[i])
			
			gameInfo.PYTHONISLEM=str(len(gameInfo.TOPLU_SIL_LIST))+"+sil"+str(silITEM)
			event.QuestButtonClick(gameInfo.PYTHONTOLUA)
			
			gameInfo.TOPLU_SIL_LIST=[]
			gameInfo.TOPLU_SIL_DURUM=0
			gameInfo.TOPLU_SIL_CAN=0
			
		else:
			gameInfo.TOPLU_SIL_LIST=[]
			gameInfo.TOPLU_SIL_DURUM=0
			gameInfo.TOPLU_SIL_CAN=0
		
		self.topluSILKONTROL()
		self.RefreshItemSlot()	
		
		self.itemDropQuestionDialog.Close()
		self.itemDropQuestionDialog = None