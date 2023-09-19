from notebook import Notebook

def main():
    notes = Notebook()

    notes.store_note("Never Gonna Give You Up")
    notes.store_note("Big Crack Like Bunda")
    notes.store_note("Quack Quack")

    notes.show_note(1)

    notes.remove_note("Quack Quack")

    notes.list_notes()


main()