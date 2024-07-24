from functools import cache
import aiohttp
import requests


SOLAR_SYSTEM = {}
WEAPON_NAME = {}


@cache
def get_shipname(ship_id:int)->str:
    # async with aiohttp.ClientSession() as session:
    #     resp = await session.get(url=f"https://ref-data.everef.net/types/{ship_id}")
    #     session.close
    #     # sleep a moment
    #     if resp.status == 200:
    #         result = await resp.json()
    #         return result.get("name",{}).get("en")
            
    #     else:
    #         raise Exception("response not 200")
    response = get_ref_data(id=ship_id)
    return response.get("name",{}).get("en")

        

def get_solar_system_name(system_id:int)->str:
    # async with aiohttp.ClientSession() as session:
    #     resp = await session.get(f"https://esi.evetech.net/v4/universe/systems/{system_id}/?datasource=tranquility&language=en")
    #     session.close

    #     if resp.status ==200:
    #         result = await resp.json()
    #         return result.get("name")
        
    #     else:
    #         raise Exception("response not 200")
    if result := SOLAR_SYSTEM.get(system_id):
        return result
    else:
        response = requests.get(url=f"https://esi.evetech.net/v4/universe/systems/{system_id}/?datasource=tranquility&language=en")
        if response.status_code == 200:
            response_json = response.json()
            solar_system_name = response_json.get("name")
            SOLAR_SYSTEM.update({system_id:solar_system_name})
            return solar_system_name
        else:
            raise Exception("response not 200")
        
@cache
def get_weapon_name(weapon_id:int)->str:
    # async with aiohttp.ClientSession() as session:
    #     resp = await session.get(f"https://ref-data.everef.net/types/{weapon_id}")
    #     session.close

    #     if resp.status == 200:
    #         result = await resp.json()
    #         return result.get("name",{}).get("en")
    #     else:
    #         raise Exception("response not 200")
    if weapon_name := WEAPON_NAME.get(weapon_id):
        return weapon_name
    else:
        response = get_ref_data(id=weapon_id)
        weapon_name = response.get("name",{}).get("en")
        WEAPON_NAME.update({weapon_id:weapon_name})
        return weapon_name
        
@cache
def get_faction_name(faction_id:int)->str:
    FACTION_NAMES = {
        500003:"Amarr Empire",
        500010: "Guristas Pirates",
        500004: "Gallente Federation",
        500011: "Angel Cartel",
        500007: "Ammatar Mandate",
        500020:"Serpentis",
        500002: "Minmatar Republic",
        500001: "Caldari State"
    }

    return FACTION_NAMES.get(faction_id,faction_id)

def get_ref_data(id:int)->dict:
    result = requests.get(url=f"https://ref-data.everef.net/types/{id}")
    if result.status_code == 200:
        json_resp = result.json()
        return json_resp
    else:
        raise Exception(f"{result.status_code=}")
    
