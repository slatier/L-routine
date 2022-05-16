from wpilib import run, TimedRobot, Joystick
import math
from wpimath.controller import PIDController
from drivetrain import Drivetrain

class Robot(wpilib.TimedRobot):
    
    joy1=Joystick(0)
    
    def __init__(self):
        super().__init__()
        self.drivetrain = Drivetrain()

    def robotInit(self):
        self.drivetrain.m_left_encoder.setPosition(0)
        self.drivetrain.m_right_encoder.setPosition(0)

        self.controller = PIDController(P, I, D)
        self.controller.setTolerance(15)

    def robotPeriodic(self):
        pass

    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        speed=-self.joy1.getRawAxis(1) * .4
        turn=self.joy1.getRawAxis(4) * .2
        #print(f"Speed: {speed} Turn: {turn}")
        self.drivetrain.set(speed+turn, speed-turn)

    def autonomousInit(self):
        self.wheel_diameter = 4  # inches
        self.wheel_circumference = self.wheel_diameter * math.pi
        self.leg_1_distance = (84)
        self.leg_1_clicks = (self.leg_1_distance / self.wheel_circumference) * 360
        self.drivetrain.set(self.leg_1_clicks, self.leg_1_clicks)

    def autonomousPeriodic(self):
        self.velocity = self.controller.calculate(measurement=self.drivetrain.m_left_encoder.getPosition())
        self.velocity = min(0.4, max(-.4, self.velocity))
        self.drivetrain.set(self.velocity, self.velocity)

if __name__ == "__main__":
    wpilib.run(Robot)
