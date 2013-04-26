#! /usr/bin/env python
#coding=utf-8
import sys
from MysqlSaber_col import printWait,printError,printResult

def Sknight():
    printWait('''
        #######################################################
        #                                                     #
        #           Mysql Saber ---- SQL Knight               #
        #               BY haxsscker#f4ck.net                 #
        #                                                     #
        #######################################################
    ''')

def Ssql(sword,sql):
    try:
        sword.execute(sql)
        query = sword.fetchall()
        for i in query:
            for j in i:
                print str(j)+"\n"
    except Exception,e:
        printError(e)
        printError("[+Saber+]===> Hey boy, the SQL is wrong!")
    else:
        printResult("[+Saber+]===> DONE! ")
        

def main(sword):
    sql = ''
    while sql != 'q':
        sql = raw_input("enter your SQL here/(press q to exit): ")
        if sql != 'q':  
            Ssql(sword,sql)
    printWait("[+Saber+]===> Quit sql and use other function? ")
    scontinue = 'y'
    scontinue = raw_input("continue?(y/n): y?")
    if scontinue == 'n':
        sword.close()
        sys.exit()
