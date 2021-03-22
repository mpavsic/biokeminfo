# DEMO: Izračun lastne matrike in njena uporaba

V spodnjem primeru je prikazan izračun lastne matrike (enako, kot pri prejšnji vaji - [VAJA: Izračun matrike zamenjav (Python)](matrika_zamenjav.ipynb)) ter uporaba tako izračunane matrike za poravnavo dveh zaporedij.

## Izračun matrike

from Bio import SeqIO
sequence1 = SeqIO.read('vhod/matrika_zamenjav-myoglobin_horse.fasta', 'fasta')
sequence2 = SeqIO.read('vhod/matrika_zamenjav-myoglobin_rat.fasta', 'fasta')
# v mapi vhod sta tudi zaporedji mišjega in človeškega nebulina, ki sta bistveno daljši
from Bio.Align import PairwiseAligner
aligner = PairwiseAligner()
aligner.mode = 'local'
aligner.match_score = 2
aligner.mismatch_score = -3
aligner.open_gap_score = -7
aligner.extend_gap_score = -2
alignments = aligner.align(sequence1.seq, sequence2.seq)
alignment = alignments[0]
from Bio.Align.substitution_matrices import Array
frequency = Array('ACGT', dims=2)
for (start1, end1), (start2, end2) in zip(*alignment.aligned):
    seq1 = sequence1[start1:end1]
    seq2 = sequence2[start2:end2]
    for c1, c2 in zip(seq1, seq2):
        frequency[c1, c2] += 1
import numpy
probabilities = frequency / numpy.sum(frequency)
probabilities = (probabilities + probabilities.transpose()) / 2.0
background = numpy.sum(probabilities, 0)
expected = numpy.dot(background[:,None], background[None, :])
oddsratios = probabilities / expected
scoring_matrix = numpy.log2(oddsratios)
print(scoring_matrix)

## Poravnava

Definirajmo zaporedji in ju poravnajmo, najprej brez uporabe matrike (vzamemo `1` za enakost in `0` za neenakost, ni posebnih kazni za vrzeli).

from Bio import pairwise2
from Bio.pairwise2 import format_alignment

seq1 = 'AGCTCGATAGACT'
seq2 = 'AGGAGGATTGACT'

alignments_global = pairwise2.align.globalxx(seq1, seq2)
print(format_alignment(*alignments_global[0]))

Zdaj pa uporabimo še zgoraj izračunano matriko, spet brez posebne kazni za vrzeli.

alignments_global = pairwise2.align.globaldx(seq1, seq2, scoring_matrix)
print(format_alignment(*alignments_global[0]))

Primerjajte poravnavi!