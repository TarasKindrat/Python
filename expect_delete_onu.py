#!/usr/bin/python3
# -*- coding: utf-8 -*-.
import time
import pexpect
import subprocess
import sys


def ping(ip):
    """
    Функція повертає 0, якщо пінг до IP іде, 1 - якщо пінга нема
    """
    import os, platform
    # Ping parameters as function of OS
    ping_str = "-n 1 " if platform.system().lower() == "windows" else "-c 1 "
    # Ping
    return subprocess.call(["ping", "-w 1", ping_str, ip], stdout=subprocess.PIPE)


def get_mac(ip, SN_MAC, login, passwd, xpon, shell):
    """
    ip - IP address of OLT
    SN_MAC - mac or serial number ONT
    shell - command prompt on OLT
    login - Login on OLT
    passwd - Password on OLT
    xpon - gpon or epon
    """
    if xpon == 'gpon':
        if shell == 'MA5680T' or shell == 'MA5683T' or shell == 'MA5608T':
            try:
                var = pexpect.spawn('telnet ' + ip, timeout=10)
                var.expect('User name:')
                var.sendline(login)
                var.expect('User password:')
                var.sendline(passwd)
                var.expect('>')
                var.sendline('enable')
                var.expect('#')
                var.sendline('display ont info by-sn ' + SN_MAC)
                time.sleep(1)
                var.sendline('Q')
                var.expect('#')
                out = var.before.decode('UTF-8')
                print(out)
                if 'does not exist' in out:
                    print("OLT does not find onu")
                    exit(1)
                elif 'F/S/P' in out:
                    print('Onu exist')
                    lines = out.split('\n')
                    for line in lines:
                        # print(line)
                        if 'F/S/P' in line:
                            second_part = line.split(':')[1]
                            INTERFACE = (second_part.split('/')[0]).strip(' ') + '/' + second_part.split('/')[1]
                            PORT = second_part.split('/')[2]
                        if 'ONT-ID' in line:
                            second_part = line.split(':')[1]
                            ONT_ID = (second_part.split('/')[0]).strip(' ')
                    print('Interface', INTERFACE)
                    print('Port', PORT)
                    print('ONT-ID', ONT_ID)
                    if INTERFACE and PORT:
                        var.sendline('config')
                        var.expect('#')
                        var.sendline(f"interface gpon {INTERFACE}")
                        var.expect('#')
                        out = var.before.decode('UTF-8')
                        print(out)
                        # Delete ONT
                        var.sendline(f"Ont del {PORT}{ONT_ID}")
                        var.expect('#')
                        var.sendline('quit')
                        var.expect('#')
                        var.sendline('quit')
                        var.expect('#')
                        var.sendline('quit')
                        var.expect(':')
                        var.sendline('y')
                        print("Done")
                        exit(0)
            except pexpect.TIMEOUT:
                print(pexpect.TIMEOUT)

        elif shell == 'MA5800-X7' or shell == 'MA5800-X2':
            try:
                var = pexpect.spawn('telnet ' + ip, timeout=10)
                var.expect('User name:')
                var.sendline(login)
                var.expect('User password:')
                var.sendline(passwd)
                var.expect('>')
                var.sendline('enable')
                var.expect('#')
                var.sendline('display ont info by-sn ' + SN_MAC)
                out = var.before.decode('UTF-8')
                print(out)
                var.expect(':')
                var.sendline()
                time.sleep(3)
                var.sendline('Q')
                var.expect('#')
                out = var.before.decode('UTF-8')
                print(out)
                if 'does not exist' in out:
                    print("OLT does not find onu")
                    exit(1)
                elif 'F/S/P' in out:
                    print('Onu exist:')
                    lines = out.split('\n')
                    for line in lines:
                        if 'F/S/P' in line:
                            Second_part = line.split(':')[1]
                            INTERFACE = (Second_part.split('/')[0]).strip(' ') + '/' + Second_part.split('/')[1]
                            PORT = Second_part.split('/')[2]
                        if 'ONT-ID' in line:
                            Second_part = line.split(':')[1]
                            ONT_ID = (Second_part.split('/')[0]).strip(' ')
                    print('Interface', INTERFACE)
                    print('Port', PORT)
                    print('ONT-ID', ONT_ID)
                    if INTERFACE and PORT:
                        var.sendline('config')
                        var.expect('#')
                        var.sendline(f"interface gpon {INTERFACE}")
                        var.expect('#')
                        out = var.before.decode('UTF-8')
                        print(out)
                        # Delete ONT
                        var.sendline(f"Ont del {PORT}{ONT_ID}")
                        var.expect('#')
                        out = var.before.decode('UTF-8')
                        print(out)
                        var.sendline('quit')
                        var.expect('#')
                        var.sendline('quit')
                        var.expect('#')
                        var.sendline('quit')
                        var.expect(':')
                        var.sendline('y')
                        print("Done")
                        exit(0)
            except pexpect.TIMEOUT:
                print("something wrong")
        else:
            print('There ara no anything')
    elif xpon == 'epon':
        if shell == 'MA5680T' or shell == 'MA5683T' or shell == 'MA5608T':
            try:
                var = pexpect.spawn('telnet ' + ip, timeout=10)
                var.expect('User name:')
                var.sendline(login)
                var.expect('User password:')
                var.sendline(passwd)
                var.expect('>')
                var.sendline('enable')
                var.expect('#')
                var.sendline('display ont info by-mac ' + SN_MAC)
                time.sleep(1)
                out = var.before.decode('UTF-8')
                print("out is here:", out)
                # if 'F/S/P' in out_str:
                #     var.sendline('q')
                var.sendline('q')
                var.expect('#')
                out = var.before.decode('UTF-8')
                print(out)
                if 'does not exist' in out:
                    print("OLT does not find onu")
                    exit(1)
                elif 'F/S/P' in out:
                    print('Onu exist')
                    lines = out.split('\n')
                    for line in lines:
                        # print(line)
                        if 'F/S/P' in line:
                            second_part = line.split(':')[1]
                            INTERFACE = (second_part.split('/')[0]).strip(' ') + '/' + second_part.split('/')[1]
                            PORT = second_part.split('/')[2]
                        if 'ONT-ID' in line:
                            second_part = line.split(':')[1]
                            ONT_ID = (second_part.split('/')[0]).strip(' ')
                    print('Interface', INTERFACE)
                    print('Port', PORT)
                    print('ONT-ID', ONT_ID)
                    if INTERFACE and PORT:
                        var.sendline('config')
                        var.expect('#')
                        var.sendline(f"interface epon {INTERFACE}")
                        var.expect('#')
                        out = var.before.decode('UTF-8')
                        print(out)
                        # Delete ONT
                        var.sendline(f"Ont del {PORT}{ONT_ID}")
                        var.expect('#')
                        var.sendline('quit')
                        var.expect('#')
                        var.sendline('quit')
                        var.expect('#')
                        var.sendline('quit')
                        var.expect(':')
                        var.sendline('y')
                        print("Done")
                        exit(0)
            except pexpect.TIMEOUT:
                print("something wrong")
        else:
            print('There ara no anything')
    else:
        print('There ara no anything')

ip = str(sys.argv[1])
SN_MAC = str(sys.argv[2])
login = str(sys.argv[3])
passwd = str(sys.argv[4])

##ПЕРЕВІРКА ДОСТУПНОСТІ ПІНГОМ##

list__ip_of_olts_MA5800 = ['172.21.34.2', '172.19.24.2', '172.21.24.2', '172.21.0.2', '172.19.158.2', '172.19.12.2',
                           '172.19.16.2', '172.21.42.2', '172.19.154.200']
list__ip_of_olts_MA568XT = ['172.19.8.2', '172.21.22.100']
list__ip_of_olts_MA568XT_EPON = ['172.21.40.10']

if ping(ip) == 1:
    print('!!!Error!!!! OLT does not pinging')
else:
    if ip in list__ip_of_olts_MA5800:
        print(ip)
        xpon = 'gpon'
        shell = 'MA5800-X7'
        get_mac(ip, SN_MAC, login, passwd, xpon, shell)
    elif ip in list__ip_of_olts_MA568XT:
        print(ip)
        xpon = 'gpon'
        shell = 'MA5683T'
        get_mac(ip, SN_MAC, login, passwd, xpon, shell)
    elif ip in list__ip_of_olts_MA568XT_EPON:
        print(ip)
        xpon = 'epon'
        shell = 'MA5683T'
        get_mac(ip, SN_MAC, login, passwd, xpon, shell)
    else:
        print("Unknown IP")
