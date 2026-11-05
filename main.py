from robot import Robot
from componente import Componente
class Main:
    def __init__(self):
        self.robots = []

    def registra_robot(self, robot: Robot) -> None:
        if robot in self.robots:
            raise ValueError("errore: componente gia presente")
        self.robots.append(robot)
    def cerca_robot(self, codice: str) -> Robot:
        for robot in self.robots:
            if robot.codice == codice:
                return robot
        return None
    def riepilogo_robot(self, nome_azienda: str):
        for robot in self.robots:
            robot_peso = robot.peso_componenti()            
            print("Codice: {robot.codice}, Modello: {robot.modello}, Applicazione: {robot.applicazione}, peso totale: {robot_peso}")

if __name__=="__main__":
    manager = Main()
    robots = [
        Robot("AA", "aereo", "e4", 34.5, "in produzione"),
        Robot("ED", "trasporto", "c4", 34.5, "finito"),
        Robot("AC", "assistente", "b42", 34.5, "riparazione"),
        Robot("AB", "magazziono", "b4", 34.5, "in produzione")
                
        
    ]
    
    
    for robot in robots:
        manager.registra_robot(robot.codice)
    manager.riepilogo_robot("la mia azienda")
    
    