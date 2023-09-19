import random


class Notebook:
    def __init__(self):
        self.__notes = []

    def store_note(self, note):
        self.__notes.append(note)

    def number_of_notes(self):
        return len(self.__notes)

    def show_note(self, note_number):
        if note_number < 0:
            print("Este não é um número de nota válido")
        elif note_number < self.number_of_notes():
            print(self.__notes[note_number])
        else :
            print("Este não é um número de nota válido")

    def remove_note(self, note):
        if note in self.__notes:
            self.__notes.remove(note)
        else:
            print("Esta não é uma nota válida")

    def list_notes(self):
        for note in self.__notes:
            print(note)

    def has_notes(self):
        return self.number_of_notes() != 0
    
    def compare_note(self, note):
        return note in self.__notes

    def show_note_random(self):
        number = random.randint(0, self.number_of_notes())
        self.show_note(number)

    def show_multi_note_random(self, amount):
        count = 0
        while count < amount:
            self.show_note_random()
            count += 1
