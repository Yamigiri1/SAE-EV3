import tkinter as tk

class CommandInterface(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Interface de commande")

        # Frame pour les boutons directionnels
        direction_frame = tk.Frame(self)
        direction_frame.grid(column=0, row=0)

        # Paramètres de style pour les boutons
        button_width = 10
        button_height = 5

        # Boutons directionnels
        up_button = tk.Button(direction_frame, text="Avant", width=button_width, height=button_height)
        up_button.grid(row=0, column=1, padx=5, pady=5) 

        down_button = tk.Button(direction_frame, text="Recul", width=button_width, height=button_height)
        down_button.grid(row=2, column=1, padx=5, pady=5)

        left_button = tk.Button(direction_frame, text="Gauche", width=button_width, height=button_height)
        left_button.grid(row=1, column=0, padx=5, pady=5)

        right_button = tk.Button(direction_frame, text="Droite", width=button_width, height=button_height)
        right_button.grid(row=1, column=2, padx=5, pady=5)

        # frame droite pour le retour vidéo
        camera_frame = tk.Frame(self)
        camera_frame.grid(row=0, column=1)
        
        # Affiche le titre retour camera
        tk.Label(camera_frame, text="Retour camera", font=("Arial", 12), bg='#3FAADF').pack()
        camera_canva = tk.Canvas(camera_frame, width=300, height=300, bg='gray')
        camera_canva.pack()

if __name__ == "__main__":
    app = CommandInterface()
    app.mainloop()
