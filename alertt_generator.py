import json
import os
import time
import openai

# Charger la clé OpenAI depuis variable d'environnement
openai.api_key = os.getenv("OPENAI_API_KEY")

# Fichier de log local des alertes
ALERT_LOG_FILE = r"C:\Users\dell\OneDrive\Bureau\NIDS\alerts.json"

def generate_alert(flow_features: dict):
    """
    Envoie le flow au LLM pour générer une alerte JSON style Suricata
    """
    prompt = f"""
    Analyze this network flow and generate a JSON alert ONLY if it looks malicious.
    Flow details: {flow_features}
    Return JSON with:
    {{
        "Timestamp": "...",
        "Src IP": "...",
        "Dst IP": "...",
        "Protocol": "...",
        "Attack Type": "...",
        "Description": "..."
    }}
    If benign, return an empty JSON: {{}}
    """

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=200
        )

        alert_text = response['choices'][0]['message']['content'].strip()

        # Convertir la réponse en dict JSON
        if alert_text and alert_text != "{}":
            alert = json.loads(alert_text)
            # Ajouter timestamp si manquant
            if "Timestamp" not in alert:
                alert["Timestamp"] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            
            # Sauvegarder localement
            save_alert(alert)
            print(f"{alert['Src IP']} → {alert['Dst IP']} | Type: {alert.get('Attack Type')}")
            return alert
        else:
            # Pas d'alerte
            return None

    except Exception as e:
        print(f"Failed to generate LLM alert: {e}")
        return None

def save_alert(alert: dict):
    """Append alert to local JSON log file"""
    try:
        if os.path.exists(ALERT_LOG_FILE):
            with open(ALERT_LOG_FILE, "r") as f:
                alerts = json.load(f)
        else:
            alerts = []

        alerts.append(alert)

        with open(ALERT_LOG_FILE, "w") as f:
            json.dump(alerts, f, indent=2)

    except Exception as e:
        print(f"Failed to save alert: {e}")
