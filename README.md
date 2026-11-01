# Engineering Material Property Analysis & Selection Suite

A Python data analytics utility designed to process, analyze, and visually model mechanical and thermal engineering properties for common design materials. This tool evaluates performance trade-offs—such as weight efficiency versus thermal management—to establish clear material selection criteria for structural and industrial applications.

## Project Scope & Objectives
* **Property Modeling**: Evaluates 10 core engineering materials across 5 distinct structural families (Ferrous, Non-Ferrous, Superalloys, Polymers, and Composites).
* **Performance Indicators**: Evaluates Density ($g/cm^3$), Tensile Strength ($MPa$), and Thermal Conductivity ($W/m\cdot K$).
* **Weight Efficiency**: Computes a derived Specific Strength metric ($MPa / (g/cm^3)$) to measure structural weight efficiency.
* **Trade-Off Optimization**: Generates dual-axis engineering scatter charts to locate material design sweet spots (e.g., aerospace frames vs. heat sinks).

## Core Architecture & Libraries
This project transitions standard procedural file-handling workflows into professional vector-based data science pipelines:
* **Pandas**: Used for seamless CSV database loading, automatic data matrix formatting, and vectorized feature generation without performance-heavy loops.
* **Matplotlib**: Utilized to handle complex multi-variable categorical plotting, custom label coordinates, and color-coded engineering legends.

## Dataset Structure (`material_properties.csv`)
The clean, structured spreadsheet database contains properties across major structural categories:
* **Ferrous Metals**: Structural Steel (A36), Stainless Steel (304)
* **Non-Ferrous Metals**: Aluminum Alloy (6061-T6), Pure Copper (C101)
* **Superalloys**: Titanium Alloy (Ti-6Al-4V), Inconel 625
* **Polymers & Composites**: ABS, Polycarbonate, Nylon 6,6, Carbon Fiber Composite (CFRP)

## Technical Installation & Execution

1. Clone or download this project repository directory to your local workstation.
2. Install the necessary data analytics libraries via your terminal:
   ```bash
   pip install pandas matplotlib
   ```
3. Open the directory within your development workspace (e.g., VS Code) and run the analytical suite:
   ```bash
   python main.py
   ```

## Analytical Project Boundaries
This project utilizes macro-level values compiled from established materials literature as a comparative baseline. It serves as an evaluative selection guide rather than a definitive final engineering specification. Actual operational profiles will vary depending on exact alloy designations, temper conditions, thermal processing histories, and custom manufacturing variables.
