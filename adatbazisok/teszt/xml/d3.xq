for $x in filmek/film
where $x/ev >= 1950 and $x/ev <= 1960 and $x/jelol > 4
order by $x/cim ascending
return $x/cim