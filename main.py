import requests

print('=' * 25)
print('API Consumindo ViaCep')
print('=' * 25)


def main():
    while True:
        cep_input = input('Digite o numero de um CEP: ')
        if cep_input == str(cep_input) and len(cep_input) != 8:
            print('CEP invalido, tente novamente...')
            cep_input = int(input('Digite o numero de um CEP: '))

        api_cep = requests.get(f'https://viacep.com.br//ws/{cep_input}/json/')
        result = api_cep.json()

        if 'erro' in result:
            print('CEP inválido!')
        else:
            print(f'CEP: {result["cep"]}')
            print(f'Rua: {result["logradouro"]}')
            print(f'Bairro: {result["bairro"]}')
            print(f'Cidade: {result["localidade"]}')
            print(f'Estado: {result["uf"]}')

        digito = input('Deseja Continuar? [S/N]').strip().upper()

        if digito == 'N':
            break


if __name__ == '__main__':
    main()
