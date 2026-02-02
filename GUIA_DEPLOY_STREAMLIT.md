# 🚀 Guia de Deploy - Streamlit Community Cloud

## Passo a Passo para Compartilhar sua Aplicação

---

## 📋 Pré-requisitos

Antes de começar, você precisa ter:

- ✅ Conta no GitHub (gratuita)
- ✅ Conta no Streamlit Community Cloud (gratuita)
- ✅ Seu projeto funcionando localmente
- ✅ Git instalado no seu computador

---

## 🔧 Parte 1: Preparar o Projeto para Deploy

### 1.1 Verificar Arquivos Essenciais

Certifique-se de que seu projeto tem estes arquivos na raiz:

```
fiap-datathon-pede/
├── app.py                  ✅ Arquivo principal
├── requirements.txt        ✅ Dependências
├── .gitignore             ✅ Arquivos a ignorar
├── data/                  ✅ Pasta de dados
├── models/                ✅ Pasta de modelos
└── README.md              ✅ Documentação
```

### 1.2 Verificar requirements.txt

Abra o arquivo `requirements.txt` e confirme que todas as dependências estão listadas:

```txt
streamlit==1.31.0
pandas==2.1.4
numpy==1.26.3
scikit-learn==1.4.0
xgboost==2.0.3
plotly==5.18.0
matplotlib==3.8.2
seaborn==0.13.1
openpyxl==3.1.2
joblib==1.3.2
imbalanced-learn==0.12.0
```

### 1.3 Verificar .gitignore

Certifique-se de que o `.gitignore` está configurado para não enviar arquivos desnecessários:

```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/

# Jupyter
.ipynb_checkpoints

# IDEs
.vscode/
.idea/

# OS
.DS_Store
Thumbs.db

# Dados grandes (opcional - se os dados forem muito grandes)
# data/raw/*.xlsx
```

**⚠️ IMPORTANTE**: Se seus dados forem muito grandes (>100MB), você precisará usar Git LFS ou hospedar os dados externamente.

---

## 📦 Parte 2: Criar Repositório no GitHub

### 2.1 Criar Novo Repositório

1. Acesse: https://github.com/new
2. Preencha os campos:
   - **Repository name**: `fiap-datathon-pede`
   - **Description**: "Datathon PEDE - Associação Passos Mágicos - Análise e Predição de Risco Educacional"
   - **Visibility**: Public (necessário para Streamlit Community Cloud gratuito)
   - **NÃO** marque "Add a README file" (você já tem um)
   - **NÃO** adicione .gitignore (você já tem um)

3. Clique em **"Create repository"**

### 2.2 Conectar Projeto Local ao GitHub

Abra o terminal na pasta do projeto e execute:

```bash
# Navegar até a pasta do projeto
cd c:\Users\robso\Downloads\fiap-datathon-pede

# Inicializar repositório Git (se ainda não foi feito)
git init

# Adicionar todos os arquivos
git add .

# Fazer o primeiro commit
git commit -m "Initial commit - Datathon PEDE"

# Adicionar o repositório remoto (substitua SEU-USUARIO pelo seu username do GitHub)
git remote add origin https://github.com/SEU-USUARIO/fiap-datathon-pede.git

# Enviar para o GitHub
git branch -M main
git push -u origin main
```

**💡 Dica**: Se pedir autenticação, use seu username do GitHub e um **Personal Access Token** (não a senha).

#### Como criar um Personal Access Token:
1. GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Generate new token (classic)
3. Marque: `repo` (full control of private repositories)
4. Generate token
5. **COPIE O TOKEN** (você não verá novamente!)
6. Use este token como senha ao fazer push

---

## ☁️ Parte 3: Deploy no Streamlit Community Cloud

### 3.1 Criar Conta no Streamlit Cloud

1. Acesse: https://share.streamlit.io/
2. Clique em **"Sign up"** ou **"Continue with GitHub"**
3. Autorize o Streamlit a acessar sua conta do GitHub
4. Confirme seu email (se solicitado)

### 3.2 Fazer Deploy da Aplicação

1. No Streamlit Cloud, clique em **"New app"**

2. Preencha as informações:
   - **Repository**: Selecione `SEU-USUARIO/fiap-datathon-pede`
   - **Branch**: `main`
   - **Main file path**: `app.py`
   - **App URL** (opcional): Escolha um nome customizado ou deixe o padrão

3. Clique em **"Deploy!"**

### 3.3 Aguardar o Deploy

O Streamlit Cloud irá:
- ✅ Clonar seu repositório
- ✅ Instalar as dependências do `requirements.txt`
- ✅ Executar sua aplicação
- ✅ Gerar uma URL pública

**Tempo estimado**: 2-5 minutos

---

## 🎉 Parte 4: Acessar e Compartilhar

### 4.1 URL da Aplicação

Após o deploy, você receberá uma URL no formato:

```
https://SEU-USUARIO-fiap-datathon-pede-app-XXXXX.streamlit.app
```

Ou, se você escolheu um nome customizado:

```
https://datathon-pede.streamlit.app
```

### 4.2 Testar a Aplicação

1. Acesse a URL gerada
2. Teste todas as funcionalidades:
   - ✅ Aba "Sobre" carrega corretamente
   - ✅ Preditor de Risco funciona
   - ✅ Dashboard mostra visualizações
   - ✅ Filtros funcionam
   - ✅ Modelo faz predições

### 4.3 Compartilhar

Copie a URL e compartilhe com:
- 👨‍🏫 Professores
- 👥 Colegas de equipe
- 📧 Email de entrega do projeto
- 📄 Apresentação/Slides

---

## 🔄 Parte 5: Atualizar a Aplicação

### 5.1 Fazer Alterações Localmente

1. Edite os arquivos necessários
2. Teste localmente: `streamlit run app.py`

### 5.2 Enviar Atualizações para o GitHub

```bash
# Adicionar arquivos modificados
git add .

# Fazer commit com mensagem descritiva
git commit -m "Atualização: [descreva o que mudou]"

# Enviar para o GitHub
git push origin main
```

### 5.3 Deploy Automático

O Streamlit Cloud detecta automaticamente as mudanças no GitHub e **re-deploya automaticamente**!

**Tempo de atualização**: 1-3 minutos

---

## ⚠️ Troubleshooting - Problemas Comuns

### Problema 1: "ModuleNotFoundError"

**Causa**: Falta alguma biblioteca no `requirements.txt`

**Solução**:
1. Adicione a biblioteca faltante no `requirements.txt`
2. Faça commit e push
3. Aguarde re-deploy automático

### Problema 2: "File not found"

**Causa**: Caminho de arquivo incorreto

**Solução**:
- Use caminhos relativos (ex: `data/raw/arquivo.xlsx`)
- Não use caminhos absolutos (ex: `C:\Users\...`)

### Problema 3: Dados muito grandes

**Causa**: GitHub tem limite de 100MB por arquivo

**Soluções**:
1. **Usar Git LFS** (Large File Storage)
2. **Hospedar dados externamente** (Google Drive, Dropbox)
3. **Comprimir dados** (se possível)

#### Opção: Usar Git LFS

```bash
# Instalar Git LFS
git lfs install

# Rastrear arquivos grandes
git lfs track "*.xlsx"
git lfs track "*.joblib"

# Adicionar .gitattributes
git add .gitattributes

# Commit e push normalmente
git add .
git commit -m "Add large files with LFS"
git push origin main
```

### Problema 4: App não carrega

**Verificar logs**:
1. No Streamlit Cloud, clique em "Manage app"
2. Veja os logs na aba "Logs"
3. Identifique o erro
4. Corrija localmente
5. Faça commit e push

### Problema 5: "Memory limit exceeded"

**Causa**: Aplicação usando muita memória

**Soluções**:
- Otimizar código
- Reduzir tamanho dos dados
- Usar `@st.cache_data` e `@st.cache_resource`
- Considerar upgrade para plano pago

---

## 📊 Parte 6: Monitoramento e Manutenção

### 6.1 Acessar Dashboard do Streamlit Cloud

1. Acesse: https://share.streamlit.io/
2. Veja suas aplicações
3. Clique em "Manage app" para:
   - Ver logs
   - Ver métricas de uso
   - Reboot da aplicação
   - Deletar aplicação

### 6.2 Métricas Disponíveis

- 📈 Número de visitantes
- ⏱️ Tempo de resposta
- 💾 Uso de memória
- 🔄 Status do deploy

### 6.3 Limites do Plano Gratuito

- **Apps**: 1 app público
- **Recursos**: 1 GB RAM
- **Uptime**: Pode hibernar após inatividade
- **Visitantes**: Ilimitados

---

## 🎯 Checklist Final

Antes de considerar o deploy completo, verifique:

- [ ] ✅ Aplicação funciona localmente
- [ ] ✅ Código no GitHub (repositório público)
- [ ] ✅ `requirements.txt` completo e correto
- [ ] ✅ Deploy no Streamlit Cloud concluído
- [ ] ✅ URL pública funcionando
- [ ] ✅ Todas as funcionalidades testadas
- [ ] ✅ URL adicionada ao README.md
- [ ] ✅ URL compartilhada com equipe/professor

---

## 📝 Adicionar URL ao README

Após o deploy, adicione a URL no topo do seu `README.md`:

```markdown
# 📚 Datathon PEDE - Associação Passos Mágicos

## 🌐 Aplicação Online
**Acesse a aplicação**: https://SEU-USUARIO-fiap-datathon-pede-app-XXXXX.streamlit.app

---

[resto do README...]
```

Faça commit e push:

```bash
git add README.md
git commit -m "Add deployed app URL to README"
git push origin main
```

---

## 🆘 Suporte

### Documentação Oficial:
- Streamlit Docs: https://docs.streamlit.io/
- Deploy Guide: https://docs.streamlit.io/streamlit-community-cloud/deploy-your-app
- GitHub Docs: https://docs.github.com/

### Comunidade:
- Streamlit Forum: https://discuss.streamlit.io/
- Stack Overflow: Tag `streamlit`

### Contato da Equipe:
Se tiver problemas, entre em contato com os membros da equipe listados no README.

---

## 💡 Dicas Extras

### Melhorar Performance:
```python
# Use cache para dados
@st.cache_data
def load_data():
    return pd.read_excel('data.xlsx')

# Use cache para modelos
@st.cache_resource
def load_model():
    return joblib.load('model.joblib')
```

### Adicionar Secrets (senhas, API keys):
1. No Streamlit Cloud: Manage app → Settings → Secrets
2. Adicione no formato TOML:
```toml
[passwords]
database = "senha123"
api_key = "abc123"
```
3. Use no código:
```python
import streamlit as st
senha = st.secrets["passwords"]["database"]
```

### Customizar URL:
- Plano gratuito: URL automática
- Plano pago: URL customizada (ex: `datathon-pede.streamlit.app`)

---

## 🎓 Resumo dos Comandos

```bash
# 1. Inicializar Git
git init
git add .
git commit -m "Initial commit"

# 2. Conectar ao GitHub
git remote add origin https://github.com/SEU-USUARIO/fiap-datathon-pede.git
git branch -M main
git push -u origin main

# 3. Atualizar depois
git add .
git commit -m "Descrição da mudança"
git push origin main
```

---

**Pronto! Sua aplicação está no ar! 🚀**

**Tempo total estimado**: 15-30 minutos (primeira vez)

---

**Desenvolvido com ❤️ para a Associação Passos Mágicos**
**FIAP Pós-Tech em Data Analytics - Datathon Fase 5 - 2026**
