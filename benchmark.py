import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.patches import Patch

# Set style
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")
plt.rcParams['figure.figsize'] = [12, 8]
plt.rcParams['font.family'] = 'DejaVu Sans'

# Data
versions = [
    "Basic Implementatio, 1 Threads",
    "Checkerboard Pattern, 1 Threads",
    "Exp lookup, 1 Threads",
    "Xorshiro RNG, 1 Threads",
    "Simple Threading, 14 Threads",
    "Bit-parallel (64 sims), 14 Threads",
    "Troyer, 14 Threads"
]

# Performance numbers (spin flips per second)
# Fill in your measured numbers
performance = [
    1.62E+07,    # Basic Implementation
    1.64E+08,  
    2.05E+08,   
    3.25E+08,
    8.45E+08,
    7.37E+09,
    2.84E+09,
]

performance_ns = [p / 1e9 for p in performance] # to nanoseconds

# Key optimizations for each version
optimizations = [
    "Base version with basic RNG",
    "Checkerboard updates",
    "Exp lookup",
    "Fast Xorshiro random number generator",
    "Multithreading",
    "64 parallel simulations using bit operations",
    "Troyer"
]

# Create figure and axis
fig, (ax1) = plt.subplots(1, 1, gridspec_kw={'hspace': 0.3})

# Create the bar plot
bars = ax1.bar(versions, performance_ns, width=0.7)

# Customize the bars
for i, bar in enumerate(bars):
    bar.set_alpha(0.7)
    bar.set_edgecolor('black')
    bar.set_linewidth(1.5)
    
    # Add value labels on top of bars
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height,
             f'{height:.3f}',
             ha='center', va='bottom', fontsize=10, fontweight='bold')

# Customize the plot
ax1.set_title('Ising Model Performance Optimization Progress, CPU M4 Pro with 14 cores', pad=20, fontsize=16, fontweight='bold')
ax1.set_ylabel('Spin Flips per Nanosecond', fontsize=12, fontweight='bold')
ax1.tick_params(axis='x', rotation=45, labelsize=10)
ax1.set_yscale('log')
ax1.grid(True, alpha=0.3)

# Overall layout adjustments
plt.gcf().set_size_inches(20, 12)
plt.tight_layout()

# Save the plot
plt.savefig('ising_optimization_progress.png', dpi=300, bbox_inches='tight')
plt.close()

# Optional: Print speedup factors
baseline = performance[0]
print("\nSpeedup factors compared to baseline:")
for v, p in zip(versions[1:], performance[1:]):
    speedup = p / baseline
    #baseline = p
    print(f"{v}: {speedup:.1f}x faster")


threads = np.arange(1, 15)

### Threading benchmark
performance_threads = [ 1.01E+08,
                        1.88E+08,
                        2.78E+08,
                        3.59E+08,
                        2.99E+08,
                        3.73E+08,
                        4.24E+08,
                        4.49E+08,
                        4.93E+08,
                        4.92E+08,
                        5.39E+08,
                        5.55E+08,
                        6.44E+08,
                        8.45E+08]

performance_64_sims = [3.41E+09,
                        4.86E+09,
                        5.81E+09,
                        6.34E+09,
                        5.63E+09,
                        6.22E+09,
                        6.33E+09,
                        6.59E+09,
                        6.86E+09,
                        7.28E+09,
                        6.95E+09,
                        6.96E+09,
                        6.77E+09,
                        7.37E+09]

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(threads, 3.25E+08  * np.ones(14), label="Xorshiro")
plt.plot(threads, performance_threads, marker='o', label="Simple Multithreading")
plt.plot(threads, performance_threads[0] * np.arange(1,15), marker='d', linestyle = 'dashed', label="Linear improvement")

#plt.plot(threads, performance_64_sims, marker='d', label="Performance 64 sims")

# Labels and legend
plt.title("Performance vs Threads", fontsize=16)
plt.xlabel("Number of Threads", fontsize=14)
plt.ylabel("Spin Flips per Seconds", fontsize=14)
plt.xticks(threads)
plt.grid(alpha=0.3)
plt.legend(fontsize=12)
#plt.yscale('log')

plt.tight_layout()


# Save the plot
plt.savefig('threading_performance.png', dpi=300, bbox_inches='tight')

# Show plot
plt.close()
