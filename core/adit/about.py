import platform



def about():
    s_color = "\033[92m" if platform.system() != "Windows" else ""
    e_color = "\033[0m" if platform.system() != "Windows" else ""
    a = f"""{s_color}
                                   ___    __                __     __  _______    __   
                                  /   |  / /_  ____  __  __/ /_   / / / / ___/   / /   
                                 / /| | / __ \/ __ \/ / / / __/  / / / /\__ \   / /    
                                / ___ |/ /_/ / /_/ / /_/ / /_   / /_/ /___/ /  /_/     
                               /_/  |_/_.___/\____/\__,_/\__/   \____//____/  (_)      
                            

               | Hencesploit framework for Cloud ethical Hacking
               | Author : Team03

    __________________________________________________________________________________________________________________
    | Hencesploit is a penetration testing framework that makes Cloud hacking simple. It's an powerful tool for many |
    | attackers and defenders. Point Hencesploit at your target, load your Hacking module,what payload to drop,      |
    |                                       and hit run.                                                             |
    ------------------------------------------------------------------------------------------------------------------
| https://www.henceforth.ma/fr
| Author : Team03
| brought by : Henceforth 
----------------------------------------------> Have a nice Hack <--------------------------------------------------
     {e_color}"""
    print(a)