#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()


# Write your program here.
ev3.speaker.beep()



#!/usr/bin/env python3

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_D, MoveTank
from ev3dev2.sensor import Sensor
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.sound import Sound
from pixy2ev3 import Pixy2

# Initialise la communication avec la caméra Pixy 2
pixy = Pixy2()

# Initialise les moteurs et le capteur tactile
tank_drive = MoveTank(OUTPUT_A, OUTPUT_D)
touch_sensor = TouchSensor()
sound = Sound()

# Fonction pour tourner la base de la tourelle jusqu'à détecter un objet
def search():
    sound.speak("Recherche")
    tank_drive.on(50, -50)
    while not touch_sensor.is_pressed:
        if pixy.get_blocks():
            sound.speak("Objet détecté")
            tank_drive.off()
            return True
    tank_drive.off()
    return False

# Fonction pour suivre un objet
def follow():
    sound.speak("Suivi de l'objet")
    while True:
        if not pixy.get_blocks():
            return False
        block = pixy.blocks[0]
        if block.signature == 1:  # Signature de l'objet à suivre
            x = block.x
            y = block.y
            error = x - pixy.frame_width / 2
            tank_drive.on(int(0.5 * (50 + error)), int(0.5 * (50 - error)))
    return False

# Fonction principale
def main():
    while True:
        if not search():
            break
        if not follow():
            break
    sound.speak("Fin du programme")

if __name__ == '__main__':
    main()




import pygame
from ev3dev2.sensor.lego import Pixy2
from ev3dev2.motor import MediumMotor, OUTPUT_A, OUTPUT_B

# Initialisez la caméra Pixy2 et les moteurs pour le retour caméra
pixy = Pixy2()
motor_a = MediumMotor(OUTPUT_A)
motor_b = MediumMotor(OUTPUT_B)

# Initialisez Pygame
pygame.init()
size = (320, 240)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pixy 2")

# Boucle principale
done = False
while not done:
    # Récupérez l'image de la caméra Pixy2
    frame = pixy.get_blocks()

    # Affichez l'image sur l'écran
    if frame:
        screen.blit(pygame.surfarray.make_surface(frame), (0, 0))

    # Mettez à jour l'écran
    pygame.display.flip()

    # Capturez les événements de la croix directionnelle
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                # Faites avancer le retour caméra
                motor_a.on(50)
                motor_b.on(50)
            elif event.key == pygame.K_DOWN:
                # Faites reculer le retour caméra
                motor_a.on(-50)
                motor_b.on(-50)
            elif event.key == pygame.K_LEFT:
                # Faites pivoter le retour caméra à gauche
                motor_a.on(-50)
                motor_b.on(50)
            elif event.key == pygame.K_RIGHT:
                # Faites pivoter le retour caméra à droite
                motor_a.on(50)
                motor_b.on(-50)
        elif event.type == pygame.KEYUP:
            # Arrêtez les moteurs lorsqu'une touche est relâchée
            motor_a.off()
            motor_b.off()

    # Quittez la boucle principale si la fenêtre est fermée
    if event.type == pygame.QUIT:
        done = True

# Quittez Pygame
pygame.quit()