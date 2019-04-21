import aminoacids
# aminoacids.all_aa         = Alle Aminosäuren
# aminoacids.neutral     = Aminosäuren mit ungeladener Seitenkette
# aminoacids.positive    = Aminosäuren mit positiv geladener Seitenkette
# aminoacids.negative    = Aminosäuren mit negativ geladener Seitenkette
# aminoacids.polar       = Aminosäuren mit polaren Seitenketten
# aminoacids.nonpolar    = Aminosäuren mit unpolaren Seitenketten
# aminoacids.hydrophobic = Hydrophobe Aminosäuren
# aminoacids.hydrophilic = Hydrophile Aminosäuren

# Show all aminoacids
print(aminoacids.all_aa)

print('\nWelche Aminosäuren haben positiv oder negativ geladene Seitenketten?')
print(aminoacids.positive | aminoacids.negative)

print('\nWelche Aminosäuren haben ungeladene Seitenketten und sind hydrophob?')
print(aminoacids.neutral & aminoacids.hydrophobic)

print('\nHat die Aminosäure Serin eine polare Seitenkette?')
print('Serin' in aminoacids.polar)

print('\nWelche Aminosäuren haben keine positiv geladene Seitenkette?')
print(aminoacids.all_aa - aminoacids.positive)

print('\nSind alle Aminosäuren mit positiv geladener Seitenkette hydrophil?')
print(aminoacids.hydrophilic >= aminoacids.positive)
