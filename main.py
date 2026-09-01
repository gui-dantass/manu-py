# print("Olá.você!")
# nome = "joão"
# senha = input("Digite uma senha: ")
              
# if senha == "abóbora":
#     print("Senha correta!")
# elif senha == "chevette":
#     print("Senha correta!")
# else:
#     print("Senha errada")
print("===BEM-VINDO AO BOT DA MANU===")
opcao = input("Digite um valor de 1 a 10: ")   

match opcao:
    case "1":
        print("Setor de atentimento:")
        print("Qual atendente você deseja falar? Sac ou rh?")

        atendente = input("qual setor de atentimento?:")
        if atendente == "Sac":
            print("Voce vai ser direcionado para o SAC")
        elif atendente == "rh":
            print("Você vai ser direcionado para o rh")
        else:
            print("Não existe esse atendimento...")

    case "2":
        print("Segunda via de boleto: ")
        boleto = input("onde deseja pedir a sua segunda via? whatsapp ou email ")
        if boleto == "whatsapp":
            print("Vamos enviar seu boleto no seu whatsapp:")
        elif boleto == "email":
            print("Vamos enviar seu boleto no seu email: ")
        else:
            print("Opção Invalida no momento: ")

    case "3":
        print("Veja a fatura do cartão")
        cartao = input("qual cartão você deseja ver fatura do cartao Itau ou Bradesco: ")
        if cartao == "Itau":
            print("Vamos de mandar a fatura do seu cartão Itau... Aguarde um momento")
        elif cartao == "Bradesco":
            print("Vamos de mandar a fatura do seu cartão Bradesco... Aguarde um momento")
        else:
            print("A fatura desse cartão está Invalida no momento:")
    case "4":
        print("Veja quanto tem de saldo no seu banco")
        pix = input("Qual banco você quer ver Nubank ou Inter?")
        if pix == "Nubank":
            print("Seu saldo vai aparecer em instantes...")
        elif pix == "Inter":
            print("Seu saldo vai aparecer em instantes...")
        else:
            print("Não existe essa opção")

    case "5":
        print("quanto gastou no cartao esse mês:")
        cartao = input("Qual banco você quer ver Nubank ou Inter?")
        if cartao == "Nubank":
            print("Seu gasto vai aparecer em instantes...")
        elif cartao == "Inter":
            print("Seu gasto vai aparecer em instantes...")

    case "6":
        print("falar com seu parente:")
        parente = input("Você quer falar com seu pai ou sua mãe?:")
        if parente == "pai":
            print("Essa ligação será encaminhada para o telefone do seu pai")
        elif parente == "mae":
             print("Essa ligação será encaminhada para o telefone do seu pai")
        else: 
            print("esse parente não pode atender o telefone nesse momento")

    case "7":
        print("falar com a marlene:")
        marlene = (" Deseja falar sobre oque com ela? suspensão ou advertencia"
        "?")
        if marlene == "suspensao":
            print("Mande mensagem para ela")
        elif marlene == "advertencia":
            print("Entre na sala dela:")
        else:
            print("Ela esta ocupada no momento")

    case "8":
        print("falar com pino:")
        pino = ("deseja falar sobre qual empresa google ou senai")
        if pino == "google":
            print("Fale com ele na sala C1")
        elif pino == "senai":
            print("Fale com ele na secretaria")   
        else:
            print("Fale com ele mais tarde")
        
    case "9":
        print("Argumento para expulsar o luiz do senai")
        luiz = input("Deseja expulsar ele por causa do celular ou do fone?")
        if luiz == "celular":
            print("Tem razão iremos expulsar ele ")
        elif luiz == "fone":
            print("Iremos dar uma advertencia para ele:")
        else:
            print("esse motivo não é suficiente")

    case "10":
        print("Demitir o lucas correa do senai")
        lucas = input("qual o seu motivo? ensina mal ou xinga os alunos: ")
        if lucas == "ensina mal":
            print("Vamos conversar com ele sobre isso")
        elif lucas == "xinga os alunos":
            print("iremos demitir ele")
        else:
            print("não é motivo suficiente")

    case _:
        print("não existe essa opção, digite de 1 a 10:")