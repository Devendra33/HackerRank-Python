# to insert data and manipulate it.
from os import path
from colorama import Fore, Back
from sys import exit
from mmap import *   # find function is important.
from re import *
while True:
    if path.isfile('bfile.dat'):
        print(Fore.GREEN + 'FILE FOUND SUCCESSFULLY!' + Fore.RESET)
        with open('bfile.dat', 'a+b') as f:
            def ins():
                f.seek(0)
                rownum = len(f.readlines()) + 1
                f.seek(0, 2)
                flag = True
                n1 = 0
                while flag:
                    try:
                        n1 = int(input('enter the number of records: '))
                        flag = False
                    except ValueError:
                        print('please enter integer value.')

                for _ in range(n1):
                    sap1 = ''
                    rep = 1
                    while len(sap1) != 9 and rep != 0:
                        sap1 = input('enter sapid?(9 digits) : ')
                        f.seek(0)
                        check = f.read().splitlines()
                        for k in range(len(check)):
                            if sap1 == check[k][-1:-10:-1][::-1].decode():
                                print(Fore.RED + 'Sap id already exists\nplease Re-enter sapid...' + Fore.RESET)
                                if len(sap1) == 9:
                                    sap1 = ''
                                break
                        else:
                            if len(sap1) == 9:
                                rep = 0
                            else:
                                rep = 1

                    name = ''
                    while name == '':
                        name = input('Enter name? ').title()
                    ph = ''
                    while len(ph) != 10:
                        ph = input('phone number?(10 digits): +91- ')

                    f.seek(0, 2)
                    comb = str(rownum)+' ' + name.rjust(25, ' ') + ph + sap1
                    rownum += 1
                    f.write(comb.encode() + b'\n')
                    print('successfully inserted...\n')

            f.seek(0)

            while True:
                print(Back.LIGHTBLACK_EX + Fore.LIGHTCYAN_EX + 'Manipulation Menu:' + Fore.RESET + Back.RESET)
                print(Fore.LIGHTCYAN_EX + '~' + Fore.RESET + 'press 0 to EXIT()')
                print(Fore.LIGHTCYAN_EX + '~' + Fore.RESET + 'press 1 to VIEW whole file.')
                print(Fore.LIGHTCYAN_EX + '~' + Fore.RESET + 'press 2 to INSERT record.')
                print(Fore.LIGHTCYAN_EX + '~' + Fore.RESET + 'press 3 to SEARCH a record.')
                print(Fore.LIGHTCYAN_EX + '~' + Fore.RESET + 'press 4 to CHANGE MobNo.')
                fun = input(Fore.LIGHTBLUE_EX+'Please Enter choice: '+Fore.RESET)

                if fun == '0':
                    exit('Program Terminated...')

                elif fun == '1':
                    f.seek(0)
                    print(Back.LIGHTBLACK_EX+Fore.LIGHTCYAN_EX+'File contents'+Fore.RESET+Back.RESET)
                    print('ROW       NAME                  PHONE NUM        SAP')
                    lst = f.read().splitlines()

                    for i in range(len(lst)):
                        j = lst[i].decode()
                        find_name = findall('\D{0,}', j)
                        find_n = find_name[1].lstrip().rstrip()
                        name_len = 25 - len(find_n)
                        print(f'{j[0:len(str(i))]}\t\t{find_n}', end=' ' * name_len)
                        print(f'{j[-10:-20:-1][::-1]}\t\t{j[-1:-10:-1][::-1]}')
                    print()

                elif fun == '2':
                    ins()

                elif fun == '3':
                    m = mmap(f.fileno(), 0)
                    sap = input('Enter sap to be searched: ').encode()
                    print()
                    ind = m.find(sap)
                    ph_ind = ind - 10
                    print(Fore.LIGHTCYAN_EX + 'phone_no:' + Fore.RESET, m[ph_ind: ind].decode())
                    res = search('\D*', m[ph_ind - 25: ph_ind].decode())
                    print(Fore.LIGHTCYAN_EX + 'Name :' + Fore.RESET, res.group().lstrip())
                    print()
                elif fun == '4':
                    m = mmap(f.fileno(), 0)
                    sap = ''
                    while len(sap) != 9:
                        sap = input('Enter sapid:(9 digits) ')

                    sap_ind = m.find(sap.encode())
                    if sap_ind != -1:
                        newnum = ''
                        while len(newnum) != 10:
                            newnum = input('Enter New Number:(10 digits) ')

                        m[sap_ind - 10:sap_ind] = newnum.encode()
                        print(Fore.LIGHTGREEN_EX + 'Mobile Number updated Successfully' + Fore.RESET)
                    else:
                        print(Fore.LIGHTRED_EX + 'Sap does not found!!' + Fore.RESET)