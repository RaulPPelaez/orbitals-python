"""Numerical integrators for ordinary differential equations."""

from abc import ABC, abstractmethod
from typing import Callable, Sequence


class Integrator(ABC):
    """Base class for one-step ODE integrators.

    :param equation: Differential equation callable.
    :param dt: Integration time step.
    """

    def __init__(
        self,
        equation: Callable[[float, Sequence[float]], Sequence[float]],
        dt: float,
    ) -> None:
        self.equation = equation
        self.dt = dt

    @abstractmethod
    def step(self, t: float, state: Sequence[float]) -> tuple[float, list[float]]:
        """Advance one integration step.

        :param t: Current simulation time.
        :param state: Current state vector.
        :return: Tuple ``(new_t, new_state)``.
        """


class EulerIntegrator(Integrator):
    """Forward Euler integrator."""

    def step(self, t: float, state: Sequence[float]) -> tuple[float, list[float]]:
        """Compute one Euler step.

        :param t: Current simulation time.
        :param state: Current state vector.
        :return: Tuple ``(t + dt, updated_state)``.
        """
        derivatives = self.equation(t, state)
        new_state = [s + ds * self.dt for s, ds in zip(state, derivatives)]
        return t + self.dt, new_state


class RK4Integrator(Integrator):
    """Classical fourth-order Runge-Kutta integrator."""

    def step(self, t: float, state: Sequence[float]) -> tuple[float, list[float]]:
        """Compute one RK4 step.

        :param t: Current simulation time.
        :param state: Current state vector.
        :return: Tuple ``(t + dt, updated_state)``.
        """
        f = self.equation
        dt = self.dt
        k1 = f(t, state)
        k2 = f(t + dt / 2, [s + k1_i * dt / 2 for s, k1_i in zip(state, k1)])
        k3 = f(t + dt / 2, [s + k2_i * dt / 2 for s, k2_i in zip(state, k2)])
        k4 = f(t + dt, [s + k3_i * dt for s, k3_i in zip(state, k3)])
        new_state = [
            s + (dt / 6) * (k1_i + 2 * k2_i + 2 * k3_i + k4_i)
            for s, k1_i, k2_i, k3_i, k4_i in zip(state, k1, k2, k3, k4)
        ]
        return t + dt, new_state
