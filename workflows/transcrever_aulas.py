#!/usr/bin/env python3
"""
transcrever_aulas.py
Script auxiliar para extrair áudio e gerar transcrições automáticas (.txt / .srt)
dos vídeos das aulas para alimentar a pasta /transcricoes na Fase 1 (Estudo).

Requisitos:
  pip install openai-whisper ffmpeg-python
  (ou utilize a ferramenta MacWhisper nativa no macOS)
"""

import os
import sys
import subprocess
from pathlib import Path

def transcrever_pasta(origem_dir: str, destino_dir: str, modelo: str = "base"):
    origem = Path(origem_dir)
    destino = Path(destino_dir)
    destino.mkdir(parents=True, exist_ok=True)

    videos = sorted(list(origem.glob("*.mp4")))
    print(f"Encontrados {len(videos)} arquivos de vídeo em: {origem}")

    for idx, video in enumerate(videos, 1):
        txt_saida = destino / f"{video.stem}.txt"
        if txt_saida.exists():
            print(f"[{idx}/{len(videos)}] Já transcrito: {video.name}")
            continue

        print(f"[{idx}/{len(videos)}] Transcrevendo: {video.name}...")
        try:
            cmd = [
                "whisper",
                str(video),
                "--model", modelo,
                "--language", "Portuguese",
                "--output_format", "txt",
                "--output_dir", str(destino)
            ]
            subprocess.run(cmd, check=True)
            print(f"Concluído: {video.name}")
        except FileNotFoundError:
            print("Erro: Whisper CLI ou ffmpeg não encontrado no PATH do sistema.")
            print("Dica: No macOS, você também pode arrastar os arquivos para o aplicativo MacWhisper.")
            break
        except Exception as e:
            print(f"Falha ao transcrever {video.name}: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python3 transcrever_aulas.py <pasta_videos> <pasta_transcricoes> [modelo]")
        sys.exit(1)
    
    transcrever_pasta(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else "base")
