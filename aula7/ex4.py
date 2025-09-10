vendas_semana = [1200, 1500, 1100, 2000, 2500, 1800, 1300]
dias = ["Segunda-feira", "Terça-feira", "Quarta-feira",
        "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]

total = sum(vendas_semana)

menor_valor = min(vendas_semana)
indice_menor = vendas_semana.index(menor_valor)
dia_menor = dias[indice_menor]

print(f"Vendas da semana: {vendas_semana}")
print(f"Total de vendas na semana: {total}")
print(f"Menor valor de venda: {menor_valor} (no dia: {dia_menor})")