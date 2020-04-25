""" Speedrun script with command line arguments. """

import argparse
import pyautogui
import time

import coords
from helper import click, sleep
from features import Adventure, Augmentation, BloodMagic, BasicTraining, FightBosses, Inventory, Misc, MoneyPit, Rebirth, TimeMachine
from navigation import Navigation
from statistics import Statistics

# commandline arguments
parser = argparse.ArgumentParser()
parser.add_argument('--duration', help='duration for the runs', default='10')
args = parser.parse_args()

print(f'called with arguments {args}')


def run3():
    """ Perform a 3 minute run. """
    start = time.time()
    Inventory.loadout(2)
    BasicTraining.basicTraining()
    FightBosses.nuke()
    Adventure.adventureZone()

    Misc.inputResource()

    print(f'TM loop (1:30 min)')
    inv1 = False
    lastZone = False
    while time.time() - start < 90:
        TimeMachine.addEnergy()
        TimeMachine.addMagic()
        if time.time() - start > 60 and not inv1:
            Inventory.loadout(1)
            BasicTraining.basicTraining()
            inv1 = True
            if not lastZone:
                Adventure.adventureZone()
                lastZone = True
        print(f'sleeping for 5 sec')
        # sleep(15)
        sleep(5)

    Misc.reclaimAll()

    print(f'Main loop (1:30 min)')
    pushAdventure = False
    while time.time() - start < 170:
        Misc.inputResource(amount='quarter', idle=True)
        for _ in range(3):
            Augmentation.augmentation()
        Augmentation.augmentation(upgrade=True)

        BloodMagic.addMagic(magic=1, cap=True)
        BloodMagic.addMagic(magic=2, cap=True)
        BloodMagic.addMagic(magic=3, cap=True)

        if not pushAdventure and time.time() - start > 120:
            Adventure.adventureZone()
            pushAdventure = True
        FightBosses.nuke()

    MoneyPit.moneyPit()
    FightBosses.nuke()
    FightBosses.fightBoss()
    # Navigation.menu('rebirth')
    print('waiting for time')
    # Statistics.screenshot('rebirth.png')
    while time.time() - start < 180:
        sleep(1)
    click(*coords.STOP)  # stop fighting
    Navigation.menu('rebirth')
    Rebirth.rebirth()


def run5():
    """ Perform a 5 minute run."""
    start = time.time()
    Inventory.loadout(2)  # loadout 2 is bars-heavy
    BasicTraining.basicTraining()
    Adventure.nuke()
    sleep(3)
    Adventure.adventureZone()  # go to latest zone

    Misc.inputResource()  # all energy

    print(f'Time Machine loop for 2:30 minutes')
    inv1 = False
    lastZone = False
    loopCounter = 0
    while time.time() - start < 150:
        loopCounter += 1
        TimeMachine.addEnergy()
        TimeMachine.addMagic()
        if time.time() - start > 120 and not inv1:
            Inventory.loadout(1)
            BasicTraining.basicTraining()
            inv1 = True
        if loopCounter == 10:
            Adventure.itopodFarm()
        # if not lastZone:
        #     Adventure.adventureZone()
        #     lastZone = True

    Misc.reclaimAll()  # reclaim energy and magic from TM

    print(f'Main loop until 5 minutes')
    mainStart = time.time()
    pushAdventure = False
    loopCounter = 0
    while time.time() - start < 280:
        loopCounter += 1
        # push to new adventure zone
        # if time.time() - mainStart > 30 and not pushAdventure:
        #     Adventure.adventureZone()
        #     pushAdventure = True
        # fight bosses
        if loopCounter == 2:
            Adventure.itopodFarm()

        FightBosses.nuke()
        for _ in range(5):
            FightBosses.fightBoss()
        # augments
        Misc.inputResource(amount='quarter', idle=True)
        for _ in range(3):
            Augmentation.augmentation(aug=1)
        Augmentation.augmentation(aug=1, upgrade=True)
        # blood magic
        BloodMagic.addMagic(cap=True)
        BloodMagic.addMagic(magic=2, cap=True)
        BloodMagic.addMagic(magic=3, cap=True)
        print(f'sleeping 15 seconds')
        sleep(15)

    MoneyPit.moneyPit()
    FightBosses.nuke()
    FightBosses.fightBoss()
    print('waiting for time')
    # Statistics.screenshot('rebirth.png')
    while time.time() - start < 300:
        sleep(1)
    click(*coords.STOP)  # stop fighting bosses
    Navigation.menu('rebirth')
    Rebirth.rebirth()


def run7():
    """ Perform a 7 minute run."""
    start = time.time()
    Inventory.loadout(2)  # loadout 2 is bars-heavy
    BasicTraining.basicTraining()
    FightBosses.fightBosses()
    Adventure.adventureZone()  # go to latest zone

    Misc.inputResource()  # all energy

    print(f'Time Machine loop for 4 minutes')
    inv1 = False
    lastZone = False
    while time.time() - start < 180:
        TimeMachine.addEnergy()
        TimeMachine.addMagic()
        if time.time() - start > 180 and not inv1:
            Inventory.loadout(1)
            BasicTraining.basicTraining()
            inv1 = True
        if not lastZone:
            Adventure.adventureZone()
            lastZone = True
        startTime = time.time()

    Misc.reclaimAll()  # reclaim energy and magic from TM

    print(f'Main loop until 7 minutes')
    mainStart = time.time()
    pushAdventure = False
    while time.time() - start < 390:
        # push to new adventure zone
        if time.time() - mainStart > 120 and not pushAdventure:
            Adventure.adventureZone()
            pushAdventure = True
        # fight bosses
        FightBosses.nuke()
        for _ in range(5):
            FightBosses.fightBoss()
        # augments
        Misc.inputResource(amount='quarter', idle=True)
        for _ in range(3):
            Augmentation.augmentation(aug=2)
        Augmentation.augmentation(aug=2, upgrade=True)
        # blood magic
        BloodMagic.addMagic(cap=True)
        BloodMagic.addMagic(magic=2, cap=True)
        BloodMagic.addMagic(magic=3, cap=True)
        print(f'sleeping 30 seconds')
        sleep(30)

    MoneyPit.moneyPit()
    FightBosses.nuke()
    FightBosses.fightBoss()
    print('waiting for time')
    # Statistics.screenshot('rebirth.png')
    while time.time() - start < 420:
        sleep(1)
    click(*coords.STOP)  # stop fighting
    Navigation.menu('rebirth')
    Rebirth.rebirth()


def run10():
    """ Perform a 10 minute run. """
    start = time.time()
    Inventory.loadout(2)  # loadout 2 is bars-heavy
    BasicTraining.basicTraining()
    FightBosses.fightBosses()
    Adventure.adventureZone()  # go to latest zone

    Misc.inputResource()  # all energy

    print(f'Time Machine loop for 5 minutes')
    while time.time() - start < 300:
        TimeMachine.addEnergy()
        TimeMachine.addMagic()
        print(f'sleeping for 30 seconds')
        sleep(30)

    Inventory.loadout(1)
    BasicTraining.basicTraining()

    Misc.reclaimAll()  # reclaim energy and magic from TM

    print(f'Main loop until 10 minutes')
    mainStart = time.time()
    pushAdventure = False
    while time.time() - start < 570:
        # push to new adventure zone
        if time.time() - mainStart > 120 and not pushAdventure:
            Adventure.adventureZone()
            pushAdventure = True
        print(f'sleeping 30 seconds')
        sleep(30)
        # fight bosses
        FightBosses.nuke()
        for _ in range(5):
            FightBosses.fightBoss()
        # augments
        Misc.inputResource(amount='quarter', idle=True)
        for _ in range(3):
            Augmentation.augmentation()
        Augmentation.augmentation(upgrade=True)
        # blood magic
        BloodMagic.addMagic(cap=True)

    MoneyPit.moneyPit()
    Navigation.menu('rebirth')
    while time.time() - start < 600:
        sleep(1)
    Rebirth.rebirth()


if __name__ == "__main__":
    print()
    print(f'{args.duration} minutes run')

    runCounter = 0
    previousExp = Statistics.getEXP()
    print(f'exp before: {previousExp}')
    start = time.time()
    while True:
        print('*' * 15)
        runCounter += 1
        print(f'run {runCounter}')
        if args.duration == '10':
            run10()
        elif args.duration == '7':
            run7()
        elif args.duration == '5':
            run5()
        elif args.duration == '3':
            run3()
        currentExp = Statistics.getEXP()
        print(f'exp: {currentExp}')
        print(f'run exp: {currentExp - previousExp}')
        previousExp = currentExp
        print('*' * 15)
        print(f'total time: {round((time.time() - start)/60)} minutes')
