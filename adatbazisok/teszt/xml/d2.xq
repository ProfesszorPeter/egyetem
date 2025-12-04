for $x in filmek/film
where $x/ev > 1950 and $x/dij >= 3
order by $x/jelol, $x/dij descending
return $x/cim || " " || $x/dij || " " || $x/jelol