#Very Indivitual Tool
#Created By Jackel Contact @ Othernet #TopKek

import os, socket, sys, re, time, threading, logging

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

Banner = bcolors.OKGREEN+"""

###########################################################################
###"""+bcolors.FAIL+"""@@@@@@@@@@        @@@@@@@@@@@@@  @@@@@    @@@@ @@@@@@@@@  @@@@@    @@"""+bcolors.OKGREEN+"""###
##"""+bcolors.FAIL+"""@@@@@@@@@@@ @@@    @@@@@@    @@@@ @@@@@   @@@@@ @@@    @@@ @@@@@   @@@@"""+bcolors.OKGREEN+"""##
#    """+bcolors.FAIL+"""@@@@@ @@@@@@@@@ @@@@@@    @@@@ @@@@@  @@@@@ @@@@    @@@ @@@@@  @@@@  """+bcolors.OKGREEN+"""#
#    """+bcolors.FAIL+"""@@@@@@@      @@@@@@@@@@@@@@@@  @@@@@@@@@@@  @@@@ @@@    @@@@@@@@@@@  """+bcolors.OKGREEN+"""#
#    """+bcolors.FAIL+"""@@@@@         @@@@@@@@         @@@@@   @@@@@ @@@@     @ @@@@@   @@@  """+bcolors.OKGREEN+"""#
##   """+bcolors.FAIL+"""@@@@@@@      @@@ @@@@@         @@@@@     @@@@ @@@@@  @@@@@@@@    @@@"""+bcolors.OKGREEN+"""##
###  """+bcolors.FAIL+"""@@@@@ @@@@@@@@@  @@@@@         @@@@@      @@@  @@@@@@@@ @@@@@     @"""+bcolors.OKGREEN+"""###
###########################################################################
"""
Starting_Anime = """
===========================================================================
###########################################################################
    *       *  """+bcolors.FAIL+"""..."""+bcolors.OKGREEN+"""     *          *          *   ... .. . .. ... |        #
*            """+bcolors.FAIL+""";::::;"""+bcolors.OKGREEN+"""          *          *         .............   \       #
        *  """+bcolors.FAIL+""";::::; :;"""+bcolors.OKGREEN+""" *             *           *   ..   ..  ..  *  '------#
    *    """+bcolors.FAIL+""";:::::'   :;"""+bcolors.OKGREEN+"""    *   *   *         *      ..  .....  ..           #
*       """+bcolors.FAIL+""";:::::;     ;."""+bcolors.OKGREEN+"""    *       """+bcolors.FAIL+"""0"""+bcolors.OKGREEN+"""   *      *      .........             #
   *   """+bcolors.FAIL+""",:::::'       ;"""+bcolors.OKGREEN+""" *     *   """+bcolors.FAIL+"""OOO\."""+bcolors.OKGREEN+"""   *     *   .. .. .. ..            #
-------"""+bcolors.FAIL+"""::::::;       ;"""+bcolors.OKGREEN+"""----------"""+bcolors.FAIL+"""OOOOO\."""+bcolors.OKGREEN+"""-----------------------------------#
       """+bcolors.FAIL+""";:::::;       ;         OOOOOOOO"""+bcolors.OKGREEN+"""                                   #
      """+bcolors.FAIL+""",;::::::;     ;'         / OOOOOOO"""+bcolors.OKGREEN+"""         _-_     _-_     _-_      #
    """+bcolors.FAIL+""";:::::::::`. ,,,;.        /  / DOOOOOO"""+bcolors.OKGREEN+"""      |RIP|   |RIP|   |RIP|     #
  """+bcolors.FAIL+""".';:::::::::::::::::;,     /  /     DOOOO"""+bcolors.OKGREEN+"""    /     \ /     \ /     \    #
 """+bcolors.FAIL+""",::::::;::::::;;;;::::;,   /  /        DOOO"""+bcolors.OKGREEN+"""   | ___ | | ___ | | ___ |    #
"""+bcolors.FAIL+""";`::::::`'::::::;;;::::: ,#/  /          DOOO"""+bcolors.OKGREEN+"""                             #
"""+bcolors.FAIL+""":`:::::::`;::::::;;::: ;::#  /            DOOO"""+bcolors.OKGREEN+"""                            #
"""+bcolors.FAIL+"""::`:::::::`;:::::::: ;::::# /              DOO"""+bcolors.OKGREEN+"""                            #
"""+bcolors.FAIL+"""`:`:::::::`;:::::: ;::::::#/               DOO"""+bcolors.OKGREEN+"""                            #
 """+bcolors.FAIL+""":::`:::::::`;; ;:::::::::##                OO"""+bcolors.OKGREEN+"""                            #
 """+bcolors.FAIL+"""::::`:::::::`;::::::::;:::#                OO"""+bcolors.OKGREEN+"""                            #
 """+bcolors.FAIL+"""`:::::`::::::::::::;'`:;::#                O"""+bcolors.OKGREEN+"""                             #
  """+bcolors.FAIL+"""`:::::`::::::::;' /  / `:#                """+bcolors.OKGREEN+"""                              #
   """+bcolors.FAIL+"""::::::`:::::;'  /  /   `#                """+bcolors.OKGREEN+"""                              #
==========================================================================#
###########################################################################
#            """+bcolors.WARNING+""" _,.-----.,_"""+bcolors.OKGREEN+"""                #"""+bcolors.FAIL+"""########"""+bcolors.OKGREEN+"""# /"""+bcolors.OKBLUE+""" To Those Tho Believe"""+bcolors.OKGREEN+"""#
#          """+bcolors.WARNING+""",-~           ~-."""+bcolors.OKGREEN+"""              #"""+bcolors.FAIL+"""######"""+bcolors.OKGREEN+"""# / """+bcolors.OKBLUE+"""In The Unkown And Un-"""+bcolors.OKGREEN+"""#
#        """+bcolors.WARNING+""",^___           ___^."""+bcolors.OKGREEN+"""             #"""+bcolors.FAIL+"""####"""+bcolors.OKGREEN+"""# | """+bcolors.OKBLUE+"""Founded, We Will Never"""+bcolors.OKGREEN+"""#
#      """+bcolors.WARNING+"""/~"   ~"   .   "~   "~ \ """+bcolors.OKGREEN+"""           #"""+bcolors.FAIL+"""####"""+bcolors.OKGREEN+"""# | """+bcolors.OKBLUE+"""Allow Those Who Stand """+bcolors.OKGREEN+"""#
#    """+bcolors.WARNING+""" Y  ,--._    I    _.--.    Y"""+bcolors.OKGREEN+"""           #"""+bcolors.FAIL+"""##"""+bcolors.OKGREEN+"""# / """+bcolors.OKBLUE+"""Before Us, To See Us """+bcolors.OKGREEN+"""###
#     """+bcolors.WARNING+""" | Y     ~-. | ,-~     Y | """+bcolors.OKGREEN+"""            ## | """+bcolors.OKBLUE+"""In Our Weakesst, We """+bcolors.OKGREEN+"""#####
#      """+bcolors.WARNING+"""| |        }:{        | | """+bcolors.OKGREEN+"""            ## | """+bcolors.OKBLUE+"""Want Them To Know We """+bcolors.OKGREEN+"""####
#      """+bcolors.WARNING+"""j l       / | \       ! l """+bcolors.OKGREEN+"""            ## | """+bcolors.OKBLUE+"""Came As Monsters, Tog-"""+bcolors.OKGREEN+""" ##
#   """+bcolors.WARNING+""".-~  (__,.--" .^. "--.,__)  ~-. """+bcolors.OKGREEN+"""         ## | """+bcolors.OKBLUE+"""ether We Can Run This """+bcolors.OKGREEN+"""###
#  """+bcolors.WARNING+"""(           / / | \ \           ) """+bcolors.OKGREEN+"""        ## | """+bcolors.OKBLUE+"""World, We Are Anonymous,"""+bcolors.OKGREEN+"""#
#   """+bcolors.WARNING+"""\.____,   ~  \/"\/  ~   .____,/ """+bcolors.OKGREEN+"""         ## | """+bcolors.OKBLUE+"""We Are Legion, We Do Not"""+bcolors.OKGREEN+"""#
#   """+bcolors.WARNING+""" ^.____                 ____.^  """+bcolors.OKGREEN+"""         ## | """+bcolors.OKBLUE+"""Forgive, We Do Not Forg-"""+bcolors.OKGREEN+"""#
#      """+bcolors.WARNING+""" | |T ~\  !   !  /~ T| |     """+bcolors.OKGREEN+"""         ## | """+bcolors.OKBLUE+"""et To Those Who Fell """+bcolors.OKGREEN+"""####
#       """+bcolors.WARNING+"""| |l   _ _ _ _ _   !| |     """+bcolors.OKGREEN+"""         ## | """+bcolors.OKBLUE+"""Under The Power Of Greed"""+bcolors.OKGREEN+"""#
#       """+bcolors.WARNING+"""| l \/V V V V V V\/ j |     """+bcolors.OKGREEN+"""         ##############################
#       """+bcolors.WARNING+"""l  \ \|_|_|_|_|_|/ /  l     """+bcolors.OKGREEN+"""         ## $$$$$$$$$$$$$$$$$$$$$$$$$$#
#        """+bcolors.WARNING+"""\  \[T T T T T TI/  /      """+bcolors.OKGREEN+"""        #"""+bcolors.FAIL+"""##"""+bcolors.OKGREEN+"""# $~~Expect~~~~~~~~~~~~~~~~#
#         """+bcolors.WARNING+"""\  `^-^-^-^-^-^'  /       """+bcolors.OKGREEN+"""       #"""+bcolors.FAIL+"""####"""+bcolors.OKGREEN+"""# $~~~~~~~~Us~~~~~~~~~~~~~#
#          """+bcolors.WARNING+"""\               /        """+bcolors.OKGREEN+"""       #"""+bcolors.FAIL+"""####"""+bcolors.OKGREEN+"""# $~~~~~~~~~~~@TopKek~~~~~#
#           """+bcolors.WARNING+"""\.           ,/         """+bcolors.OKGREEN+"""      #"""+bcolors.FAIL+"""######"""+bcolors.OKGREEN+"""# $~~~~~~~~~~~~~~<(o)>~~~#
#             """+bcolors.WARNING+""""^-.___,-^"           """+bcolors.OKGREEN+"""     #"""+bcolors.FAIL+"""########"""+bcolors.OKGREEN+"""# $$$$$$$$$$$$$$$$$$$$$$#
###########################################################################



"""

atscan_help = """
target      - Set Target
sql         - Toggle Sql Scan
lfi         - Toggle Lfi Scan
wp          - Toggle Wp Scan
port        - Set Port
port.scan   - Toggle Port scan
email       - Set Email
save        - Save Scan
tcp         - Set Tcp Scan ( port.scan must be True )
udp         - set Udp Scan ( port.scan must be True )
start       - Begin Scan
"""

Help = """
Commands:
-h              Displays This Help Screen

Crunch          Create A Word List

atscan.start    Basic Atscan
                Will Run command 'proxychains atscan
                -t 'target' --sql --wp --lfi --ip --email'

chdir           Change Directory

server.start    Starts Server

client.start    Starts Client
      .list     Lists All Known Tested Connection's
      .listadd  Add Servers

refresh.screen  Refreshes Console Screen
"""

stringset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

def atscan_Run():
    target      = "none"
    save_f_name = "OnlyForCunts.txt"
    sqlscan     = True
    wpscan      = False
    lfiscan     = False
    portscan    = False
    defaultp    = "80"
    proxychains = False
    emailscan   = False
    dorkscan    = False
    os.system("clear")
    print bcolors.OKGREEN + "["+socket.gethostname()+"]?:>> "+bcolors.HEADER+"#TopKek"+bcolors.OKGREEN+" Atscan Assistance Tool"
    print bcolors.OKGREEN + "["+socket.gethostname()+"]?:>> Variable Status"
    print bcolors.OKGREEN + "["+socket.gethostname()+"]?:>> Variable Sql Scan: "+bcolors.HEADER+str(sqlscan)
    print bcolors.OKGREEN + "["+socket.gethostname()+"]?:>> Variable Wp Scan: "+bcolors.HEADER+str(wpscan)
    print bcolors.OKGREEN + "["+socket.gethostname()+"]?:>> Variable LFI Scan: "+bcolors.HEADER+str(lfiscan)
    print bcolors.OKGREEN + "["+socket.gethostname()+"]?:>> Variable Port Scan: "+bcolors.HEADER+str(portscan)
    print bcolors.OKGREEN + "["+socket.gethostname()+"]?:>> Variable Default Port: "+bcolors.HEADER+str(defaultp)
    print bcolors.OKGREEN + "["+socket.gethostname()+"]?:>> Variable Email Scan: "+bcolors.HEADER+str(emailscan)
    print bcolors.OKGREEN + "["+socket.gethostname()+"]?:>> Variable Proxychains: "+bcolors.HEADER+str(proxychains)
    print bcolors.OKGREEN + "["+socket.gethostname()+"]?:>> Variable Dork Scan: "+bcolors.HEADER+str(dorkscan)
    print bcolors.OKGREEN + "["+socket.gethostname()+"]?:>> Variable Target: "+bcolors.HEADER+str(target)
    print "==================================================="
    print "............ /   / ...."+bcolors.HEADER+"./ \."+bcolors.OKGREEN+".... \   \  ..........."
    print "Use 'help'. <   /  ..."+bcolors.FAIL+"TOP   KEK"+bcolors.OKGREEN+"...  \    > .For Help"
    print "............ \  \  ....."+bcolors.HEADER+"\_/"+bcolors.OKGREEN+"...... /  / ............"
    print "==================================================="
    atscan_input    = raw_input("["+socket.gethostname()+"]?:>> ")
    if atscan_input == str("help"):
        print bcolors.OKBLUE + str(atscan_help)
        atscan_Run()

    elif atscan_input == str("target"):
        atscan_target_input = raw_input("["+socket.gethostname()+"]"+bcolors.FAIL+"(Target, IE: http://www.target.com)"+bcolors.OKGREEN+"?:>> ")
        target = str(atscan_target_input)
        os.system("clear")
        atscan_Run()

    elif atscan_input == str("home"):
        os.system("clear")
        Running()

    elif atscan_input == str("exit"):
        sys.exit(1)


    else:
        print bcolors.FAIL + "Invalid Operation..."
        atscan_Run()

def StartingAnime():
    print str(Starting_Anime)
    time.sleep(5)
    Running()

def Client_SList():
    try:
        SLIST = open("SLIST.txt", "r")
        for line in SLIST:
            server_list == SLIST

        SLIST.close()
        print bcolors.OKBLUE + str(SLIST)

    except:
        print bcolors.FAIL + "Operation Failed Have You Created A List?"
        Main_Commands()


def Client_Start():
    try:
        os.system("python Client.py")

    except:
        print bcolors.WARNING + "Operation Failed Is It Installed"
        Main_Commands()

def Server_Start():
    try:
        os.system("python Server.py")

    except:
        print bcolors.WARNING + "Operation Failed Is It Installed?"
        Main_Commands()

def Main_Commands():
    print bcolors.ENDC + "CopyRight @ #TopKek"
    Main_Input = raw_input("["+socket.gethostname()+"]?:>> ")
    if Main_Input == str("-?"):
        print bcolors.ENDC + Help
        Main_Commands()

    elif Main_Input == str("server.start"):
        Server_Start()

    elif Main_Input == str("client.start"):
        Client_Start()

    elif Main_Input == str("client.list"):
        Client_SList()

    elif Main_Input == str("chdir"):
        print bcolors.ENDC + "["+socket.gethostname()+"]?:>>" +"Current Directory Is: "+os.getcwd()
        Directory_Input = raw_input("["+socket.gethostname()+"]"+bcolors.OKGREEN+"(Target Directory:)"+bcolors.ENDC+"?:>> ")
        print bcolors.OKBLUE + "["+socket.gethostname()+"]?:>> " +"Directory Entered: "+Directory_Input
        print bcolors.WARNING + "["+socket.gethostname()+"]?:>> Attmepting To Change To Directory..."
        os.chdir(str(Directory_Input))
        print bcolors.OKGREEN + "["+socket.gethostname()+"]?:>> Operation Successfull, Directory Changed To: "+os.getcwd()
        os.system("clear")
        Running()

    elif Main_Input == str("exit"):
        print bcolors.FAIL + "Then Bye Saucy Mother Fucking Cunt"
        sys.exit(1)

    elif Main_Input == str("refresh.screen"):
        Running()

    elif Main_Input == str("atscan"):
        atscan_Run()

    else:
        print bcolors.WARNING + "Invalid Command"
        Main_Commands()

def Running():
    print bcolors.HEADER + Banner
    print bcolors.OKBLUE + "CopyRight @ Jackel | #TopKek / Othernet"
    print bcolors.UNDERLINE + "Time: "+time.asctime()
    print bcolors.ENDC + "Directory: "+os.getcwd()
    print bcolors.WARNING + """
    Please Remember All Tools Enclosed Are For
            'Educational' Purposes Only
    """
    print bcolors.OKBLUE + "-? for help"
    print
    Main_Commands()

StartingAnime()
