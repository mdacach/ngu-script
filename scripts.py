from helper import *
from coords import *
from features import *
import time


def run15():
    start = time.time()
    sleep(10)  # wait for energy to all trainings
    BasicTraining.basicTraining()
    FightBosses.fightBosses()
    Adventure.adventureZone()
    # basic loop
    counter = 0
    timeElapsed = time.time() - start
    while ((timeElapsed)/60 < 13):  # until 13 minutes
        Misc.inputResource(amount='half', idle=True)
        TimeMachine.addEnergy()
        Augmentation.augmentation()
        FightBosses.fightBosses()
        BloodMagic.addMagic()
        Adventure.killMonsters(kills=20)
        Inventory.boostAndMergeEquips()
        timeElapsed = time.time() - start
        counter += 1
    Misc.reclaimEnergy()
    Misc.inputResource()
    Augmentation.augmentation(upgrade=True)
    Adventure.adventureZone()
    FightBosses.fightBosses()
    MoneyPit.moneyPit()
    timeElapsed = time.time() - start
    while (timeElapsed/60 < 15):
        pyautogui.sleep(2)
    Rebirth.rebirth()


def farmAdventure():
    print('farming script')
    print('which zone: ')
    zones = ""
    for z in Adventure.zones.keys():
        zones += z + "  "
    print(zones)
    zone = input()
    print('would you like to kil only bosses? (y/n)')
    boss = input()
    print('would you like to kill GRB? (y/n)')
    titan = input()
    counter = 0
    start = time.time()
    while True:
        if boss == 'y':
            Adventure.killMonsters(zone=zone, bossOnly=True)
        else:
            Adventure.killMonsters(zone=zone)
        counter += 20
        Inventory.boostAndMergeEquips()
        if titan == 'y':
            Adventure.killTitan()
        MoneyPit.moneyPit()
        print(f'killed {counter} monsters')
        print(f'{round((time.time() - start)/60)}min elapsed')
        print()
