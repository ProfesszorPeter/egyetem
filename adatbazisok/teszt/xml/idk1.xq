for $y in dataroot/Etlap
where $y/kcal =
min(
  for $x in dataroot/Etlap
  where $x/kategoria = "Szárnyas ételek"
  return $x/kcal
) and $y/kategoria = "Szárnyas ételek"
return $y/megnevezes