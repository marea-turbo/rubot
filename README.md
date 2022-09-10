## Guide de Desenvolvimento

### Setando um ambiente virtual
Sempre que houver alteração no `requirements.txt` siga os seguintes passos
1. Instale a ferramenta pipenv (se n tiver) e crie uma pasta `.venv`
```
python -m pip install --user pipenv
mkdir .venv
```
2. Instale as novas dependências
```
python -m pipenv install -r requirements.txt
```
3. Inicie o Ambiente Virtual
```
python -m pipenv shell
```

### Exportando um ambiente virtual
Quando for dar um `git push`, e teve alterações nas bibliotecas usadas, jogue esse comando abaixo, para salvar os novos requirements
```
pip freeze > requirements.txt
```