# VAJA: Programski dostop do GenBank (Python)

Spodaj je primer kode (rešitev naloge), kjer enostavno preštejemo G+C ter izračunamo njihov delež v CDS ter v regijah, ki niso CDS. Dodani so koraki, ki izpišejo, kaj se trenutno dogaja. Koda vsebuje tudi relevantne komentarje.

V primeru je analizirano genomsko zaporedje s kodo zapisa [CP020452](https://www.ncbi.nlm.nih.gov/nuccore/CP020452.2). Gre za genom bakterije [*Neisseria mucosa*](https://en.wikipedia.org/wiki/Neisseria_mucosa) velikosti 2783943 bp.

# uvozimo potrebne module
from Bio import Entrez
from Bio import SeqIO
from Bio.Seq import Seq

# identificiramo se
Entrez.email = 'vas.e-postni@naslov.si'

# definiramo zapis, ki ga bomo uporabili za analizo
acode = 'CP020452'

# prenesemo zapis
print('Prenašam zaporedje ...')
handle = Entrez.efetch(db='nucleotide', rettype='gb', retmode='text', id=acode)
rec = SeqIO.read(handle, 'gb')

# definiramo spremenljivke
num_gc_cds = 0   # število G+C v CDS
num_cds = 0      # število CDS
len_cds = 0      # vsota dolžin vseh CDS
len_all = len(rec.seq)    # dolžina zaporedja

# izpišemo dolžino celotnega zaporedja
print('Dolžina zaporedja: %i bp' % len_all)

# preštejemo vse G in C v celotnem zaporedju
print('Štejem G+C v celotnem zaporedju ...')
num_gc_all = rec.seq.count('C') + rec.seq.count('G')

# preštejemo, koliko CDS je v zaporedju, ter izpišemo število
print('Preštevam CDS ...')
for feature in rec.features:
   if feature.type == 'CDS':
      num_cds += 1
print('Število CDS: %i' % num_cds)

# preštejemo vse G in C v vseh CDS
print('Štejem G+C v CDS ...')
for feature in rec.features:
   if feature.type == 'CDS':
      num_gc_cds += feature.location.extract(rec).seq.count('C') + feature.location.extract(rec).seq.count('G')
      len_cds += len(feature.location.extract(rec).seq)

# izvedemo izračune
print('Še zadnji izračuni ...')
num_gc_nocds = num_gc_all - num_gc_cds
len_nocds = len_all - len_cds
gc_ratio_cds = (num_gc_cds / len_cds) * 100
gc_ratio_nocds = (num_gc_nocds / len_nocds) * 100

# izpišemo rezultate
print('=======')
print('Delež GC v CDS [odstotki]: %0.2f' % gc_ratio_cds)
print('Delež GC izven CDS [odstotki]: %0.2f' % gc_ratio_nocds)