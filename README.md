# Waveguide-Lens FDTD Simulation

A 2D Finite-Difference Time-Domain (FDTD) simulation demonstrating electromagnetic 
wave propagation through a bent dielectric waveguide coupled to a plano-convex lens, 
built using the [LightWave2D](https://github.com/MartinPdeS/LightWave2D) package.

## Overview

This simulation models a point source injecting a monochromatic wave (λ = 1390 nm) 
into a straight waveguide segment, which bends at 45° before reaching a curved lens 
that diverges the output beam. The full field propagation is captured over 1200 
time steps and rendered as an animated GIF.

## Structure

- **Waveguide (ε_r = 60)**: Two parallel channels with a 45° bend, guiding the wave 
  from the source to the lens interface.
- **Lens (ε_r = 2.5)**: A curved dielectric element placed at the waveguide output 
  to diverge the transmitted beam.
- **Point Source**: Emits at 1390 nm with amplitude 50, positioned at the input end 
  of the waveguide.
- **PML Boundary**: Absorbs outgoing waves at the domain edges to prevent 
  reflections (order 1, width 10%, σ_max = 5000).

## Simulation Parameters

| Parameter          | Value      |
|------------------- |----------- |
| Grid resolution    | 0.1 μm     |
| Domain size        | 60 × 50 μm |
| Time steps         | 1200       |
| Wavelength         | 1390 nm    |

## Output

- Static field distribution at the final time step (`plot_frame`)
- Animated propagation GIF (`assignment_waveguide_lens.gif`)

## Requirements

```bash
pip install LightWave2D MPSPlots matplotlib
```

## Usage

```bash
python assignment_waveguide_lens.py
```

## Dependencies

- [LightWave2D](https://github.com/MartinPdeS/LightWave2D) — FDTD simulation engine
- [MPSPlots](https://github.com/MartinPdeS/MPSPlots) — colormap utilities
- Matplotlib
