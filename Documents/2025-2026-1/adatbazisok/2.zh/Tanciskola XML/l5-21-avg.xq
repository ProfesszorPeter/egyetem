(:Írassuk ki, azon férfi táncosok neveit, akik a féri átlagmagasság felett vannak!:)
for $y in /Tanciskola/Tancpar
where $y/FerfiMagassag > avg(
  for $x in /Tanciskola/Tancpar
  return $x/FerfiMagassag)
return $y/FerfiNev