import sqlite3
from enum import Enum
import json

CONNECTION = sqlite3.connect('june.db') 
CURSOR = CONNECTION.cursor()


class Shipclass(Enum):
    FRIGATE = 'Frigate'
    DESTROYER = 'Destroyer'
    CRUISER = 'Cruiser'


def get_attacker_rank(shipclass:Shipclass)->list:
    statement = f"Select count(*) as count, killmail.attacker_ship_name from killmail WHERE killmail.ship_class = '{shipclass.value}' group by killmail.attacker_ship_name ORDER by count DESC"
    CURSOR.execute(statement)
    output = CURSOR.fetchall()
    return output


def get_victim_rank(shipclass:Shipclass)->list:
    statement = f"Select count(*) as count, killmail.victim_ship_name from killmail WHERE killmail.ship_class = '{shipclass.value}' group by killmail.victim_ship_name ORDER by count DESC"
    CURSOR.execute(statement)
    output = CURSOR.fetchall()
    return output


def get_system_rank(shipclass:Shipclass|None)->list:
    if shipclass: 
        statement = f"SELECT count(*) as total, killmail.system_name  from killmail WHERE killmail.ship_class = '{shipclass.value}' GROUP by killmail.system_name ORDER by total DESC"
    else:
        statement = f"SELECT count(*) as total, killmail.system_name  from killmail GROUP by killmail.system_name ORDER by total DESC"
    CURSOR.execute(statement)
    output = CURSOR.fetchall()
    return output


def get_attacker_faction_rank(shipclass:Shipclass|None)->list:
    statement= f"SELECT count(*) as total, killmail.attacker_faction_name  from killmail WHERE killmail.ship_class = '{shipclass.value}' GROUP by killmail.attacker_faction_name ORDER by total DESC"
    CURSOR.execute(statement)
    output = CURSOR.fetchall()
    return output


def get_victim_faction_rank(shipclass:Shipclass|None)->list:
    statement = f"SELECT count(*) as total, killmail.victim_faction_name  from killmail WHERE killmail.ship_class = '{shipclass.value}' GROUP by killmail.victim_faction_name ORDER by total DESC;"
    CURSOR.execute(statement)
    output = CURSOR.fetchall()
    return output


def get_attacker_weapon_rank(shipclass:Shipclass|None)->list:
    statement = f"Select count(*) as count, killmail.attacker_ship_name, killmail.attacker_weapon_name, killmail.victim_ship_name from killmail WHERE killmail.ship_class = '{shipclass.value}' group by killmail.victim_ship_name ORDER by count DESC;"
    CURSOR.execute(statement)
    output = CURSOR.fetchall()
    return output

def get_all_frigate():
    frigate_attacker_rank_result = get_attacker_rank(shipclass=Shipclass.FRIGATE)
    with open('./data/6/frigate_attacker_rank.json', 'w') as output_file:
        json.dump(frigate_attacker_rank_result, output_file, indent=2)
        output_file.close()
    
    frigate_victim_rank_result = get_victim_rank(shipclass=Shipclass.FRIGATE)
    with open('./data/6/frigate_victim_rank.json', 'w') as output_file:
        json.dump(frigate_victim_rank_result, output_file, indent=2)
        output_file.close()

    frigate_system_rank_result = get_system_rank(shipclass=Shipclass.FRIGATE)
    with open('./data/6/frigate_system_rank.json', 'w') as output_file:
        json.dump(frigate_system_rank_result, output_file, indent=2)
        output_file.close()

    frigate_attacker_faction_rank_result = get_attacker_faction_rank(shipclass=Shipclass.FRIGATE)
    with open('./data/6/frigate_attacker_faction_rank.json', 'w') as output_file:
        json.dump(frigate_attacker_faction_rank_result, output_file, indent=2)
        output_file.close()

    frigate_victim_faction_rank_result = get_victim_faction_rank(shipclass=Shipclass.FRIGATE)
    with open('./data/6/frigate_victim_faction_rank.json', 'w') as output_file:
        json.dump(frigate_victim_faction_rank_result, output_file, indent=2)
        output_file.close()

    frigate_attacker_weapon_rank_result = get_attacker_weapon_rank(shipclass=Shipclass.FRIGATE)
    with open('./data/6/frigate_attacker_weapon_rank.json', 'w') as output_file:
        json.dump(frigate_attacker_weapon_rank_result, output_file, indent=2)
        output_file.close()


def get_all_destroyer():
    destroyer_attacker_rank_result = get_attacker_rank(shipclass=Shipclass.DESTROYER)
    with open('./data/6/destroyer_attacker_rank.json', 'w') as output_file:
        json.dump(destroyer_attacker_rank_result, output_file, indent=2)
        output_file.close()
    
    destroyer_victim_rank_result = get_victim_rank(shipclass=Shipclass.DESTROYER)
    with open('./data/6/destroyer_victim_rank.json', 'w') as output_file:
        json.dump(destroyer_victim_rank_result, output_file, indent=2)
        output_file.close()

    destroyer_system_rank_result = get_system_rank(shipclass=Shipclass.DESTROYER)
    with open('./data/6/destroyer_system_rank.json', 'w') as output_file:
        json.dump(destroyer_system_rank_result, output_file, indent=2)
        output_file.close()

    destroyer_attacker_faction_rank_result = get_attacker_faction_rank(shipclass=Shipclass.DESTROYER)
    with open('./data/6/destroyer_attacker_faction_rank.json', 'w') as output_file:
        json.dump(destroyer_attacker_faction_rank_result, output_file, indent=2)
        output_file.close()

    destroyer_victim_faction_rank_result = get_victim_faction_rank(shipclass=Shipclass.DESTROYER)
    with open('./data/6/destroyer_victim_faction_rank.json', 'w') as output_file:
        json.dump(destroyer_victim_faction_rank_result, output_file, indent=2)
        output_file.close()

    destroyer_attacker_weapon_rank_result = get_attacker_weapon_rank(shipclass=Shipclass.DESTROYER)
    with open('./data/6/destroyer_attacker_weapon_rank.json', 'w') as output_file:
        json.dump(destroyer_victim_faction_rank_result, output_file, indent=2)
        output_file.close()


def get_all_cruiser():
    cruiser_attacker_rank_result = get_attacker_rank(shipclass=Shipclass.CRUISER)
    with open('./data/6/cruiser_attacker_rank.json', 'w') as output_file:
        json.dump(cruiser_attacker_rank_result, output_file, indent=2)
        output_file.close()
    
    cruiser_victim_rank_result = get_victim_rank(shipclass=Shipclass.CRUISER)
    with open('./data/6/cruiser_victim_rank.json', 'w') as output_file:
        json.dump(cruiser_victim_rank_result, output_file, indent=2)
        output_file.close()

    cruiser_system_rank_result = get_system_rank(shipclass=Shipclass.CRUISER)
    with open('./data/6/cruiser_system_rank.json', 'w') as output_file:
        json.dump(cruiser_system_rank_result, output_file, indent=2)
        output_file.close()

    cruiser_attacker_faction_rank_result = get_attacker_faction_rank(shipclass=Shipclass.CRUISER)
    with open('./data/6/cruiser_attacker_faction_rank.json', 'w') as output_file:
        json.dump(cruiser_attacker_faction_rank_result, output_file, indent=2)
        output_file.close()

    cruiser_victim_faction_rank_result = get_victim_faction_rank(shipclass=Shipclass.CRUISER)
    with open('./data/6/cruiser_victim_faction_rank.json', 'w') as output_file:
        json.dump(cruiser_victim_faction_rank_result, output_file, indent=2)
        output_file.close()

    cruiser_attacker_weapon_rank_result = get_attacker_weapon_rank(shipclass=Shipclass.CRUISER)
    with open('./data/6/cruiser_attacker_weapon_rank.json', 'w') as output_file:
        json.dump(cruiser_attacker_weapon_rank_result, output_file, indent=2)
        output_file.close()


def get_all_overview(month):
    statement = f"Select count(*) as total, killmail.ship_class from killmail GROUP by killmail.ship_class"
    CURSOR.execute(statement)
    output = CURSOR.fetchall()
    with open(f'./data/{month}/all_overview.json', 'w') as output_file:
        json.dump(output, output_file, indent=2)
        output_file.close

def get_ship_overview(month, shipclass):
    statement = f"Select count(*) as total, killmail.attacker_ship_name, killmail.victim_ship_name from killmail WHERE killmail.ship_class == '{shipclass.value}' GROUP by killmail.attacker_ship_name,killmail.victim_ship_name  ORDER by  total DESC,killmail.attacker_ship_name ASC, killmail.victim_ship_name ASC"
    CURSOR.execute(statement)
    output = CURSOR.fetchall()
    with open(f"./data/{month}/{shipclass.value.lower()}_overview.json", "w") as output_file:
        json.dump(output, output_file, indent=2)
        output_file.close()

# get_all_frigate()
# get_all_destroyer()
# get_all_cruiser()  
# get_all_overview(5)

get_ship_overview(6,Shipclass.FRIGATE)
get_ship_overview(6,Shipclass.DESTROYER)
get_ship_overview(6,Shipclass.CRUISER)