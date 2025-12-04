(:Írassuk ki, hogy hány olyan lány van, akinek a nevében szerepel az „óra”!:)
count(
  for $x in Tanciskola/Tancpar
  where contains($x/LanyNev, 'óra')
  return $x
)