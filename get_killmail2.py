# import aiohttp
# import asyncio
import json
import pathlib
import get_static
import sqlite3
import os

base_path = pathlib.Path(__file__).parent.resolve()


def main(month=None):
    frigate_ids =  [582, 583, 584, 585, 586, 587, 589, 590, 591, 592, 593, 594, 595, 597, 598, 599, 600, 602, 603, 605, 607, 608, 609, 613, 614, 616, 618, 619, 1896, 1898, 1900, 1902, 2161, 3532, 3751, 3753, 3766, 3768, 11019, 11940, 11942, 17360, 17619, 17703, 17705, 17707, 17812, 17841, 17924, 17926, 17928, 17930, 17932, 29248, 32880, 32983, 32985, 32987, 32989, 33190, 33468, 33655, 33657, 33659, 33661, 33663, 33665, 33667, 33669, 33677, 33816, 34443, 37453, 37454, 37455, 37456, 47269, 54731, 58745, 72903, 72904, 72907, 72913, 77114]
    cruiser_ids = [620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 1904, 2006, 11011, 17634, 17709, 17713, 17715, 17718, 17720, 17722, 17843, 17922, 25560, 29336, 29337, 29340, 29344, 33470, 33553, 33639, 33641, 33643, 33645, 33647, 33649, 33651, 33653, 33818, 34445, 34475, 34590, 47270, 49712, 52267, 54732]
    destroyer_ids = [16236, 16238, 16240, 16242, 32840, 32842, 32844, 32846, 32848, 32872, 32874, 32876, 32878, 33099, 33877, 33879, 33881, 33883, 42685, 49710, 73789, 73794, 73795, 73796, 78333, 78367]

    conn = sqlite3.connect('june.db') 
    cursor = conn.cursor() 

    delete_list = []


    try:
        #Get json file directory list
        file_list = pathlib.Path(f"{base_path}/killmails/2024/6/killmails").glob("*.json")
        for json_path in file_list:
            with open(json_path, 'r') as open_file:
                result = json.load(open_file) #Single killmail
                # print(result)
            
                attacker_list = result.get("attackers")
                victim = result.get("victim")

                #Check if attack is solo
                if len(attacker_list)> 2:
                    delete_list.append(json_path)
                    continue

                #Check if contain NPC attack
                if len(attacker_list) == 2 and attacker_list[1].get("character_id", None) != None :
                    delete_list.append(json_path)
                    continue        

                #Check if is frigate, destroyer or cruiser
                attacker_ship = attacker_list[0]
                attacker_ship_id = attacker_ship.get("ship_type_id","")

                victim_ship_id =  victim.get("ship_type_id")
                #Frigate group
                if attacker_ship_id in frigate_ids and victim_ship_id in frigate_ids:
                    print("Frigate Match")
                    ship_class = "Frigate"
                    attacker_ship_name = get_static.get_shipname(ship_id=attacker_ship_id)
                    victim_ship_name = get_static.get_shipname(ship_id=victim_ship_id )
                    print(f"{attacker_ship_name=} , {victim_ship_name=}")
                
                # Destroyer group
                elif attacker_ship_id in destroyer_ids and victim_ship_id in destroyer_ids:
                    print("Destroyer match")
                    ship_class = "Destroyer"
                    attacker_ship_name = get_static.get_shipname(ship_id=attacker_ship_id)
                    victim_ship_name = get_static.get_shipname(ship_id=victim_ship_id )
                    print(f"{attacker_ship_name=} , {victim_ship_name=}")

                # Cruiser group
                elif attacker_ship_id in cruiser_ids and victim_ship_id in cruiser_ids:
                    print("Cruiser match")
                    ship_class = "Cruiser"
                    attacker_ship_name = get_static.get_shipname(ship_id=attacker_ship_id)
                    victim_ship_name = get_static.get_shipname(ship_id=victim_ship_id )
                    print(f"{attacker_ship_name=} , {victim_ship_name=}")

                else:
                    # print(" no match")
                    delete_list.append(json_path)
                    continue

                system_id = result.get("solar_system_id")
                system_name = get_static.get_solar_system_name(system_id=system_id)

                attacker_weapon_id = attacker_ship.get("weapon_type_id")
                attacker_weapon_name = get_static.get_weapon_name(weapon_id=attacker_weapon_id)

                attacker_id = attacker_ship.get("character_id")
                attacker_faction_id = attacker_ship.get("faction_id")
                attacker_faction_name = get_static.get_faction_name(faction_id=attacker_faction_id)

                victim_id = victim.get("character_id")
                victim_faction_id = victim.get("faction_id")
                victim_faction_name = get_static.get_faction_name(faction_id=victim_faction_id)


                killmail_time = result.get("killmail_time")

                # killmail(kill_id, hash, ship_class, system_id, system_name, killmail_time, attacker_id, attacker_ship_id, attacker_ship_name, attacker_weapon_id, attacker_weapon_name, victim_id, victim_faction_id, victim_faction_name)

                # Queries to INSERT records. 
                sql = "INSERT INTO killmail (kill_id, hash, ship_class, system_id, system_name, killmail_time, attacker_id,attacker_faction_id, attacker_faction_name, attacker_ship_id, attacker_ship_name, attacker_weapon_id, attacker_weapon_name, victim_id, victim_faction_id, victim_faction_name,victim_ship_id, victim_ship_name) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
                
                val = (result.get("killmail_id"), result.get("killmail_hash"), ship_class, str(system_id), system_name, killmail_time, str(attacker_id), str(attacker_faction_id), str(attacker_faction_name), str(attacker_ship_id), attacker_ship_name, str(attacker_weapon_id), attacker_weapon_name, str(victim_id), str(victim_faction_id), str(victim_faction_name), str(victim_ship_id),str(victim_ship_name))

                cursor.execute(sql, val) 

                # Commit your changes in the datab ase     
                conn.commit() 
                delete_list.append(json_path)
    except Exception as e:
        print(f"{e=}")
        # Delete
        for each in delete_list:
            os.remove(each)

main()