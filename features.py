""" Module for various features handling."""

from helper import *
from coords import *
import time


class BasicTraining:
    @staticmethod
    def basicTraining():
        click(*BASIC_TRAINING)
        click(*BASIC_TRAINING_ADD, button="right")  # training auto advance
        # click(*ATK1)
        # click(*DEF1)
        # click(*ATK2)
        # click(*DEF2)
        # click(*ATK3)
        # click(*DEF3)
        # click(*ATK4)
        # click(*DEF4)
        # click(*DEF5)
        # click(*ATK5)


class FightBosses:
    @staticmethod
    def fightBosses():
        click(*FIGHT_BOSS)
        click(*NUKE)
        for _ in range(5):  # wait for boss to die
            pyautogui.sleep(2)
            click(*FIGHT)


class Adventure:
    zones = {'safe': 0,
             'tutorial': 1,
             'sewers': 2,
             'forest': 3,
             'cave': 4,
             'sky': 5,
             'hsb': 6,
             'grb': 7,
             'clock': 8,
             'gct': 9,
             '2d': 10}

    @staticmethod
    def turnIdleOn():
        if (not Adventure.isIdle()):
            pyautogui.press('q')

    @staticmethod
    def turnIdleOff():
        if (Adventure.isIdle()):
            pyautogui.press('q')

    @staticmethod
    def showZones():
        z = ""
        for zone in Adventure.zones:
            z += zone + " "
        print(z)

    @staticmethod
    def isIdle():
        pix = getCoords(*IS_IDLE)
        return pyautogui.pixelMatchesColor(*pix, IS_IDLE_COLOR)

    @staticmethod
    def itopodFarm(floor='optimal'):
        click(*ADVENTURE)
        click(*ITOPOD_ENTER)
        if floor == 'optimal':
            click(*ITOPOD_OPTIMAL)
        else:
            click(*ITOPOD_START_INPUT)
            pyautogui.write(floor, interval=0.2)
            click(*ITOPOD_END_INPUT)
            pyautogui.write(floor, interval=0.2)
        click(*ITOPOD_ENTER_CONFIRMATION)

    @staticmethod
    def itopodPush(floor='200'):
        """floor is a string representing the floor number"""
        click(*ADVENTURE)
        click(*ITOPOD_ENTER)
        click(*ITOPOD_MAX)
        click(*ITOPOD_END_INPUT)
        pyautogui.write(floor, interval=0.2)
        click(*ITOPOD_ENTER_CONFIRMATION)

    @staticmethod
    def adventureZone(zone='latest'):
        click(*ADVENTURE)
        click(*GO_BACK_ZONE, button="right")   # start at 0
        if zone == 'latest':
            click(*ADVANCE_ZONE, button="right")
        else:
            times = Adventure.zones[zone]
            for _ in range(times):
                click(*ADVANCE_ZONE)

    @staticmethod
    def sendAttacks():
        pyautogui.press('y')
        pyautogui.press('t')
        # pyautogui.press('r')
        pyautogui.press('e')
        pyautogui.press('w')

    @staticmethod
    def killTitan():  # for grb currently
        """ go to lastest titan and attempts to kill it """
        click(*ADVENTURE)
        click(*ADVANCE_ZONE, button="right")
        click(*ADVANCE_ZONE)
        # pyautogui.press('q')
        Adventure.turnIdleOff()
        # grb health bar color is not red
        enemy_hp = getCoords(*ENEMY_HEALTH_BAR)
        sleep(6)
        if not pyautogui.pixelMatchesColor(*enemy_hp, (255, 255, 255)):
            print('titan spawned')
            start = time.time()
            while not Adventure.isEnemyDead() or (time.time() - start)/60 < 3:
                Adventure.sendAttacks()
                sleep(0.1)
        # pyautogui.press('q')
        Adventure.turnIdleOn()

    @staticmethod
    def killMonsters(zone='latest', bossOnly=False, kills=20):
        """ kills {kills} monsters in {zone} and returns"""
        Adventure.adventureZone(zone)
        # pyautogui.press('q')  # idle mode
        Adventure.turnIdleOff()
        counter = 0
        currentZone = zone
        while True:
            if currentZone == 'safe':
                Adventure.adventureZone(zone)
                currentZone = zone
            # print('checking spawn')
            if Adventure.enemySpawn():
                # print('spawned')
                if (not bossOnly):
                    Adventure.kill()
                    if Adventure.isPlayerLow():
                        Adventure.healHP()
                        currentZone = 'safe'
                    counter += 1
                    sleep(1)
                    pyautogui.press('d')  # heal
                else:
                    if Adventure.isBoss():
                        Adventure.kill()
                        if (Adventure.isPlayerLow()):
                            Adventure.healHP()
                            currentZone = 'safe'
                        counter += 1
                        sleep(1)
                        pyautogui.press('d')  # heal
                    else:
                        Adventure.refreshZone()
            else:
                sleep(0.1)  # wait a little
            if (counter > 0 and counter % kills == 0):
                # pyautogui.press('q')  # after 15 fights
                Adventure.turnIdleOn()
                return

    @staticmethod
    def kill():
        while not Adventure.isEnemyDead():
            Adventure.sendAttacks()
            sleep(0.1)
        # after this, player may be dead

    @staticmethod
    def isEnemyDead():
        border = getCoords(*ENEMY_HEALTH_BAR_BORDER)
        if (pyautogui.pixelMatchesColor(*border, (255, 255, 255))):
            # print('dead')
            return True
        else:
            return False
            # print('not dead')

    @staticmethod
    def isPlayerLow():
        border = getCoords(*MY_HEALTH_BAR)
        if (pyautogui.pixelMatchesColor(*border, (255, 255, 255))):
            return True
        else:
            return False

    @staticmethod
    def healHP():
        Adventure.adventureZone('safe')
        sleep(25)
        # click(*ADVANCE_ZONE, button="right")

    @staticmethod
    def enemySpawn():
        enemy_hp = getCoords(*ENEMY_HEALTH_BAR_BORDER)
        return pyautogui.pixelMatchesColor(*enemy_hp, HEALTH_BAR_RED)

    @staticmethod
    def reclaimEnergy():
        click(*BASIC_TRAINING)
        pyautogui.press('r')  # should reclaim energy

    @staticmethod
    def isBoss():
        # get the pixel of the crown
        # match it with yellow
        crown = getCoords(*CROWN_LOCATION)
        return pyautogui.pixelMatchesColor(*crown, CROWN_COLOR)

    @staticmethod
    def refreshZone():
        click(*GO_BACK_ZONE)
        click(*ADVANCE_ZONE)


class Augmentation:
    @staticmethod
    def augmentation(aug=1, upgrade=False):
        click(*AUGMENTATION)
        if upgrade:
            x, y = AUG1_UPGRADE[0], AUG1_UPGRADE[1] + (aug - 1) * AUG_DIFF
        else:
            x, y = AUG1[0], AUG1[1] + (aug - 1) * AUG_DIFF
        click(x, y)


class Inventory:
    @staticmethod
    def mergeItem(x, y):
        moveTo(x, y)
        sleep(0.1)
        pyautogui.press('d')

    @staticmethod
    def boostItem(x, y):
        moveTo(x, y)
        sleep(0.1)
        pyautogui.press('a')

    @staticmethod
    def boostAndMergeEquips():
        click(*INVENTORY)

        Inventory.mergeItem(*WEAPON)
        Inventory.boostItem(*WEAPON)
        Inventory.mergeItem(*ACC1)
        Inventory.boostItem(*ACC1)
        Inventory.mergeItem(*ACC2)
        Inventory.boostItem(*ACC2)
        Inventory.mergeItem(*ACC3)
        Inventory.boostItem(*ACC3)
        Inventory.mergeItem(*HEAD)
        Inventory.boostItem(*HEAD)
        Inventory.mergeItem(*CHEST)
        Inventory.boostItem(*CHEST)
        Inventory.mergeItem(*LEGS)
        Inventory.boostItem(*LEGS)
        Inventory.mergeItem(*BOOTS)
        Inventory.boostItem(*BOOTS)

        click(*CUBE, button="right")

        for col in range(3):
            for row in range(12):  # boost and merge front row
                x = SLOT1[0] + INV_DIFF * row
                y = SLOT1[1] + INV_DIFF * col
                Inventory.mergeItem(x, y)
                Inventory.boostItem(x, y)

          # boost infinity cube

    @staticmethod
    def trashItems():
        click(*INVENTORY)
        for col in range(3, 5):
            for row in range(12):
                x = SLOT1[0] + INV_DIFF * row
                y = SLOT1[1] + INV_DIFF * col
                Inventory.trashItem(x, y)

    @staticmethod
    def trashItem(x, y):
        moveTo(x, y)
        sleep(0.1)
        pyautogui.keyDown('ctrl')
        sleep(0.1)
        pyautogui.click()
        sleep(0.1)
        pyautogui.keyUp('ctrl')

    @staticmethod
    def transformPendants():
        locations = Inventory.locatePendants()
        for loc in locations:
            center = pyautogui.center(loc)
            rawMove(*center)  # show tooltip
            sleep(0.1)
            if Inventory.checkTransformable():
                ctrlClick()
                # print('control click')

    @staticmethod
    def locatePendants():
        region = (CORNER[0], CORNER[1], GAME_WIDTH, GAME_HEIGHT)
        locations = pyautogui.locateAllOnScreen('pendant.png', region=region)
        # for loc in locations:
        #     center = pyautogui.center(loc)
        #     rawMove(*center)
        return locations

    @staticmethod
    def transformItems():
        click(*INVENTORY)
        for col in range(2, 3):  # only one col
            for row in range(12):
                x = SLOT1[0] + INV_DIFF * row
                y = SLOT1[1] + INV_DIFF * col
                Inventory.transformItem(x, y)

    @staticmethod
    def checkTransformable():
        region = (CORNER[0], CORNER[1], GAME_WIDTH, GAME_HEIGHT)
        if pyautogui.locateOnScreen('transformable.png', region=region) != None:
            return True
        return False

    @staticmethod
    def transformItem(x, y):
        moveTo(x, y)
        sleep(0.3)
        # if transformable
        region = (CORNER[0], CORNER[1], GAME_WIDTH, GAME_HEIGHT)
        if pyautogui.locateOnScreen('transformable.png', region=region) != None:
            pyautogui.keyDown('ctrl')
            sleep(0.1)
            pyautogui.click()
            sleep(0.1)
            pyautogui.keyUp('ctrl')


class TimeMachine:
    @staticmethod
    def addEnergy():
        click(*TIME_MACHINE)
        click(*TM_ADD_ENERGY)
        click(CORNER[0], CORNER[1])

    @staticmethod
    def addMagic():
        click(*TIME_MACHINE)
        click(*TM_ADD_MAGIC)


class BloodMagic:
    @staticmethod
    def addMagic(aug=1, cap=False):
        click(*BLOOD_MAGIC)
        if cap:
            x, y = BM1_CAP[0], BM1_CAP[1] + (aug - 1) * BM_DIFF
        else:
            x, y = BM1_ADD[0], BM1_ADD[1] + (aug - 1) * BM_DIFF
        click(x, y)


class MoneyPit:
    @staticmethod
    def moneyPit():
        click(*MONEY_PIT)
        click(*FEED_ME)
        click(*FEED_YEAH)


class Rebirth:
    @staticmethod
    def rebirth():
        click(*REBIRTH_MENU)
        sleep(5)  # to see if it's crashing
        click(*REBIRTH_BUTTON)
        click(*REBIRTH_CONFIRMATION)


class Yggdrasil:
    @staticmethod
    def harvestGold():
        click(*YGGDRASIL)
        click(*FRUIT_GOLD_HARVEST)
        click(*FRUIT_POWER_HARVEST)


class Misc:
    @staticmethod
    def reclaimEnergy():
        click(*BASIC_TRAINING)
        pyautogui.press('r')

    @staticmethod
    def reclaimMagic():
        click(*BASIC_TRAINING)
        pyautogui.press('t')

    @staticmethod
    def inputResource(amount='cap', idle=False):
        click(*BASIC_TRAINING)
        if amount == 'cap':
            click(*ENERGY_CUSTOM_AMOUNT_CAP)
        elif amount == 'half':
            if idle:
                click(*ENERGY_CUSTOM_AMOUNT_HALF_IDLE)
            else:
                click(*ENERGY_CUSTOM_AMOUNT_HALF)
