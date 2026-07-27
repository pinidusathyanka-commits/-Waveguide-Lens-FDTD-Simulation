# %%
# Importing the necessary packages
import matplotlib.pyplot as plt
from LightWave2D.grid import Grid
from LightWave2D.experiment import Experiment
from MPSPlots.colormaps import polytechnique

# %%
# Define the simulation grid
grid = Grid(
    resolution=0.1e-6,  # Grid resolution in meters
    size_x=60e-6,       # Grid size in the x direction in meters
    size_y=50e-6,       # Grid size in the y direction in meters
    n_steps=1200        # Number of time steps to capture full propagation
)

# Initialize the assignment experiment
experiment = Experiment(grid=grid)

# %%
# 1. Adding multiple waveguides to bend the EM field at 45 degrees
# Top Straight Section
scatterer1 = experiment.add_waveguide(
    position_0=('10%', '90%'),
    position_1=('30%', '90%'),
    width=1e-6,
    epsilon_r=60  # Increased permittivity to minimize spill out
)

# Bottom Straight Section
scatterer2 = experiment.add_waveguide(
    position_0=('10%', '80%'),
    position_1=('30%', '80%'),
    width=1e-6,
    epsilon_r=60
)

# Top 45-degree Bend Section
scatterer3 = experiment.add_waveguide(
    position_0=('30%', '90%'),
    position_1=('50%', '70%'),
    width=1e-6,
    epsilon_r=60
)

# Bottom 45-degree Bend Section
scatterer4 = experiment.add_waveguide(
    position_0=('30%', '80%'),
    position_1=('50%', '60%'),
    width=1e-6,
    epsilon_r=60
)


# %%
# 2. Adding a Lens at the output end of the Waveguide to diverge the beam
try:
    lens_scatterer = experiment.add_lense(
        position=('52%', '65%'),  # Output end of the waveguide
        epsilon_r=2.5,            # Relative permittivity of the lens
        curvature=8e-6,           # Curvature to diverge the beam
        width=3e-6                # Width of the lens
    )
except AttributeError:
    lens_scatterer = experiment.add_lens(
        position=('52%', '65%'),
        epsilon_r=2.5,
        curvature=8e-6,
        width=3e-6
    )


# %%
# 3. Adding a Point Source calculated for Index: 2023t01659 (Wavelength = 1390nm)
source = experiment.add_point_source(
    wavelength=1390e-9,       # 800 + (10 * 59) = 1390nm
    position=('15%', '85%'),  # Input end of the waveguide
    amplitude=50              # Amplitude of the source
)


# %%
# 4. Adding a perfectly matched layer (PML) to absorb boundary reflections
experiment.add_pml(
    order=1,          
    width='10%',      
    sigma_max=5000    
)


# %%
# Plot the experiment layout
print("Plotting assignment layout...")
experiment.plot()
plt.show()


# %%
# Run the FDTD simulation
print("Running FDTD simulation for assignment...")
experiment.run_fdtd()
print("Simulation complete.")


# %%
# Plot the resulting electric field distribution at the final frame
experiment.plot_frame(
    frame_number=-1,
    scale_max=5,
    colormap=polytechnique.red_black_blue
)
plt.show()


# %%
# Render and Save the animation of the wave propagation over time
print("Rendering propagation animation...")
try:
    animation = experiment.render_propagation(
        skip_frame=10,
        colormap=polytechnique.red_black_blue,
        scale_max=15
    )
except AttributeError:
    animation = experiment.show_propagation(
        skip_frame=10,
        colormap=polytechnique.red_black_blue,
        scale_max=15
    )

# Save as GIF
animation.save('./assignment_waveguide_lens.gif', writer='pillow', fps=20)
print("Assignment simulation completed successfully!")
