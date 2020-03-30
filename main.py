from scripts import *
import time


def main():
    print('starting the script')
    print('check if adventure is in Idle mode!')
    print('1 - speedrun')
    print('2 - farming')
    choice = input()
    if choice == '1':
        print('speedrun script')
        scriptStart = time.time()
        counter = 0
        while True:
            runStart = time.time()
            print('*' * 10)
            run15()
            runEnd = time.time()
            print(f'rebirth {counter} time: {round((runEnd - runStart)/60)}')
            counter += 1
            print()
    elif choice == '2':
        print('farming script')
        print('boss only? (y/n)')
        choice = input()
        print('which zone would you like to farm')
        zones = ""
        for z in Adventure.zones.keys():
            zones += z + " "
        print(zones)
        zone = input()
        if choice == "y":
            while True:
                Adventure.killMonsters(zone=zone, bossOnly=True)
        else:
            while True:
                Adventure.killMonsters(zone=zone)


if __name__ == "__main__":
    main()
