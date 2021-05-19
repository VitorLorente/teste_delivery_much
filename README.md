# Testes automatizados para verificação de endpoints conversores de inteiro para nome extenso

## Passo a passo para execução dos testes:

* Baixe o repositório na sua máquina local
* Tenha a certeza de que você possui, em sua máquina, a versão 3.9 do python e a lib pipenv
    * Caso sua versão do python seja diferente, altere a variável "python_version" no arquivo Pipfile, substituindo o 3.9 pela sua versão (a versão deve ser 3.6 ou superior)
    * Caso não possua o pipenv, instale-o com pip:
        * ```pip install pipenv```
* Com o terminal aberto na raiz do projeto, instale as depências num ambiente virtual:
    * ```pipenv install```
* Ative o ambiente virtual:
    * ```pipenv shell```
* Agora, é só rodar os testes com este comando (substitua < nome_arquivo > pelo nome do relatório que você irá gerar, por exemplo, "meuRelatorio"):
    * ```pytest --html=reports/< nome_arquivo >.html```
    * O comando executará os testes e irá gerar o relatório HTML dentro da pasta "reports/"
    * Para visualizar o relatório, clique duas vezes sobre o arquivo
    * Na pasta reports/ há um relatório gerado de exemplo