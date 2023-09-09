# MEGAT P&ID Extractor (v0.001)
MEGAT P&ID Extractor Streamlit App

## Background
P & ID or Process and Instrumentation Diagram is one of the most important drawings for Chemical Engineer/ Process Engineers. P&ID is a non-proportional and not-drawn-to-scale schematic illustration that shows process flow of a piping system, connected with instrumentations and system equipments. This diagram is like a master document for everything we are going to build in piping system. The diagram is used for multiple purposes. Such as mass balance calculation/ hydraulic calculation / risk assessment / hazard and operability analysis and for general troubleshooting. Currently, the reading of the drawing are done manually. I'm looking for ways to automated this reading and making things easier for me as a process engineer.

## Version 0.01 (Line Number Extractor)
This is the hardest part, so I'm doing this part first. There isn't a standard way on how to properly put a line number. So I'm googling to find the most common ways for people to write the line number. This is what found:

So i'm using this to find the most common pattern line number. Inputting that into regular expression and yes, we can extract the line number. But if other patterns exist, you may contact me, so I may adjust my code.
![c8a58de8a891ca4b5efa522e1b6eaaee007aba4b](https://github.com/maercaestro/pidextractor/assets/129637227/f110e9b2-ef2d-4285-ba5e-7e9c8a14ac2e)
![hqdefault](https://github.com/maercaestro/pidextractor/assets/129637227/7bd9c972-2cb7-4de5-9205-1cb1c6b26b75)



## Future Plans
There are few other plans that I have for this. All are listed below:
1. Extracting all process type information
2. Extracting all equipment information
3. Highlighting potential hazard/risk so it can help during HAZOP / Risk Assessment

