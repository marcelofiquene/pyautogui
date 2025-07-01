Automação de Preenchimento de Formulários
Este projeto Python automatiza o preenchimento de um formulário HTML usando dados de um arquivo CSV. Ele utiliza a biblioteca pyautogui para simular interações do usuário (cliques e digitação) e pandas para ler os dados dos clientes.

🚀 Funcionalidades
Leitura de Dados: Carrega dados de clientes de um arquivo clientes.csv.

Abertura de Formulário: Abre automaticamente um arquivo form.html no navegador padrão.

Preenchimento Automatizado: Preenche campos de texto, seleciona opções de rádio (Educação, Sexo) e de dropdown (Anos de Experiência).

Formato de Data: Converte e preenche datas no formato correto.

Verificação de Resolução: Garante que a resolução da tela seja de 1920x1080 para garantir o funcionamento correto da automação.

📋 Pré-requisitos
Certifique-se de ter o Python instalado em sua máquina. Este projeto foi desenvolvido e testado com Python 3.x.

As seguintes bibliotecas Python são necessárias:

pandas: Para manipulação e leitura de dados CSV.

pyautogui: Para automação de GUI (simulação de teclado e mouse).

📦 Instalação
Clone o repositório (ou baixe os arquivos do projeto):

git clone https://github.com/marcelofiquene/pyautogui.git
cd marcelofiquene/pyautogui

Instale as dependências usando:

pip install -r requirements.txt

⚙️ Configuração
Para que o script funcione corretamente, você precisará dos seguintes arquivos na mesma pasta do script main.py:

clientes.csv: Um arquivo CSV contendo os dados dos clientes a serem preenchidos. As colunas esperadas são: first_name, last_name, job_title, education, sex, experience, date.
Exemplo de clientes.csv:

first_name,last_name,job_title,education,sex,experience,date
João,Silva,Engenheiro de Software,College,Male,2-5,2023-01-15
Maria,Souza,Designer UX,Grad School,Female,6+,2022-05-20
Carlos,Ferreira,Analista de Dados,High School,Male,0-1,2024-03-10

form.html: O arquivo HTML do formulário que será preenchido. O script espera que os elementos do formulário estejam em posições específicas na tela, conforme as coordenadas definidas no código.

Importante: A automação é baseada em coordenadas de tela. Se o layout do form.html for alterado ou se a resolução da tela não for 1920x1080, as coordenadas no script (coords no main.py) precisarão ser ajustadas.

🚀 Como Usar
Verifique a Resolução da Tela: Certifique-se de que a resolução da sua tela esteja configurada para 1920x1080. O script verificará isso e será encerrado se a resolução for diferente.

Execute o Script:

python app.py

Não Interaja com o Mouse/Teclado: Enquanto o script estiver em execução, evite mover o mouse ou digitar. A automação simula essas ações e qualquer intervenção manual pode causar erros no preenchimento.

O script abrirá o form.html no seu navegador padrão e começará a preencher os campos para cada cliente no clientes.csv. Mensagens de progresso e erros serão exibidas no console.

⚠️ Notas Importantes
Dependência de Resolução: Este script é altamente dependente da resolução da tela (1920x1080). Se você usa uma resolução diferente, precisará ajustar as coordenadas no dicionário coords dentro do arquivo app.py.

Não Mover o Mouse: Durante a execução, o script assume controle do mouse e teclado. Qualquer movimento ou clique manual pode desalinhar as coordenadas e levar a preenchimentos incorretos.

Velocidade de Preenchimento: Os time.sleep() no código são usados para dar tempo ao sistema para reagir. Você pode ajustá-los se a automação estiver muito rápida ou muito lenta para o seu sistema.

🤝 Contribuições
Contribuições são bem-vindas! Se você tiver sugestões para melhorias, como tornar o script mais robusto a diferentes resoluções ou layouts de formulário, sinta-se à vontade para abrir uma issue ou enviar um pull request.

📄 Licença
Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.
