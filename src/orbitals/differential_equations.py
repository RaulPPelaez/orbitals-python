from abc import ABC, abstractmethod
import numpy as np


class DifferentialEquation(ABC):
    @abstractmethod
    def __call__(self, t, state):
        pass


class OrbitalMotion(DifferentialEquation):
    def __init__(self, G, M):
        self.G = G
        self.M = M

    def __call__(self, t, state):
        x, y, vx, vy = state
        r = np.sqrt(x**2 + y**2)
        ax = -self.G * self.M * x / r**3
        ay = -self.G * self.M * y / r**3
        return [vx, vy, ax, ay]


class OrbitalMotionTwoSuns(DifferentialEquation):
    def __init__(self, G, M):
        self.G = G
        self.M = M

    def __call__(self, t, state):
        x, y, vx, vy = state
        r = np.sqrt(x**2 + y**2)
        # Second sun at (2,0)
        rp = np.sqrt((x - 2) ** 2 + y**2)
        ax = -self.G * self.M * x / r**3 - self.G * self.M * (x - 2) / rp**3
        ay = -self.G * self.M * y / r**3 - self.G * self.M * y / rp**3
        return [vx, vy, ax, ay]

class OrbitalMotionPosition(DifferentialEquation):
    def __init__(self, G, M, positions):
        """
        positions: list of (x, y) tuples — locations of each sun
        M: either a single mass (used for all) or a list of masses (same length as positions)
        """
        self.G = G
        self.positions = positions
        if isinstance(M, (int, float)):
            # Use same mass for all suns
            self.masses = [M] * len(positions)
        else:
            assert len(M) == len(positions), "Length of M and positions must match"
            self.masses = M
    def __call__(self, t, state):
        x, y, vx, vy = state
        ax, ay = 0, 0
        for (x_sun, y_sun), M in zip(self.positions, self.masses):
            dx = x - x_sun
            dy = y - y_sun
            r = np.sqrt(dx**2 + dy**2) + 1e-8  # avoid division by zero
            ax -= self.G * M * dx / r**3
            ay -= self.G * M * dy / r**3
        return [vx, vy, ax, ay]
