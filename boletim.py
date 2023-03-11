import re
from datetime import datetime, timedelta

# Pedir informações sobre o paciente
nome_paciente = input("Qual o nome do paciente? ")
especie = input("Espécie? ")
especie = "Cão" if especie.lower() == "c" else "Gato"
comeu = input("O paciente comeu? (s/n) ")
comeu = "Sim" if comeu.lower() == "s" else "Não"
evacuou = input("O paciente evacuou? (s/n) ")
evacuou = "Sim" if evacuou.lower() == "s" else "Não"
urinou = input("O paciente urinou? (s/n) ")
urinou = "Sim" if urinou.lower() == "s" else "Não"
evolucao = input("A evolução do paciente está dentro do previsto? (s/n) ")
evolucao = "Sim" if evolucao.lower() == "s" else "Não"
previsao_alta = input("Existe previsão de alta para o paciente? (s/n) ")
previsao_alta = "Sim" if previsao_alta.lower() == "s" else "Não"

# Verificar a previsão de alta e obter a data, se houver
if previsao_alta == "Sim":
    while True:
        data_str = input("Qual é a data da previsão de alta? (formato DD/MM ou dd-mm ou dd.mm) ")
        pattern = re.compile(r"(\d{1,2})[\/\.-](\d{1,2})")
        match = pattern.match(data_str)
        if match:
            dia = int(match.group(1))
            mes = int(match.group(2))
            ano = datetime.now().year
            data = datetime(ano, mes, dia)
            if data == datetime.today():
                previsao_alta = "hoje"
            elif data == datetime.today() + timedelta(days=1):
                previsao_alta = "amanhã"
            else:
                previsao_alta = data.strftime("%d/%m")
            break
        else:
            print("Data inválida. Tente novamente.")
else:
    previsao_alta = "Não"

# Gerar a mensagem para o tutor
mensagem = f"Boa noite, aqui vai o relatório médico do {nome_paciente}\nComeu? {comeu}\nEvacuou? {evacuou}\nUrinou? {urinou}\nEvolução dentro do previsto? {evolucao}\n"
if previsao_alta.lower() == "sim":
    mensagem += f"Previsão de alta? Sim, {previsao_alta}."
else:
    mensagem += "Previsão de alta? Não."

# Imprimir a mensagem para o tutor
print("Mensagem para o tutor do paciente:")
print("----------------------------------")
print(mensagem)
