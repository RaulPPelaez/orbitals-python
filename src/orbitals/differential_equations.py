"""Differential equation models used by :mod:`orbitals`."""

from abc import ABC, abstractmethod
from typing import Sequence

import numpy as np


class DifferentialEquation(ABC):
    """Abstract interface for first-order differential equation systems."""

    @abstractmethod
    def __call__(self, t: float, state: Sequence[float]) -> list[float]:
        """Evaluate derivatives for a given time and state.

        :param t: Simulation time.
        :param state: Current state vector.
        :return: Time derivatives with the same ordering as ``state``.
        """


class OrbitalMotion(DifferentialEquation):
    """Planar motion under gravity from a single mass at the origin.

    :param G: Gravitational constant.
    :param M: Mass of the central body.
    """

    def __init__(self, G: float, M: float) -> None:
        self.G = G
        self.M = M

    def __call__(self, t: float, state: Sequence[float]) -> list[float]:
        """Return derivatives for state ``[x, y, vx, vy]``.

        :param t: Simulation time (kept for interface compatibility).
        :param state: Current state ``[x, y, vx, vy]``.
        :return: Derivatives ``[dx/dt, dy/dt, dvx/dt, dvy/dt]``.
        """
        x, y, vx, vy = state
        r = np.sqrt(x**2 + y**2)
        ax = -self.G * self.M * x / r**3
        ay = -self.G * self.M * y / r**3
        return [vx, vy, ax, ay]


class OrbitalMotionTwoSuns(DifferentialEquation):
    """Planar motion under gravity from two equal masses.

    The masses are fixed at ``(0, 0)`` and ``(2, 0)``.

    :param G: Gravitational constant.
    :param M: Mass of each fixed body.
    """

    def __init__(self, G: float, M: float) -> None:
        self.G = G
        self.M = M

    def __call__(self, t: float, state: Sequence[float]) -> list[float]:
        """Return derivatives for state ``[x, y, vx, vy]``.

        :param t: Simulation time (kept for interface compatibility).
        :param state: Current state ``[x, y, vx, vy]``.
        :return: Derivatives ``[dx/dt, dy/dt, dvx/dt, dvy/dt]``.
        """
        x, y, vx, vy = state
        r = np.sqrt(x**2 + y**2)
        # Second sun at (2,0)
        rp = np.sqrt((x - 2) ** 2 + y**2)
        ax = -self.G * self.M * x / r**3 - self.G * self.M * (x - 2) / rp**3
        ay = -self.G * self.M * y / r**3 - self.G * self.M * y / rp**3
        return [vx, vy, ax, ay]
