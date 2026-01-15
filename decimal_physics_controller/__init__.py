from .core import DecimalPhysicsEngine
from .schrodinger_cat import SchrodingerCatSimulation
from .quantum_entropy import QuantumState, QuantumZenoEffect
from .thermodynamics import ThermodynamicSystem, OptimizationDeath
from .ai_controller import DeterministicAIController

__version__ = "0.1.0"

class PhysicsController(DecimalPhysicsEngine):
    """
    Main Interface for the Decimal Physics Library.
    Inherits all precision capabilities from the Core Engine.
    """
    def __init__(self, precision: int = 50):
        super().__init__(precision=precision)
        # Optional: Logging or Status checks here

__all__ = [
    'DecimalPhysicsEngine',
    'PhysicsController',
    'SchrodingerCatSimulation',
    'QuantumState',
    'QuantumZenoEffect',
    'ThermodynamicSystem',
    'OptimizationDeath',
    'DeterministicAIController',
]