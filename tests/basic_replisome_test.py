# -*- coding: utf-8 -*-
"""Simple tests for replisome.py."""

from dataclasses import dataclass
from typing import List

from amplifyp.dna import DNA, DNAType
from amplifyp.replisome import Replisome


@dataclass(frozen=True, slots=True)
class ReplisomeExample:
    """A class representing test cases of replisome.

    Attributes:
        target (DNA): The target DNA sequence.
        primer (DNA): The primer DNA sequence.
    """

    target: DNA
    primer: DNA
    origin_index: int


replisome_examples: List[ReplisomeExample] = []
replisome_examples.append(
    ReplisomeExample(
        target=DNA("GTGTACTCAGTTCCATAAACGAGCTATTAGATATGAGGTCCGTAGATTGAAAAGGGTGA"),
        primer=DNA("TTCCATA", DNAType.PRIMER),
        origin_index=10,
    )
)

replisome_examples.append(
    ReplisomeExample(
        target=DNA("ATTGTGCGATCCCTGCACCTCAGCTAAGGTAGCTACCAATATTTAGTTTCTAAGCCTTGC"),
        primer=DNA("GCGATC", DNAType.PRIMER),
        origin_index=5,
    )
)


def test_origin_equality() -> None:
    """Test replication origin generation by replisome."""
    for ex in replisome_examples:
        replisome = Replisome(ex.target, ex.primer)
        origin = replisome.origin(ex.origin_index)

        # Make sure that the primer is correct
        assert origin.primer == ex.primer.upper().reverse().sequence

        # Make sure for the example replication index, the replication origin in
        # question is the same as the primer
        target_slice = slice(ex.origin_index, ex.origin_index + len(ex.primer))
        assert origin.target == ex.target.upper().reverse().sequence[target_slice]

        # Make sure that the target in the generated replication origin is the
        # same as if we slicce the target sequence of the replisome manually.
        for i in replisome.range:
            exp_str = ex.target.upper().reverse().sequence[i : i + len(origin.primer)]
            assert replisome.origin(i).target == exp_str
