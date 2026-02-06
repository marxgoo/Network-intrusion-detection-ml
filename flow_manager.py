import time
import numpy as np
from collections import defaultdict
from predictor import predict_flow

# Stockage des flows
flows = defaultdict(lambda: {
    "start_time": time.time(),
    "last_time": time.time(),
    "fwd_pkts": 0,
    "bwd_pkts": 0,
    "fwd_bytes": 0,
    "bwd_bytes": 0,
    "pkt_lengths": [],
    "syn": 0, "ack": 0, "fin": 0, "rst": 0, "psh": 0, "urg": 0
})

FLOW_TIMEOUT = 10  # secondes

def process_packet(packet):
    src = packet["IP"].src
    dst = packet["IP"].dst
    proto = packet["IP"].proto
    length = len(packet)

    key = (src, dst, proto)
    flow = flows[key]

    now = time.time()
    flow["last_time"] = now
    flow["fwd_pkts"] += 1
    flow["fwd_bytes"] += length
    flow["pkt_lengths"].append(length)

    if "TCP" in packet:
        flags = packet["TCP"].flags
        if flags & 0x02: flow["syn"] += 1
        if flags & 0x10: flow["ack"] += 1
        if flags & 0x01: flow["fin"] += 1
        if flags & 0x04: flow["rst"] += 1
        if flags & 0x08: flow["psh"] += 1
        if flags & 0x20: flow["urg"] += 1

    # Si flow expiré → calcul features + prédiction
    if now - flow["start_time"] > FLOW_TIMEOUT:
        features = build_features(src, dst, proto, flow)
        predict_flow(features)
        del flows[key]

def build_features(src, dst, proto, flow):
    duration = max(flow["last_time"] - flow["start_time"], 0.0001)
    total_pkts = flow["fwd_pkts"] + flow["bwd_pkts"]
    total_bytes = flow["fwd_bytes"] + flow["bwd_bytes"]

    pkt_mean = np.mean(flow["pkt_lengths"]) if flow["pkt_lengths"] else 0
    pkt_std = np.std(flow["pkt_lengths"]) if flow["pkt_lengths"] else 0

    features = {
        "Src IP": src,
        "Dst IP": dst,
        "Protocol": proto,
        "Flow Duration": duration * 1_000_000,
        "Tot Fwd Pkts": flow["fwd_pkts"],
        "Tot Bwd Pkts": flow["bwd_pkts"],
        "TotLen Fwd Pkts": flow["fwd_bytes"],
        "TotLen Bwd Pkts": flow["bwd_bytes"],
        "Fwd Pkt Len Mean": pkt_mean,
        "Bwd Pkt Len Mean": pkt_mean,
        "Flow Byts/s": total_bytes / duration,
        "Flow Pkts/s": total_pkts / duration,
        "Pkt Len Mean": pkt_mean,
        "Pkt Len Std": pkt_std,
        "SYN Flag Cnt": flow["syn"],
        "ACK Flag Cnt": flow["ack"],
        "FIN Flag Cnt": flow["fin"],
        "RST Flag Cnt": flow["rst"],
        "PSH Flag Cnt": flow["psh"],
        "URG Flag Cnt": flow["urg"],
    }

    return features
