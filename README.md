# 💕 Dia dos Namorados - Apresentação Interativa

Uma apresentação visual e interativa para compartilhar sua história de amor com alguém especial!

## ✨ Funcionalidades

- 🎬 **Slides animados** - Navegue pela sua história
- 📸 **Adicione fotos** - Em cada seção (momentos, viagens, final, música)
- 🎵 **Música de fundo** - Toca enquanto você passa pelos slides
- 📱 **Totalmente responsivo** - Funciona em celular, tablet e desktop
- 🚀 **Funciona offline** - Sem internet, sem problema!

## 🚀 Como Usar

### 1. Abra o arquivo HTML
Abra `dia-dos-namorados (1).html` em qualquer navegador

### 2. Adicione as fotos
Clique nas áreas de foto para adicionar:
- 💑 **Nossos momentos** - Uma foto de vocês
- 🎵 **Nossa música** - A capa da música ou uma foto
- 🏖️ **Viagens** - Uma foto de cada destino
- 💕 **Final** - A foto final (casal)

### 3. Compartilhe
- **No WhatsApp**: Envie o arquivo pelo app
- **No GitHub**: Envie para um repositório (veja abaixo)
- **Por Email**: Compartilhe o arquivo HTML

## 📤 Como Enviar pelo GitHub

### Passo 1: Coloque as fotos na pasta `imagens/`

Estrutura de pastas:
```
imagens/
├── nossos-momentos.jpg    (500x600px - ideal)
├── musica.jpg             (300x300px)
├── final.jpg              (500x600px)
└── viagens/
    ├── trip-0.jpg         (Colônia Witmarsum)
    ├── trip-1.jpg         (São Paulo)
    ├── trip-2.jpg         (Ilha do Mel)
    ├── trip-3.jpg         (Guaratuba)
    ├── trip-4.jpg         (Guarujá)
    ├── trip-5.jpg         (Morretes)
    ├── trip-6.jpg         (Lapa)
    ├── trip-7.jpg         (Gramado)
    ├── trip-8.jpg         (Praia Grande)
    ├── trip-9.jpg         (Torres)
    ├── trip-10.jpg        (Balneário Camboriú)
    └── trip-11.jpg        (Porto de Galinhas)
```

### Passo 2: Rode o script para embutir as fotos
```bash
python3 embutir_fotos.py
```

### Passo 3: Faça push para GitHub
```bash
git add .
git commit -m "Adicionando fotos do Dia dos Namorados"
git push origin master
```

### Passo 4: Ative GitHub Pages
1. Vá em **Settings** do repositório
2. Procure por **Pages**
3. Escolha **master** como branch
4. Pronto! Seu site estará em: `https://holanda-057.github.io/Dia-dos-Namorados/`

## 📖 Seções

1. **Capa** - Apresentação visual
2. **Desde quando** - Contagem de dias
3. **Fotos** - Suas melhores fotos
4. **Nossos momentos** - Timeline com marco importantes
5. **Nossa música** - Música com player
6. **Mensagem** - Sua mensagem de amor
7. **Nossas viagens** - Galeria de destinos
8. **Final** - Fechamento com mensagem

## 🎨 Personalizações

Abra o arquivo `dia-dos-namorados (1).html` em um editor de texto e procure por:
- `CONFIG.startDate` - Mude a data de início
- `CONFIG.msgBody` - Mude a mensagem
- `CONFIG.milestones` - Mude os marcos da relação

## 💾 Arquivo de Música

A música está embutida como Base64. Se quiser trocar:
1. Baixe uma música em MP3
2. Substitua `musica.mp3`
3. Rode `embutir_fotos.py` de novo

## 🔗 Links Úteis

- [GitHub](https://github.com/holanda-057)
- [Ver apresentação online](https://holanda-057.github.io/Dia-dos-Namorados/)

## 💕 Dicas

- Use fotos em alta qualidade (mas não muito pesadas)
- Teste primeiro localmente antes de enviar
- Se a página ficar lenta, reduza o tamanho das fotos
- As fotos são salvas em Base64 para funcionarem sem internet

---

**Feito com ❤️ para o Dia dos Namorados**
