"""Regenerates the figures and numbers shown in the README.

    pip install matplotlib
    python docs/figures/make_figures.py      # run inside the git clone (uses `git log`)
"""
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
from matplotlib import font_manager

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
for f in Path("/usr/share/fonts/lm").glob("lm*10-*.otf"):  # Latin Modern, if installed
    font_manager.fontManager.addfont(str(f))
plt.style.use(HERE / "paper.mplstyle")
C = plt.rcParams["axes.prop_cycle"].by_key()["color"]


def save(fig, name):
    fig.savefig(HERE / name, metadata={"Date": None})
    plt.close(fig)


def git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True).stdout


# ---- Figure 1: when each piece of material entered the repository
ROWS = [  # (label, path prefix, regex giving the number shown next to each dot)
    ("Lectures", "pc/Teoricas/", r"Teorica (\d+)"),
    ("Practice guides", "pc/Practicas/Guia", r"Guia(\d+)"),
    ("Tutorials", "pc/Tutorial/", r"Tutorial(\d+)"),
    ("Problem classes", "pc/Clase de Problemas/", r"problemas (\d+)"),
    ("Assignments", "pc/Tp1/", None),
    ("Art appreciation", "Apreciacion artistica/", None),
]
fig, ax = plt.subplots(figsize=(7.2, 2.9))
for yi, (label, prefix, rx) in enumerate(ROWS[::-1]):
    files = [f for f in git("ls-files", prefix + "*").splitlines() if f.endswith((".py", ".c", ".txt", ".tex"))]
    groups = {}  # first-commit date -> numbers shown next to the dot
    for f in files:
        follow = ["--follow"] if (ROOT / f).stat().st_size else []  # --follow mismatches empty files
        d = date.fromisoformat(git("log", *follow, "--diff-filter=A", "--format=%ad", "--date=short", "--", f).split()[-1])
        m = re.search(rx, f) if rx else None
        groups.setdefault(d, set()).update({int(m.group(1))} if m else set())
    for k, (d, nums) in enumerate(sorted(groups.items())):
        ax.plot(d, yi, "o", color=C[yi % len(C)], ms=4.2)
        if nums:
            ax.annotate(",".join(map(str, sorted(nums))), (d, yi), xytext=(0, 5 + 6 * (k % 2)),
                        textcoords="offset points", ha="center", fontsize=7.5)
tp2 = date.fromisoformat(git("log", "--diff-filter=A", "--format=%ad", "--date=short", "--", "TP_2_PC").split()[-1])
ax.plot(tp2, 1, "s", color=C[1], ms=4.2)
ax.annotate("TP 2 (submodule)", (tp2, 1), xytext=(-4, 6), textcoords="offset points", ha="right", fontsize=7.5)
ax.annotate("TP 1", (date(2023, 3, 30), 1), xytext=(6, 6), textcoords="offset points", fontsize=7.5)
ax.set_yticks(range(len(ROWS)), [r[0] for r in ROWS[::-1]])
ax.set_ylim(-0.6, len(ROWS) - 0.2)
ax.tick_params(axis="y", length=0, right=False)
ax.tick_params(top=False)
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
ax.set_xlim(date(2023, 3, 22), date(2023, 6, 18))
ax.set_xlabel("date the file was first committed")
save(fig, "fig1-semester.svg")

# ---- Figure 2: TP 1, harvested logistic model of the fish population of a lake
# Same update rule and constants as pc/Tp1/*.py
ALFA, BETA, GAMA, DIAS = 0.000082, 24487, 0.1, 90


def step(y, x):
    return y + ALFA * y * (BETA - y) - GAMA * y - x


def trajectory(y, x, n):
    ys = [y]
    for _ in range(n):
        y = step(y, x)
        ys.append(max(y, 0.0))
        if y <= 0:
            break
    return ys


def days_alive(y, x, n=5000):
    for t in range(1, n + 1):
        y = step(y, x)
        if y <= 0:
            return t
    return None


def run_original(name):  # output of the submitted scripts
    out = subprocess.run([sys.executable, "-I", ROOT / "pc/Tp1" / name], capture_output=True, text=True).stdout
    return int(re.search(r"\d+", out).group())


y_min, x_max = run_original("poblacion_minima_viable.py"), run_original("maximo_rendimiento_posible.py")
r = ALFA * BETA - GAMA  # net growth rate
x_eq = r ** 2 / (4 * ALFA)  # largest catch with an equilibrium
y_sep = (r - (r ** 2 - 4 * ALFA * 237) ** 0.5) / (2 * ALFA)  # unstable equilibrium for x = 237
y_up = (r + (r ** 2 - 4 * ALFA * 237) ** 0.5) / (2 * ALFA)
print(f"minimum viable population (script): {y_min}; unstable equilibrium: {y_sep:.2f}; stable: {y_up:.0f}")
print(f"maximum daily catch over {DIAS} days (script): {x_max}; equilibrium bound: {x_eq:.1f}")
print(f"days alive with catch {x_max}: {days_alive(0.9 * BETA, x_max)}")

fig, axes = plt.subplots(1, 2, figsize=(7.2, 2.8))
ax = axes[0]
for y0, c, ls in ((y_min - 1, C[1], "--"), (y_min, C[0], "-")):
    ys = trajectory(y0, 237, DIAS)
    alive = [y for y in ys if y > 0]
    ax.semilogy(range(len(alive)), alive, color=c, ls=ls, label=f"$y_0 = {y0}$")
    if len(alive) < len(ys):
        ax.plot(len(alive) - 1, alive[-1], "x", color=c, ms=6, mew=1.2)
        ax.annotate(f"extinct on day {len(alive)}", (len(alive) - 1, alive[-1]), xytext=(6, -3),
                    textcoords="offset points", fontsize=7.5, color=c, va="top")
ax.axhline(y_up, color="#8c8c8c", lw=0.6, ls=":")
ax.text(DIAS, y_up * 0.75, "stable equilibrium", ha="right", va="top", fontsize=7.5, color="#4d4d4d")
ax.set_xlabel("day $t$")
ax.set_ylabel("fish $y_t$")
ax.set_title("(a) Catch $x = 237$/day")
ax.legend(loc="center right")
ax.set_xlim(0, DIAS)
ax.set_ylim(1, 6e4)

ax = axes[1]
xs = list(range(11060, 11161))
life = [days_alive(0.9 * BETA, x) for x in xs]
ax.semilogy([x for x, d in zip(xs, life) if d], [d for d in life if d], color=C[0])
ax.axhline(DIAS, color="#8c8c8c", lw=0.6, ls=":")
ax.axvline(x_eq, color=C[2], lw=0.9, ls="--", label=f"equilibrium bound {x_eq:,.0f}")
ax.axvline(x_max, color=C[1], lw=0.9, label=f"script answer {x_max:,}")
ax.text(xs[-1], DIAS * 1.12, "90-day horizon", ha="right", fontsize=7.5, color="#4d4d4d")
ax.set_xlabel("daily catch $x$")
ax.set_ylabel("days until extinction")
ax.set_yticks([40, 60, 100, 200, 400], ["40", "60", "100", "200", "400"])
ax.yaxis.set_minor_formatter(plt.NullFormatter())
ax.set_title("(b) Start at $0.9\\,\\beta$")
ax.legend(loc="upper right")
fig.tight_layout()
save(fig, "fig2-fish-model.svg")
