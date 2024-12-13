# /// script
# dependencies = [
#   "rich",
# ]
# ///

# `uv run readme.py` to generate README.md
from rich.console import Console
from rich.tree import Tree

console = Console(record=True, width=100)

tree = Tree("[link=https://theorashid.github.io/]Theo Rashid", guide_style="bold bright_black")

self_tree = tree.add("code for me", guide_style="bright_black")
self_tree.add("[bold link=https://github.com/theorashid/probabilistic-programming-packages]probabilistic-programming-packages[/]  - [bright_black]same forecasting model, different PPLs")
self_tree.add("[bold link=https://github.com/theorashid/mortality-statsmodel]mortality-statsmodel[/]                - [bright_black]scalable, Bayesian spatiotemporal models for mortality")
self_tree.add("[bold link=https://github.com/sparklabnyc/bayesian-envhealth-models]bayesian-envhealth-models[/]           - [bright_black]Bayesian models for environmental health")
self_tree.add("[bold link=https://github.com/sparklabnyc/cookiecutter-r-project]cookiecutter-r-project[/]              - [bright_black]template for analysis project in R")
self_tree.add("[bold link=https://github.com/theorashid/numba-oslo]numba-oslo[/]                          - [bright_black]fractal simulation in numba")
self_tree.add("[bold link=https://github.com/theorashid/xarray-tropical-cyclones]xarray-tropical-cyclones[/]            - [bright_black]tropical cyclone analysis with xarray")

contrib_tree = tree.add("code I helped with", guide_style="bright_black")
contrib_tree.add("[bold link=https://github.com/pyro-ppl/numpyro]numpyro[/]                             - [bright_black]probabilistic programming, jax backend")
contrib_tree.add("[bold link=https://github.com/pymc-devs/pymc]pymc[/]                                - [bright_black]probabilistic programming, pytensor backend")
contrib_tree.add("[bold link=https://github.com/pymc-devs/pytensor]pytensor[/]                            - [bright_black]python C/jax/numba tensor library")
contrib_tree.add("[bold link=https://github.com/jax-ml/bayeux]bayeux[/]                              - [bright_black]inference for Bayesian models in jax")
contrib_tree.add("[bold link=https://github.com/thomaspinder/GPJax]GPJax[/]                               - [bright_black]Gaussian processes in jax")

future_tree = tree.add("code I would like to work on", guide_style="bright_black")
future_tree.add("[bold link=https://github.com/blackjax-devs/blackjax]blackjax[/]                            - [bright_black]samplers in jax")
future_tree.add("[bold link=https://github.com/probml/dynamax]dynamax[/]                             - [bright_black]state space models in jax")
future_tree.add("[bold link=https://github.com/nimble-dev/nimble]nimble[/]                              - [bright_black]probabilistic programming in R, customisable samplers")

work_tree = tree.add("work", guide_style="bright_black")

work_tree.add("Amazon                              - [bright_black]Applied Scientist II, probabilistic forecasting")
work_tree.add("Faculty                             - [bright_black]Data Science Fellow")
work_tree.add("Freelance                           - [bold link=https://www.loamin.com/]Loamin[/], [bold link=https://sparklabnyc.github.io/site/home.html]Robbie Parks, Columbia[/], [bold link=https://sethrf.com/]Seth Flaxman, Oxford[/]")
work_tree.add("Amazon                              - [bright_black]Applied Scientist intern")

imperial_tree = work_tree.add("Imperial College London")
thesis_tree = imperial_tree.add("PhD, Biostatistics              - [bright_black]Scalable spatiotemporal mortality modelling")
thesis_tree.add("[bold link=https://github.com/theorashid/thesis]thesis[/]                      - [bright_black]thesis, written in quarto")
thesis_tree.add("[bold link=https://github.com/theorashid/thesis-analysis]thesis-analysis[/]             - [bright_black]code for postprocessing and plotting in thesis")
imperial_tree.add("MSci, Theoretical Physics       - [bright_black]Mostly maths")

console.print(tree)
console.print("")
console.print("Read [bold link=https://theorashid.github.io/notes/]what I'm learning[/].")

CONSOLE_HTML_FORMAT = """\
<pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">{code}</pre>
"""

console.save_html("README.md", inline_styles=True, code_format=CONSOLE_HTML_FORMAT)
