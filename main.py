import sys

class Rover:
    def __init__(self,end_coordinates:list, start_coordinates:list) -> None:
        self.end_coordinates=end_coordinates
        self.current_coordinates=start_coordinates
        

    def move(self,direction:str)->None:

        if direction=="M":
            if self.current_coordinates[2]==0 and self.current_coordinates[1]+1<=self.end_coordinates[1]:#N
                self.current_coordinates[1]=self.current_coordinates[1]+1

            elif self.current_coordinates[2]==2 and self.current_coordinates[1]>=0:#S
                self.current_coordinates[1]=self.current_coordinates[1]-1
                
            elif self.current_coordinates[2]==1 and self.current_coordinates[0]+1<=self.end_coordinates[0]:
                self.current_coordinates[0]=self.current_coordinates[0]+1

            elif self.current_coordinates[2]==3 and self.current_coordinates[0]-1>=0:
                self.current_coordinates[0]=self.current_coordinates[0]-1
            
            else:
                print("At the boundary")

        elif direction=="L":
            self.current_coordinates[2]=(self.current_coordinates[2]-1)%4
        
        elif direction=="R":
            self.current_coordinates[2]=(self.current_coordinates[2]+1)%4

        else:
            print("Invlaid Direction")




def process_rover_input():
    input_lines = sys.stdin.readlines()
    rovers = []
    end_coordinates=list(map(int, input_lines[0].strip().split()))
    

    for i in range(1,len(input_lines)-1,2):
        start_coordinates=[int(j) if j.isdigit() else ["N","E","S","W"].index(j) for j in input_lines[i].strip().split()]
        directions=list(input_lines[i+1].strip())
        rover=Rover(end_coordinates=end_coordinates,start_coordinates=start_coordinates)
        print(start_coordinates)
        for i in directions:
            
            rover.move(i)
            print(rover.current_coordinates)
        print()
        rovers.append(rover)

    return rovers

if __name__ == "__main__":
    rovers = process_rover_input()
    direction={0:"N",1:"E",2:"S",3:"W"}
    # Print final positions of the rovers
    for i in rovers:
        print(i.current_coordinates[0],i.current_coordinates[1],direction[i.current_coordinates[2]])
        

