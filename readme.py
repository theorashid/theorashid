from rich.console import Console
from rich.tree import Tree

console = Console(record=True, width=100)

tree = Tree("[link=https://theorashid.github.io/]Theo Rashid", guide_style="bold bright_black")

self_tree = tree.add("code for me", guide_style="bright_black")
self_tree.add("[bold link=https://github.com/theorashid/probabilistic-programming-packages]probabilistic-programming-packages[/]  - [bright_black]same forecasting model, different probabilistic programming languages")
self_tree.add("[bold link=https://github.com/theorashid/mortality-statsmodel]mortality-statsmodel[/]                - [bright_black]scalable, hierarchical Bayesian models for mortality over space and time")

contrib_tree = tree.add("code I helped with", guide_style="bright_black")
contrib_tree.add("[bold link=https://github.com/pyro-ppl/numpyro]numpyro[/]                             - [bright_black]probabilistic programming, jax backend")
contrib_tree.add("[bold link=https://github.com/pymc-devs/pymc]pymc[/]                                - [bright_black]probabilistic programming, aesara backend")

future_tree = tree.add("code I would like to work on", guide_style="bright_black")
future_tree.add("[bold link=https://github.com/blackjax-devs/blackjax]blackjax[/]                            - [bright_black]samplers in jax")
future_tree.add("[bold link=https://github.com/aesara-devs/aemcmc]aemcmc[/]                              - [bright_black]samplers in aesara")
future_tree.add("[bold link=https://github.com/probml/dynamax]dynamax[/]                             - [bright_black]state space models in jax")
future_tree.add("[bold link=https://github.com/thomaspinder/GPJax]GPJax[/]                               - [bright_black]Gaussian Processes in jax")
future_tree.add("[bold link=https://github.com/nimble-dev/nimble]nimble[/]                              - [bright_black]probabilistic programming with customisable samplers in R")

work_tree = tree.add("work", guide_style="bright_black")

amazon_tree = work_tree.add("Amazon                              - [bright_black]Applied Scientist intern, Bayesian multivariate time series")

imperial_tree = work_tree.add("Imperial College London")
imperial_tree.add("PhD, Biostatistics (in progress)- [bright_black]Scalable, Bayesian spatiotemporal mortality modelling")
imperial_tree.add("MSci, Theoretical Physics       - [bright_black]Mostly maths")

console.print(tree)
console.print("")
console.print("[green]Follow me on twitter [bold link=https://twitter.com/theorashid]@theorashid[/]")

CONSOLE_HTML_FORMAT = """\
<pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">{code}</pre>
"""

console.save_html("README.md", inline_styles=True, code_format=CONSOLE_HTML_FORMAT)
