import aiohttp
import asyncio
import get_static
import sqlite3
frigate_ids =  [582, 583, 584, 585, 586, 587, 589, 590, 591, 592, 593, 594, 595, 597, 598, 599, 600, 602, 603, 605, 607, 608, 609, 613, 614, 616, 618, 619, 1896, 1898, 1900, 1902, 2161, 3532, 3751, 3753, 3766, 3768, 11019, 11940, 11942, 17360, 17619, 17703, 17705, 17707, 17812, 17841, 17924, 17926, 17928, 17930, 17932, 29248, 32880, 32983, 32985, 32987, 32989, 33190, 33468, 33655, 33657, 33659, 33661, 33663, 33665, 33667, 33669, 33677, 33816, 34443, 37453, 37454, 37455, 37456, 47269, 54731, 58745, 72903, 72904, 72907, 72913, 77114]
cruiser_ids = [620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 1904, 2006, 11011, 17634, 17709, 17713, 17715, 17718, 17720, 17722, 17843, 17922, 25560, 29336, 29337, 29340, 29344, 33470, 33553, 33639, 33641, 33643, 33645, 33647, 33649, 33651, 33653, 33818, 34445, 34475, 34590, 47270, 49712, 52267, 54732]
destroyer_ids = [16236, 16238, 16240, 16242, 32840, 32842, 32844, 32846, 32848, 32872, 32874, 32876, 32878, 33099, 33877, 33879, 33881, 33883, 42685, 49710, 73789, 73794, 73795, 73796, 78333, 78367]



def get_failed(conn, cursor)->list:
    statement = 'SELECT * FROM fail'
    cursor.execute(statement)
    output = cursor.fetchall()
    return output


def delete_failed(conn,cursor, kill_id):
    statement = 'DELETE FROM fail WHERE kill_id = ?'
    cursor.execute(statement,(kill_id,))
    conn.commit()
    return


async def insert_killmail(conn,cursor, key, value, result):
    attacker_list = result.get("attackers")
    victim = result.get("victim")

    #Check if attack is solo
    if len(attacker_list)> 2:
        return 

    #Check if contain NPC attack
    if len(attacker_list) == 2 and attacker_list[1].get("character_id", None) != None :
        return

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
        return
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
    
    val = (key, value, ship_class, str(system_id), system_name, killmail_time, str(attacker_id), str(attacker_faction_id), str(attacker_faction_name), str(attacker_ship_id), attacker_ship_name, str(attacker_weapon_id), attacker_weapon_name, str(victim_id), str(victim_faction_id), str(victim_faction_name), str(victim_ship_id),str(victim_ship_name))

    cursor.execute(sql, val) 

    # Commit your changes in the datab ase     
    conn.commit() 

async def fetch_json(kill_id:str, hash:str)->dict:
    async with aiohttp.ClientSession() as session:
        resp = await session.get(url=f"https://esi.evetech.net/latest/killmails/{kill_id}/{hash}/?datasource=tranquility")
        session.close
        if resp.status == 200:
            return await resp.json()
            
        else:
            raise Exception("response not 200")


async def run(conn, cursor, killid,hash):

    try:
        print(f"{killid=} , {hash=}")
        result = await fetch_json(kill_id=killid, hash=hash)

        await insert_killmail(conn=conn, cursor=cursor, key=killid, value=hash, result=result)

        delete_failed(conn=conn, cursor=cursor, kill_id=killid)
        return 
    except sqlite3.IntegrityError as e:
        print(f"{e=}")
        delete_failed(conn=conn, cursor=cursor, kill_id=killid)
        return 
    except Exception as e:
        print(f"{e=}")


async def main():
    conn = sqlite3.connect('may.db') 
    cursor = conn.cursor()

    fail_list = get_failed(conn, cursor)
    
    for index in range (0, len(fail_list), 10):
        fail_batch = fail_list[index:index+10]
        
        await asyncio.gather(*[run(conn, cursor, k,v) for k,v in fail_batch])


    # Closing the connection 
    conn.close()

if __name__ == '__main__':
    asyncio.run(main())