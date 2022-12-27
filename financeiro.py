import json
import os

months_list = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro',
               'outubro', 'novembro', 'dezembro')


def save_finances(data_for_save):
    if not os.path.exists('finance.json'):
        finance_file = open('finance.json', 'w')
        json.dump(data_for_save, finance_file, indent=6)
        finance_file.close()
    else:
        finance_file = open('finance.json', 'r')

        with open("finance.json", encoding='utf-8') as finance_json:
            data = json.load(finance_json)
            data_saved = []

            if type(data) == dict:
                data_saved.append(data)
            elif type(data) == list:
                data_saved = data

            if len(data_for_save) > 0:
                for dt in data_for_save:
                    data_saved.append(dt)

            if len(data_saved) > 0:
                finance_file = open('finance.json', 'w')
                json.dump(data_saved, finance_file, indent=6)
                finance_file.close()


def delete_finances():
    while True:
        type_of_delete = input('O que você deseja deletar, gasto ou ganho? ').lower()

        if type_of_delete != 'gasto' and type_of_delete != 'ganho':
            print('Por favor digite somente gasto ou ganho')
            continue
        break

    finance_file = open('finance.json', 'r')

    with open("finance.json", encoding='utf-8') as finance_json:
        data = json.load(finance_json)
        data_saved = []

        if type(data) == dict:
            data_saved.append(data)
        elif type(data) == list:
            data_saved = data

        if len(data_saved) > 0:
            print(f'Digite os dados do {type_of_delete} que deseja excluir')

            while True:
                value = input('Valor: ')
                if not value.isdigit() and not value.replace('.', '', 1).isdigit():
                    print('O valor não pode ser diferente de número')
                    continue
                elif float(value) < 1:
                    print('O valor do ganho não pode ser menor que 1')
                    continue
                break

            while True:
                year = input('Ano: ')
                if not year.isdigit():
                    print('O ano não pode ser diferente de número')
                    continue
                elif len(year) < 4 or len(year) > 4:
                    print('O ano não pode ter menos ou mais que 4 caracteres')
                    continue
                break

            while True:
                month = input('Mês: ')
                if month.isdigit():
                    if int(month) < 1 or int(month) > 12:
                        print('O mês deve estar escrito com o respectivo nome ou em um intervalo de 1 a 12')
                        continue
                    else:
                        month = int(month)
                        break
                if not month.isdigit():
                    if not month.lower() in months_list:
                        print('Mês inválido')
                        continue
                    else:
                        month = months_list.index(month.lower()) + 1
                break

            while True:
                day = input('Dia: ')
                if not day.isdigit():
                    print('O dia não pode ser diferente de número')
                    continue
                elif int(day) < 1 or int(day) > 31:
                    print('O dia deve estar em um intervalo de 1 a 31')
                    continue
                break

            type_delete_finance = input('Tipo: ')

            for dele in data_saved:
                if dele['id'] == 'ganho':
                    if dele['Valor'] == float(value) and dele['Ano'] == int(year) and dele['Mes'] == int(month) and \
                            dele['Dia'] == int(day) and dele['Tipo de Ganho'] == type_delete_finance:
                        finance_index = data_saved.index(dele)
                        data_saved.pop(finance_index)
                        break

                elif dele['id'] == 'gasto':
                    if dele['Valor']['valor'] == float(value) and dele['Ano'] == int(year) and dele['Mes'] == int(
                            month) and dele['Dia'] == int(day) and dele['Tipo de Gasto'] == type_delete_finance:
                        finance_index = data_saved.index(dele)
                        data_saved.pop(finance_index)
                        break

        if len(data_saved) > 0:
            finance_file = open('finance.json', 'w')
            json.dump(data_saved, finance_file, indent=6)
            finance_file.close()


def edit_finances():
    while True:
        type_of_edit = input('O que você deseja editar, gasto ou ganho? ').lower()

        if type_of_edit != 'gasto' and type_of_edit != 'ganho':
            print('Por favor digite somente gasto ou ganho')
            continue
        break

    finance_file = open('finance.json', 'r')

    with open("finance.json", encoding='utf-8') as finance_json:
        data = json.load(finance_json)
        data_saved = []

        if type(data) == dict:
            data_saved.append(data)
        elif type(data) == list:
            data_saved = data

        if len(data_saved) > 0:
            print(f'Digite os dados do {type_of_edit} que deseja editar')

            while True:
                value = input('Valor: ')
                if not value.isdigit() and not value.replace('.', '', 1).isdigit():
                    print('O valor não pode ser diferente de número')
                    continue
                elif float(value) < 1:
                    print('O valor do ganho não pode ser menor que 1')
                    continue
                break

            while True:
                year = input('Ano: ')
                if not year.isdigit():
                    print('O ano não pode ser diferente de número')
                    continue
                elif len(year) < 4 or len(year) > 4:
                    print('O ano não pode ter menos ou mais que 4 caracteres')
                    continue
                break

            while True:
                month = input('Mês: ')
                if month.isdigit():
                    if int(month) < 1 or int(month) > 12:
                        print('O mês deve estar escrito com o respectivo nome ou em um intervalo de 1 a 12')
                        continue
                    else:
                        month = int(month)
                        break
                if not month.isdigit():
                    if not month.lower() in months_list:
                        print('Mês inválido')
                        continue
                    else:
                        month = months_list.index(month.lower()) + 1
                break

            while True:
                day = input('Dia: ')
                if not day.isdigit():
                    print('O dia não pode ser diferente de número')
                    continue
                elif int(day) < 1 or int(day) > 31:
                    print('O dia deve estar em um intervalo de 1 a 31')
                    continue
                break

            type_edit_finance = input('Tipo: ')

            for dele in data_saved:
                if dele['id'] == 'ganho':
                    if dele['Valor'] == float(value) and dele['Ano'] == int(year) and dele['Mes'] == int(month) and \
                            dele['Dia'] == int(day) and dele['Tipo de Ganho'] == type_edit_finance:
                        print(f'Digite os novos dados do {type_of_edit} que deseja editar')

                        while True:
                            new_value = input('Valor: ')
                            if not new_value.isdigit() and not new_value.replace('.', '', 1).isdigit():
                                print('O valor não pode ser diferente de número')
                                continue
                            elif float(new_value) < 1:
                                print('O valor do ganho não pode ser menor que 1')
                                continue
                            break

                        while True:
                            new_year = input('Ano: ')
                            if not new_year.isdigit():
                                print('O ano não pode ser diferente de número')
                                continue
                            elif len(new_year) < 4 or len(new_year) > 4:
                                print('O ano não pode ter menos ou mais que 4 caracteres')
                                continue
                            break

                        while True:
                            new_month = input('Mês: ')
                            if new_month.isdigit():
                                if int(new_month) < 1 or int(new_month) > 12:
                                    print('O mês deve estar escrito com o respectivo nome ou em um intervalo de 1 a 12')
                                    continue
                                else:
                                    new_month = int(new_month)
                                    break
                            if not new_month.isdigit():
                                if not new_month.lower() in months_list:
                                    print('Mês inválido')
                                    continue
                                else:
                                    new_month = months_list.index(new_month.lower()) + 1
                            break

                        while True:
                            new_day = input('Dia: ')
                            if not new_day.isdigit():
                                print('O dia não pode ser diferente de número')
                                continue
                            elif int(new_day) < 1 or int(new_day) > 31:
                                print('O dia deve estar em um intervalo de 1 a 31')
                                continue
                            break

                        new_type_finance = input('Tipo: ')
                        new_obs = input('Observação: ')

                        dele.update({'Valor': float(new_value)})
                        dele.update({'Ano': int(new_year)})
                        dele.update({'Mes': int(new_month)})
                        dele.update({'Dia': int(new_day)})
                        dele.update({'Tipo de Ganho': new_type_finance})
                        dele.update({'Obs': new_obs})

                        break

                elif dele['id'] == 'gasto':
                    if dele['Valor']['valor'] == float(value) and dele['Ano'] == int(year) and dele['Mes'] == int(
                            month) and dele['Dia'] == int(day) and dele['Tipo de Gasto'] == type_edit_finance:
                        print(f'Digite os novos dados do {type_of_edit} que deseja editar')

                        while True:
                            new_value = input('Valor: ')
                            if not new_value.isdigit() and not new_value.replace('.', '', 1).isdigit():
                                print('O valor não pode ser diferente de número')
                                continue
                            elif float(new_value) < 1:
                                print('O valor do ganho não pode ser menor que 1')
                                continue
                            break

                        while True:
                            new_year = input('Ano: ')
                            if not new_year.isdigit():
                                print('O ano não pode ser diferente de número')
                                continue
                            elif len(new_year) < 4 or len(new_year) > 4:
                                print('O ano não pode ter menos ou mais que 4 caracteres')
                                continue
                            break

                        while True:
                            new_month = input('Mês: ')
                            if new_month.isdigit():
                                if int(new_month) < 1 or int(new_month) > 12:
                                    print('O mês deve estar escrito com o respectivo nome ou em um intervalo de 1 a 12')
                                    continue
                                else:
                                    new_month = int(new_month)
                                    break
                            if not new_month.isdigit():
                                if not new_month.lower() in months_list:
                                    print('Mês inválido')
                                    continue
                                else:
                                    new_month = months_list.index(new_month.lower()) + 1
                            break

                        while True:
                            new_day = input('Dia: ')
                            if not new_day.isdigit():
                                print('O dia não pode ser diferente de número')
                                continue
                            elif int(new_day) < 1 or int(new_day) > 31:
                                print('O dia deve estar em um intervalo de 1 a 31')
                                continue
                            break

                        new_type_finance = input('Tipo: ')
                        new_obs = input('Observação: ')

                        dele['Valor'].update({'valor': float(new_value)})
                        dele.update({'Ano': int(new_year)})
                        dele.update({'Mes': int(new_month)})
                        dele.update({'Dia': int(new_day)})
                        dele.update({'Tipo de Ganho': new_type_finance})
                        dele.update({'Obs': new_obs})

                        break

        if len(data_saved) > 0:
            finance_file = open('finance.json', 'w')
            json.dump(data_saved, finance_file, indent=6)
            finance_file.close()


def show_historic():
    print('Para buscar um histórico, digite o mês e depois o ano desejado')

    try:
        finance_file = open('finance.json', 'r')
        with open("finance.json", encoding='utf-8') as finance_json:
            data = json.load(finance_json)

            while True:
                filter_month = input('Digite o mês: ')
                if filter_month.isdigit():
                    if int(filter_month) < 1 or int(filter_month) > 12:
                        print('O mês deve estar escrito com o respectivo nome ou em um intervalo de 1 a 12')
                        continue
                    else:
                        filter_month = int(filter_month)
                        break
                if not filter_month.isdigit():
                    if not filter_month.lower() in months_list:
                        print('Mês inválido')
                        continue
                    else:
                        filter_month = months_list.index(filter_month.lower()) + 1
                    break

            while True:
                filter_year = input('Digite o ano: ')
                if not filter_year.isdigit():
                    print('O ano não pode ser diferente de número')
                    continue
                elif len(filter_year) < 4 or len(filter_year) > 4:
                    print('O ano não pode ter menos ou mais que 4 caracteres')
                    continue
                break

            filtered_historic = []

            for dt in data:
                if dt['Ano'] == int(filter_year) and dt['Mes'] == filter_month:
                    filtered_historic.append(dt)

            print(f'Histórico {filter_month}/{filter_year}'.center(60, '-'))
            if len(filtered_historic) == 0:
                print('Nenhum Histórico encontrado')
                print(60 * "-")
            else:
                for result in filtered_historic:
                    if result['id'] == 'gasto':
                        print(
                            f'Gasto | {result["Tipo de Gasto"]} = R$ {result["Valor"]["valor"]} /  parcela ({result["Valor"]["parcela"]})')
                        print(60 * "-")
                    else:
                        print(f'Ganho | {result["Tipo de Ganho"]}  = R$  {result["Valor"]}')
                        print(60 * "-")
    except:
        print('Ooops, nada encontrado!')


def user_gain():
    print('Cadastre um ganho\n')

    while True:

        value = input('Valor: ')
        if not value.isdigit() and not value.replace('.', '', 1).isdigit():
            print('O valor não pode ser diferente de número')
            continue
        elif float(value) < 1:
            print('O valor do ganho não pode ser menor que 1')
            continue

        while True:
            year = input('Ano: ')
            if not year.isdigit():
                print('O ano não pode ser diferente de número')
                continue
            elif len(year) < 4 or len(year) > 4:
                print('O ano não pode ter menos ou mais que 4 caracteres')
                continue
            break

        while True:
            month = input('Mês: ')
            if month.isdigit():
                if int(month) < 1 or int(month) > 12:
                    print('O mês deve estar escrito com o respectivo nome ou em um intervalo de 1 a 12')
                    continue
                else:
                    month = int(month)
                    break
            if not month.isdigit():
                if not month.lower() in months_list:
                    print('Mês inválido')
                    continue
                else:
                    month = months_list.index(month.lower()) + 1
            break

        while True:
            day = input('Dia: ')
            if not day.isdigit():
                print('O dia não pode ser diferente de número')
                continue
            elif int(day) < 1 or int(day) > 31:
                print('O dia deve estar em um intervalo de 1 a 31')
                continue
            break

        type_gain = input('Tipo: ')
        obs = input('Observação: ')

        gain = {'id': 'ganho', 'Ano': int(year), 'Mes': month, 'Dia': int(day), 'Valor': float(value),
                'Tipo de Ganho': type_gain,
                'Obs': obs}

        return gain


def user_spent():
    print('Cadastre um gasto\n')

    while True:
        division_spent = input('Deseja cadastrar uma recorrência em meses? (s/n) ')

        if division_spent.lower() != 's' and division_spent.lower() != 'n':
            print('Por favor digite apenas s ou n\n')
            continue
        break

    while True:
        if division_spent == 's':
            value = input('Digite o valor da parcela: ')
            if not value.isdigit() and not value.replace('.', '', 1).isdigit():
                print('O valor não pode ser diferente de número')
                continue
            elif float(value) < 1:
                print('O valor do gasto não pode ser menor que 1')
                continue
            if value.isdigit():
                month_qtd = input('Digite a quantidade de parcerlas: ')
                if not month_qtd.isdigit():
                    continue
            break
        else:
            value = input('Valor: ')
            if not value.isdigit() and not value.replace('.', '', 1).isdigit():
                print('O valor não pode ser diferente de número')
                continue
            elif float(value) < 1:
                print('O valor do gasto não pode ser menor que 1')
                continue
            break

    while True:
        year = input('Ano: ')
        if not year.isdigit():
            print('O ano não pode ser diferente de número')
            continue
        elif len(year) < 4 or len(year) > 4:
            print('O ano não pode ter menos ou mais que 4 caracteres')
            continue
        break

    validate = True
    while validate:
        month = input('Mês: ')
        if month.isdigit():
            if int(month) < 1 or int(month) > 12:
                print('O mês deve estar escrito com o respectivo nome ou em um intervalo de 1 a 12')
                continue
            else:
                month = int(month)
                break
        if not month.isdigit():
            if not month.lower() in months_list:
                print('Mês inválido')
                continue
            else:
                month = months_list.index(month.lower()) + 1
        break

    while True:
        day = input('Dia: ')
        if not day.isdigit():
            print('O dia não pode ser diferente de número')
            continue
        elif int(day) < 1 or int(day) > 31:
            print('O dia deve estar em um intervalo de 1 a 31')
            continue
        break

    type_spent = input('Tipo: ')
    obs = input('Observação: ')

    if division_spent == 's':
        spent = []
        if type(month) == int:
            month = month
            for mon in range(int(month_qtd)):
                spent.append(
                    {'id': 'gasto', 'Ano': int(year), 'Mes': month, 'Dia': int(day),
                     'Valor': {'valor': float(value), 'parcela': int(mon) + 1}, 'Tipo de Gasto': type_spent,
                     'Obs': obs})
                if month + 1 > 12:
                    month = 1
                    year = int(year)
                    year += 1
                else:
                    month += 1
    else:
        spent = {'id': 'gasto', 'Ano': int(year), 'Mes': month, 'Dia': int(day),
                 'Valor': {'valor': float(value), 'parcela': ''}, 'Tipo de Gasto': type_spent, 'Obs': obs}

    return spent


def show_menu():
    gain_list = []
    spent_list = []

    total_gain = 0
    total_spent = 0

    while True:
        finance = 'Financeiro'

        print(finance.center(60, '-'))
        print(f'| Digite 1 para cadastrar ganhos {25 * " "} |\n')
        print(f'| Digite 2 para cadastrar gastos {25 * " "} |\n')
        print(f'| Digite 3 para ver histórico por mês {20 * " "} |\n')
        print(f'| Digite 4 para deletar gastos/ganhos {20 * " "} |\n')
        print(f'| Digite 5 para editar gastos/ganhos {21 * " "} |')
        print(60 * "-")
        option = input('Digite aqui a opção desejada: ')

        if option != '1' and option != '2' and option != '3' and option != '4' and option != '5':
            print('Por favor digite 1, 2,3 ou 4 somente\n')
            continue

        new_gain = ''
        new_spent = ''

        if option == '1':
            new_gain = user_gain()
        elif option == '2':
            new_spent = user_spent()
        elif option == '3':
            show_historic()
        elif option == '4':
            delete_finances()
        elif option == '5':
            edit_finances()

            while True:

                exit_his = input('Deseja fazer uma nova operação? (s/n) ')
                print('')

                if exit_his != 's' and exit_his != 'n':
                    print('Por favor digite apenas s ou n\n')
                    continue
                break

            if exit_his == 's':
                continue
            else:
                return

        if new_gain:
            gain_list.append(new_gain)
        if new_spent:
            if type(new_spent) == list:
                spent_list = new_spent
            else:
                spent_list.append(new_spent)

        if len(gain_list) > 0:
            save_finances(gain_list)

        if len(spent_list) > 0:
            save_finances(spent_list)

        while True:

            exit = input('Deseja fazer uma nova operação? (s/n) ')
            print('')

            if exit != 's' and exit != 'n':
                print('Por favor digite apenas s ou n\n')
                continue
            break

        if exit == 's':
            continue
        else:
            break

    finance_file = open('finance.json', 'r')
    with open("finance.json", encoding='utf-8') as finance_json:
        data = json.load(finance_json)

        if len(data) > 0:
            for finance_value in data:
                if finance_value['id'] == 'ganho':
                    total_gain += finance_value['Valor']
                else:
                    total_spent += finance_value['Valor']['valor']

        total_value = total_gain - total_spent
        print('')
        print(f'Valor total em conta: {total_value} ')
        print('Tipos de Gastos'.center(60, '-'))
        if total_spent == 0:
            print('Nenhum gasto encontrado')
            print(60 * "-")
        else:
            for spent_type in data:
                if spent_type['id'] == 'gasto':
                    print(
                        f'{spent_type["Tipo de Gasto"]} = {spent_type["Valor"]["valor"]}  {spent_type["Valor"]["parcela"]}')
                    print(60 * "-")


show_menu()
