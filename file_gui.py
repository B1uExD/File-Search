import PySimpleGUI as psg
psg.ChangeLookAndFeel('Dark')


class FileSearchGui:
    def __init__(self):
        self.layout = [[psg.Text('Search Term', size=(10, 1)),
                             psg.Input(size=(50, 1), focus=True, key='TERM'),
                             psg.Radio('Contains', group_id='choice', key='CONTAINS', default=True),
                             psg.Radio('Starts with', group_id='choice', key='STARTSWITH'),
                             psg.Radio('Ends with', group_id='choice', key='ENDSWITH')],
                            [psg.Text('Root Path', size=(10, 1)),
                             psg.Input('C:/', size=(50, 1), key='PATH'),
                             psg.FolderBrowse('Browse', size=(10, 1)),
                             psg.Button('Re-Index', size=(10, 1), key='B_INDEX'),
                             psg.Button('Search', size=(10, 1), bind_return_key=True, key='B_SEARCH')],
                            [psg.Output(size = (110, 30))]]
        self.window = psg.Window('File Search Engine').Layout(self.layout)


def test2():
    fsg = FileSearchGui()
    while True:
        event, values = fsg.window.Read()
        print(event, values)

#test2()

