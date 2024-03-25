import pytest 
from main import Rover 


def test_rover_at_north_boundary():
    rover=Rover([5,5],[5,5,"N"])
    rover.controller(["M","M","M","L","R"])
    assert rover.current_coordinates==[5,5,"N"]

def test_rover_at_south_boundary():
    rover=Rover([5,5],[0,0,"S"])
    rover.controller(["M","M","M","L","R"])
    assert rover.current_coordinates==[0,0,"S"]

def test_rover_at_east_boundary():
    rover=Rover([5,5],[5,5,"E"])
    rover.controller(["M","M","M","L","R"])
    assert rover.current_coordinates==[5,5,"E"]

def test_rover_at_west_boundary():
    rover=Rover([5,5],[0,0,"W"])
    rover.controller(["M","M","M","L","R"])
    assert rover.current_coordinates==[0,0,"W"]

def test_rover_with_invalid_orientation():
    with pytest.raises(ValueError,match=r"Invalid Orientation *") as e:
        rover=Rover([5,5],[4,5,"L"])
    
def test_rover_with_invalid_direction():
    with pytest.raises(ValueError,match=r"Invalid Direction *") as e:
        rover=Rover([5,5],[4,5,"S"])
        rover.controller(["M","M","O"])

def test_rover_with_invalid_start_position():
    with pytest.raises(ValueError,match=r"Invalid Starting Coordinates *") as e:
        rover=Rover([5,5],[-1,5,"S"])
        rover.controller(["M","M","O"])
    
    with pytest.raises(ValueError,match=r"Invalid Starting Coordinates *") as e:
        rover=Rover([5,5],[1,-5,"S"])
        rover.controller(["M","M","O"])
    

    with pytest.raises(ValueError,match=r"Invalid Starting Coordinates *") as e:
        rover=Rover([5,5],[1,6,"S"])
        rover.controller(["M","M","O"])
    

    with pytest.raises(ValueError,match=r"Invalid Starting Coordinates *") as e:
        rover=Rover([5,5],[10,5,"S"])
        rover.controller(["M","M","O"])

    
    with pytest.raises(ValueError,match=r"Invalid Starting Coordinates *") as e:
        rover=Rover([5,5],[-1,-5,"S"])
        rover.controller(["M","M","O"])

    
    with pytest.raises(ValueError,match=r"Invalid Starting Coordinates *") as e:
        rover=Rover([5,5],[10,50,"S"])
        rover.controller(["M","M","O"])
    

def test_very_large_plateau():
    
    instructions = "M"*100 + "L" + "M"*200
    rover=Rover([10000, 10000],[5000, 5000, "N"]  )
    rover.controller(list(instructions))
    assert rover.current_coordinates==[4800,5100,"W"]

