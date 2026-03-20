-- Used to perform data analysis for Tableau
IF [NDVI_Score] < 0.2 AND [Rain_Last_24h] > 40 THEN "Predicted Drain Damage"
ELSEIF [Rain_Last_24h] > 35 THEN "Waterlogged"
ELSEIF [Surface_Temp] > 31 AND [NDVI_Score] < 0.4 THEN "Crop Stress"
ELSEIF [Rain_Last_24h] > 20 THEN "Potential Drain Risk"
ELSE "Nominal"
END