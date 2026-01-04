import tkinter as tk
from tkinter import messagebox

# Création de la fenêtre principale
root = tk.Tk()
root.title("Formulaire")
root.geometry("400x200")

# Label en haut avec pack
label_titre = tk.Label(root, text="Formulaire de saisie", font=("Arial", 14, "bold"))
label_titre.pack(pady=10)

# Frame pour la grille avec grid
frame_formulaire = tk.Frame(root)
frame_formulaire.pack(pady=20)

# Grille de labels et champs avec grid
label_nom = tk.Label(frame_formulaire, text="Nom:")
label_nom.grid(row=0, column=0, padx=10, pady=5, sticky="e")

champ_nom = tk.Entry(frame_formulaire, width=20)
champ_nom.grid(row=0, column=1, padx=10, pady=5)

label_prenom = tk.Label(frame_formulaire, text="Prénom:")
label_prenom.grid(row=1, column=0, padx=10, pady=5, sticky="e")

champ_prenom = tk.Entry(frame_formulaire, width=20)
champ_prenom.grid(row=1, column=1, padx=10, pady=5)

# Fonction pour afficher le message
def afficher_bonjour():
    nom = champ_nom.get()
    prenom = champ_prenom.get()
    
    if nom and prenom:
        messagebox.showinfo("Message", f"Bonjour {nom} {prenom}")
    else:
        messagebox.showwarning("Attention", "Veuillez remplir tous les champs")

# Bouton en bas avec place
bouton_valider = tk.Button(root, text="Valider", command=afficher_bonjour, 
                          font=("Arial", 10), padx=20, pady=5)
bouton_valider.place(relx=0.5, rely=0.9, anchor="s")

# Lancement de l'application
root.mainloop()

