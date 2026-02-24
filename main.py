import sys

from client.src.game import Engine


r"""


                                                                  ,---, 
    ,----..                                                    ,`--.' | 
   /   /   \                         ___                       |   :  : 
  /   .     :                      ,--.'|_                     '   '  ; 
 .   /   ;.  \                     |  | :,'             __  ,-.|   |  | 
.   ;   /  ` ;           .--.--.   :  : ' :           ,' ,'/ /|'   :  ; 
;   |  ; \ ; |     .--, /  /    '.;__,'  /     ,---.  '  | |' ||   |  ' 
|   :  | ; | '   /_ ./||  :  /`./|  |   |     /     \ |  |   ,''   :  | 
.   |  ' ' ' :, ' , ' :|  :  ;_  :__,'| :    /    /  |'  :  /  ;   |  ; 
'   ;  \; /  /___/ \: | \  \    `. '  : |__ .    ' / ||  | '   `---'. | 
 \   \  ',  / .  \  ' |  `----.   \|  | '.'|'   ;   /|;  : |    `--..`; 
  ;   :    /   \  ;   : /  /`--'  /;  :    ;'   |  / ||  , ;   .--,_    
   \   \ .'     \  \  ;'--'.     / |  ,   / |   :    | ---'    |    |`. 
    `---`        :  \  \ `--'---'   ---`-'   \   \  /          `-- -`, ;
                  \  ' ;                      `----'             '---`" 
                   `--`                                                 

Developed by - Yash Bavishi (constryo)

"""


def main() -> int:
    import logging

    logging.basicConfig(
        format="%(asctime)s %(levelname)s %(message)s", level=logging.DEBUG
    )

    logging.info("Commencing game")
    Engine().start()
    Engine().run()
    return 0


if __name__ == "__main__":
    sys.exit(main())
