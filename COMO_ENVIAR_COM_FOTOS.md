# 📸 Como Enviar Pelo GitHub com Fotos

## Passo 1: Coloque as fotos na pasta `imagens/`

Crie uma pasta chamada `imagens/` e coloque as fotos assim:

```
imagens/
├── nossos-momentos.jpg     ← Foto da seção "Nossos momentos"
├── musica.jpg              ← Foto da seção "Nossa música"
├── final.jpg               ← Foto da página final
└── viagens/                ← Fotos de cada viagem (opcional)
    ├── trip-0.jpg          ← Colônia Witmarsum
    ├── trip-1.jpg          ← São Paulo
    └── ... (até trip-11)
```

## Passo 2: Rode o script para embutir as fotos

Execute este comando no terminal:

```bash
python3 embutir_fotos.py
```

## Passo 3: Envie para o GitHub

```bash
git add .
git commit -m "Adicionando fotos do Dia dos Namorados"
git push
```

## Passo 4: Compartilhe o link!

O link será: `https://seu-usuario.github.io/Dia dos namorados`

Quando ela abrir, **todas as fotos já estarão lá!** 💕

---

**Pronto!** As fotos ficarão embutidas no HTML em Base64, como a música. 🎵📸
