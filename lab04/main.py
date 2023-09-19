from notebook import Notebook

def main():
    notes = Notebook()

    for i in range(10):
        note = input()
        notes.store_note(note)

    note = "Quack Quack"
    notes.store_note(note)

    print(notes.has_notes())

    notes.show_note(1)

    notes.remove_note("Quack Quack")

    notes.list_notes()

    print(notes.compare_note("Quack Quack"))

    notes.show_note_random()

    notes.show_multi_note_random(5)

main()