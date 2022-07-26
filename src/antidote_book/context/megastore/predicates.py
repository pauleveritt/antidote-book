"""Custom Antidote predicates."""
from antidote import QualifiedBy


class NotQualified:
    """Allow matching on implementations with no `.when`."""

    @staticmethod
    def evaluate(predicate: QualifiedBy | None) -> bool:
        """The protocol for predicate evaluation."""
        return predicate is None
