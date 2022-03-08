import uiScriptLocale
import gameInfo

ROOT = "d:/ymir work/ui/game/"
FACE_SLOT_FILE = "d:/ymir work/ui/game/windows/box_face.sub"
#PATH=str(gameInfo.CONFIG_YOL)+"geridonusum/"

WIDTH = 562
HEIGHT = 211-41

X=16
Y=35
X_EK=38

THIN_X=14+9000
THIN_Y=33
THIN_X_EK=43
THIN_WIDTH=36
THIN_HEIGHT=100

window = {
	"name" : "GeriDonusumDialog",

	"x" : SCREEN_WIDTH - 176 - 269,
	"y" : SCREEN_HEIGHT - 37 - 565 + 36,

	"style" : ("movable", "float",),

	"width" : WIDTH,
	"height" : HEIGHT,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"width" : WIDTH,
			"height" : HEIGHT,

			"children" :
			(
				## Title
				{
					"name" : "TitleBar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 8,
					"y" : 8,
 
					"width" : WIDTH - 15,
					"color" : "gray",

					"children" :
					(
						{ "name":"TitleName", "type":"text", "x":WIDTH / 2 - 9, "y":3, "text":"Geri Dönüþüm Kutusu", "text_horizontal_align":"center" },
					),
				},
				
				{"name": "ItemThin1","type":"thinboard","x":THIN_X,"y":THIN_Y,"width":THIN_WIDTH,"height":THIN_HEIGHT},
				{"name": "ItemThin2","type":"thinboard","x":THIN_X+THIN_X_EK,"y":THIN_Y,"width":THIN_WIDTH,"height":THIN_HEIGHT},
				{"name": "ItemThin3","type":"thinboard","x":THIN_X+THIN_X_EK*2,"y":THIN_Y,"width":THIN_WIDTH,"height":THIN_HEIGHT},
				{"name": "ItemThin4","type":"thinboard","x":THIN_X+THIN_X_EK*3,"y":THIN_Y,"width":THIN_WIDTH,"height":THIN_HEIGHT},
				{"name": "ItemThin5","type":"thinboard","x":THIN_X+THIN_X_EK*4,"y":THIN_Y,"width":THIN_WIDTH,"height":THIN_HEIGHT},
				{"name": "ItemThin6","type":"thinboard","x":THIN_X+THIN_X_EK*5,"y":THIN_Y,"width":THIN_WIDTH,"height":THIN_HEIGHT},
				{"name": "ItemThin7","type":"thinboard","x":THIN_X+THIN_X_EK*6,"y":THIN_Y,"width":THIN_WIDTH,"height":THIN_HEIGHT},
				{"name": "ItemThin8","type":"thinboard","x":THIN_X+THIN_X_EK*7,"y":THIN_Y,"width":THIN_WIDTH,"height":THIN_HEIGHT},
				{"name": "ItemThin9","type":"thinboard","x":THIN_X+THIN_X_EK*8,"y":THIN_Y,"width":THIN_WIDTH,"height":THIN_HEIGHT},
				{"name": "ItemThin10","type":"thinboard","x":THIN_X+THIN_X_EK*9,"y":THIN_Y,"width":THIN_WIDTH,"height":THIN_HEIGHT},
				{"name": "ItemThin11","type":"thinboard","x":THIN_X+THIN_X_EK*10,"y":THIN_Y,"width":THIN_WIDTH,"height":THIN_HEIGHT},
				{"name": "ItemThin12","type":"thinboard","x":THIN_X+THIN_X_EK*11,"y":THIN_Y,"width":THIN_WIDTH,"height":THIN_HEIGHT},
				{"name": "ItemThin13","type":"thinboard","x":THIN_X+THIN_X_EK*12,"y":THIN_Y,"width":THIN_WIDTH,"height":THIN_HEIGHT},
				{"name": "ItemThin14","type":"thinboard","x":THIN_X+THIN_X_EK*13,"y":THIN_Y,"width":THIN_WIDTH,"height":THIN_HEIGHT},
				
				{"name" : "ItemSlot1","type" : "grid_table","x" : X,"y" : Y,"start_index" : 0,"x_count" : 1,"y_count" : 3,"x_step" : 32,"y_step" : 32,"image" : "d:/ymir work/ui/public/Slot_Base.sub"},
				{"name" : "ItemSlot2","type" : "grid_table","x" : X+X_EK,"y" : Y,"start_index" : 0,"x_count" : 1,"y_count" : 3,"x_step" : 32,"y_step" : 32,"image" : "d:/ymir work/ui/public/Slot_Base.sub"},
				{"name" : "ItemSlot3","type" : "grid_table","x" : X+X_EK*2,"y" : Y,"start_index" : 0,"x_count" : 1,"y_count" : 3,"x_step" : 32,"y_step" : 32,"image" : "d:/ymir work/ui/public/Slot_Base.sub"},
				{"name" : "ItemSlot4","type" : "grid_table","x" : X+X_EK*3,"y" : Y,"start_index" : 0,"x_count" : 1,"y_count" : 3,"x_step" : 32,"y_step" : 32,"image" : "d:/ymir work/ui/public/Slot_Base.sub"},
				{"name" : "ItemSlot5","type" : "grid_table","x" : X+X_EK*4,"y" : Y,"start_index" : 0,"x_count" : 1,"y_count" : 3,"x_step" : 32,"y_step" : 32,"image" : "d:/ymir work/ui/public/Slot_Base.sub"},
				{"name" : "ItemSlot6","type" : "grid_table","x" : X+X_EK*5,"y" : Y,"start_index" : 0,"x_count" : 1,"y_count" : 3,"x_step" : 32,"y_step" : 32,"image" : "d:/ymir work/ui/public/Slot_Base.sub"},
				{"name" : "ItemSlot7","type" : "grid_table","x" : X+X_EK*6,"y" : Y,"start_index" : 0,"x_count" : 1,"y_count" : 3,"x_step" : 32,"y_step" : 32,"image" : "d:/ymir work/ui/public/Slot_Base.sub"},
				{"name" : "ItemSlot8","type" : "grid_table","x" : X+X_EK*7,"y" : Y,"start_index" : 0,"x_count" : 1,"y_count" : 3,"x_step" : 32,"y_step" : 32,"image" : "d:/ymir work/ui/public/Slot_Base.sub"},
				{"name" : "ItemSlot9","type" : "grid_table","x" : X+X_EK*8,"y" : Y,"start_index" : 0,"x_count" : 1,"y_count" : 3,"x_step" : 32,"y_step" : 32,"image" : "d:/ymir work/ui/public/Slot_Base.sub"},
				{"name" : "ItemSlot10","type" : "grid_table","x" : X+X_EK*9,"y" : Y,"start_index" : 0,"x_count" : 1,"y_count" : 3,"x_step" : 32,"y_step" : 32,"image" : "d:/ymir work/ui/public/Slot_Base.sub"},
				{"name" : "ItemSlot11","type" : "grid_table","x" : X+X_EK*10,"y" : Y,"start_index" : 0,"x_count" : 1,"y_count" : 3,"x_step" : 32,"y_step" : 32,"image" : "d:/ymir work/ui/public/Slot_Base.sub"},
				{"name" : "ItemSlot12","type" : "grid_table","x" : X+X_EK*11,"y" : Y,"start_index" : 0,"x_count" : 1,"y_count" : 3,"x_step" : 32,"y_step" : 32,"image" : "d:/ymir work/ui/public/Slot_Base.sub"},
				{"name" : "ItemSlot13","type" : "grid_table","x" : X+X_EK*12,"y" : Y,"start_index" : 0,"x_count" : 1,"y_count" : 3,"x_step" : 32,"y_step" : 32,"image" : "d:/ymir work/ui/public/Slot_Base.sub"},
				{"name" : "ItemSlot14","type" : "grid_table","x" : X+X_EK*13,"y" : Y,"start_index" : 0,"x_count" : 1,"y_count" : 3,"x_step" : 32,"y_step" : 32,"image" : "d:/ymir work/ui/public/Slot_Base.sub"},
					

				#{"name":"geriButton","type":"button", "x":11,"y":HEIGHT/2, "text": "<<<", "default_image":"d:/ymir work/ui/public/middle_button_01.sub","over_image":"d:/ymir work/ui/public/middle_button_02.sub","down_image":"d:/ymir work/ui/public/middle_button_03.sub"},
				#{"name":"ileriButton","type":"button", "x":WIDTH - 69,"y":HEIGHT/2, "text": ">>>", "default_image":"d:/ymir work/ui/public/middle_button_01.sub","over_image":"d:/ymir work/ui/public/middle_button_02.sub","down_image":"d:/ymir work/ui/public/middle_button_03.sub"},
				#{"name" : "sayfaSlot","type" : "image","x" : 0,"y" : HEIGHT - 51 + 19,"image" : "d:/ymir work/ui/public/Parameter_Slot_02.sub","horizontal_align":"center","children" :
				#	(
				#		{"name" : "sayfaSlotValue","type" : "text","x" : 30,"y" : 3,"text" : "I","text_horizontal_align":"center"},
				#	),
				#},
				
				{"name":"ileriButton","type":"button", "x":WIDTH - 79,"y":HEIGHT - 53 + 19, "text": ">>>", "default_image":"d:/ymir work/ui/public/middle_button_01.sub","over_image":"d:/ymir work/ui/public/middle_button_02.sub","down_image":"d:/ymir work/ui/public/middle_button_03.sub"},
				{"name":"geriButton","type":"button", "x":WIDTH - 65 - 138,"y":HEIGHT - 53 + 19, "text": "<<<", "default_image":"d:/ymir work/ui/public/middle_button_01.sub","over_image":"d:/ymir work/ui/public/middle_button_02.sub","down_image":"d:/ymir work/ui/public/middle_button_03.sub"},
				{"name" : "sayfaSlot","type" : "image","x" : WIDTH - 142,"y" : HEIGHT - 54 + 19,"image" : "d:/ymir work/ui/public/Parameter_Slot_02.sub","children" :
					(
						{"name" : "sayfaSlotValue","type" : "text","x" : 30,"y" : 3,"text" : "I","text_horizontal_align":"center"},
					),
				},
				
				#{"name":"oxoARKA","type":"image","image":PATH+"arka.tga","x":38,"y":67},
				#{"name":"oxoPESETbutton","type":"button", "x":445,"y":44, "text": "Pes Et", "default_image":"d:/ymir work/ui/public/middle_button_01.sub","over_image":"d:/ymir work/ui/public/middle_button_02.sub","down_image":"d:/ymir work/ui/public/middle_button_03.sub"},
				#{"name":"oxoBENtext", "type": "text", "x":139,"y":44, "text" : "Ben : X"},
				#{"name":"oxoRAKIPtext", "type": "text", "x":328,"y":44, "text" : "Rakip : O"},
				#{"name":"oxoBENIMSUREtext", "type": "text", "x":328,"y":44 + 9000, "text" : "Rakip : O"},
				#{"name":"oxoRAKIPSUREtext", "type": "text", "x":328,"y":44 + 9000, "text" : "Rakip : O"},
				
				#{"name":"oxoOYNA1","type":"button", "x":93,"y":137, "text": "OYNA", "default_image":"d:/ymir work/ui/public/small_button_01.sub","over_image":"d:/ymir work/ui/public/small_button_02.sub","down_image":"d:/ymir work/ui/public/small_button_03.sub"},
				
			),
		},
	),
}