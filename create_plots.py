import importlib
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

os.makedirs("img", exist_ok=True)
os.makedirs("img/gif", exist_ok=True)

sections = [
    "plots_intro",
    "plots_time_space",
    "plots_world_line",
    "plots_dil_con",
    "plots_vel_add",
    "plots_doppler",
    "plots_doppler_echo",
    "plots_doppler_length",
    "plots_muon",
    "plots_twins",
]

for section in sections:
    importlib.import_module(f"plots.{section}").run()