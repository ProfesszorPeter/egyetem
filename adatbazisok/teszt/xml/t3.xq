count(
  for $x in Tanciskola/Tancpar
where contains($x/LanyNev, "óra")
return $x
)