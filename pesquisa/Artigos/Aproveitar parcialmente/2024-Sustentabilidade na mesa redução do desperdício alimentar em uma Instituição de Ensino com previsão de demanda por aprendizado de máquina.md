---
source_file: "2024-Sustentabilidade na mesa redução do desperdício alimentar em uma Instituição de Ensino com previsão de demanda por aprendizado de máquina.txt"
original_rel_path: "Trabalhos\Artigos\Aproveitar parcialmente\txt\2024-Sustentabilidade na mesa redução do desperdício alimentar em uma Instituição de Ensino com previsão de demanda por aprendizado de máquina.txt"
category: "Artigos_Aproveitar_parcialmente"
extension: ".txt"
sha256: "524ce68273405e3bf6f450607120a06712439dbf45d54b33aeeaab63c5a6fdfb"
extracted_at: "2026-09-20T00:50:21.681556"
---

﻿XIX SIMPÓSIO DOS PROGRAMAS DE MESTRADO 
PROFISSIONAL 

 UNIDADE DE PÓS-GRADUAÇÃ O, EXTENSÃO E PESQUISA 
São Paulo/SP – 05, 06 e 07  de novembro de 2024 

  

O uso da Inteligência Artificial na Educ ação Profissional e em  
Sistemas Produ tivos: desafios e práticas 

 
 
Relato Técnico 
 
Sustentabilidade na mesa: redução do desperdício alimentar em 

uma Instituição de Ensino com previsão de demanda por 
aprendizado de máquina. 

 
Michel Silva de Souza 

https://orcid.org/0009-0003-3951-202X 

 
Rafael Nobre Orsi 

https://orcid.org/0000-0003-4719-0131 

 
 

Resumo 
O desperdício de alimentos é um problema global significativo que compromete a segurança 
alimentar e a sustentabilidade do planeta. No Brasil, a situação é agravada pela desigualdade social 
e pela insegurança alimentar, tornando a questão ainda mais crítica. Este estudo se concentra no 
desperdício de alimentos em uma instituição de ensino, abordando a necessidade urgente de reduzir 
o desperdício e otimizar a gestão de recursos disponíveis. Para enfrentar esse desafio, foi proposto 
e implementado um sistema de previsão de demanda de refeições, utilizando técnicas de Machine 
Learning, com ênfase na regressão linear. O desenvolvimento do sistema incluiu a criação de um 
formulário online para que os alunos pudessem reservar suas refeições antecipadamente, 
permitindo uma coleta organizada de dados relevantes. Esses dados foram posteriormente tratados 
em planilhas do Google, assegurando sua integridade e prontidão para análise. Para facilitar a 
visualização e a interpretação das informações, foram criados dashboards interativos que 
permitiram uma análise mais intuitiva do consumo de refeições. O desenvolvimento dos modelos 
preditivos foi realizado utilizando Python e suas bibliotecas, como Pandas, Numpy, Matplotlib e 
Scikit-learn, proporcionando uma base sólida para a construção de previsões confiáveis. Os 
resultados obtidos mostraram que a regressão linear se destacou como uma ferramenta promissora 
para prever a demanda por refeições, demonstrando capacidade de identificar padrões relevantes. 
No entanto, a análise dos dados também revelou a necessidade de aprimorar a precisão das 
previsões. Para isso, é fundamental incluir variáveis adicionais, como o histórico de presenças dos 
alunos, previsões climáticas, períodos de provas e o calendário escolar, fatores que podem 
influenciar significativamente a demanda. As lições aprendidas com a implementação deste projeto 
não apenas ressaltam a importância da qualidade e da consistência dos dados, mas também 
enfatizam a necessidade de um monitoramento constante e de colaborações entre diferentes 
setores da instituição. Essa experiência impulsiona a busca por aprimoramentos contínuos e o 
investimento em tecnologias e ferramentas que promovam uma gestão de recursos mais 
responsável e sustentável nas instituições de ensino, contribuindo assim para a redução do 
desperdício de alimentos e para a promoção de um ambiente educacional mais eficiente e 
equitativo. 
 
Palavras-chave: Desperdício de Alimentos. Previsão de Demanda. Machine Learning. 
Regressão Linear. Sustentabilidade  
 
 
Abstract 
Food waste is a significant global issue that compromises food security and the sustainability of our 
planet. In Brazil, the situation is aggravated by social inequality and food insecurity, making the 
problem even more critical. This study focuses on food waste in an educational institution, addressing 

 
   
 



 
   
 
the urgent need to reduce waste and optimize the management of available resources. To address 
this challenge, a meal demand forecasting system was proposed and implemented using Machine 
Learning techniques, with an emphasis on linear regression. The system's development included the 
creation of an online form for students to reserve their meals in advance, enabling the organized 
collection of relevant data. This data was then processed in Google Sheets, ensuring its integrity and 
readiness for analysis. To facilitate the visualization and interpretation of the information, interactive 
dashboards were created, allowing for a more intuitive analysis of meal consumption. The 
development of the predictive models was carried out using Python and its libraries, such as Pandas, 
Numpy, Matplotlib, and Scikit-learn, providing a solid foundation for constructing reliable predictions. 
The results obtained showed that linear regression stood out as a promising tool for predicting meal 
demand, demonstrating an ability to identify relevant patterns. However, the data analysis also 
revealed the need to improve the accuracy of predictions. To this end, it is essential to include 
additional variables, such as student attendance history, weather forecasts, exam periods, and the 
school calendar, factors that can significantly influence demand. The lessons learned from 
implementing this project not only highlight the importance of data quality and consistency but also 
emphasize the need for constant monitoring and collaborations between different sectors of the 
institution. This experience drives the pursuit of continuous improvements and investment in 
technologies and tools that promote more responsible and sustainable resource management in 
educational institutions, thereby contributing to the reduction of food waste and fostering a more 
efficient and equitable educational environment. 
 
Keywords: Food Waste. Demand Forecasting. Machine Learning. Linear Regression. 
Sustainability. 
 
 
1 Introdução 
 

De acordo com a Organização das Nações Unidas para a Alimentação e a 
Agricultura (FAO, 2021), o desperdício de alimentos compromete a capacidade de 
alimentar a população mundial de forma sustentável, representando um desafio 
global com impactos diretos na segurança alimentar. Estima-se que cerca de um 
terço de toda a comida produzida para consumo humano seja desperdiçada, o que 
corresponde aproximadamente a um terço de todos os alimentos produzidos. 
Estima que foram desperdiçados cerca de cerca de 1,05 bilhão de toneladas de 
alimentos em 2022 (FAO, 2024).  

O impacto desse desperdício vai além do aspecto econômico. Em um país 
com histórico de desigualdade social, a fome e da insegurança alimentar é um 
problema de alto impacto social (BEZERRA et. al., 2019). Por outro lado, a lei nº 
11.346 garante o direito humano à alimentação adequada e reconhece a 
alimentação como um direito fundamental e um dever do Estado (BRASIL, 2006). 
Diante desse cenário, o desperdício de alimentos torna-se uma questão de justiça 
social, impactando diretamente o bem-estar da população e a garantia de acesso 
a uma dieta saudável e nutritiva. 

O presente estudo aborda a problemática do desperdício de alimentos no 
contexto específico de uma instituição de ensino. O problema se intensifica quando 
é analisado o desperdício em refeitórios, cujos recursos são desperdiçados em 
grandes quantidades. Em especial, este estudo se concentra no Instituto Federal 
de São Paulo (IFSP) – Campus Itaquaquecetuba, onde o desperdício de refeições 
representa perdas significativas, de forma a afetar diretamente o orçamento da 
instituição e o acesso dos alunos à alimentação. A busca por soluções eficientes e 
inovadoras para reduzir o desperdício em refeitórios é crucial para garantir a 

 
   
 



 
   
 
sustentabilidade orçamentária da instituição de ensino e o acesso à alimentação de 
qualidade para todos os alunos. 

 
 

2 Objetivo 
 
Este relato técnico tem como objetivo desenvolver e implementar um sistema 

de previsão de demanda de refeições no IFSP – Campus Itaquaquecetuba, 
utilizando técnicas de regressão linear, com base no histórico de reservas e 
consumo de refeições.  

 
 

3 Análise do problema e solução proposta 
 

O desperdício de alimentos é um problema global com impactos 
socioeconômicos e ambientais significativos. No Brasil, a perda de alimentos ao 
longo da cadeia de produção, processamento, distribuição e consumo é um desafio 
crítico, agravado pela insegurança alimentar e a necessidade de garantir o direito 
à alimentação adequada para todos (SANTOS et. al., 2020). 

A presente análise se concentra no problema do desperdício de alimentos 
no IFSP – Campus Itaquaquecetuba, especificamente no contexto do refeitório. Em 
2023, o campus registrou um índice de desperdício de aproximadamente 30% das 
refeições preparadas, o que corresponde a um custo de R$172.500,00 de um 
montante de R$575.000,00 que é destinado a alimentação e é equivalente a 37% 
do orçamento total da instituição. 

A legislação brasileira - bem como a EC 64, uma alteração na Constituição 
Federal que garante o direito humano à alimentação adequada, promulgada em 
2010 e a PNSAN, instituída pela Lei Orgânica de Segurança Alimentar e Nutricional 
(LOSAN - Lei nº 10.633/2003), define diretrizes para a promoção da segurança 
alimentar e nutricional no Brasil - incentiva a redução do desperdício e o 
aproveitamento integral dos alimentos. No entanto, a proibição da doação de 
sobras de alimentos impede a utilização de alimentos ainda em condições de 
consumo, intensificando o problema. 

Nesse contexto, é fundamental analisar as diferentes etapas da cadeia de 
produção onde ocorrem perdas e desperdícios no contexto brasileiro. No entanto, 
este estudo se concentra no desperdício na etapa de consumo, para o referido 
campus. 

Para tentar solucionar esse problema, foi proposta a implementação de um 
sistema de previsão de demanda de refeições utilizando técnicas de Aprendizado 
de Máquina, especificamente a técnica de regressão linear. Essa abordagem 
permite identificar padrões em dados históricos e gerar previsões mais precisas do 
que métodos tradicionais (MONTGOMERY, PECK e VINING, 2021).  

Com essa abordagem, espera-se aumentar a eficiência dos gastos com 
alimentação, por meio da redução da taxa de desperdício de alimentos, para 
viabilizar uma melhor alocação dos recursos disponíveis no IFSP – Campus 
Itaquaquecetuba, contribuindo para a sustentabilidade da instituição e o bem-estar 
dos alunos. 
 
   
 



 
   
 
4 Implementação e resultados  
 

A implementação da proposta para reduzir o desperdício de alimentos foi 
utilizada com um conjunto de ferramentas integradas. O uso de ferramentas como 
o Google Workspace e bibliotecas da linguagem Python viabilizou a 
implementação, permitindo um monitoramento contínuo e melhorias na gestão das 
refeições no campus. 

Para implementar a solução que visa reduzir o desperdício de alimentos no 
IFSP, foram propostas as seguintes etapas, cada uma desempenhando um papel 
crucial no processo de coleta, análise, visualização e predição de dados. 

 
 

4.1 Coleta de Dados 
 

Foi implementado um sistema online, utilizando o formulário do Google, para 
que os alunos reservassem suas refeições com antecedência. A ferramenta era 
responsável por coletar dados como: nome do aluno; número da matrícula; turma; 
e data da reserva. 

Os dados de reserva foram integrados a uma planilha do Google, garantindo 
um registro centralizado e organizado das informações. 

 
 

4.2 Tratamento e Armazenamento dos Dados 
 

Com a ajuda do Google Planilhas e do recurso de programação Apps Script, 
os dados coletados foram tratados e organizados, incluindo a remoção de entradas 
duplicadas e o preenchimento de valores ausentes, assegurando que as 
informações estivessem prontas para análises posteriores. 

 
 
4.3 Visualização e Análise de Dados 
 

Para entender melhor as tendências e padrões nos dados, foi utilizado o 
Looker Studio. Esta ferramenta permitiu a criação de dashboards interativos que 
facilitam a visualização das reservas e do consumo de refeições, conforme a figura 
1, possibilitando uma análise mais intuitiva e acessível. O dashboard exibe 
informações como: 

● O número de reservas por dia, por turma e por semana. 
● A taxa de consumo (porcentagem de alunos que reservaram e consumiram 

a refeição). 
● A previsão de demanda para os próximos dias. 
● Os dias com maior desperdício e as causas prováveis. 

 
 
 
 
 
 

 
   
 



 
   
 

Figura 1 - Dashboard dos Dados das Refeições 

 
Fonte: Própria do Autor (2024). 

 
 
4.4 Desenvolvimento de Modelos Preditivos 
 

O desenvolvimento dos modelos preditivos para estimar a demanda de 
refeições no IFSP – Campus Itaquaquecetuba foi realizado utilizando o Google 
Colab como plataforma de desenvolvimento, permitindo a execução de códigos em 
Python com as bibliotecas Pandas, Numpy, Matplotlib e Scikit-learn. A biblioteca 
Pandas foi crucial para manipular e organizar os dados, incluindo a leitura dos 
arquivos CSV, o agrupamento dos dados por data, o tratamento de valores 
ausentes e a criação de novas variáveis explicativas. Já a biblioteca Numpy foi 
utilizada para operações matemáticas e transformações de dados, como o 
tratamento de valores ausentes e a conversão de dados para o formato adequado 
para os modelos de regressão. A biblioteca Matplotlib, por sua vez, foi empregada 
para a visualização de dados, gerando gráficos que ilustram a correlação entre as 
variáveis, como a demanda de refeições em relação ao dia da semana e eventos 
no campus. E, por fim, a biblioteca Scikit-learn foi utilizada para o desenvolvimento 
dos modelos de regressão linear, incluindo a implementação dos modelos de 
regressão linear, Ridge, Ridge com Validação Cruzada, Lasso e Lasso com 
Validação Cruzada. 

Com os dados pré-processados e organizados com Pandas, foram 
implementados e avaliados os seguintes modelos de regressão: o modelo de 
regressão linear, treinado com os dados de treinamento e ajustado aos dados de 
teste, utilizando a função LinearRegression() da biblioteca Scikit-learn; a regressão 

 
   
 



 
   
 
Ridge, uma variante da regressão linear com um termo de regularização para evitar 
overfitting, implementada com a função Ridge() da biblioteca Scikit-learn; a 
regressão Ridge com Validação Cruzada, que otimiza o parâmetro de regularização 
do modelo de regressão Ridge por meio da função RidgeCV(); a regressão Lasso, 
outra variante da regressão linear com termo de regularização e capacidade de 
selecionar as variáveis mais relevantes, implementada com a função Lasso() da 
biblioteca Scikit-learn; e a regressão Lasso com Validação Cruzada, que otimiza o 
parâmetro de regularização do modelo Lasso por meio da função LassoCV(). 

Para avaliar a performance dos modelos, foram utilizadas as seguintes 
métricas: o Mean Squared Error (MSE), que mede a média dos erros quadrados 
entre as predições e os valores reais; o Mean Absolute Error (MAE), que mede a 
média dos erros absolutos entre as predições e os valores reais; e o R2-score, que 
indica a proporção da variância do target que é explicada pelo modelo.  

A aplicação das bibliotecas Python, como Pandas, Numpy, Matplotlib e 
Scikit-learn, em conjunto com técnicas de regressão linear no Google Colab, 
permitiu a construção de modelos preditivos para analisar a demanda de refeições 
no IFSP - Campus Itaquaquecetuba. Essa abordagem possibilitou a identificação 
de padrões e a geração de previsões, mesmo que ainda existam desafios em 
relação à subestimação da demanda, indicando a necessidade de aprimoramentos 
futuros.  

 
 

4.5 Resultados dos Modelos Preditivos 
 

O projeto utilizou a regressão linear como técnica principal para prever a taxa 
de consumo de refeições, considerando variáveis como o dia da semana, o número 
de reservas realizadas e o histórico de consumo anterior. A regressão linear, por 
meio da identificação e modelagem da relação linear entre essas variáveis 
preditoras (features) e o resultado que se desejava estimar (a taxa de consumo), 
permitiu desenvolver um modelo preditivo capaz de antecipar o comportamento dos 
alunos em relação ao consumo de refeições. 

A partir desta abordagem foi gerado um conjunto de dados para otimizar a 
gestão alimentar e reduzir o desperdício, simplificando a visualização dos dados 
em uma equação linear, facilitando a interpretação e a tomada de decisões. Os 
resultados obtidos demonstram que a regressão linear se mostrou eficaz na 
previsão da demanda por refeições, contribuindo para a redução do desperdício de 
alimentos no campus. 

 

Tabela 1 - Predição para o dia 05/12/2023 

Reservas Refeições Servidas Desperdício 
136 121 15 

Modelo Nome do Modelo Predição 
1 Linear Regression 106 
2 Ridge 106 
3 Ridge CV 106 
4 Lasso 107 
5 Lasso CV 106 

Fonte: Própria do Autor (2024). 
 
   
 



 
   
 

A tabela 1 apresenta os resultados de um modelo de predição de demanda 
de refeições para o dia 05/12/2023. Foram utilizadas 5 técnicas de Aprendizado de 
Máquina para a predição: Regressão Linear, Ridge, Ridge com Validação Cruzada 
(CV), Lasso e Lasso com Validação Cruzada (CV). As predições foram comparadas 
com o número real de refeições servidas, considerando também o número de 
reservas feitas para o dia. 

Observando os dados da tabela 1, pode-se notar que o número de reservas 
foi de 136, enquanto o número de refeições servidas foi de 121. Isso indica um 
desperdício de 15 refeições. 

Ao analisar os resultados dos modelos de predição, percebemos que, em 
sua maioria, as predições ficaram abaixo do número de refeições servidas. A 
regressão linear previu 106 refeições, o Ridge previu 106, o Ridge com CV previu 
106, o Lasso previu 107 e o Lasso com CV previu 106. 

Em resumo, os modelos de Machine Learning testados apresentaram uma 
tendência a subestimar a demanda de refeições, com o número de predições 
variando entre 106 e 107, enquanto o número de refeições servidas foi de 121. 
Essa subestimação indica que, para o dia em questão, os modelos poderiam ter 
sido otimizados para prever uma demanda maior, o que resultaria em um menor 
desperdício de alimentos. 

 
Tabela 2 - Predição para o dia 06/12/2023 

Reservas Refeições Servidas Desperdício 
113 93 20 

Modelo Nome do Modelo Predição 
1 Linear Regression 93 
2 Ridge 93 
3 Ridge CV 93 
4 Lasso 89 
5 Lasso CV 92 

Fonte: Própria do Autor (2024). 
 
No dia 06/12, conforme tabela 2, foram feitas 113 reservas, mas apenas 93 

refeições foram servidas, gerando um desperdício de 20 refeições. Nos modelos 
de Machine learning os resultados foram distintos/diversos: 

● A Regressão Linear, Ridge e Ridge com Validação Cruzada (CV) tiveram 
previsões precisas, prevendo 93 refeições cada, o mesmo número de 
refeições servidas. 

● O modelo Lasso previu 89 refeições, subestimando a demanda em 4 
refeições. 

● O modelo Lasso com Validação Cruzada (CV) previu 92 refeições, 
subestimando a demanda em 1 refeição. 

Comparando com os resultados do dia 05/12, os modelos de Machine 
Learning tiveram um desempenho melhor no dia 06/12, especialmente a Regressão 
Linear, Ridge e Ridge com Validação Cruzada (CV), que conseguiram prever a 
demanda com precisão. 

 
 
   
 



 
   
 

Tabela 3 - Predição para o dia 07/12/2023 

Reservas Refeições Servidas Desperdício 
113 107 6 

Modelo Nome do Modelo Predição 
1 Linear Regression 103 
2 Ridge 103 
3 Ridge CV 103 
4 Lasso 103 
5 Lasso CV 104 

Fonte: Própria do Autor (2024). 
 
No dia 07/12/2023, de acordo com a tabela 3, foram realizadas 113 reservas 

e servidas 107 refeições, resultando em um desperdício de 6 refeições. 

Os modelos de predição apresentaram resultados variados: 

● Regressão Linear, Ridge, Ridge com CV e Lasso previram 103 refeições, 
subestimando a demanda em 4 refeições. 

● Lasso com CV previu 104 refeições, subestimando a demanda em 3 
refeições. 

Comparando com os dias anteriores, os modelos de Machine Learning 
tiveram um desempenho similar, com a maioria subestimando a demanda. Apesar 
de algumas previsões estarem próximas ao número de refeições servidas, os 
modelos ainda precisam de ajustes para se tornarem mais precisos e reduzir o 
desperdício de alimentos. 

 
Tabela 4 - Predição para o dia 08/12/2023 

Reservas Refeições Servidas Desperdício 
89 62 27 

Modelo Nome do Modelo Predição 
1 Linear Regression 69 
2 Ridge 69 
3 Ridge CV 71 
4 Lasso 72 
5 Lasso CV 72 

Fonte: Própria do Autor (2024). 
 
No dia 08/12/2023, conforme a tabela 4, foram feitas 89 reservas e servidas 

62 refeições, resultando em um desperdício de 27 refeições. 

Os modelos de predição apresentaram resultados foram distintos/diversos: 

● Regressão Linear previu 69 refeições, subestimando a demanda em 7 
refeições. 

● Ridge previu 69 refeições, subestimando a demanda em 7 refeições. 
● Ridge com CV previu 71 refeições, subestimando a demanda em 9 refeições. 
● Lasso e Lasso com CV previram 72 refeições, subestimando a demanda em 

10 refeições. 
 

 
   
 



 
   
 

Comparando com os dias anteriores, os modelos de Machine Learning 
tiveram um desempenho pior no dia 08/12, subestimando a demanda em maior 
proporção. Essa diferença pode estar relacionada a fatores como a época do ano, 
eventos no campus ou outros fatores que influenciaram a demanda de refeições. 

É importante analisar os dados e ajustar os modelos de predição para 
melhorar a precisão das previsões e reduzir o desperdício de alimentos. 

 
Figura 2 - Comparativo entre os Modelos de Predição 

 
Fonte: Própria do Autor (2024). 

 
A figura 2 apresenta os resultados da predição de demanda de refeições 

para 4 dias, utilizando 5 modelos de Machine Learning: Regressão Linear, Ridge, 
Ridge com Validação Cruzada (CV), Lasso e Lasso com Validação Cruzada (CV). 
Ao analisar os dados, podemos notar que: 

● O desperdício é alto: Em todos os dias analisados, a quantidade de 
refeições servidas foi menor que o número de reservas. O desperdício variou 
de 6 a 27 refeições por dia, evidenciando a necessidade de melhorar a 
precisão das previsões. 

● Predições variam: As previsões dos modelos de Machine Learning tiveram 
resultados divergentes, com algumas subestimando a demanda e outras se 
aproximando mais do número de refeições servidas. 

● Regressão linear e Ridge com CV se destacam: Para os 4 dias 
analisados, o modelo de Regressão Linear e o Ridge com Validação 
Cruzada (CV) apresentaram as menores diferenças entre a predição e o 
número real de refeições servidas. 

● Lasso e Lasso com CV tiveram desempenho similar: Os modelos Lasso 
e Lasso com Validação Cruzada (CV) tiveram um desempenho similar, com 
uma subestimação consistente da demanda. 

Uma visão completa da concepção do projeto e aplicação dos métodos de 
aprendizagem de máquina está disponível no link a seguir: [link]. O código-fonte do 
projeto está disponível no Google Colab, permitindo a replicação do estudo e a 
exploração das técnicas de Machine Learning aplicadas para a previsão da 
demanda de refeições. A disponibilização do código facilita a compreensão da 
metodologia utilizada e sua aplicação em outros contextos. 

Em resumo, os modelos de Machine Learning testados mostraram 
resultados promissores, mas ainda apresentam margem para melhorias na 
precisão. A análise dos dados indica que a Regressão Linear e o Ridge com 
Validação Cruzada (CV) se mostraram como os modelos mais precisos para esse 
conjunto de dados. É importante continuar a análise e o ajuste dos modelos para 

 
   
 



 
   
 
aprimorar as previsões e reduzir o desperdício de alimentos no IFSP - Campus 
Itaquaquecetuba. 

 
 

5 Lições aprendidas 
 
A implementação de um sistema de previsão de demanda de refeições no 

IFSP - Campus Itaquaquecetuba, utilizando técnicas de Machine Learning, 
destacou a importância da consistência e integridade dos dados para a precisão 
dos modelos, além da escolha adequada do modelo e do monitoramento contínuo. 
A colaboração entre as diferentes áreas da instituição foi essencial para o sucesso 
dessa iniciativa. 

Embora os resultados tenham sido promissores, a análise dos dados indicou 
a necessidade de aprimoramentos no sistema. A inclusão de variáveis adicionais, 
como o histórico de presença dos alunos, previsões meteorológicas, períodos de 
provas e o calendário escolar, poderia aumentar a precisão das previsões e reduzir 
o desperdício de alimentos. Esse passo não apenas melhoraria o modelo, mas 
também permitiria uma análise mais abrangente e personalizada da demanda. 

A análise de correlação entre as variáveis "dia da semana", "reservas", 
"reservas do dia anterior" e "consumo do dia anterior" revelou relações significativas 
conforme a figura 3. A correlação mais forte foi entre "reservas" e "taxa de 
consumo", sugerindo que um maior número de reservas tende a resultar em um 
aumento na taxa de consumo. 

 
Figura 3 - Correlação entre as variáveis 

 
Fonte: Própria do Autor (2024). 

 

 
   
 



 
   
 

As métricas de desempenho dos modelos de predição, avaliadas por MSE, 
MAE e R², conforme o gráfico 1, oferecem insights sobre a qualidade do ajuste do 
modelo aos dados. O MSE (Mean Squared Error) apresentou um valor em torno de 
0,03, indicando um bom alinhamento entre previsões e valores reais. O MAE (Mean 
Absolute Error) ficou em aproximadamente 0,11, o que sugere uma baixa diferença 
média entre as previsões e os resultados efetivos, evidenciando a precisão do 
modelo. Já o R² (R-squared) foi de 0,19, o que indica que o modelo explica apenas 
uma parte limitada da variabilidade dos dados. Isso sugere que, embora o 
desempenho em termos de MSE e MAE seja bom, o modelo ainda pode ser 
aprimorado com a inclusão de novas variáveis ou a exploração de diferentes 
abordagens modelares. 

 
Gráfico 1 - Gráfico de Resíduos 

 
Fonte: Própria do Autor (2024). 

 
A análise da correlação entre as variáveis, juntamente com as métricas de 

desempenho, é crucial para entender melhor como o modelo se ajusta aos dados 
e identificar oportunidades de otimização. 

A busca por soluções inovadoras para garantir uma gestão de recursos mais 
eficiente e sustentável no IFSP - Campus Itaquaquecetuba permanece uma 
prioridade. 

 
 

6 Considerações finais 
 

A presente análise explorou a problemática da questão do desperdício de 
alimentos no refeitório do IFSP - Campus Itaquaquecetuba, com o objetivo de 
identificar soluções inovadoras que otimizem a gestão de recursos e promovam a 
sustentabilidade da instituição. A implementação de um sistema de previsão de 
demanda de refeições, utilizando técnicas de Machine Learning, especialmente a 

 
   
 



 
   
 
regressão linear, mostrou-se uma estratégia promissora para reduzir o desperdício 
e aumentar a eficiência do serviço de alimentação. 

A experiência proporcionou valiosos aprendizados sobre coleta, tratamento 
e análise de dados, além da seleção e aplicação de modelos de Machine Learning 
para prever a demanda. Com a criação de um sistema online de reservas, o uso de 
ferramentas como Google Planilhas e Apps Script para tratamento de dados, e o 
desenvolvimento de dashboards interativos no Looker Studio, conseguimos 
visualizar e analisar informações de maneira mais eficaz, o que facilitou a tomada 
de decisões estratégicas. 

No entanto, a busca por soluções para a redução do desperdício de 
alimentos continua. A análise dos dados coletados e a avaliação do desempenho 
dos modelos de Machine Learning destacaram a necessidade de aprimorar a 
precisão das previsões. É fundamental explorar técnicas mais adequadas ao nosso 
contexto e realizar análises mais profundas, levando em conta fatores adicionais 
que influenciam a demanda de refeições. 

Acredita-se que desenvolver soluções inovadoras para a gestão de recursos 
e a redução do desperdício de alimentos é crucial para garantir a sustentabilidade 
do IFSP - Campus Itaquaquecetuba. As lições aprendidas ao longo deste projeto 
nos incentivam a buscar melhorias contínuas e a investir em tecnologias e 
ferramentas que promovam uma gestão de recursos mais responsável e eficiente. 
 
 
Referências 
 
BEZERRA, Mariana Silva; JACOB, Michelle Cristine Medeiros; FERREIRA, 
Maria Angela Fernandes; VALE, Diôgo; MIRABAL, Isabelle Ribeiro Barbosa; 
LYRA, Clélia de Oliveira. Insegurança alimentar e nutricional no Brasil e 
sua correlação com indicadores de vulnerabilidade. Revista Ciência & 
Saúde Coletiva. Disponível em: 
<https://www.scielo.br/j/csc/a/vpGZNFNcKySWVrVy4KR3Gtc/>. Acesso em: 
1 out. 2024. 
 
BRASIL. Lei nº 11.346, de 15 de dezembro de 2006. Disponível em: 
<https://www.planalto.gov.br/ccivil_03/_ato2004-2006/2006/lei/l11346.htm>. 
Acesso em: 4 out. 2024. 
 
Food and Agriculture Organization of the United Nations – FAO. (2021). Food 
waste Index Report. Roma: FAO. Disponível em: 
<https://www.unep.org/resources/report/unep-food-waste-index-report-2021>. 
Acesso em: 5 Out. 2024. 
 
Food and Agriculture Organization of the United Nations – FAO. (2024). Food 
waste Index Report. Roma: FAO. Disponível em: 
https://www.unep.org/resources/publication/food-waste-index-report-2024. Acesso 
em: 5 Out. 2024. 

 

 
   
 



 
   
 
MONTGOMERY, Douglas C.; PECK, Elizabeth A.; VINING, Geoffrey. 
Introduction to Linear Regression Analysis. New York: Wiley, 2021. 
 
SANTOS, K. L., PANIZZON, J., CENCI, M. M., GRABOWSKI, G., & JAHNO, 
V. D. (2020). Food losses and waste: reflections on the current brazilian 
scenario. Brazilian Journal of Food Technology, 2020. Disponível em: 
<https://www.scielo.br/j/bjft/a/yhXZXHzvzPTqRWJpLcVt9Bx> Acesso em: 6 
Out. 2024.