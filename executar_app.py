"""
Script Inicializador do Artefato Web Operacional
Inicia a aplicação Streamlit em localhost para suporte à decisão da nutricionista.
"""

import os
import sys
import subprocess

def main():
    print("=" * 70)
    print("🍽️  ARTEFATO DE PREVISÃO DE REFEIÇÕES ESCOLARES (DSR / CEETEPS)")
    print("    Iniciando interface web operacional em localhost...")
    print("=" * 70)
    
    app_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "src", "app", "main.py"))
    
    if not os.path.exists(app_path):
        print(f"[ERRO] Arquivo principal da aplicação não encontrado: {app_path}")
        sys.exit(1)
        
    cmd = [
        sys.executable, "-m", "streamlit", "run", app_path,
        "--server.headless", "true",
        "--server.port", "8501"
    ]
    
    try:
        subprocess.run(cmd)
    except KeyboardInterrupt:
        print("\n[OK] Aplicação encerrada pelo usuário.")

if __name__ == "__main__":
    main()
