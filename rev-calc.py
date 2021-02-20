#!/usr/bin/env python3
import itertools
import math
import sys
import time
from typing import List, Dict, Tuple

#this is done
abilities: List[str] = ["ANTICIPATION", "ASPHYXIATE", "ASSAULT", "BACKHAND", "BARGE", "BASH",
                        "BERSERK", "BINDING SHOT", "BLOOD TENDRILS", "BOMBARDMENT", "CHAIN", "CLEAVE", "COMBUST",
                        "CONCENTRATED BLAST", "CORRUPTION BLAST", "CORRUPTION SHOT", "DAZING SHOT", "DEADSHOT",
                        "DEATH'S SWIFTNESS", "DEBILITATE", "DECIMATE", "DEEP IMPACT", "DEMORALISE", "DESTROY",
                        "DEVOTION", "DISMEMBER", "DRAGON BREATH", "ESCAPE", "FLURRY", "FORCEFUL BACKHAND",
                        "FRAGMENTATION SHOT", "FREEDOM", "FRENZY", "FURY", "GOLDEN TOUCH", "HAVOC", "HORROR", "HURRICANE",
                        "IMPACT", "INCENDIARY SHOT", "KICK", "MASSACRE", "METAMORPHOSIS", "METEOR STRIKE", "NEEDLE STRIKE",
                        "OMNIPOWER", "OVERPOWER", "PIERCING SHOT", "PULVERISE", "PUNISH", "QUAKE", "RAPID FIRE", "RICOCHET",
                        "ROUT", "SACRIFICE", "SALT THE WOUND", "SEVER", "SHADOW TENDRILS", "SHOCK", "SLAUGHTER", "SLICE",
                        "SMASH", "SMOKE TENDRILS", "SNAP SHOT", "SNIPE", "SONIC WAVE", "STOMP", "SUNSHINE",
                        "SURGE", "TIGHT BINDINGS", "TSUNAMI","TUSKA'S WRATH", "UNLOAD", "WILD MAGIC", "WRACK"]

# --- Defining how abilities work --- #

# Define cooldowns for cases where no abilities may be used --done
attack_speed_cooldowns: Dict[str, float] = {"FASTEST": 2.4, "FAST": 3.0, "AVERAGE": 3.6, "SLOW": 4.2, "SLOWEST": 7.2}

# Define ability damage for every ability
ability_damage: Dict[str, float] = {"ANTICIPATION": , "ASPHYXIATE": , "ASSAULT": , "BACKHAND": , "BARGE": , "BASH": ,
                        "BERSERK": , "BINDING SHOT": , "BLOOD TENDRILS": , "BOMBARDMENT": , "CHAIN": , "CLEAVE": , "COMBUST": ,
                        "CONCENTRATED BLAST": , "CORRUPTION BLAST": , "CORRUPTION SHOT": , "DAZING SHOT": , "DEADSHOT": ,
                        "DEATH'S SWIFTNESS": , "DEBILITATE": , "DECIMATE": , "DEEP IMPACT": , "DEMORALISE": , "DESTROY": ,
                        "DEVOTION": , "DISMEMBER": , "DRAGON BREATH": , "ESCAPE": , "FLURRY": , "FORCEFUL BACKHAND": ,
                        "FRAGMENTATION SHOT": , "FREEDOM": , "FRENZY": , "FURY": , "GOLDEN TOUCH": , "HAVOC": , "HORROR": , "HURRICANE": ,
                        "IMPACT": , "INCENDIARY SHOT": , "KICK": , "MASSACRE": , "METAMORPHOSIS": , "METEOR STRIKE": , "NEEDLE STRIKE": ,
                        "OMNIPOWER": , "OVERPOWER": , "PIERCING SHOT": , "PULVERISE": , "PUNISH": , "QUAKE": , "RAPID FIRE": , "RICOCHET": ,
                        "ROUT": , "SACRIFICE": , "SALT THE WOUND": , "SEVER": , "SHADOW TENDRILS": , "SHOCK": , "SLAUGHTER": , "SLICE": ,
                        "SMASH": , "SMOKE TENDRILS": , "SNAP SHOT": , "SNIPE": , "SONIC WAVE": , "STOMP": , "SUNSHINE": ,
                        "SURGE": , "TIGHT BINDINGS": , "TSUNAMI": ,"TUSKA'S WRATH": , "UNLOAD": , "WILD MAGIC": , "WRACK": }

# Define the cooldown of abilities (in seconds)
ability_cooldown: Dict[str, float] = {"ANTICIPATION": 40, "ASPHYXIATE": 34, "ASSAULT": 50, "BACKHAND": 25, "BARGE": 34, "BASH": 25,
                        "BERSERK": 100, "BINDING SHOT": 25, "BLOOD TENDRILS": 75, "BOMBARDMENT": 50, "CHAIN": 17, "CLEAVE": 12, "COMBUST": 25,
                        "CONCENTRATED BLAST": 9, "CORRUPTION BLAST": 25, "CORRUPTION SHOT": 25, "DAZING SHOT": 9, "DEADSHOT": 50,
                        "DEATH'S SWIFTNESS": 100, "DEBILITATE": 50, "DECIMATE": 12, "DEEP IMPACT": 25, "DEMORALISE": 25, "DESTROY": 34,
                        "DEVOTION": 100, "DISMEMBER": 25, "DRAGON BREATH": 17, "ESCAPE": 34, "FLURRY": 34, "FORCEFUL BACKHAND": 25,
                        "FRAGMENTATION SHOT": 25, "FREEDOM": 50, "FRENZY": 100, "FURY": 9, "GOLDEN TOUCH": 200, "HAVOC": 17, "HORROR": 25, "HURRICANE": 34,
                        "IMPACT": 25, "INCENDIARY SHOT": 100, "KICK": 25, "MASSACRE": 100, "METAMORPHOSIS": 100, "METEOR STRIKE": 100, "NEEDLE STRIKE": 9,
                        "OMNIPOWER": 50, "OVERPOWER": 50, "PIERCING SHOT": 5, "PULVERISE": 100, "PUNISH": 5, "QUAKE": 34, "RAPID FIRE": 34, "RICOCHET": 17,
                        "ROUT": 25, "SACRIFICE": 50, "SALT THE WOUND": 25, "SEVER": 25, "SHADOW TENDRILS": 75, "SHOCK": 25, "SLAUGHTER": 50, "SLICE": 5,
                        "SMASH": 17, "SMOKE TENDRILS": 75, "SNAP SHOT": 34, "SNIPE": 17, "SONIC WAVE": 9, "STOMP": 25, "SUNSHINE": 100,
                        "SURGE": 34, "TIGHT BINDINGS": 25, "TSUNAMI": 100,"TUSKA'S WRATH": 25, "UNLOAD": 100, "WILD MAGIC": 34, "WRACK": 5}

# How long it takes to use each ability
ability_time: Dict[str, float] = {"ANTICIPATION": 0.6, "ASPHYXIATE": 5.4, "ASSAULT": 5.4, "BACKHAND": 0.9, "BARGE": 0.6, "BASH": 0.6,
                        "BERSERK": 0.6, "BINDING SHOT": 0.6, "BLOOD TENDRILS": 0.6, "BOMBARDMENT": 0.6, "CHAIN": 0.6, "CLEAVE": 0.6, "COMBUST": 0.6,
                        "CONCENTRATED BLAST": 3.6, "CORRUPTION BLAST": 0.6, "CORRUPTION SHOT": 0.6, "DAZING SHOT": 0.6, "DEADSHOT": 0.6,
                        "DEATH'S SWIFTNESS": 0.6, "DEBILITATE": 0.6, "DECIMATE": 0.6, "DEEP IMPACT": 0.6, "DEMORALISE": 0.6, "DESTROY": 5.4,
                        "DEVOTION": 0.6, "DISMEMBER": 0.6, "DRAGON BREATH": 0.6, "ESCAPE": 0.6, "FLURRY": 5.4, "FORCEFUL BACKHAND": 0.6,
                        "FRAGMENTATION SHOT": 0.6, "FREEDOM": 0.6, "FRENZY": 5.4, "FURY": 3, "GOLDEN TOUCH": 0.6, "HAVOC": 0.6, "HORROR": 0.6, "HURRICANE": 0.6,
                        "IMPACT": 0.6, "INCENDIARY SHOT": 0.6, "KICK": 0.6, "MASSACRE": 0.6, "METAMORPHOSIS": 0.6, "METEOR STRIKE": 0.6, "NEEDLE STRIKE": 0.6,
                        "OMNIPOWER": 0.6, "OVERPOWER": 0.6, "PIERCING SHOT": 0.6, "PULVERISE": 0.6, "PUNISH": 0.6, "QUAKE": 0.6, "RAPID FIRE": 6, "RICOCHET": 0.6,
                        "ROUT": 0.6, "SACRIFICE": 0.6, "SALT THE WOUND": 0.6, "SEVER": 0.6, "SHADOW TENDRILS": 0.6, "SHOCK": 0.6, "SLAUGHTER": 0.6, "SLICE": 0.6,
                        "SMASH": 0.6, "SMOKE TENDRILS": 5.4, "SNAP SHOT": 0.6, "SNIPE": 4.2, "SONIC WAVE": 0.6, "STOMP": 0.6, "SUNSHINE": 0.6,
                        "SURGE": 0.6, "TIGHT BINDINGS": 0.6, "TSUNAMI": 0.6,"TUSKA'S WRATH": 0.6, "UNLOAD": 5.4, "WILD MAGIC": 0.6, "WRACK": 0.6}

# Define the type of abilities (B = basic, T = threshold, U = ultimate)
ability_type: Dict[str, str] = {"ANTICIPATION": "B", "ASPHYXIATE": "T", "ASSAULT": "T", "BACKHAND": "B", "BARGE": "B", "BASH": "B",
                        "BERSERK": "U", "BINDING SHOT": "B", "BLOOD TENDRILS": "T", "BOMBARDMENT": "T", "CHAIN": "B", "CLEAVE": "B", "COMBUST": "B",
                        "CONCENTRATED BLAST": "B", "CORRUPTION BLAST": "B", "CORRUPTION SHOT": "B", "DAZING SHOT": "B", "DEADSHOT": "U",
                        "DEATH'S SWIFTNESS": "U", "DEBILITATE": "T", "DECIMATE": "B", "DEEP IMPACT": "T", "DEMORALISE": "B", "DESTROY": "T",
                        "DEVOTION": "T", "DISMEMBER": "B", "DRAGON BREATH": "B", "ESCAPE": "B", "FLURRY": "T", "FORCEFUL BACKHAND": "T",
                        "FRAGMENTATION SHOT": "B", "FREEDOM": "B", "FRENZY": "U", "FURY": "B", "GOLDEN TOUCH": "B", "HAVOC": "B", "HORROR": "T", "HURRICANE": "T",
                        "IMPACT": "B", "INCENDIARY SHOT": "U", "KICK": "B", "MASSACRE": "U", "METAMORPHOSIS": "U", "METEOR STRIKE": "U", "NEEDLE STRIKE": "B",
                        "OMNIPOWER": "U", "OVERPOWER": "U", "PIERCING SHOT": "B", "PULVERISE": "U", "PUNISH": "B", "QUAKE": "T", "RAPID FIRE": "T", "RICOCHET": "B",
                        "ROUT": "T", "SACRIFICE": "B", "SALT THE WOUND": "T", "SEVER": "B", "SHADOW TENDRILS": "T", "SHOCK": "S", "SLAUGHTER": "T", "SLICE": "B",
                        "SMASH": "B", "SMOKE TENDRILS": "T", "SNAP SHOT": "T", "SNIPE": "B", "SONIC WAVE": "B", "STOMP": "T", "SUNSHINE": "U",
                        "SURGE": "B", "TIGHT BINDINGS": "T", "TSUNAMI": "U","TUSKA'S WRATH": "B", "UNLOAD": "U", "WILD MAGIC": "T", "WRACK": "B"}

# Define a flag to decide if you can use abilities (based on adrenaline)
ability_ready: Dict[str, bool] = {"ANTICIPATION": True, "ASPHYXIATE": False, "ASSAULT": False, "BACKHAND": True, "BARGE": True, "BASH": True,
                        "BERSERK": False, "BINDING SHOT": True, "BLOOD TENDRILS": False, "BOMBARDMENT": False, "CHAIN": True, "CLEAVE": True, "COMBUST": True,
                        "CONCENTRATED BLAST": True, "CORRUPTION BLAST": True, "CORRUPTION SHOT": True, "DAZING SHOT": True, "DEADSHOT": False,
                        "DEATH'S SWIFTNESS": False, "DEBILITATE": False, "DECIMATE": True, "DEEP IMPACT": False, "DEMORALISE": True, "DESTROY": False,
                        "DEVOTION": False, "DISMEMBER": True, "DRAGON BREATH": True, "ESCAPE": True, "FLURRY": False, "FORCEFUL BACKHAND": False,
                        "FRAGMENTATION SHOT": True, "FREEDOM": True, "FRENZY": False, "FURY": True, "GOLDEN TOUCH": True, "HAVOC": True, "HORROR": False, "HURRICANE": False,
                        "IMPACT": True, "INCENDIARY SHOT": False, "KICK": True, "MASSACRE": False, "METAMORPHOSIS": False, "METEOR STRIKE": False, "NEEDLE STRIKE": True,
                        "OMNIPOWER": False, "OVERPOWER": False, "PIERCING SHOT": True, "PULVERISE": False, "PUNISH": True, "QUAKE": False, "RAPID FIRE": False, "RICOCHET": True,
                        "ROUT": False, "SACRIFICE": True, "SALT THE WOUND": False, "SEVER": True, "SHADOW TENDRILS": False, "SHOCK": "S", "SLAUGHTER": False, "SLICE": True,
                        "SMASH": True, "SMOKE TENDRILS": False, "SNAP SHOT": False, "SNIPE": True, "SONIC WAVE": True, "STOMP": False, "SUNSHINE": False,
                        "SURGE": True, "TIGHT BINDINGS": False, "TSUNAMI": False,"TUSKA'S WRATH": True, "UNLOAD": False, "WILD MAGIC": False, "WRACK": True}

# Define the time DOT abilities last (in seconds) 1 DOT application takes 2 ticks or 1.2 seconds
bleeds: Dict[str, float] = {"BLOOD TENDRILS": 4.8, "COMBUST": 6, "CORRUPTION BLAST": 6, "CORRUPTION SHOT": 6,
                            "DEADSHOT": 6, "DISMEMBER": 6, "FRAGMENTATION SHOT": 6, "MASSACRE": 6,
                            "SHADOW TENDRILS": 1.8, "SLAUGHTER": 6, "SMOKE TENDRILS": 5.4}

# Define damage multiplier of walking bleeds
walking_bleeds: Dict[str, float] = {"COMBUST": 1, "FRAGMENTATION SHOT": 1, "SLAUGHTER": 1.5}

# Define bleed abilities that have their first hit affected by damage modifying abilities
special_bleeds: List[str] = ["DEADSHOT", "MASSACRE", "SMOKE TENDRILS"]

# Define abilities that take longer than 1.8 seconds to use but will still have full impact from abilities in the
# crit_boost list
special_abilities: List[str] = ["DETONATE", "SNIPE"]

# How long stuns, DPS increases .. etc last
buff_time: Dict[str, float] = {"BARGE": 6.6, "BERSERK": 19.8, "BINDING SHOT": 9.6, "CONCENTRATED BLAST": 5.4,
                               "DEATH'S SWIFTNESS": 30, "DEEP IMPACT": 3.6, "FORCEFUL BACKHAND": 3.6, "FURY": 5.4,
                               "METAMORPHOSIS": 15, "NEEDLE STRIKE": 3.6, "RAPID FIRE": 6, "STOMP": 3.6, "SUNSHINE": 30,
                               "TIGHT BINDINGS": 9.6}

# Define the Multiplier for boosted damage
buff_effect: Dict[str, float] = {"BERSERK": 2, "CONCENTRATED BLAST": 1.1, "DEATH'S SWIFTNESS": 1.5, "FURY": 1.1,
                                 "METAMORPHOSIS": 1.625, "NEEDLE STRIKE": 1.07, "PIERCING SHOT": 2, "PUNISH": 2,
                                 "SLICE": 1.506, "SUNSHINE": 1.5, "WRACK": 2}

# Define crit-boosting abilities
crit_boost: List[str] = ["BERSERK", "CONCENTRATED BLAST", "DEATH'S SWIFTNESS", "FURY", "METAMORPHOSIS", "NEEDLE STRIKE",
                         "SUNSHINE"]

# Define the abilities that do extra damage when the target is stun or bound
punishing: List[str] = ["PIERCING SHOT", "PUNISH", "SLICE", "WRACK"]

# Define abilities that can stun or bind the target
debilitating: List[str] = ["BARGE", "BINDING SHOT", "DEEP IMPACT", "FORCEFUL BACKHAND", "RAPID FIRE", "STOMP",
                           "TIGHT BINDINGS"]

# Define abilities that bind the target
binds: List[str] = ["BARGE", "BINDING SHOT", "DEEP IMPACT", "TIGHT BINDINGS"]

# Define area of effect abilities
aoe: List[str] = ["BOMBARDMENT", "CHAIN", "CLEAVE", "CORRUPTION BLAST", "CORRUPTION SHOT", "DRAGON BREATH", "FLURRY",
                  "HURRICANE", "QUAKE", "RICOCHET", "TSUNAMI"]

start_adrenaline: int
gain: int
attack_speed: str
activate_bleeds: bool
my_abilities: List[str]
auto_adrenaline: int
cycle_duration: float


# Will return how much damage an ability bar will do over a given time
def ability_rotation(permutation: List[str]) -> float:
    # Will check if an auto attack is needed to be used
    def auto_available() -> bool:
        for ability in track_cooldown:
            if (ability_cooldown[ability] - track_cooldown[ability]) < attack_speed_cooldowns[attack_speed]:
                return False
        return True

    # Decreases Cooldowns of abilities and buffs as well as modifying and damage multipliers
    def adjust_cooldowns(current_buff: float, adrenaline: int, cooldown_time: float) -> float:
        for ability in track_cooldown:
            track_cooldown[ability] += cooldown_time
            track_cooldown[ability] = round(track_cooldown[ability], 1)
            if track_cooldown[ability] >= ability_cooldown[ability]:
                track_cooldown[ability] = 0
                if ability in threshold_ability_list:
                    if adrenaline >= 50:
                        ability_ready[ability] = True
                elif ability in ultimate_ability_list:
                    if adrenaline == 100:
                        ability_ready[ability] = True
                else:
                    ability_ready[ability] = True
        for ability in permutation:
            if ability in track_cooldown and track_cooldown[ability] == 0:
                del track_cooldown[ability]
        for ability in track_buff:
            track_buff[ability] += cooldown_time
            track_buff[ability] = round(track_buff[ability], 1)
            if track_buff[ability] >= buff_time[ability]:
                track_buff[ability] = 0
        for ability in permutation:
            if ability in track_buff and track_buff[ability] == 0:
                del track_buff[ability]
                if (ability not in punishing) and (ability in buff_effect):
                    current_buff = current_buff / buff_effect[ability]
        return current_buff

    # Determines if enemy vulnerable to extra damage due to stuns or binds
    def buff_available() -> bool:
        for ability in debilitating:
            if ability in track_buff:
                return True
        return False

    def modify_time(cycle_duration: float, time_elapsed: float, ability: str) -> float:
        if (ability in bleeds) and (ability != "SHADOW TENDRILS") and (
                    (cycle_duration - time_elapsed) < bleeds[ability]):
            return (cycle_duration - time_elapsed) / bleeds[ability]
        else:
            if (ability not in special_abilities) and (ability_time[ability] > 1.8) and (
                        (cycle_duration - time_elapsed) < ability_time[ability]):
                return (cycle_duration - time_elapsed) / ability_time[ability]
        return 1

    # --- Defining Variables --- #
    damage_dealt: float = 0
    current_buff: float = 1
    time_elapsed: float = 0
    shards: float = 0
    adrenaline = start_adrenaline
    # --- Calculations begin here --- #
    ability_path.append(f"AUTO D: {round(damage_dealt, 1)} T: {round(time_elapsed, 1)} A: {adrenaline}")
    damage_dealt += 50
    adrenaline += auto_adrenaline
    if adrenaline >= 100:
        adrenaline = 100
        for tracked_ability in ultimate_ability_list:
            ability_ready[tracked_ability] = True
        for tracked_ability in threshold_ability_list:
            ability_ready[tracked_ability] = True
    elif adrenaline >= 50:
        for tracked_ability in threshold_ability_list:
            ability_ready[tracked_ability] = True
    elif adrenaline < 0:
        adrenaline = 0
    time_elapsed += 0.6
    time_elapsed = round(time_elapsed, 1)
    while time_elapsed < cycle_duration:
        for ability in permutation:
            # Checks if ability can be used TODO: Check if this is necessary
            if time_elapsed < cycle_duration and ability_ready[ability] is True:
                ability_ready[ability] = False
                # --- Modifying adrenaline as required --- #
                ability_path.append(f"{ability} D: {round(damage_dealt, 1)} T: {round(time_elapsed, 1)}"
                                    f" A: {adrenaline}")
                if ability in basic_ability_list:
                    adrenaline += 8
                elif ability in threshold_ability_list:
                    adrenaline -= 15
                else:
                    adrenaline = gain
                if adrenaline > 100:
                    adrenaline = 100
                # --- Adding shards if they are used, or using them if activated --- #
                if ability == "STORM SHARDS":
                    if shards < 10:
                        shards += 1
                elif ability == "SHATTER":
                    damage_dealt += round(shards * 85, 1)
                    shards = 0
                    # --- Calculating how much damage abilities should do --- #
                more_binds: bool = False
                altered_bleeds: bool = False
                modified_damage: bool = False
                damage_multiplier: float = 1  # Multiplier for damage due to damage boosting abilities
                bleed_multiplier: float = 1  # Multiplier in case target is bound (and bind about to run out)
                for tracked_ability in track_buff:
                    if tracked_ability in crit_boost:
                        if ((buff_time[tracked_ability] - track_buff[tracked_ability]) < ability_time[ability]) and (
                                    (ability not in special_abilities) and (ability_time[ability] > 1.8)):
                            damage_multiplier *= (
                                (((buff_time[tracked_ability] - track_buff[tracked_ability]) / ability_time[ability]) *
                                 (buff_effect[tracked_ability] - 1)) + 1)
                        else:
                            damage_multiplier *= buff_effect[tracked_ability]
                    elif (tracked_ability in binds) and (activate_bleeds is True) and (ability in walking_bleeds) and (
                                len(debilitating) > 0):
                        if (more_binds is False) and (
                                        buff_time[tracked_ability] - track_buff[tracked_ability] < bleeds[ability]):
                            bleed_multiplier = walking_bleeds[ability] * (
                                1 + (buff_time[tracked_ability] - track_buff[tracked_ability]) / bleeds[ability])
                        else:
                            bleed_multiplier = 1
                            more_binds = True
                        altered_bleeds = True
                if (activate_bleeds is True) and (ability in walking_bleeds) and (altered_bleeds is False):
                    bleed_multiplier = walking_bleeds[ability] * 2
                time_multiplier = modify_time(cycle_duration, time_elapsed, ability)
                if ability in bleeds:
                    if ability in special_bleeds:
                        if ability == "SMOKE TENDRILS":
                            damage_dealt += (ability_damage[ability] * damage_multiplier)
                        else:
                            ability_damage[ability] = ((112.8 * damage_multiplier) + 313.33)
                            modified_damage = True
                    damage_dealt += round(ability_damage[ability] * bleed_multiplier * time_multiplier, 1)
                    if modified_damage is True:
                        ability_damage[ability] = 426.13
                elif (ability in punishing) and (buff_available() is True):
                    damage_dealt += round(ability_damage[ability] * buff_effect[ability] * damage_multiplier *
                                          time_multiplier, 1)
                else:
                    damage_dealt += round(ability_damage[ability] * damage_multiplier * time_multiplier, 1)
                # --- Increasing rotation duration and managing cooldowns --- #
                time_elapsed += ability_time[ability]
                time_elapsed = round(time_elapsed, 1)
                track_cooldown[ability] = float(0)
                if ability in buff_time and ability not in punishing:
                    track_buff[ability] = 0
                    if ability in buff_effect:
                        current_buff = current_buff * buff_effect[ability]
                # Will also manage cooldowns
                current_buff = adjust_cooldowns(current_buff, adrenaline, ability_time[ability])
                break
        # --- Determines whether thresholds or ultimates may be used --- #
        if time_elapsed < cycle_duration:
            if adrenaline == 100:
                for tracked_ability in (a for a in ultimate_ability_list if a not in track_cooldown):
                    ability_ready[tracked_ability] = True
                for tracked_ability in (a for a in threshold_ability_list if a not in track_cooldown):
                    ability_ready[tracked_ability] = True
            elif adrenaline >= 50:
                for tracked_ability in (a for a in threshold_ability_list if a not in track_cooldown):
                    ability_ready[tracked_ability] = True
            elif adrenaline < 50:
                for tracked_ability in threshold_ability_list:
                    ability_ready[tracked_ability] = False
            if adrenaline != 100:
                for tracked_ability in ultimate_ability_list:
                    ability_ready[tracked_ability] = False
        # --- Determines if any abilities available/ whether auto attacks must be used --- #
        if time_elapsed < cycle_duration:
            ability_available = False
            for _ in (a for a in permutation if ability_ready[a]):
                ability_available = True
                break
            if ability_available is False:
                if auto_available() is True:
                    if (time_elapsed + attack_speed_cooldowns[attack_speed]) <= cycle_duration:
                        time_elapsed += attack_speed_cooldowns[attack_speed]
                    else:
                        time_elapsed += (cycle_duration - time_elapsed)
                        break
                    ability_path.append(f"AUTO D: {round(damage_dealt, 1)} T: {round(time_elapsed, 1)} A: {adrenaline}")
                    if float(cycle_duration - time_elapsed) >= 0.6:
                        damage_dealt += round(50 * current_buff, 1)
                    else:
                        damage_dealt += round(float(50 * round(float((cycle_duration - time_elapsed) / 0.6), 1)) *
                                              current_buff, 1)
                    adrenaline += auto_adrenaline
                    time_elapsed += 0.6
                    if adrenaline > 100:
                        adrenaline = 100
                    # Will also manage cooldowns
                    current_buff = adjust_cooldowns(current_buff, adrenaline, (attack_speed_cooldowns[attack_speed] +
                                                                               0.6))
                else:
                    time_elapsed += 0.6
                    current_buff = adjust_cooldowns(current_buff, adrenaline, 0.6)
                time_elapsed = round(time_elapsed, 1)
    return damage_dealt


def setup_config() -> None:
    global start_adrenaline, gain, attack_speed, activate_bleeds, debilitating, my_abilities, auto_adrenaline, cycle_duration

    def compare(lines) -> bool:
        # configuration followed by line number
        correct_data: Dict[str, int] = {"Adrenaline": 2, "Gain": 3, "AttackSpeed": 4, "Bleeds": 5, "Stuns": 6,
                                        "Abilities": 7, "Style": 8, "Time": 9, "units": 13}
        for setting in correct_data:
            if setting != lines[correct_data[setting]]:
                return False
        return True

    def validate(configurations) -> List[str]:
        error_log: List[str] = []
        empty_field: bool = False
        for config in configurations:
            if config == "":
                empty_field = True
        if empty_field is True:
            error_log.append("One or more settings have been left empty.")

        try:
            setting: int = int(configurations[0])
            if not (0 <= setting <= 100):
                error_log.append("Adrenaline must be between 0 and 100 inclusive.")
        except ValueError:
            error_log.append("Adrenaline must be an integer.")

        try:
            setting: int = int(configurations[1])
            if not (0 <= setting <= 100):
                error_log.append("Gain must be a positive integer between 0 and 100 inclusive.")
        except ValueError:
            error_log.append("Gain must be an integer.")

        if configurations[2].upper() not in ("SLOWEST", "SLOW", "AVERAGE", "FAST", "FASTEST"):
            error_log.append("AttackSpeed must either be one of the following options: ('slowest, slow, average, fast,"
                             " fastest').")

        setting: str = configurations[3]
        if not ((setting.lower() == "false") or (setting.lower() == "true")):
            error_log.append("Bleeds must be true or false.")

        setting: str = configurations[4]
        if not ((setting.lower() == "false") or (setting.lower() == "true")):
            error_log.append("Stuns must be true or false.")

        setting: str = configurations[5]
        if setting[0] == "[" and setting[-1] == "]":
            setting = setting[1:-1].split(",")
            counter: Dict[str, int] = {}
            if len(setting) > 0:
                for ability in setting:
                    ability = ability.upper().strip()
                    if (ability not in abilities) and (ability not in counter):
                        error_log.append(f"{ability.strip()} is not a recognised ability, or is not included in this "
                                         f"calculator.")
                    if ability in counter:
                        counter[ability] += 1
                        if counter[ability] == 2:
                            error_log.append(f"{(ability.strip())} is referenced 2 or more times within array. Ensure "
                                             f"it is only referenced once.")
                    else:
                        counter[ability] = 1
            else:
                error_log.append("No abilities were added")
        else:
            error_log.append("Abilities must be surrounded by square brackets [], and separated by comma's (,).")

        setting: str = configurations[6]
        if setting[0] == "(" and setting[-1] == ")":
            setting = setting[1:-1].split(",")
            if setting[0].upper() not in ("MAGIC", "RANGED", "MELEE"):
                error_log.append("First style option must be 'magic', 'ranged' or 'melee' (without quotes).")
            if setting[1] not in ("1", "2"):
                error_log.append("Second style option must be 1 or 2 (for 1 handed / 2 handed weapon)3")
        else:
            error_log.append("Style must start and end with round brackets (), with each option separated by a single "
                             "comma (,).")

        try:
            setting: float = float(configurations[7])
            if not (setting > 0):
                error_log.append("Time must be a number greater than zero.")
        except ValueError:
            error_log.append("Time must be a number.")

        if configurations[8].upper() not in ("SECONDS", "TICKS"):
            error_log.append("Units must be either 'seconds' or 'ticks' (without quotes).")

        return error_log

    def repair_config_file() -> None:
        repair: str = input("config.txt has been modified, perform repair? (Y/N).\n>> ").upper()
        if (repair == "Y") or (repair == "YES"):
            import os
            correct_data: List[str] = ["# Rotation Parameters", "", "Adrenaline: ", "Gain: ", "AttackSpeed: ",
                                       "Bleeds: ", "Stuns: ", "Abilities: [,,,]", "Style: (,)", "Time: ", "", "# Mode",
                                       "", "units: seconds"]
            if os.path.exists("config.txt"):
                os.remove("config.txt")
            with open("config.txt", "w") as settings:
                for line in correct_data:
                    settings.write(line + str("\n"))
            input("Repair successful! fill out settings in config.txt before running calculator again. "
                  "Press enter to exit.\n>> ")
        sys.exit()

    # --- Gets data for setup  --- #
    filedata: List[str] = []
    configurations: List[str] = []
    try:
        with open("config.txt", "r") as settings:
            for line in settings:
                filedata.append(line.split(":")[0])
                if ":" in line:
                    configurations.append(line.split(":")[1].strip())
        if compare(filedata) is False:
            repair_config_file()
    except:
        repair_config_file()
    error_log = validate(configurations)
    if len(error_log) > 0:
        print("Errors were found!!!\n")
        for error in error_log:
            print(error)
        input("\nCould not complete setup, please change fields accordingly and run the calculator again. "
              "Press enter to exit.\n>> ")
        sys.exit()
    start_adrenaline = int(configurations[0])
    gain = int(configurations[1])
    attack_speed = configurations[2].upper()
    activate_bleeds = configurations[3]
    bound: str = configurations[4]
    if bound == "False":
        debilitating = []
    my_abilities = []
    for ability in configurations[5][1:-1].split(","):
        my_abilities.append(ability.strip().upper())
    # --- Different styles of combat tree give varying amounts of adrenaline from auto attacks --- #
    style: Tuple[str, str] = tuple(configurations[6][1:-1].split(","))
    if style[0] == "MAGIC":
        auto_adrenaline = 2
    else:
        if style[1] != "2":
            auto_adrenaline = 2
        else:
            auto_adrenaline = 3
    cycle_duration = float(configurations[7])
    units: str = configurations[8]
    if units == "ticks":
        cycle_duration *= 0.6


def main() -> None:
    global basic_ability_list, threshold_ability_list, ultimate_ability_list, track_cooldown, track_buff, ability_path, ability_ready

    # Converts raw seconds into Years, Weeks, etc...
    def get_time(seconds: int) -> str:
        years: int = int(seconds / 31449600)
        seconds -= years * 31449600
        weeks: int = int(seconds / 604800)
        seconds -= weeks * 604800
        days: int = int(seconds / 86400)
        seconds -= days * 86400
        hours: int = int(seconds / 3600)
        seconds -= hours * 3600
        minutes: int = int(seconds / 60)
        seconds -= minutes * 60
        eta: str = f"{years} years, {weeks} weeks, {days} days, {hours} hours, {minutes} minutes and {seconds} seconds."
        return eta

    # Removes abilities from lists and dictionaries not being used to save runtime and memory
    def remove() -> Dict[str, bool]:
        for ability in abilities:
            if not (ability in my_abilities):
                del ability_damage[ability]
                del ability_cooldown[ability]
                del ability_type[ability]
                del ability_time[ability]
                del ability_ready[ability]
                if ability in walking_bleeds:
                    del walking_bleeds[ability]
                if ability in bleeds:
                    del bleeds[ability]
                if ability in buff_time:
                    del buff_time[ability]
                if ability in buff_effect:
                    del buff_effect[ability]
                if ability in punishing:
                    punishing.remove(ability)
                if ability in debilitating:
                    debilitating.remove(ability)
                if ability in crit_boost:
                    crit_boost.remove(ability)
                if ability in special_bleeds:
                    special_bleeds.remove(ability)
                if ability in special_abilities:
                    special_abilities.remove(ability)
                if ability in aoe:
                    aoe.remove(ability)
        return dict(ability_ready)

    setup_config()
    # --- Dictionaries, lists and other data types laid out here --- #
    print("Starting process ...")
    copy_of_ready = remove()
    basic_ability_list = [a for a in ability_type if ability_type[a] == "B"]
    threshold_ability_list = [a for a in ability_type if ability_type[a] == "T"]
    ultimate_ability_list = [a for a in ability_type if ability_type[a] == "U"]
    track_cooldown = {}
    track_buff = {}
    ability_path = []
    best_rotation: List[str] = []
    worst_rotation: List[str] = []
    # --- Calculations for estimation of time remaining --- #
    permutation_count: int = math.factorial(len(my_abilities))
    time_remaining_calculation: int = permutation_count / 10000
    runthrough: int = 0
    # --- Tracking of highest and lowest damaging ability bars  --- #
    current_highest: float = 0
    current_lowest: float = float("inf")
    # Define the amount of targets affected by area of effect attacks
    aoe_average_targets_hit: float = 2.5
    # --- Gets rotation length --- #
    while True:
        try:
            if len(aoe) > 0:  # Only ask if AoE abilities are in my_abilities
                aoe_average_targets_hit = float(input("How many targets on average will your AoE abilities hit? "))
                if aoe_average_targets_hit < 1:
                    print("Area of effect abilities should hit at least 1 target per use.")
                    continue
            break
        except:
            print("Invalid Input.")
    if aoe_average_targets_hit > 1:
        for ability in my_abilities:
            if ability in aoe:
                ability_damage[ability] = ability_damage[ability] * aoe_average_targets_hit
    print("Startup Complete! Warning, the more the abilities, and the higher the cycle time, the more time it will take"
          " to process. A better processor will improve this speed.")
    choice: str = input("Start Calculations? (Y/N) ").upper()
    if (choice != "Y") and (choice != "YES"):
        sys.exit()
    # --- Calculations start here --- #
    start: int = int(time.time())  # Record time since epoch (UTC) (in seconds)
    try:  # Will keep running until Control C (or other) is pressed to end process
        for permutation in itertools.permutations(my_abilities):
            damage_dealt: float = ability_rotation(permutation)
            # --- Reset data ready for next ability bar to be tested
            # and check if any better/worse bars have been found --- #
            ability_ready = dict(copy_of_ready)
            track_cooldown = {}
            track_buff = {}
            if round(damage_dealt, 1) > current_highest:
                current_highest = round(damage_dealt, 1)
                best_rotation = []
                best_rotation = list(ability_path)
                best_bar: List[str] = list(permutation)
                print(f"New best bar with damage {current_highest}: {best_bar}")
            if round(damage_dealt, 1) < current_lowest:
                current_lowest = round(damage_dealt, 1)
                worst_rotation: List[str] = []
                worst_rotation: List[str] = list(ability_path)
                worst_bar = list(permutation)
            ability_path = []
            runthrough += 1
            # --- Time Remaining estimation calculations every 10,000 bars analysed --- #
            if runthrough == 10000:
                end_estimation = int(time_remaining_calculation * (time.time() - start))
            if runthrough % 10000 == 0:
                print(f"\r===== {round(float(runthrough / permutation_count) * 100, 3)}"
                      f"% ===== Estimated time remaining: {get_time(int(end_estimation - (time.time() - start)))}"
                      f"; Best found: {current_highest}%" + (" " * 22), end="")
                time_remaining_calculation -= 1
                end_estimation = int(time_remaining_calculation * (time.time() - start))
                start = time.time()
    except KeyboardInterrupt:
        print("\nProcess terminated!")
    # --- Display results --- #
    print(f"\n\nHighest ability damage: {current_highest}%")
    print(f"Best ability bar found: {best_bar}")
    print(f"{best_rotation}\n")
    print(f"Lowest ability damage: {current_lowest}%")
    print(f"Worst ability bar found: {worst_bar}")
    print(worst_rotation)
    input("\nPress enter to exit\n")


# Execute main() function
if __name__ == "__main__":
    main()
