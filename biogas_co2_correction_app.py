import streamlit as st
from math import isclose

# Constants
R = 0.0821  # L·atm/mol·K
T = 298     # Temperature in K (25°C)
P = 1       # Pressure in atm
CO2_molar_mass = 44.01  # g/mol

st.title("Biogas CO₂ Correction Calculator")
st.write("Estimate CO₂ loss into water or brine during biogas measurement using water displacement.")

# Inputs
measured_volume = st.number_input("Measured Gas Volume (L)", min_value=0.0, value=5.0, step=0.1)
water_volume = st.number_input("Water/Brine Volume in Contact with Gas (L)", min_value=0.0, value=1.0, step=0.1)
solubility_water = st.number_input("CO₂ Solubility in Water (g/L)", min_value=0.0, value=1.7, step=0.01)
solubility_brine = st.number_input("CO₂ Solubility in Brine (g/L)", min_value=0.0, value=1.3, step=0.01)

# Calculations
n_CO2_water = solubility_water / CO2_molar_mass
n_CO2_brine = solubility_brine / CO2_molar_mass

V_CO2_loss_water = n_CO2_water * R * T * water_volume
V_CO2_loss_brine = n_CO2_brine * R * T * water_volume

corrected_volume_water = measured_volume + V_CO2_loss_water
corrected_volume_brine = measured_volume + V_CO2_loss_brine

# Output
st.subheader("Results")
st.write(f"**CO₂ loss into Water:** {V_CO2_loss_water:.3f} L")
st.write(f"**Corrected Gas Volume (Water):** {corrected_volume_water:.3f} L")
st.write(f"**CO₂ loss into Brine:** {V_CO2_loss_brine:.3f} L")
st.write(f"**Corrected Gas Volume (Brine):** {corrected_volume_brine:.3f} L")

if isclose(V_CO2_loss_water, 0.0, abs_tol=0.001):
    st.success("Negligible CO₂ loss detected under given conditions.")
else:
    st.info("Consider using brine or applying correction for more accurate methane yield estimates.")

st.caption("Developed by [Your Name] | For small-scale anaerobic digestion experiments")