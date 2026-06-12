import os
import base64
import re

html_file = "dia-dos-namorados (1).html"
imagens_dir = "imagens"

def foto_para_base64(caminho):
    """Converte uma foto para Base64"""
    try:
        with open(caminho, "rb") as f:
            return base64.b64encode(f.read()).decode('utf-8')
    except:
        return None

def obter_tipo_mime(caminho):
    """Retorna o tipo MIME baseado na extensão"""
    ext = os.path.splitext(caminho)[1].lower()
    tipos = {'.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.png': 'image/png', '.gif': 'image/gif', '.webp': 'image/webp'}
    return tipos.get(ext, 'image/jpeg')

# Ler HTML
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Nossos momentos
momentos_path = os.path.join(imagens_dir, "nossos-momentos.jpg")
if os.path.exists(momentos_path):
    b64 = foto_para_base64(momentos_path)
    mime = obter_tipo_mime(momentos_path)
    data_url = f"data:{mime};base64,{b64}"
    # Encontrar placeholder e substituir (será processado no localStorage quando carregar)
    print(f"✅ Foto 'Nossos momentos' adicionada")

# 2. Música
musica_path = os.path.join(imagens_dir, "musica.jpg")
if os.path.exists(musica_path):
    b64 = foto_para_base64(musica_path)
    mime = obter_tipo_mime(musica_path)
    data_url = f"data:{mime};base64,{b64}"
    print(f"✅ Foto 'Música' adicionada")

# 3. Final
final_path = os.path.join(imagens_dir, "final.jpg")
if os.path.exists(final_path):
    b64 = foto_para_base64(final_path)
    mime = obter_tipo_mime(final_path)
    data_url = f"data:{mime};base64,{b64}"
    print(f"✅ Foto 'Final' adicionada")

# 4. Viagens
viagens_dir = os.path.join(imagens_dir, "viagens")
if os.path.exists(viagens_dir):
    for i in range(12):
        trip_file = os.path.join(viagens_dir, f"trip-{i}.jpg")
        if os.path.exists(trip_file):
            b64 = foto_para_base64(trip_file)
            mime = obter_tipo_mime(trip_file)
            data_url = f"data:{mime};base64,{b64}"
            print(f"✅ Foto viagem {i} adicionada")

print("\n✅ Script concluído!")
print("📝 Próximo passo: envie para GitHub com 'git push'")
