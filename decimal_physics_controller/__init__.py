from .core import DecimalPhysicsEngine

__version__ = "0.1.0"

class PhysicsController(DecimalPhysicsEngine):
    """
    Main Interface for the Decimal Physics Library.
    Inherits all precision capabilities from the Core Engine.
    """
    def __init__(self, precision: int = 50):
        super().__init__(precision=precision)
        # Optional: Logging or Status checks here