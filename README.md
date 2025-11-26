# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Administração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# FarmTech Solutions - Assistente Agrícola Inteligente

## Grupo: FarmTech Solutions

## 👨‍🎓 Integrantes: 
- <a href="https://www.linkedin.com/in/gabriel-oliveira-b6353a16b/">Gabriel Oliveira dos Santos</a>
- <a href="https://www.linkedin.com/in/roberson-pedrosa-304ab523a/">Roberson Pedrosa de Oliveira Junior</a>
- <a href="https://www.linkedin.com/in/arthur-bruttel-7171b8381">Arthur Bruttel Nascimento</a> 
- <a href="https://www.linkedin.com/in/jonviotti/">Jonatan Viotti Rodrigues da Silva</a> 
- <a href="https://www.linkedin.com/in/eusamuelrocha/">Samuel Nicolas Oliveira Rocha</a>

## 👩‍🏫 Professores:
### Tutor(a) 
- <a href="https://www.linkedin.com/in/sabrina-otoni-22525519b/">Sabrina Otoni</a>
### Coordenador(a)
- <a href="https://www.linkedin.com/company/inova-fusca">André Godoi Chiovato</a>

## 📜 Descrição

O FarmTech Solutions é um sistema de assistência agrícola inteligente desenvolvido como trabalho acadêmico para ajudar agricultores a otimizar a produtividade de suas colheitas. O sistema utiliza Machine Learning para prever a produtividade da colheita com base em dados do solo, clima e nutrientes.

Este sistema visa fornecer aos agricultores uma ferramenta baseada em dados para tomar decisões informadas sobre manejo do solo, irrigação e fertilização.

O projeto implementa conceitos avançados de ciência de dados e engenharia de software, incluindo:
- Machine Learning com Scikit-Learn (Random Forest Regressor)
- Integração com banco de dados Oracle
- Dashboard interativo com Streamlit
- Geração de dados sintéticos para treinamento
- Análise de correlações e visualizações

## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- <b>assets</b>: Arquivos relacionados a elementos não-estruturados deste repositório, como imagens e logo da FIAP.

- <b>config</b>: Arquivos de configuração do banco de dados Oracle e scripts de população de dados.
  - `database.py`: Gerencia conexão e operações com Oracle Database
  - `populate_db.py`: Script para popular o banco com dados sintéticos

- <b>src</b>: Código-fonte principal do projeto.
  - `data_generator.py`: Gera dados agrícolas sintéticos
  - `train_model.py`: Treina o modelo de Machine Learning

- <b>app.py</b>: Aplicação principal do dashboard Streamlit com interface interativa.

- <b>model.joblib</b>: Modelo treinado de Random Forest para previsões.

- <b>requirements.txt</b>: Dependências Python do projeto.

- <b>walkthrough.md</b>: Guia passo a passo de instalação e uso do sistema.

- <b>README.md</b>: Arquivo que serve como guia e explicação geral sobre o projeto (o mesmo que você está lendo agora).

## 🔧 Como executar o código

### Pré-requisitos

**Software Necessário:**
- Python 3.8 ou superior
- Oracle Database (ou Oracle XE para desenvolvimento) - Opcional
- pip (gerenciador de pacotes Python)

**Bibliotecas Python:**
- streamlit (interface web)
- pandas (manipulação de dados)
- scikit-learn (machine learning)
- numpy (computação numérica)
- matplotlib e seaborn (visualizações)
- oracledb (conectividade com Oracle)
- sqlalchemy (ORM e conexão com banco)
- python-dotenv (variáveis de ambiente)

### Instalação

**Passo 1: Clonar o repositório**
```bash
git clone <url-do-repositorio>
cd fase4-cap-pia
```

**Passo 2: Criar ambiente virtual (recomendado)**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows
```

**Passo 3: Instalar dependências**
```bash
pip install -r requirements.txt
```

**Passo 4: Configurar variáveis de ambiente (Opcional - para usar Oracle)**

Criar arquivo `.env` na raiz do projeto:
```env
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_DSN=seu_dsn_host:port/service_name
```

> **Nota:** Se você não configurar o Oracle, o sistema usará automaticamente dados sintéticos para demonstração.

### Execução

**Passo 1: Popular o banco de dados (Opcional)**
```bash
python config/populate_db.py
```

**Passo 2: Treinar o modelo de Machine Learning**
```bash
python src/train_model.py
```

**Passo 3: Executar o dashboard**
```bash
streamlit run app.py
```

O sistema abrirá automaticamente no navegador em `http://localhost:8501`

### Funcionalidades do Dashboard

**1. Início**
- Visão geral do projeto
- Descrição das funcionalidades
- Stack tecnológica utilizada

**2. Visualização de Dados**
- Tabela completa dos dados agrícolas
- Estatísticas descritivas (média, desvio padrão, min, max)

**3. Previsões**
- Interface interativa com sliders para ajustar parâmetros:
  - Umidade do Solo (%)
  - Nível de pH
  - Temperatura (°C)
  - Chuva (mm)
  - Nitrogênio, Fósforo, Potássio (NPK)
- Previsão de produtividade em tempo real
- Recomendações personalizadas baseadas nos parâmetros:
  - Análise de umidade do solo
  - Análise de pH
  - Análise de temperatura
  - Análise de precipitação
  - Análise de nutrientes (NPK)
  - Classificação da produtividade prevista

**4. Analytics**
- Mapa de calor de correlação entre variáveis
- Gráficos de dispersão interativos
- Análise visual de tendências

### Exemplo de Uso

**Fazendo uma Previsão:**
1. Acesse a página "Previsões"
2. Ajuste os sliders conforme as condições do seu solo:
   - Umidade do Solo: 60%
   - pH: 6.5
   - Temperatura: 25°C
   - Chuva: 120mm
   - Nitrogênio: 50
   - Fósforo: 45
   - Potássio: 55
3. Clique em "Prever Produtividade"
4. Visualize a previsão e as recomendações personalizadas

### Funcionalidades Implementadas

- ✅ Geração de dados sintéticos realistas
- ✅ Integração com banco de dados Oracle (com fallback para dados sintéticos)
- ✅ Treinamento de modelo Random Forest Regressor
- ✅ Dashboard interativo com Streamlit
- ✅ Previsão de produtividade baseada em 7 parâmetros
- ✅ Sistema de recomendações inteligentes
- ✅ Visualizações de correlação e tendências
- ✅ Interface totalmente em Português (pt-BR)
- ✅ Análise completa de todos os parâmetros agrícolas

## 🗃 Histórico de lançamentos

* 1.0.0 - 25/11/2024
    * Sistema completo de previsão de produtividade
    * Recomendações expandidas para todos os parâmetros
    * Integração SQLAlchemy para Oracle
    * Dashboard Streamlit com 4 páginas funcionais
* 0.3.0 - 24/11/2024
    * Implementação do modelo Random Forest
    * Sistema de recomendações básicas
    * Visualizações com matplotlib e seaborn
* 0.2.0 - 22/11/2024
    * Criação do gerador de dados sintéticos
    * Integração com Oracle Database
    * Scripts de população de banco
* 0.1.0 - 21/11/2024
    * Estrutura inicial do projeto
    * Definição de requisitos e arquitetura
    * Configuração do ambiente

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>

---

**🌱 FarmTech Solutions - Assistente Agrícola Inteligente**  
*Tecnologia e Machine Learning a serviço da agricultura* 🚜
