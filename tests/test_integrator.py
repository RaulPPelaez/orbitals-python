"""Tests for integrator implementations."""

from orbitals import EulerIntegrator


def test_euler() -> None:
    """Check Euler integration for ``dx/dt = a*x`` over one step."""
    factor = 5.0
    initial = 1.0
    dt = 0.01

    eq = lambda t, state: [factor * state[0]]
    i = EulerIntegrator(eq, dt=dt)
    t, state = 0, [initial]
    assert i.step(t, state) == (dt, [initial + factor * initial * dt])
