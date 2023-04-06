<p align="center">
  <img src="./logo/iut-mulhouse.jpg">
</p>

## Bienvenue sur la SAE LEGO EV3 

## Equipe : Elliot Veglio / Maxime Wegbecher / Jean Vogel

## Référent : M.Mourllion / M.Hueber

      
### Présentation rapide de la SAE

#### Contexte de la SAE

Sur un robot industriel, l'interface graphique est essentiel car elle permet aux opérateur de suivre le robot et de savoir s'il commet des erreurs, de plus un robot industriel ce doit d'être autonome une fois en fonctionnement, il ce doit de pouvoir suivre un parcours et d'avoir des automatismes de sécurité si jamais des obstacles ce mettent sur son parcours. Au sein de l'IUT nous avons des robot lego EV3 qui peuvent nous donner un apercu académique des robots industirels, les robots EV3 de l'IUT ne sont pour l'instant qu'utilsé avec le logiciel fourni par Lego (Mindstorms) et avec des programme assez simple. 

Le LEGO EV3 est robot pédagogique fournit par l’entreprise Lego. Il peut s'assembler de plusieurs façons, de nombreux capteurs sont compatibles. Ce qui en fait un des robot les plus complets pour l'enseignement. 

#### But du travail

En tant qu'étudient, notre but était donc d'instrumenter ce robot pour avoir d'une part un retour d'information et d'autre part un robot stable sur 2 roue qui ce déplace en suivant des lignes au sol et qui esquive les obstacles. 

### Analyse critique de nos travaux

#### Synthèse sur l'étude des capteurs

Maxime/Jean

#### Réalisation du cable 

Elliot

#### Construction

Sur la base des plans du Gyro boy fournie par LEGO, nous avons fait quelques modifications en enlevant le capteur de couleur pour avoir un port capteur disponible et attacher un caméra Pixy V2. Comme dit précédemment nous avons modifier un câble de communication RJ11 qui servait pour la transmission de données entre la brick et le capteur pour l’adapter aux pins de la caméra.

Robot : [Gyro + Caméra](https://github.com/Yamigiri1/SAE-EV3/tree/main/Images/Robot_Face_avant)

#### Explication partie importante du code 

La partie la plus importante du Gyropode est le PID qui permet au Gyropode de tenir sur ses deux roues.

En effectuant des études du PID par tâtonnements en changeant les variables des différents correcteurs (Proportionnel, Intégrale et Dérivé) :

```py

# valeurs d'origine : -0.01 / 0.8 / 15 / 0.08 / 0.12
        output_power = (-0.01 * drive_speed) + (0.8 * robot_body_rate +
                                                20 * robot_body_angle +
                                                0.08 * wheel_rate +
                                                0.12 * wheel_angle)
        if output_power > 100:
            output_power = 100
        if output_power < -100:
            output_power = -100

        # Drive the motors.
        left_motor.dc(output_power - 0.1 * steering)
        right_motor.dc(output_power + 0.1 * steering)

```

Par consequent ayant déjà fait des moidifications sur l'action du PID, nous avons trouvé par tâtonnement que le terme multiplier au 'robot_body_angle' devait être de 40 et qu'en parallèle l'output power devait être soustrait à +/- 0.3.
Avec cette correction le gyro était beaucoup plus réactif et ne titubait plus.

Code après test :
```py

        output_power = (-0.01 * drive_speed) + (0.8 * robot_body_rate +
                                                40 * robot_body_angle +
                                                0.08 * wheel_rate +
                                                0.12 * wheel_angle)
        if output_power > 100:
            output_power = 100
        if output_power < -100:
            output_power = -100

        # Drive the motors.
        left_motor.dc(output_power - 0.3 * steering)
        right_motor.dc(output_power + 0.3 * steering)

```

#### Problème rencontrés

Jean

### Résultat :

Vous pouvez voir les photos et vidéo [ici](https://github.com/Yamigiri1/SAE-EV3/tree/main/Images)

### Synthèse : 

Au cours de cette année, nous avons appris à instrumentaliser, et reguler un robot Lego EV3 pour améliorer ses performances. L'amélioration majeure apportée est une caméra qui permet de suivre des parcours plus complexe et avec une meilleur précision car comparé a un capteur de couleur qui est pointé vers le bas et qui ne peut analyser en avance, la caméra vois sur une longue porté. Dans un second temps la caméra nous permet le retour d'informations qui est un grand plus en permetant de suivre le robot sans forcement l'avoir sous les yeux, le retour d'informations nous permet aussi de faire des mesures grâces a une croix directionelle, on peut par exemple connaitre la latence entre la demande manuel de direction et le retour caméra. Nous avons découvert, pour certain, GitHub. Nous avons appris à nous servir de Mindstorms et enrichi nos connaissances en Python. 

Nous avons réalisé le projet sur une période de 108 heures et nous n'avons pas pu respecter les délais que nous étions fixé. Vous pouvez voir [ici](https://github.com/Yamigiri1/SAE-EV3/tree/main/Images) le gantt théorique, le gantt réel, ainsi que le tableau des coûts. Et voici le [Trello](https://trello.com/invite/b/C0O8bNfg/ATTIc7ef8f9a206cdfd3b2054dab92e7c462C8E4378A/sae-4-lego-mindstorm)

### Perspective pour les suites éventuelles

Après la réalisation de notre projet, notre système permet au robot à 3 roue de suivre une ligne avec la caméra tout en esquivant les obstacles éventuelles, ce qui nous ouvre la voie à de nombreuses perspectives.

Tout d'abord, on pourrait améliorer le PID, pour ainsi avoir la meilleur stabilité et rapipdité possible. On pourrait par la suite envisagé de lier la caméra et le détectur d'obstacles a un Gyropode pour ajouter une contrainte au projet. On pourrait également terminer l'interface graphique pour avoir un retour d'information de la caméra, ainsi qu'une commande manuelle pour diriger le robot vers un parcours a suivre par exemple. 
      
### Source :

[Bibliothéque Pixy2](https://docs.pixycam.com/wiki/doku.php?id=wiki:v2:start)

[Site d'achat Pixy2](https://www.generationrobots.com/fr/403011-camera-pixy-2-v2-1.html)

[GitHub Pixy2](https://github.com/charmedlabs/pixycamev3)

[Lego Education](https://education.lego.com/fr-fr/downloads/mindstorms-ev3/software)


