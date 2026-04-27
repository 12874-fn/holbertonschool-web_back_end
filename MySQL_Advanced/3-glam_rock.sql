-- Lists Glam rock bands ranked by longevity up to 2024
SELECT band_name, (2024 - formed) AS lifespan
FROM metal_bands
WHERE style = 'Glam rock'
ORDER BY lifespan DESC;


