#### and gamma and 

click_play = True
while click_play:
    class gameclass:
        def __init__(self,playerName,playerlife,playerpower,playerposition):
          self.playerName = playerName
          self.playerlife = playerlife
          self.playerpower = playerpower
          self.playerposition = playerposition
        def getplayername(self):
            return f"joueur{self.playerName}"
       
        def getplayerlife(self):
            return f"le point de vie est de {self.playerlife}"
        
        def getplayerpower(self):
            return f"la puissance du joueur est {self.playerpower}"
        
        def getplayerposition(self):
            return f"la position du joueur est {self.playerposition}"

        def attack(self,coup ):
            if coup > self.playerpower :
                print("vous n'avat pas asses de puissance pour influger cette attack votre puissance maximal est{self.playerpower}")
            elif coup == self.playerpower:
                choix = input("voulez vous utiliser toute votre puissance pour cette attack repondez par 1 oui ou 2 nom()")
                if choix == 1 :
                    playerpower -= self.coup
                else:
                 print("attack annuler")
            else:
                self.playerpower -= coup
                print(f"vous avez utiliser {coup} de puissance  vous avez maintenant {self.playerpower} de puissance")
                if self.playerpower <= 0:
                    print("vous n'avait pas de puissance pour attacker")

        def playertoucher(self,coup):
            if coup == 2:
                self.playerlife -= 1
            
            if self.playerlife == 0:
                print("print le joueur est finis vous etait mort")
             



        def attack_inflix(self, cibble,coup):
            cibble.attack(self.coup)
            cibble.playertoucher(self.coup)
            return f"le joueur {cibble} est toucher de {self.coup} coup "
    

    player1 = gameclass("pl1",100,1,0)
    player2 = gameclass("pl2",100,10,1)
    
  #  print(player1.attack_inflix(player2,))
    player1.attack(player2,4)
   
