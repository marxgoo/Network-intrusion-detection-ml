from sniffer import start_sniffing

if __name__ == "__main__":
    print("="*80)
    print("IDS ML Temps Réel - Démarrage")
    print("Seules les anomalies sont affichées")
    print("Ctrl+C pour arrêter")
    print("="*80)

    try:
        start_sniffing(interface=None)  # ou "Wi-Fi"
    except KeyboardInterrupt:
        print("\n[*] IDS arrêté par l'utilisateur")
    except Exception as e:
        print("[ERROR Main]", e)
