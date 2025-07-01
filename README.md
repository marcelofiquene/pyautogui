
# 📝 Automação de Preenchimento de Formulários

Este projeto Python automatiza o preenchimento de um formulário HTML usando dados de um arquivo CSV. Ele utiliza a biblioteca `pyautogui` para simular interações do usuário (cliques e digitação) e `pandas` para ler os dados dos clientes.

---

## 🚀 Funcionalidades

- **Leitura de Dados**: Carrega dados de clientes de um arquivo `clientes.csv`.
- **Abertura de Formulário**: Abre automaticamente um arquivo `form.html` no navegador padrão.
- **Preenchimento Automatizado**: Preenche campos de texto, seleciona opções de rádio (Educação, Sexo) e de dropdown (Anos de Experiência).
- **Formato de Data**: Converte e preenche datas no formato correto.
- **Verificação de Resolução**: Garante que a resolução da tela seja de **1920x1080** para o funcionamento correto da automação.

---

## 📋 Pré-requisitos

Certifique-se de ter o **Python 3.x** instalado em sua máquina.

As seguintes bibliotecas Python são necessárias:

- `pandas`: Para manipulação e leitura de dados CSV.
- `pyautogui`: Para automação de GUI (simulação de teclado e mouse).

---

## 📦 Instalação

Clone o repositório (ou baixe os arquivos do projeto):

```bash
git clone https://github.com/marcelofiquene/pyautogui.git
cd pyautogui
```

Instale as dependências com:

```bash
pip install -r requirements.txt
```

---

## ⚙️ Configuração

Para que o script funcione corretamente, você precisará dos seguintes arquivos na **mesma pasta** do script `app.py`:

- **clientes.csv**: Um arquivo CSV contendo os dados dos clientes. As colunas esperadas são:  
  `first_name`, `last_name`, `job_title`, `education`, `sex`, `experience`, `date`.

### Exemplo de `clientes.csv`:

```csv
first_name,last_name,job_title,education,sex,experience,date
João,Silva,Engenheiro de Software,College,Male,2-5,2023-01-15
Maria,Souza,Designer UX,Grad School,Female,6+,2022-05-20
Carlos,Ferreira,Analista de Dados,High School,Male,0-1,2024-03-10
```

- **form.html**: O arquivo HTML do formulário que será preenchido.  
  O script espera que os elementos estejam em **posições específicas da tela**, conforme as **coordenadas** definidas no código.

> ⚠️ **Importante:** A automação é baseada em coordenadas de tela.  
> Se o layout do `form.html` for alterado ou a resolução não for **1920x1080**,  
> será necessário ajustar o dicionário `coords` no arquivo `app.py`.

---

## 🚀 Como Usar

1. **Verifique a Resolução da Tela**:  
   Certifique-se de que a resolução esteja configurada para **1920x1080**.

2. **Execute o Script**:

```bash
python app.py
```

3. **Evite Interagir com o Mouse/Teclado**:  
   Enquanto o script estiver em execução, **não mova o mouse** ou digite.  
   A automação simula essas ações e qualquer interferência pode causar falhas no preenchimento.

O script abrirá o `form.html` no navegador padrão e preencherá os campos para cada cliente no `clientes.csv`.  
Mensagens de progresso e erros serão exibidas no console.

---

## ⚠️ Notas Importantes

- **Dependência de Resolução**: O script depende da resolução **1920x1080**.  
  Se estiver usando outra, será necessário ajustar as coordenadas em `coords`.

- **Não Mover o Mouse**: Durante a execução, o script assume controle do mouse e teclado.  
  Evite qualquer interação manual.

- **Velocidade de Preenchimento**:  
  Os `time.sleep()` no código ajudam a sincronizar a automação com o sistema.  
  Ajuste-os conforme o desempenho do seu computador.

---

## 🤝 Contribuições

Contribuições são bem-vindas!  
Se tiver sugestões para melhorias (como suporte a diferentes resoluções ou detecção de elementos via imagem), sinta-se à vontade para abrir uma *issue* ou enviar um *pull request*.

---

## 📄 Licença

Este projeto está licenciado sob a **Licença MIT**.
