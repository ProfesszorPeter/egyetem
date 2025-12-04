(:Irassuk ki a lányok, fiúk neveit a magasságukkal együtt. A magasságadatokhoz illesszük hozzá a cm-t (pl: 185 cm). A lista a fiúk szerinti magasságadatok alapján csökkenően legyen rendezve:)

for $x in Tanciskola/Tancpar
where $x/LanyMagassag > 165
order by $x/LanyNev
return ($x/LanyNev,$x/FerfiNev)