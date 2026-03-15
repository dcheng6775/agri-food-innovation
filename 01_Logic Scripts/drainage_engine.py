# --- Observe (Inputs) ------------------------------------------------------
# Mock inputs for the data sources mentioned in the project notes.

# Satellite Data
ndvi = 0.35  # Normalized Difference Vegetation Index (0-1), lower values indicate stress
surface_temperature_c = 32.4  # Surface temperature in Celsius

# Drone Data
thermal_anomaly_score = 0.8  # 0-1 score where higher indicates a thermal anomaly
rgb_image_quality = "good"  # placeholder string to show that we have imagery available

# Environmental
recent_rainfall_mm = 28.0  # mm of rain in the last 24 hours (post-precip monitoring)
soil_moisture_pct = 42.0  # volumetric water content (%)

# Location / context for actions (mocked)
field_latlon = (42.12345, -93.12345)

# --- Detect & Infer (Rule-based logic) -------------------------------

flags = []

# Rule 1 (The Blowout): thermal anomaly + heavy rain => potential tile blowout.
if thermal_anomaly_score > 0.7 and recent_rainfall_mm >= 20:
    flags.append("Potential Tile Blowout")

# Rule 2 (Crop Stress): low NDVI despite high soil moisture => poor aeration / waterlogging.
if ndvi < 0.4 and soil_moisture_pct > 35:
    flags.append("Poor Aeration/Waterlogging")

# Additional inference rules can be added here as the system grows.

# --- Act (Actionable Output) -------------------------------------------

print("=== Actionable Insights ===")

if "Potential Tile Blowout" in flags:
    lat, lon = field_latlon
    print(f"Inspect Tile Outlet at [{lat:.5f}, {lon:.5f}] (Potential Tile Blowout detected)")

if "Poor Aeration/Waterlogging" in flags:
    print("Spray 2L of fertilizer in Row 2, Column 3 (Crop stress + high moisture indicates waterlogging)")

if not flags:
    print("No immediate drainage-related actions detected. Continue monitoring.")
