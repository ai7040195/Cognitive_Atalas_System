"""
ADVANCED MODULES - Quantum and Bio-Inspired Computing Systems
"""

from .quantum_brain_emulator import create_quantum_emulator, QuantumBrainEmulator
from .bio_inspired_computing import create_bio_computing, BioInspiredComputing
from .temporal_fractal_memory import create_temporal_memory, TemporalFractalMemory

__all__ = [
    'create_quantum_emulator',
    'QuantumBrainEmulator', 
    'create_bio_computing',
    'BioInspiredComputing',
    'create_temporal_memory', 
    'TemporalFractalMemory'
]
