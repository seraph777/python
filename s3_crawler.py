# Jorge Alberto de Oliveira
# oliveira.jorgealberto@gmail.com
# Linkedin: https://www.linkedin.com/in/oliveirajorgealberto/
# Cel/WhatsUp: 11987847967
# versao Python utilizada: Python 2.7.17

# Data de criacao: 21/04/2020


#Obs.: Eh obvio, mas nao custa dizer, tem que configurar as credentials do aws configure antes de tudo ...


#### Modulos utilizados
import boto3
import os
import platform




#### Variaveis
op = ''
client = boto3.client('s3')
response = client.list_buckets()

#### Funcoes

def nome_bucket():
        for bucket in response["Buckets"]:
            print('{}'.format(bucket['Name']))
        ss3 = boto3.resource ('s3')
        count_obj = 0
        bucket = ss3.Bucket (bucket['Name'])
def get_matching_s3_keys(bucket, prefix='', suffix=''):
    s3 = boto3.client ('s3')
    kwargs = {'Bucket': bucket}
    if isinstance (prefix, str):
        kwargs['Prefix'] = prefix

    while True:
        resp = s3.list_objects_v2 (**kwargs)
        for obj in resp['Contents']:
            key = obj['Key']
            if key.startswith (prefix) and key.endswith (suffix):
                yield key
        try:
            kwargs['ContinuationToken'] = resp['NextContinuationToken']
        except KeyError:
            break

def limpatela():
    plataforma = str (platform.system())
    if plataforma == "Linux":
        os.system('clear')
    else:
        os.system('cls')

limpatela()


#### Menu

while True:
    print "\n"
    print ('Olah caro Devops, escolha sua opcao:')
    print ('')
    print ('1. Listar nome dos S3 ')
    print ('2. Listar nome e data criacao dos S3 ')
    print ('3. Listar nome e quantidade de Objetos do S3 ')
    print ('4. Lista arquivos do s3 com extensao desejada, formato: ex: .txt .docx .jpg  ?')
    print ('5. Precos ')
    print ('99. Sair do s3_crawler')
    print ('')
    print ('Escolha uma opcao: ')

### Leitura do input

    op = raw_input('Escolha.: ')
    digito = (type (op) is str)
    if digito == False:
        limpatela()
        break

#### onde a brincadeira comeca

    else:
        if op == "1":
            nome_bucket()
        if op == "2":
            for bucket in response["Buckets"]:
                print('S3 name; {}; Created; {}'.format (
                    bucket['Name'], bucket['CreationDate']))
                ss3 = boto3.resource('s3')
                count_obj = 0
                bucket = ss3.Bucket (bucket['Name'])
            print '\n'
            print '\n'
        if op == "3":
            for bucket in response["Buckets"]:

                print('S3 name; {}; Created; {}'.format(
                        bucket['Name'], bucket['CreationDate']))
                ss3 = boto3.resource('s3')
                count_obj = 0
                bucket = ss3.Bucket(bucket['Name'])
                for i in bucket.objects.all():
                    count_obj = count_obj + 1
                print("Objects; " + str(count_obj))
                print ("============ Proximo ============")
            print '\n'
            print '\n'
        if op == "4":
            nome_bucket()
            print "\n"
            meu_balde = raw_input("Qual o nome do S3: ")
            extensao = raw_input("Qual extensao: ")
            try:
                for key in get_matching_s3_keys (bucket=meu_balde, suffix=(extensao)):
                    print(key)
            except:
                print "Ajuda ai neh, que tal usar um bucket valido ?"
                print "\n"
                nome_bucket()
                print "\n"
        if op == "5":
            print "Favor consultar o billing em:\n "
            print "https://console.aws.amazon.com/billing/home?region=us-east-1#/"
        if op == "99":
            limpatela()
            print ".................................................................................."
            print ".....................................&#..........................................."
            print ".................................%%@*..@&*@@@@@..................................."
            print ".............................&/@@&&..@.@@@@@&....................................."
            print "...........................#@@@@@/@@@@@@@@@@@@@@&................................."
            print ".........................*@@@@@@@&(@@@@@@&@@@@/.@@@.%............................."
            print ".........................&@@@&@@@/@@@&@@@&@@(&@@@&@@@*............................"
            print "...................../...@@@@@@@@&@@@@@@@@@@@@@@@@@@@@@&.........................."
            print "......................&@.@@@@@@@@&@@@@@@@@@@@@@@@&@@@@@@@#........................"
            print ".......................@@@@@@@@@@&@@@@@@@@@@@@@@@@@@@@@@@@@@......................"
            print "......................#@@&@@@@@@@&@@@@@@@&@@@@@@@&@@@@@@@&@@%*...................."
            print ".....................@@@@@@@&....&@@@@@@@@@@@@@#........@@@@@*...................."
            print "....................@@@@@@@#................./@@@&@@@....@@@@%...................."
            print "....................@(@@@@@@...........................@.%@@@@...................."
            print "......................@&@&@&@&@&(..............%@&@&@&@&@.@&@&...................."
            print ".......................@@@@@@........./@@@@@@...........@@@@......................"
            print "........................&@@@&........../@...@...........@@@@......................"
            print "..........................&@@..........@&...&@*.......*@@@@......................."
            print "..........................@@.&@.....@@@.......&@@&@@@@*.@&@......................."
            print "...........................@@..........................@@@........................"
            print "...........................@@@@.....(#&......%@@@&/&@@@@@@........................"
            print "............................@@@@@&@@@@@@@@@@@@@@@@@@@@@@.........................."
            print ".............................&@@@&@@@&@@&.(&@#.....@@&@@.........................."
            print "...............................@@&@@............&@@@@@@..........................."
            print "...............................&@&@@@(...@@@@.(@@&@@@............................."
            print "..................................&@@@@@@@@@@&@@@@@@.............................."
            print "....................................&@@@@&@@@@@@@&@..............................."
            print "..........................................&**.*..................................."
            print ".................................................................................."
            print "..................%@@.@@@@@@@@@@@@@(.............................................."
            print ".........*(@@@@@@@@@@@@@@@@@@@@@@@@@@@@#.........................................."
            print "........@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@..........*#@@@@@@@@@@@@@@@@@@.........."
            print "..........@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&.......@@@@@@@@@@@@@@@@@@@............"
            print "............&@@@@/.........#@@@@@@@@@@@@@@@@@.......*@@@@@@@@@@@@@................"
            print "........................@@@@@@@@@@@@@@@@@@@@&.........%@@@@@@....................."
            print ".....................@@@@@@@@@@@@@@@@@@@@@%......................................."
            print ".................&@@@@@@@@@@@@@@@@@@@@@,.........................................."
            print "..............%@@@@@@@@@@@@@@@@@@@@............./((*.............................."
            print "...........(@@@@@@@@@@@@@@@@@@@.........*@@@@@@@@@@@@@@@@........................."
            print "........@@@@@@@@@@@@@@@@@@@@.........@@@@@@@@@@@@@@@@@@@@@@......................."
            print "...../@@@@@@@@@@@@@@@@@@...........@@@@@@@@@@@@@@@@@@@@@@@@@......................"
            print "....#@@@@@@@@@@@@@@@@@.............@@@@@@@@@@@@@*....@@@@@@@@#...................."
            print "..@@@@@@@@@@@@@@@@................@@@@@@@@@@%....@@@@@@@@@@......................."
            print "%@@@@@@@@@@@@&....................@@@@@@@@*.#@@@@@@@@@@@@........................."
            print "@@@@@@@@@@@@.......................@@@@@@@@@@@@@@@@@@@............................"
            print ".@@@@@@@@@%..................##&@@@@@@@@@@@@@@@@@@,.....,%@@@@@@@ ................"
            print "..,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&...................."
            print "....@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%   @@@@@@@@@@@@@@@.........................."
            print ".......,@@@@@@@@@@@@@@@@@@#*,....................................................."
            print ".................................................................................."

            break
