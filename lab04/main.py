from notebook import Notebook

def main():
    notes = Notebook()

    note = input()
    notes.store_note(note)

    note = input()
    notes.store_note(note)

    note = "Quack Quack"
    notes.store_note(note)

    notes.show_note(1)

    notes.remove_note("Quack Quack")

    notes.list_notes()


main()