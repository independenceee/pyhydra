from __future__ import annotations

from dataclasses import dataclass
from typing import List


@dataclass
class HydraParty:
    """
    Represents a single participant (party) in a Hydra Head.
    Contains only the verification key of the participant.
    """
    vkey: str

@dataclass
class HydraHeadParameters:
    """
    Parameters required to initialize a Hydra Head (used in the Init message).
    This structure is sent/received when opening a new Hydra Head on Cardano.
    """
    contestationPeriod: int
    parties: List[HydraParty]   