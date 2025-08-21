#!/usr/bin/env python3
"""
SAVAGE SCIENTIFIC COMMAND SELECTOR
PhD-level randomness with cryptographic entropy
"""

import os
import hashlib
import random
from pathlib import Path
from datetime import datetime

def get_cryptographic_random_commands(commands_dir="commands", count=5):
    """Use system entropy + timestamp for true randomness"""
    
    # Get all command files
    cmd_path = Path(commands_dir)
    all_commands = list(cmd_path.glob("*.md"))
    
    # Create seed from system entropy + timestamp
    entropy = os.urandom(32)  # 256 bits of entropy
    timestamp = str(datetime.now().timestamp()).encode()
    
    # Create cryptographic hash for seed
    hasher = hashlib.sha256()
    hasher.update(entropy)
    hasher.update(timestamp)
    seed = int(hasher.hexdigest(), 16) % (2**32)
    
    # Initialize random with cryptographic seed
    random.seed(seed)
    
    # Select commands
    selected = random.sample(all_commands, min(count, len(all_commands)))
    
    print(f"🎲 CRYPTOGRAPHIC SELECTION (seed: {seed})")
    print(f"📊 Selected {len(selected)} commands from {len(all_commands)} available")
    
    for i, cmd in enumerate(selected, 1):
        print(f"{i}. {cmd.name}")
    
    return selected

if __name__ == "__main__":
    selected = get_cryptographic_random_commands()