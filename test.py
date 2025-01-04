class Studente:
    def __init__(self, nome, cognome, anno_iscrizione, matricola):
        self.nome = nome
        self.cognome = cognome
        self.anno_iscrizione = anno_iscrizione
        self.matricola = matricola

    def __str__(self):
        return f"{self.nome} {self.cognome} - ({self.matricola})"


class Professore:
    def __init__(self, cognome, email):
        self.cognome = cognome
        self.email = email #ciao

    def __str__(self):
        return f"{self.cognome} - email: {self.email}"


class GestioneStudenti:
    def __init__(self):
        self.studenti_iscritti = []

    def add_studente(self, studente):
        if studente.nome not in [s.nome for s in self.studenti_iscritti]:
            self.studenti_iscritti.append(studente)
        else:
            print(f"Lo studente {studente.nome} è già iscritto al corso.")

    def remove_studente(self, studente):
        for s in self.studenti_iscritti:
            if s.nome == studente.nome:
                self.studenti_iscritti.remove(s)
                return
        print(f"Lo studente {studente.nome} non è iscritto al corso.")

    def get_studenti(self):
        return [f"{studente.nome} {studente.cognome}" for studente in self.studenti_iscritti]


class Corso:
    def __init__(self, nome_corso, professore, gestione_studenti):
        self.nome_corso = nome_corso
        self.professore = professore
        self.gestione_studenti = gestione_studenti

    def change_professore(self, professore):
        self.professore = professore

    def get_professore(self):
        return self.professore

# Franco ciao!
# Oggetti di esempio
Giacomo = Studente("Giacomo", "Franchini", 2008, "GIAFRA2008X")
Lorenza = Studente("Lorenza", "Boldi", 2012, "LORBOL2012B")
Bernardini = Professore("Bernardini", "giovanni.bernardini@studuniroma.it")
gestione_studenti = GestioneStudenti()

# Uso
gestione_studenti.add_studente(Giacomo)
gestione_studenti.add_studente(Lorenza)
Analisi_Tecnica = Corso("Analisi Tecnica", Bernardini, gestione_studenti)

#A schermo
print(Analisi_Tecnica.get_professore())
print(Analisi_Tecnica.gestione_studenti.get_studenti())
