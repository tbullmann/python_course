# all amino acids
all_aa = { "Alanine", "Arginine", "Asparagine", "Aspartic acid", "Cysteine", "Glutamic acid",
"Glutamine", "Glycine", "Histidine", "Isoleucine", "Leucine", "Lysine",
"Methionine", "Phenylalanine", "Proline", "Serine", "Threonine", "Tryptophan", 
"Tyrosine", "Valine" }

#side-chain charge
neutral = {"Alanine", "Asparagine", "Cysteine", "Glutamine", "Glycine", "Histidine", 
"Isoleucine", "Leucine", "Methionine", "Phenylalanine", "Proline", "Serine", "Threonine", "Tryptophan", 
"Tyrosine", "Valine" }
positive = { "Arginine", "Lysine" }
negative = { "Aspartic acid", "Glutamic acid" }

# side-chain polarity
polar = { "Arginine", "Asparagine", "Aspartic acid", "Glutamic acid",
"Glutamine", "Histidine", "Lysine", "Serine", "Threonine", "Tyrosine" }
nonpolar = { "Alanine",  "Cysteine", "Glycine", "Isoleucine", "Leucine", "Methionine", "Phenylalanine", 
"Proline", "Tryptophan", "Valine" }

# hydrophobicity
hydrophobic = { "Alanine", "Isoleucine", "Leucine", "Methionine", "Phenylalanine", "Proline", 
"Tryptophan", "Valine" }
hydrophilic = { "Arginine", "Asparagine", "Aspartic acid", "Cysteine", "Glutamic acid",
"Glutamine", "Glycine", "Histidine", "Lysine", "Serine", "Threonine", "Tyrosine" }
