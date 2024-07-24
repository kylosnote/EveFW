import sqlite3

con = sqlite3.connect("june.db")
cur = con.cursor()
cur.execute(
    "CREATE TABLE killmail(kill_id, hash, ship_class, system_id, system_name, killmail_time, attacker_id, attacker_faction_id, attacker_faction_name,attacker_ship_id, attacker_ship_name, attacker_weapon_id, attacker_weapon_name, victim_id, victim_faction_id, victim_faction_name, victim_ship_id, victim_ship_name)"
    )

# cur.execute(
#     "CREATE TABLE fail(kill_id, hash)"
#     )


con.close()