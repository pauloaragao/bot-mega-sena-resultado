from action import search_google, get_numbers, back_page, open_url

menu_options = {
    1: 'Rodar somente uma busca',
    2: 'Personalize sua busca',
    3: 'Sobre o desenvolvedor',
    4: 'Exit',
}


def print_menu():
    print ("Bot Mega Sena com Python e Selenium")
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

def option1():
    open_url()
    search_google()
    get_numbers()
    phrase_search = "Mega-Sena/Concurso "
    number_prizedraw = number_prizedraw + 1
    back_page()

def option2():
     print('Escolhida Opcao 2')

def option3():
     print('Escolhida Opcao 3')

if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Entre com sua escolha: '))
        except:
            print('Entrada errada, entre com um numero valido ...')
        if option == 1:
           option1()
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif option == 4:
            print('Muito obrigado por testar esse codigo')
            exit()
        else:
            print('Invalida entrada, entre com valores validos de 1 a 4 somente. :)')
