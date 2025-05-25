def start_system():
    print("Iniciando sistema do robô (modo simulado)...")
    from web.server import run_web
    run_web()
