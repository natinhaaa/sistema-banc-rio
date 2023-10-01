from classes import *
import os

def Main():

    banco = Banco_Brasil()
    contID = 00

    while True:

        try:
            print("Você está no banco do Brasil!")
            print("Vocé é:")
            print("1. Cliente\n2. Administrador")
            opção = int(input("Qual valor deseja? > "))
            os.system("cls")

            match opção:

                case 1:
                    print("===Login Cliente===")
                    nome_L = input("Digite seu nome: ").upper()
                    id_L = int(input("Digite seu ID: "))
                    os.system("cls")

                    match banco.LoginCliente(id_L, nome_L):

                        case 1:

                            while True:
                                print(f"===Bem vindo {banco.getNome(id_L)}===")
                                print(f"Saldo disponível: {banco.getSaldo(id_L)}")
                                print("1. Transferência\n2. Saque\n3. Depósito \n4. Sair")
                                função = int(input("O que você deseja fazer?\n> "))
                                os.system("cls")

                                match função:

                                    case 1:
                                        print("Essa é a área de TRANSFERÊNCIA")
                                        destinatário = int(input("Digite o ID do destinário que você deseja enviar o valor: "))
                                        valor = float(input("Digite o valor que deseja transferir: R$"))
                                        banco.Transferência(id_L, destinatário, valor)
                                        os.system("pause")
                                        os.system("cls")
                                
                                    case 2:
                                        print("Essa é a área de SAQUE")
                                        valor = float(input("Digite o valor que deseja sacar: R$"))
                                        banco.Saque(id_L, valor)
                                        os.system("pause")
                                        os.system("cls")
                                
                                    case 3:
                                        print("Essa é a área de DEPÓSITO")
                                        valor = float(input("Digite o valor que deseja depositar: R$"))
                                        banco.Depósito(id_L, valor)
                                        os.system("pause")
                                        os.system("cls")

                                    case 4:
                                        break

                                    case _:
                                        print("A opção não existe")
                                        os.system("pause")
                                        os.system("cls")
                                        
                        case _:
                            print("ID ou nome incorretos")
                            os.system("pause")
                            os.system("cls")

                case 2:
                    print("===Login ADM===")
                    nome_A = input("Digite seu nome: ").upper()
                    senha_A = int(input("Digite sua senha: "))
                    os.system("cls")

                    match banco.LoginAdms(nome_A, senha_A):

                        case 1:

                            while True:
                                print(f"===Bem vindo {nome_A}===")
                                print("1. Criar Cliente \n2. Listar Clientes \n3. Excluir Cliente \n4. Atualizar Dados \n5. Criar ADM \n6. Listar ADMs \n7. Excluir ADM \n8. Sair")
                                função = int(input("O que você deseja fazer? > "))
                                os.system("cls")

                                match função:

                                    case 1:
                                        print("Essa é a área de CRIAR CONTA")
                                        contID += 1
                                        nome = input("Nome do usuário: ").upper()
                                        rg = int(input("RG: "))
                                        cep = int(input("CEP: "))
                                        banco.CadastrarClientes(nome, rg, cep, contID)
                                        os.system("pause")
                                        os.system("cls")
                                    
                                    case 2:
                                        print("===Lista de Clientes===")
                                        banco.ListarClientes()
                                        os.system("pause")
                                        os.system("cls")

                                    case 3:
                                        print("===EXCLUIR CONTA===\n")
                                        banco.ListarClientes()
                                        conta = int(input("\nQual ID da conta você deseja excluir? "))
                                        banco.ExcluirClientes(conta)
                                        os.system("pause")
                                        os.system("cls")
                                    
                                    case 4:
                                        print("===ATUALIZAR DADOS===")
                                        id_M = int(input("Informe o ID do cliente: "))
                                        print("O que você deseja atualizar? \n1 - Nome \n2 - RG \n3 - CEP")
                                        conta = int(input("Qual item você deseja atualizar? "))
                                        os.system("pause")
                                        os.system("cls")

                                        match conta:

                                            case 1:
                                                nome_NU = input("Digite um novo nome: ")
                                                nome_N = nome_NU.upper()
                                                banco.setNome(id_M, nome_N)
                                                print("Novo nome registrado.")
                                                os.system("pause")
                                                os.system("cls")

                                            case 2:
                                                rg_N = input("Digite um novo RG: ")
                                                banco.setRG(id_M, rg_N)
                                                print("Novo RG registrado.")
                                                os.system("pause")
                                                os.system("cls")

                                            case 3:
                                                cep_N = input("Digite um novo CEP: ")
                                                banco.setCEP(id_M, cep_N)
                                                print("Novo CEP registrado.")
                                                os.system("pause")
                                                os.system("cls")
                                            
                                            case _:
                                                print("A opção não existe.")
                                                os.system("pause")
                                                os.system("cls")

                                    case 5:
                                        print("===Criar ADM==")
                                        nome_AD = input("Digite o nome: ").upper()
                                        senha_AD = int(input("Digite a senha: "))
                                        banco.AdicionarAdms(nome_AD, senha_AD)
                                        print("ADM adicionado.")
                                        os.system("pause")
                                        os.system("cls")

                                    case 6:
                                        print("===Lista de AMDs===")
                                        banco.ListarAdms()
                                        os.system("pause")
                                        os.system("cls")

                                    case 7:
                                        print("===Excluir ADM===")
                                        banco.ListarAdms()
                                        vetor = int(input("Digite o ID do ADM a ser excluido: "))
                                        banco.ExcluirAdms(vetor)
                                        print("ADM excluído.")
                                        os.system("pause")
                                        os.system("cls")

                                    case 8:
                                        break

                                    case _:
                                        print("A opção não existe.")
                                        os.system("pause")
                                        os.system("cls")
                        case _:
                            print("Nome ou senha incorretos.")
                            os.system("pause")
                            os.system("cls")

                case _:
                    print("Opção Inválida.")
                    os.system("pause")
                    os.system("cls")

        except Exception as erro:
            print("Valor inválido.")
            print(erro.__class__.__name__)
            os.system("pause")
            os.system("cls")