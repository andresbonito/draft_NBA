import random
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
import time

class DraftLotteryGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulação da Loteria do Draft da NBA 2025")
        self.root.geometry("800x600")
        
        # Times participantes da loteria e suas combinações
        self.teams = {
            "Utah Jazz": 140,
            "Washington Wizards": 140,
            "Charlotte Hornets": 140,
            "New Orleans Pelicans": 125,
            "Philadelphia 76ers": 105,
            "Brooklyn Nets": 90,
            "Toronto Raptors": 75,
            "San Antonio Spurs": 60,
            "Houston Rockets (via Phoenix)": 38,
            "Portland Trail Blazers": 37,
            "Dallas Mavericks": 18,
            "Chicago Bulls": 17,
            "Atlanta Hawks (via Sacramento Kings)": 8,
            "San Antonio Spurs (via Atlanta Hawks)": 7
        }
        
        # Criar widgets
        self.create_widgets()
        
    def create_widgets(self):
        # Área de texto para mostrar o progresso
        self.text_area = scrolledtext.ScrolledText(self.root, width=70, height=20)
        self.text_area.pack(pady=10, padx=10)
        
        # Frame para botões
        button_frame = ttk.Frame(self.root)
        button_frame.pack(pady=10)
        
        # Botão para iniciar simulação
        self.start_button = ttk.Button(button_frame, text="Iniciar Simulação", command=self.run_simulation)
        self.start_button.pack(side=tk.LEFT, padx=5)
        
        # Botão para resetar
        self.reset_button = ttk.Button(button_frame, text="Resetar", command=self.reset_simulation)
        self.reset_button.pack(side=tk.LEFT, padx=5)
        
    def log_message(self, message):
        self.text_area.insert(tk.END, message + "\n")
        self.text_area.see(tk.END)
        self.root.update()
        
    def run_simulation(self):
        self.start_button.config(state='disabled')
        self.text_area.delete(1.0, tk.END)
        
        self.log_message("Iniciando simulação da loteria do Draft da NBA 2025...\n")
        
        # Gerar combinações
        all_combinations = set()
        while len(all_combinations) < 1000:
            combo = tuple(sorted(random.sample(range(1, 15), 4)))
            all_combinations.add(combo)
            
        self.log_message(f"{len(all_combinations)} combinações únicas geradas para o sorteio.")
        
        # Distribuir combinações
        all_combinations = list(all_combinations)
        random.shuffle(all_combinations)
        
        assignment = {}
        index = 0
        for team, num_combos in self.teams.items():
            for _ in range(num_combos):
                assignment[all_combinations[index]] = team
                index += 1
                
        self.log_message("Combinações distribuídas entre os times.\n")
        
        # Sorteio das 4 primeiras escolhas
        selected_teams = set()
        draft_order = []
        
        self.log_message("Sorteando as 4 primeiras escolhas...\n")
        
        while len(draft_order) < 4:
            combo = tuple(sorted(random.sample(range(1, 15), 4)))
            team = assignment.get(combo)
            self.log_message(f"Combinação sorteada: {combo}")
            time.sleep(1)  # Adiciona um pequeno delay para visualização
            
            if team and team not in selected_teams:
                pick_number = len(draft_order) + 1
                draft_order.append((pick_number, team, combo))
                selected_teams.add(team)
                self.log_message(f"Pick #{pick_number}: {team}\n")
            elif team:
                self.log_message(f"{team} já foi sorteado. Ignorando combinação.\n")
            else:
                self.log_message("Combinação não atribuída a nenhum time. Sorteando novamente...\n")
        
        # Preencher o restante da ordem
        self.log_message("Definindo as posições restantes com os times que não foram sorteados...\n")
        remaining_teams = [team for team in self.teams if team not in selected_teams]
        
        for i, team in enumerate(remaining_teams, start=5):
            draft_order.append((i, team, None))
            self.log_message(f"Pick #{i}: {team}")
            time.sleep(0.5)  # Pequeno delay para visualização
        
        self.start_button.config(state='normal')
        
    def reset_simulation(self):
        self.text_area.delete(1.0, tk.END)
        self.start_button.config(state='normal')

if __name__ == "__main__":
    root = tk.Tk()
    app = DraftLotteryGUI(root)
    root.mainloop()