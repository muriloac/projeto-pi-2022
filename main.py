import PySimpleGUI as sg
from Mysql import Mysql
import generate
import os


def make_main():
    layout = [[sg.Text('PROJETO DE PI - MURILO')], [sg.Text('Escolha alguma ação:')],
              [sg.Button('Insert All'), sg.Button('Truncate All'), sg.Button('Abrir Power BI')],
              [sg.Text('')],
              [sg.Button('Sair', button_color=('white', 'firebrick4'))]]
    return sg.Window('Pagina Inicial', layout, location=(800, 600), size=(300, 150), finalize=True,
                     element_justification='c')


def make_insert():
    layout = [[sg.Text('INSERT')],
              [sg.Text('Escolha alguma ação:')],
              [sg.Button('Inserir'), sg.Button('Voltar para Pagina Inicial')],
              [sg.ProgressBar(sum([len(element) for element in generate.get_data_ranges()]), orientation='h',
                              size=(20, 20), key='progressbarInsert')]]
    return sg.Window('Insert All', layout, location=(800, 600), finalize=True)


def make_truncate():
    layout = [[sg.Text('TRUNCATE')],
              [sg.Text('Escolha alguma ação:')],
              [sg.Button('Limpar Tabela'), sg.Button('Voltar para Pagina Inicial')]]
    return sg.Window('Truncate All', layout, location=(800, 600), finalize=True)


mysql = Mysql('root', 'Murilo@14', 'localhost', 'g2_pi')

mysql.connect()

window1, window2, window3 = make_main(), None, None
while True:
    window, event, values = sg.read_all_windows()
    if event == sg.WIN_CLOSED or event == 'Sair':
        window.close()
        if window == window3:
            window3 = None
        if window == window2:
            window2 = None
        elif window == window1:
            break
    elif event == 'Insert All':
        window1.close()
        window2 = make_insert()
    elif event == 'Truncate All':
        window1.close()
        window3 = make_truncate()
    elif event == 'Voltar para Pagina Inicial':
        if window == window2:
            window2.close()
        if window == window3:
            window3.close()
        window1 = make_main()
    elif event == 'Inserir':
        progress_bar = window['progressbarInsert']
        dados = generate.generate_data()
        count = 0
        for valores in dados:
            mysql.insert(valores)
            count += 1
            progress_bar.UpdateBar(count)
    elif event == 'Limpar Tabela':
        value = mysql.truncate()
        if value:
            sg.Popup('Tabela Limpa com Sucesso!')
        else:
            sg.Popup('Erro ao Limpar Tabela!')
    elif event == 'Abrir Power BI':
        sg.Popup('Abrindo Power BI')
        filepath = 'graficos.pbix'
        os.startfile(filepath)
mysql.close()
window.close()
