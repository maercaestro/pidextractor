# MEGAT P&ID Extractor (v0.001)
MEGAT P&ID Extractor Streamlit App

## Background
P & ID or Process and Instrumentation Diagram is one of the most important drawings for Chemical Engineer/ Process Engineers. P&ID is a non-proportional and not-drawn-to-scale schematic illustration that shows process flow of a piping system, connected with instrumentations and system equipments. This diagram is like a master document for everything we are going to build in piping system. The diagram is used for multiple purposes. Such as mass balance calculation/ hydraulic calculation / risk assessment / hazard and operability analysis and for general troubleshooting. Currently, the reading of the drawing are done manually. I'm looking for ways to automated this reading and making things easier for me as a process engineer.

## Version 0.01 (Line Number Extractor)
This is the hardest part, so I'm doing this part first. There isn't a standard way on how to properly put a line number. So I'm googling to find the most common ways for people to write the line number. This is what found:

So i'm using this to find the most common pattern line number. Inputting that into regular expression and yes, we can extract the line number. But if other patterns exist, you may contact me, so I may adjust my code.
https://www.google.com/url?sa=i&url=https%3A%2F%2Fforumautomation.com%2Ft%2Fidentification-of-pipe-line-number-in-p-id%2F10658&psig=AOvVaw2qybvftmR_-NludjYDLEFy&ust=1694387841548000&source=images&cd=vfe&opi=89978449&ved=0CBAQjRxqFwoTCLjroZLVnoEDFQAAAAAdAAAAABAI![image](https://github.com/maercaestro/pidextractor/assets/129637227/c4b6d771-30cb-4ddb-9c81-ee0d111f2cb0)


## Future Plans
There are few other plans that I have for this. All are listed below:
1. Extracting all process type information
2. Extracting all equipment information
3. Highlighting potential hazard/risk so it can help during HAZOP / Risk Assessment

