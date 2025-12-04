let $szarnyas := dataroot/Etlap[kategoria="Szárnyas ételek"]
let $minKcal := min($szarnyas/kcal)
return $szarnyas[kcal = $minKcal]/megnevezes