# -*- coding: utf-8 -*-
"""Amplify P core logics - Replisome and DNA."""
from typing import Final, FrozenSet


class DNA:
    """Contains a DNA sequence."""

    def __init__(self, sequence: str) -> None:
        """Construct a DNA sequence."""
        # Check if the sequence contains invalid characters.
        # Note that we allow lower case characters.
        test_set: Final[FrozenSet[str]] = frozenset(sequence.upper())
        valid_char_set: Final[FrozenSet[str]] = frozenset(
            "ACGTU"
            + "RYKMSW"  # Single bases
            + "BDGV"  # Double bases
            + "N"  # Triple bases  # Wildcard
        )
        if not test_set <= valid_char_set:
            raise ValueError("DNA sequence contains invalid characters.")

        self._sequence = sequence

    def __str__(self) -> str:
        """Return the string representation of a DNA sequence."""
        return self.sequence

    @property
    def sequence(self) -> str:
        """Return the DNA sequence."""
        return self._sequence

    @property
    def reverse(self) -> str:
        """Return the reverse complement of the DNA sequence."""
        return self._sequence[::-1]

    @property
    def lower(self) -> str:
        """Return the DNA sequence in lower case."""
        return self._sequence.lower()

    @property
    def upper(self) -> str:
        """Return the DNA sequence in upper case."""
        return self._sequence.upper()

    @property
    def complement(self) -> str:
        """Return the complement of the DNA sequence.

        Note that the complement of non-ACGT bases are undefined.
        """
        return self._sequence.translate(str.maketrans("ACGTacgt", "TGCAtgca"))
