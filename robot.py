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

        self.turn_controller = PIDController(P, I, D)

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
        wheel_diameter = 4  # inches
        wheel_circumference = wheel_diameter * math.pi
        leg_1_distance = (84)
        leg_1_clicks = (leg_1_distance / wheel_circumference) * 360
        self.drivetrain.set(leg_1_clicks, leg_1_clicks)
        # self.drivetrain.gyro.setYaw(O)
        # self.drivetrain.m_right_encoder(0)


    def autonomousPeriodic(self):
        self.turn_controller.setSetpoint(90)
        turn_clicks = self.turn_controller.calculate(measurement=self.drivetrain.gyro.setYaw())
        self.drivetrain.set(-turn_clicks, turn_clicks)

if __name__ == "__main__":
    wpilib.run(Robot)
