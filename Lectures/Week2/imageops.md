# Vision - Image operations

## Pixel Based Operations 
Voor elke pixel in het originele beeld bepaal je de waarde voor dezelfde pixel in het nieuwe beeld. Dus alleen op
basis van de oude waarde van die specifieke pixel. 

De oude pixelwaarde is 'x' en de nieuwe pixelwaarde is 'y'.

## Functies
- Identiteitsfunctie: x == y 
- Inverse: y = (max_intensiteit - x)
- Drempelfunctie: van grijswaarde naar zwart-wit(alles onder drempel is wit, alles boven drempel is zwart)
- Gamma Correctie: De constract en felheid anapassen van een afbeelding zodat mensen het beter kunnen waarnemen(mensen nemen intensiteit niet lineair waar.) Gebruik niet voor computer vision. Er gaat informatie verloren.
- Constract Stretching: Uitrekken van het histogram over het hele bereik van het histogram, zodat er meer contrast is. 

## Histogram Equalization 
Voor het vergelijken van afbeeldingen op basis van een specifieke eigenschap, bijvoorbeeld textuur.
Dit is handig voor afbeeldingen die nder nadelige omstandigheden zijn gemaakt. 
Normaliseren van het histogram tot een 'standaard' histogram.

Bij histogram equalization is de afstand tussen pieken niet gelijk(in tegenstelling tot constract stretching)
Histogtam equalization kan het beeld ook verslechten als je de hele image neemt, maar je slechts 1 object wil
weten. 

## Kleuren Histogrammen
Bij kleuren histogrammen hebben we een histogram voor elk kanaal. Pas op bij het aanpassen van het Hue kanaal, want hier gaat kleur dus verloren en krijg je andere kleuren dan normaal.

