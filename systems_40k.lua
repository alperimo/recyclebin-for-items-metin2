--[[

TR: Tüm özel sistemler, fonksiyonlar, methodlar, ve yol...
TRL : All Special Systems, funcs, method and the way to...

Geliþtirici : .. Fatihbab34™ ..
Paketler ; LuaToPython, PythonToLua, PythonIslem
Fonksiyonlar ; "split('#blabla#blabla#', '#'), systems.getinput('PythonIslem'), io funcs(open, remove, write, read, readline, readlines), table forms, pc.getqf(), pc.setqf()"

--]]

quest systems begin
	state start begin
	
		function geridonusum_ekle(yer)
			local ac_kontrol = io.open('/usr/game/share/locale/turkey/quest/systems/geridonusum/'..pc.get_name()..'.cfg', 'r')
			if ac_kontrol then
				local env_yer = yer
				local items = {}
				local pos = 0
				for fx in ac_kontrol:lines() do		
					table.insert(items, fx)
				end
				local ci = io.open('/usr/game/share/locale/turkey/quest/systems/geridonusum/'..pc.get_name()..'.cfg', "w+")
				for i = 1, table.getn(items) do
					if pos == 0 then
						ci:write(yer.."\\n"..items[i].."\\n")
						pos=1
					else
						ci:write(items[i].."\\n")
					end
				end
				ci:flush()
				ci:close()
			end
		end
		
		function geridonusum_gerial(yer)
			local ac_kontrol = io.open('/usr/game/share/locale/turkey/quest/systems/geridonusum/'..pc.get_name()..'.cfg', 'r')
			if ac_kontrol then
				local env_yer = yer
				local items = {}
				for fx in ac_kontrol:lines() do
					local bol = systems.split(fx,"#")
					if tonumber(env_yer) == tonumber(bol[26]) then
						print "birþey yapma.."
					else
						table.insert(items, fx)
					end
				end
				local ci = io.open('/usr/game/share/locale/turkey/quest/systems/geridonusum/'..pc.get_name()..'.cfg', "w+")
				for i = 1, table.getn(items) do
					ci:write(items[i].."\\n")
				end
				ci:flush()
				ci:close()
			end
		end
		
		function zaman()
			pc.setqf("kontrolgeridonusum", get_time()+30)
		end
		
		when login begin
			cmdchat("PythonToLua "..q.getcurrentquestindex())
			if pc.getqf("iteminevskontrol") != 0 then pc.delqf("iteminevskontrol") end
		end
		
		when logout begin if pc.getqf("iteminevskontrol") != 0 then pc.delqf("iteminevskontrol") end end

		when button begin
			local gelen = systems.getinput("PYTHONISLEM")

			if string.find(gelen, "geridonusum_gerial") then
				local ac_kontrol = io.open('/usr/game/share/locale/turkey/quest/systems/geridonusum/'..pc.get_name()..'.cfg', 'r')
				if ac_kontrol then
					if pc.getqf("kontrolgeridonusum") <= get_time() then
						if tonumber(pc.get_money()) < 3000000 then
							syschat("<System>: Bu itemi geri almak için yeterli yangýn yok.")
							return
						end
						
						local env_yer = systems.split(gelen, "#")
						local items = {}
							
						for fx in ac_kontrol:lines() do
							local bol = systems.split(fx,"#")
							if tonumber(env_yer[2]) == tonumber(bol[26]) then
								if not pc.enough_inventory(tonumber(bol[1])) then
									syschat("<System>: Bu itemini geri almak için envanterinde yeterli yer yok.")
									return
								end
								systems.geridonusum_gerial(env_yer[2])
								pc.change_money(-3000000)
								pc.give_item2_select(tonumber(bol[1]),tonumber(bol[2]))
								cmdchat("LuaToPython geridonusum_gerial|#"..fx)
								local attr,socket = {},{}
								for i = 10,23 do table.insert(attr,{bol[i],bol[i+1]}) i = i+1 end
								for i = 4,6 do table.insert(socket,bol[i]) end
								for i = 1, table.getn(attr) do 
									item.set_attribute(i-1, attr[i][1], attr[i][2]) 
								end 
								for i = 1, table.getn(socket) do if tonumber(socket[i]) > 0 then item.set_socket(i-1, socket[i]) end end
							end
							
						end
						systems.zaman()
					end
				end
			end
		
			if string.find(gelen,"geridonusum_itemlerial") then
				local ac_kontrol = io.open('/usr/game/share/locale/turkey/quest/systems/geridonusum/'..pc.get_name()..'.cfg', 'r')
				if ac_kontrol then
					for fx in ac_kontrol:lines() do
						local bol = systems.split(fx,"#")
						cmdchat("LuaToPython geridonusum_itemler|#"..fx)
					end
				end
			end
			
			if string.find(gelen,"+sil#") then
				local bol = systems.split(gelen, "#")
				local bol2 = systems.split(gelen, "+")
				
				for i=1, tonumber(bol2[1]) do
					item.select_cell(bol[i+1])
					
					if tonumber(item.get_cell()) != tonumber(bol[i+1]) then
						syschat("<System>: & silinmesi gereken item bulunamadi.")
						return
					end
					
					local attr = {{item.get_attribute_type(0),item.get_attribute_value(0)}, {item.get_attribute_type(1),item.get_attribute_value(1)}, {item.get_attribute_type(2),item.get_attribute_value(2)}, {item.get_attribute_type(3),item.get_attribute_value(3)},{item.get_attribute_type(4),item.get_attribute_value(4)},{item.get_attribute_type(5),item.get_attribute_value(5)},{item.get_attribute_type(6),item.get_attribute_value(6)}}
					local socket, itemVnum, itemCount = {item.get_socket(0), item.get_socket(1), item.get_socket(2),item.get_socket(3),item.get_socket(4),item.get_socket(5)}, item.get_vnum(), item.get_count()
					local fxd = 0
					local kontrol = 0
					local toplam = 0
					local ac_kontrol = io.open('/usr/game/share/locale/turkey/quest/systems/geridonusum/'..pc.get_name()..'.cfg', 'r')
					if ac_kontrol then
						
						for fx in ac_kontrol:lines() do
							kontrol=1
							
							local bol = systems.split(fx,"#")
							if tonumber(bol[25]) == tonumber(item.get_id()) then
								fxd = 1
							end
							
							if toplam == 0 then
								toplam = tonumber(bol[26])
							end
							
						end
						ac_kontrol:close()
						
						if kontrol==0 then
							local ac_ = io.open('/usr/game/share/locale/turkey/quest/systems/geridonusum/'..pc.get_name()..'.cfg', 'w')
							ac_:write(itemVnum.."#"..itemCount.."#"..(bol[2]).."#"..socket[1].."#"..socket[2].."#"..socket[3].."#"..socket[4].."#"..socket[5].."#"..socket[6].."#"..attr[1][1].."#"..attr[1][2].."#"..attr[2][1].."#"..attr[2][2].."#"..attr[3][1].."#"..attr[3][2].."#"..attr[4][1].."#"..attr[4][2].."#"..attr[5][1].."#"..attr[5][2].."#"..attr[6][1].."#"..attr[6][2].."#"..attr[7][1].."#"..attr[7][2].."#"..pc.get_name().."#"..item.get_id().."#1".."\\n")
							ac_:close()
							fxd=1
						end
						
						if fxd == 0 then
						
							systems.geridonusum_ekle(itemVnum.."#"..itemCount.."#"..(bol[2]).."#"..socket[1].."#"..socket[2].."#"..socket[3].."#"..socket[4].."#"..socket[5].."#"..socket[6].."#"..attr[1][1].."#"..attr[1][2].."#"..attr[2][1].."#"..attr[2][2].."#"..attr[3][1].."#"..attr[3][2].."#"..attr[4][1].."#"..attr[4][2].."#"..attr[5][1].."#"..attr[5][2].."#"..attr[6][1].."#"..attr[6][2].."#"..attr[7][1].."#"..attr[7][2].."#"..pc.get_name().."#"..item.get_id().."#"..(toplam+1))
							--local ac = io.open('/usr/game/share/locale/turkey/quest/systems/geridonusum/'..pc.get_name()..'.cfg', 'a+')
							--ac:write(itemVnum.."#"..itemCount.."#"..(bol[2]).."#"..socket[1].."#"..socket[2].."#"..socket[3].."#"..socket[4].."#"..socket[5].."#"..socket[6].."#"..attr[1][1].."#"..attr[1][2].."#"..attr[2][1].."#"..attr[2][2].."#"..attr[3][1].."#"..attr[3][2].."#"..attr[4][1].."#"..attr[4][2].."#"..attr[5][1].."#"..attr[5][2].."#"..attr[6][1].."#"..attr[6][2].."#"..attr[7][1].."#"..attr[7][2].."#"..pc.get_name().."#"..item.get_id().."#"..(toplam+1).."\\n")
							--ac:close()
						end
					else
						
						local ac_ = io.open('/usr/game/share/locale/turkey/quest/systems/geridonusum/'..pc.get_name()..'.cfg', 'w')
						ac_:write(itemVnum.."#"..itemCount.."#"..(bol[2]).."#"..socket[1].."#"..socket[2].."#"..socket[3].."#"..socket[4].."#"..socket[5].."#"..socket[6].."#"..attr[1][1].."#"..attr[1][2].."#"..attr[2][1].."#"..attr[2][2].."#"..attr[3][1].."#"..attr[3][2].."#"..attr[4][1].."#"..attr[4][2].."#"..attr[5][1].."#"..attr[5][2].."#"..attr[6][1].."#"..attr[6][2].."#"..attr[7][1].."#"..attr[7][2].."#"..pc.get_name().."#"..item.get_id().."#1".."\\n")
						ac_:close()
						
					end
			
					item.remove()
			
				end
				syschat("<System>: Nesneler baþarýyla yok edildi.")
			end
			
		end

		function getinput(gelen)
			local input1 = "#quest_input#"
			local input0 = "#quest_inputbitir#"
			cmdchat("LuaToPython "..input1)
			local al = input(cmdchat("PythonIslem "..gelen))
			cmdchat("LuaToPython "..input0)
			return al
		end

		function split(command_, ne)
			return systems.split_(command_,ne)
		end
		
		function split_(string_,delimiter)
			local result = { }
			local from  = 1
			local delim_from, delim_to = string.find( string_, delimiter, from  )
			while delim_from do
				table.insert( result, string.sub( string_, from , delim_from-1 ) )
				from  = delim_to + 1
				delim_from, delim_to = string.find( string_, delimiter, from  )
			end
			table.insert( result, string.sub( string_, from  ) )
			return result
		end

	end
end