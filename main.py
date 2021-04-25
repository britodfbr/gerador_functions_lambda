import locale


# locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8') 

produto = 0.1
serviço = 0.15
royalties = 0.25

def tax(taxa):
    return lambda preco: preco * (1 + taxa)

calc_preco_produto = tax(produto)
calc_preco_servico = tax(serviço)
calc_preco_royalties = tax(royalties)

# print(locale.currency(calc_preco_produto(1000), grouping=True))
# print(locale.currency(calc_preco_servico(1000), grouping=True))
# print(locale.currency(calc_preco_royalties(12345678.90), grouping=True))

print(calc_preco_produto(1000))
print(calc_preco_servico(1000))
print(calc_preco_royalties(12345678.90))
