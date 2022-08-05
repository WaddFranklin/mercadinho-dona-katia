class Color:
    SUCCESS = '\033[92m'  # green
    WARNING = '\033[93m'  # yellow
    DANGER = '\033[91m'   # red
    RESET = '\033[0m'     # default

def printListAsTable(title, list):
    if len(list) == 0:
        print(f"{Color.WARNING} --- Nao ha produtos em estoque! ---{Color.RESET}")
    else:
        strHeader = "| {:>2} {:>20} {:>10} {:>13} {:>20} {:>20} {:>15} {:>10} {:>15} {:>20} |".format('id', 'nome', 'tipo', 'preco (R$)', 'marca', 'data_vencimento', 'data_adicao', 'peso (g)', 'volume (ml)', 'quantidade (unid.)')
        strHeaderSize = len(strHeader)
        titleSize = len(title)
        space = int((strHeaderSize - titleSize) / 2)
        
        print('+' + '-'*(strHeaderSize - 2) + '+')
        print('|' + ' '*space + title + ' '*(space - 1) + '|')
        print('+' + '-'*(strHeaderSize - 2) + '+')
        print(strHeader)
        print('+' + '-'*(strHeaderSize - 2) + '+')
        
        for produto in list:
            keyValue = produto.__dict__
            str = "| {:>2} {:>20} {:>10} {:>13,.2f} {:>20} {:>20} {:>15} {:>10} {:>15} {:>20} |".format(
                keyValue["id"],
                keyValue["nome"],
                keyValue["tipo"],
                keyValue["preco"],
                keyValue["marca"],
                keyValue["data_vencimento"].strftime('%d/%m/%Y'),
                keyValue["data_adicao"].strftime('%d/%m/%Y'),
                keyValue["peso"] if "peso" in produto.__dict__.keys() else "",
                keyValue["volume"] if "volume" in produto.__dict__.keys() else "",
                keyValue["quantidade"] if "quantidade" in produto.__dict__.keys() else ""
            )
            print(str)
            print('+' + '-'*(strHeaderSize - 2) + '+')
        
        