# Vision - Vision Systemen 

## Algemene Structuur 
1. Beeldacquisitie(opnemen beeld etc) 
2. Pre-processing(converteren image, ruisverminderen, etc) 
3. Segmentatie(Edge detection, tresholding, feature extraction)
4. High-level processing(Clustering, Classificatie, OCR)
5. Beslissing Nemen 

### Deep Learning
Deep neural networks kunnen een deel van de pre-processing en de volledige segmentatie en high-level processing automatisch leren doen.

## Herkenning 
Herkenning omvat: 
- Het herkennen van (klassen van) objecten, zoals mensen, voertuigen en omgeving. 
- Identificatie van individuele instanties(vingerafdruk, irisscan)
- Detectie (inbraakdetectie, tumor in weefsel etc)

## Bewegeningsanalyse 
- Bepaal plaats- en bewegingsparameters van de camera of een gefilmd object 
- Pose estimation(Bepaal de positie en orientatie van een object tov de camera(fabricage))
- Optical Flow(in de omgeving, van de camera en in de omgeving)

## Scene Reconstruction 
- Bereken een 3d model van de omgeving op basis van meerdere beelden 
- Nodig voor autonome voertuigen(SLAM: Simulatneos Localization & Mapping)
- Vaak: edge detection -> 3D Object 

