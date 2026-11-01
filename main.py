import pandas as pd
import matplotlib.pyplot as plt

# --- 1. DATA LOADING & MANIPULATION ---
# In A-Level, you used open(). In data science, pandas reads CSVs directly into a 'DataFrame'
df = pd.read_csv('material_properties.csv')

# Calculate Specific Strength (Strength-to-Weight Efficiency)
# Pandas allows vector operations without writing explicit 'for' loops!
df['Specific_Strength'] = df['Tensile_Strength_MPa'] / df['Density_g_cm3']

print("--- Cleaned Dataset with Calculated Specific Strength ---")
print(df.to_string())

# --- 2. DESCRIPTIVE STATISTICS ---
print("\n--- Summary Statistics Across All Material Families ---")
# .describe() instantly calculates count, mean, min, max, and quartiles
print(df.describe().round(2))

# Group data by Material Family to find local averages
print("\n--- Average Properties by Material Family ---")
print(df.groupby('Family')[['Specific_Strength', 'Thermal_Conductivity_W_mK']].mean().round(2))

# --- 3. DATA VISUALIZATION ---
# Initialize a scatter plot window
plt.figure(figsize=(10, 6))

# Map families to distinct colors for professional rendering
colors = {
    'Ferrous Metal': '#4A5568', 
    'Non-Ferrous Metal': '#ED8936', 
    'Superalloy': '#E53E3E', 
    'Polymer': '#3182CE', 
    'Composite': '#38A169'
}

# Plot each material point and add interactive text labels
for index, row in df.iterrows():
    plt.scatter(
        row['Thermal_Conductivity_W_mK'], 
        row['Specific_Strength'], 
        color=colors[row['Family']], 
        s=120, 
        edgecolor='black', 
        alpha=0.8
    )
    # Annotate point with its Material Name
    plt.text(
        row['Thermal_Conductivity_W_mK'] + 5, 
        row['Specific_Strength'] + 2, 
        row['Material'], 
        fontsize=9
    )

# Apply Styling and Labels
plt.title('Engineering Material Performance Trade-offs', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Thermal Conductivity (W/m·K) — [Higher means better Heat Dissipation]', fontsize=11)
plt.ylabel('Specific Strength (MPa / (g/cm³)) — [Higher means lighter/stronger structure]', fontsize=11)
plt.grid(True, linestyle='--', alpha=0.5)

# Render a custom color legend manually
from matplotlib.lines import Line2D
legend_elements = [Line2D([0], [0], marker='o', color='w', label=fam, markerfacecolor=col, markersize=10, markeredgecolor='black') 
                   for fam, col in colors.items()]
plt.legend(handles=legend_elements, title="Material Families", loc="upper right")

plt.tight_layout()
plt.show() # Renders chart in an interactive graphical window
