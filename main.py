import sys

class Rover:
    def __init__(self,end_coordinates:list, start_coordinates:list) -> None:
        
        direction={"N":0,"E":1,"S":2,"W":3}

        # Convert cardinal direction into int
        try:
            start_coordinates[-1]=direction[start_coordinates[-1]]
        except KeyError as e:
            raise ValueError("Invalid Orientation",start_coordinates[-1])
        
        # Check for valid starting coordinates
        if (start_coordinates[0]<0 or start_coordinates[1]<0 or start_coordinates[0]>end_coordinates[0] or start_coordinates[1]>end_coordinates[1] or start_coordinates[-1] not in [0,1,2,3]):
            raise ValueError("Invalid Starting Coordinates", start_coordinates)
        
        # Initialize rover
        self.end_coordinates=end_coordinates
        self.current_coordinates=start_coordinates    


    # Interface for testing
    def controller(self,directions:list)->None:
        direction={0:"N",1:"E",2:"S",3:"W"}
        for i in directions:
            self.move(i)
        self.current_coordinates[-1]=direction[self.current_coordinates[-1]]
        
    # Move the rover
    def move(self,direction:str)->None:

        # Check Orientation and if the move is valid
        if direction=="M":

            # North direction
            if self.current_coordinates[2]==0 and self.current_coordinates[1]+1<=self.end_coordinates[1]:
                self.current_coordinates[1]=self.current_coordinates[1]+1

            # South direction
            elif self.current_coordinates[2]==2 and self.current_coordinates[1]-1>=0:
                self.current_coordinates[1]=self.current_coordinates[1]-1
                
            # East direction
            elif self.current_coordinates[2]==1 and self.current_coordinates[0]+1<=self.end_coordinates[0]:
                self.current_coordinates[0]=self.current_coordinates[0]+1

            # West direction
            elif self.current_coordinates[2]==3 and self.current_coordinates[0]-1>=0:
                self.current_coordinates[0]=self.current_coordinates[0]-1
            
            else:
                print("At the boundary can not move forward")

        # Turn 90 degrees to the left
        elif direction=="L":
            self.current_coordinates[2]=(self.current_coordinates[2]-1)%4
        
        # Turn 90 degrees to the right
        elif direction=="R":
            self.current_coordinates[2]=(self.current_coordinates[2]+1)%4

        else:
            raise ValueError("Invalid Direction",direction)
        



# Process inputs for the rover
def process_rover_input():

    input_lines = sys.stdin.readlines() # Read all the line in stdin
    rovers = []
    end_coordinates=list(map(int, input_lines[0].strip().split())) # Get the size of plateau
    direction={0:"N",1:"E",2:"S",3:"W"}

    for i in range(1,len(input_lines)-1,2):
        inputs=[i for i in input_lines[i].strip().split() if i!=" "] # Remove any unnecessary " "
        start_coordinates=start_coordinates=[int(j) if j.isdigit() else j for j in inputs ] # Convert string to int
        directions=list(input_lines[i+1].strip()) # Get inputs for a particular rover
    
        rover=Rover(end_coordinates=end_coordinates,start_coordinates=start_coordinates) # Initialize rover
        
        for i in directions:    # Start rover
            rover.move(i)
            print(rover.current_coordinates)
            
        
        rover.current_coordinates[-1]=direction[rover.current_coordinates[-1]] # Converting int to cardinal direction
        rovers.append(rover)

    return rovers

if __name__ == "__main__":
    # All the inputs must be provided at once 
    rovers = process_rover_input()
    
    # Print final positions of the rovers
    for i in rovers:
        print(i.current_coordinates[0],i.current_coordinates[1],i.current_coordinates[2])
        
