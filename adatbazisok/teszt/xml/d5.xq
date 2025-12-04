count(
    for $y in filmek/film
  where $y/cim != "La La Land"
  and $y/dij =  (
    for $x in filmek/film
  where $x/cim = "La La Land"
return $x/dij
  )
return $y
)
 
