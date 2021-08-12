from colored import fg,attr
def do_help():
    a = """%s
                           __  __     __         __  ___        __   
                          / / / /__  / /___     /  |/  /__     / /   
                         / /_/ / _ \/ / __ \   / /|_/ / _ \   / /    
                        / __  /  __/ / /_/ /  / /  / /  __/  /_/     
                       /_/ /_/\___/_/ .___/  /_/  /_/\___/  (_)      
                                   /_/                               
                 ____________________________________________________________________
                 | welcome to your search Shell please follow the next instructions |
                 --------------------------------------------------------------------


    - in order to find a specific exploit or module please enter the following command :
    
            ---> search < exploit name >                    search for the exploits you wish to use
            ---> search < module name >                     search for the modules you wish to use
            
    - In order to see all the available modules or exploits please enter the following command :
    
            ---> search                                      show all available exploits/modules
    %s""" % (fg(219),attr(0))

    print(a)