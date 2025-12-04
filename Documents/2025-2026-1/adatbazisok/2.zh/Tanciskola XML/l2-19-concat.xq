(:Irassuk ki a lányok, fiúk neveit a magasságukkal együtt. A magasságadatokhoz illesszük hozzá a cm-t (pl: 185 cm). A lista a fiúk szerinti magasságadatok alapján csökkenően legyen rendezve:)
for $x in Tanciskola/Tancpar
order by $x/FerfiMagassag
return concat($x/LanyNev|| ' ', $x/LanyMagassag||  'cm, ', $x/FerfiNev|| ' ' ,$x/FerfiMagassag|| 'cm')