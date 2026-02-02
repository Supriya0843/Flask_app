import random

def quantum_route_optimizer(zones):
    """
    Quantum-inspired optimization logic
    """
    sorted_zones = sorted(zones, key=lambda x: x["waste"], reverse=True)

    if random.random() > 0.7:
        random.shuffle(sorted_zones)

    return sorted_zones
