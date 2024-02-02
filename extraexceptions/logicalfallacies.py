class LogicBase(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f'"{self.__class__.__name__}" in "{self.message}" has been found'
        else:
            return f'Except {self.__class__.__name__} has been raised'


class AdHominem(LogicBase):
    def __init__(self, *args):
        super().__init__(*args)


class AppealToAuthority(LogicBase):
    def __init__(self, *args):
        super().__init__(*args)


class AppealToNature(LogicBase):
    def __init__(self, *args):
        super().__init__(*args)


class AppealToEmotion(LogicBase):
    def __init__(self, *args):
        super().__init__(*args)


class AppealToTradition(LogicBase):
    def __init__(self, *args):
        super().__init__(*args)


class AppealToIgnorance(LogicBase):
    def __init__(self, *args):
        super().__init__(*args)


class AppealToStone(LogicBase):
    def __init__(self, *args):
        super().__init__(*args)


class AppealToAccomplishment(LogicBase):
    def __init__(self, *args):
        super().__init__(*args)


class AppealToConsequences(LogicBase):
    def __init__(self, *args):
        super().__init__(*args)


class AppealToNovelty(LogicBase):
    def __init__(self, *args):
        super().__init__(*args)


class AffirmingTheConsequent(LogicBase):
    def __init__(self, *args):
        super().__init__(*args)


class AnecdotalFallacy(LogicBase):
    def __init__(self, *args):
        super().__init__(*args)


class AmbiguityFallacy(LogicBase):
    def __init__(self, *args):
        super().__init__(*args)


class AffirmingADisjunction(LogicBase):
    def __init__(self, *args):
        super().__init__(*args)


class AssociationFallacy(LogicBase):
    def __init__(self, *args):
        super().__init__(*args)


class BurdenOfProof(LogicBase):
    def __init__(self, *args):
        super().__init__(*args)


class Bulverism(LogicBase):
    def __init__(self, *args):
        super().__init__(*args)


class CircularReasoning(LogicBase):
    def __init__(self, *args):
        super().__init__(*args)


class CompositionFallacy(LogicBase):
    def __init__(self, *args):
        super().__init__(*args)


class ContinuumFallacy(LogicBase):
    def __init__(self, *args):
        super().__init__(*args)


class CherryPicking(LogicBase):
    def __init__(self, *args):
        super().__init__(*args)


class CourtiersReply(LogicBase):
    def __init__(self, *args):
        super().__init__(*args)


class ChronologicalSnobbery(LogicBase):
    def __init__(self, *args):
        super().__init__(*args)


class CircumnstantialAdHominem(LogicBase):
    def __init__(self, *args):
        super().__init__(*args)


class DivisionFallacy(LogicBase):
    def __init__(self, *args):
        super().__init__(*args)


class DenyingTheAntecedent(LogicBase):
    def __init__(self, *args):
        super().__init__(*args)


class DefinistFallacy(LogicBase):
    def __init__(self, *args):
        super().__init__(*args)


class EquivocationFallacy(LogicBase):
    def __init__(self, *args):
        super().__init__(*args)


class EcologicalFallacy(LogicBase):
    def __init__(self, *args):
        super().__init__(*args)


class EtymologicalFallacy(LogicBase):
    def __init__(self, *args):
        super().__init__(*args)


class FalseDilemmaFallacy(LogicBase):
    def __init__(self, *args):
        super().__init__(*args)


class FaultyAnalogy(LogicBase):
    def __init__(self, *args):
        super().__init__(*args)


class FalseCause(LogicBase):
    def __init__(self, *args):
        super().__init__(*args)


class FalseEquivalence(LogicBase):
    def __init__(self, *args):
        super().__init__(*args)


class FallacyOfSingleCause(LogicBase):
    def __init__(self, *args):
        super().__init__(*args)


class GeneticFallacy(LogicBase):
    def __init__(self, *args):
        super().__init__(*args)


class HastyGeneralization(LogicBase):
    def __init__(self, *args):
        super().__init__(*args)


class RedHerring(LogicBase):
    def __init__(self, *args):
        super().__init__(*args)


class TuQuoQue(LogicBase):
    def __init__(self, *args):
        super().__init__(*args)


class SlipperySlope(LogicBase):
    def __init__(self, *args):
        super().__init__(*args)


class SpecialPleading(LogicBase):
    def __init__(self, *args):
        super().__init__(*args)


class LoadedQuestion(LogicBase):
    def __init__(self, *args):
        super().__init__(*args)


class StrawmanFallacy(LogicBase):
    def __init__(self, *args):
        super().__init__(*args)


class NoTrueScotsman(LogicBase):
    def __init__(self, *args):
        super().__init__(*args)


class TexasSharpshooter(LogicBase):
    def __init__(self, *args):
        super().__init__(*args)


class SuppressedCorrelative(LogicBase):
    def __init__(self, *args):
        super().__init__(*args)


class PersonalIncredulity(LogicBase):
    def __init__(self, *args):
        super().__init__(*args)


class MiddleGroundFallacy(LogicBase):
    def __init__(self, *args):
        super().__init__(*args)


class SunkCostFallacy(LogicBase):
    def __init__(self, *args):
        super().__init__(*args)


class QuotingOutOfContext(LogicBase):
    def __init__(self, *args):
        super().__init__(*args)


class HistoriansFallacy(LogicBase):
    def __init__(self, *args):
        super().__init__(*args)


class InflationOfConflict(LogicBase):
    def __init__(self, *args):
        super().__init__(*args)


class IncompleteComparison(LogicBase):
    def __init__(self, *args):
        super().__init__(*args)


class LudicFallacy(LogicBase):
    def __init__(self, *args):
        super().__init__(*args)


class MoralisticFallacy(LogicBase):
    def __init__(self, *args):
        super().__init__(*args)


class NirvanaFallacy(LogicBase):
    def __init__(self, *args):
        super().__init__(*args)


class ProofByAssertion(LogicBase):
    def __init__(self, *args):
        super().__init__(*args)


class PsychologistsFallacy(LogicBase):
    def __init__(self, *args):
        super().__init__(*args)


class ReificationFallacy(LogicBase):
    def __init__(self, *args):
        super().__init__(*args)


class RetrospectiveDeterminism(LogicBase):
    def __init__(self, *args):
        super().__init__(*args)


class ThoughtTerminatingCliche(LogicBase):
    def __init__(self, *args):
        super().__init__(*args)


class MissingPointFallacy(LogicBase):
    def __init__(self, *args):
        super().__init__(*args)


class TonePolicing(LogicBase):
    def __init__(self, *args):
        super().__init__(*args)


class ImEntitledToMyOpinion(LogicBase):
    def __init__(self, *args):
        super().__init__(*args)


class TwoWrongsMakeARight(LogicBase):
    def __init__(self, *args):
        super().__init__(*args)


class VacuousTruth(LogicBase):
    def __init__(self, *args):
        super().__init__(*args)
