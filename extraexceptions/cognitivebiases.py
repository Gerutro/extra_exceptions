class CognitiveBase(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f'Cognitive Bias "{self.__class__.__name__}" in "{self.message}" has been found'
        else:
            return f'Cognitive bias has been raised'


"""
Anchoring bias
"""


class CommonSourceBias(CognitiveBase):
    def __init__(self, *args):
        super().__init__(*args)


class ConservatismBias(CognitiveBase):
    def __init__(self, *args):
        super().__init__(*args)


class FunctionalFixedness(CognitiveBase):
    def __init__(self, *args):
        super().__init__(*args)


class LawOfInstrument(CognitiveBase):
    def __init__(self, *args):
        super().__init__(*args)


"""
Apophenia
"""


class ClusteringIllusion(CognitiveBase):
    def __init__(self, *args):
        super().__init__(*args)


class IllusoryCorrelation(CognitiveBase):
    def __init__(self, *args):
        super().__init__(*args)


class Pareidolia(CognitiveBase):
    def __init__(self, *args):
        super().__init__(*args)


"""
Availability heuristic
"""


class AnthropocentricThinking(CognitiveBase):
    def __init__(self, *args):
        super().__init__(*args)


class Anthropomorphism(CognitiveBase):
    def __init__(self, *args):
        super().__init__(*args)


class AttentionalBias(CognitiveBase):
    def __init__(self, *args):
        super().__init__(*args)


class FrequencyIllusion(CognitiveBase):
    def __init__(self, *args):
        super().__init__(*args)


class ImplicitAssociation(CognitiveBase):
    def __init__(self, *args):
        super().__init__(*args)


class SalienceBias(CognitiveBase):
    def __init__(self, *args):
        super().__init__(*args)


class SelectionBias(CognitiveBase):
    def __init__(self, *args):
        super().__init__(*args)


class SurvivorshipBias(CognitiveBase):
    def __init__(self, *args):
        super().__init__(*args)


class WellTravelledRoadEffect(CognitiveBase):
    def __init__(self, *args):
        super().__init__(*args)


"""
Cognitive dissonance
"""


class NormalcyBias(CognitiveBase):
    def __init__(self, *args):
        super().__init__(*args)


class EffortJustification(CognitiveBase):
    def __init__(self, *args):
        super().__init__(*args)


class BenFranklinEffect(CognitiveBase):
    def __init__(self, *args):
        super().__init__(*args)


"""
Confirmation bias
"""


class BackfireEffect(CognitiveBase):
    def __init__(self, *args):
        super().__init__(*args)


class CongruenceBias(CognitiveBase):
    def __init__(self, *args):
        super().__init__(*args)


class ExpectationBias(CognitiveBase):
    def __init__(self, *args):
        super().__init__(*args)


class ObserverExpectancyEffect(CognitiveBase):
    def __init__(self, *args):
        super().__init__(*args)


class SelectivePerception(CognitiveBase):
    def __init__(self, *args):
        super().__init__(*args)


class SemmelweisReflex(CognitiveBase):
    def __init__(self, *args):
        super().__init__(*args)


"""
Egocentric bias
"""


class BiasBlindSpot(CognitiveBase):
    def __init__(self, *args):
        super().__init__(*args)


class FalseConsensusEffect(CognitiveBase):
    def __init__(self, *args):
        super().__init__(*args)


class FalseUniquenessBias(CognitiveBase):
    def __init__(self, *args):
        super().__init__(*args)


class ForerEffect(CognitiveBase):
    def __init__(self, *args):
        super().__init__(*args)


class IllusionOfAsymmetricInsight(CognitiveBase):
    def __init__(self, *args):
        super().__init__(*args)


class IllusionOfControl(CognitiveBase):
    def __init__(self, *args):
        super().__init__(*args)


class IllusionOfTransparency(CognitiveBase):
    def __init__(self, *args):
        super().__init__(*args)


class IllusionOfValidity(CognitiveBase):
    def __init__(self, *args):
        super().__init__(*args)


class IllusorySuperiority(CognitiveBase):
    def __init__(self, *args):
        super().__init__(*args)


class NaiveCynicism(CognitiveBase):
    def __init__(self, *args):
        super().__init__(*args)


class NaiveRealism(CognitiveBase):
    def __init__(self, *args):
        super().__init__(*args)


class OverconfidenceEffect(CognitiveBase):
    def __init__(self, *args):
        super().__init__(*args)


class PlanningFallacy(CognitiveBase):
    def __init__(self, *args):
        super().__init__(*args)


class RestraintBias(CognitiveBase):
    def __init__(self, *args):
        super().__init__(*args)


class TraitAscriptionBias(CognitiveBase):
    def __init__(self, *args):
        super().__init__(*args)


class ThirdPersonEffect(CognitiveBase):
    def __init__(self, *args):
        super().__init__(*args)


"""
Extension neglect
"""


class BaseRateFallacy(CognitiveBase):
    def __init__(self, *args):
        super().__init__(*args)


class CompassionFade(CognitiveBase):
    def __init__(self, *args):
        super().__init__(*args)


class ConjunctionFallacy(CognitiveBase):
    def __init__(self, *args):
        super().__init__(*args)


class DurationNeglect(CognitiveBase):
    def __init__(self, *args):
        super().__init__(*args)


class HyperbolicDiscounting(CognitiveBase):
    def __init__(self, *args):
        super().__init__(*args)


class InsensitivityToSampleSize(CognitiveBase):
    def __init__(self, *args):
        super().__init__(*args)


class LessIsBetterEffect(CognitiveBase):
    def __init__(self, *args):
        super().__init__(*args)


class NeglectOfProbability(CognitiveBase):
    def __init__(self, *args):
        super().__init__(*args)


class ScopeNeglect(CognitiveBase):
    def __init__(self, *args):
        super().__init__(*args)


class ZeroRiskBias(CognitiveBase):
    def __init__(self, *args):
        super().__init__(*args)


"""
False priors
"""


class AgentDetectionBias(CognitiveBase):
    def __init__(self, *args):
        super().__init__(*args)


class AutomationBias(CognitiveBase):
    def __init__(self, *args):
        super().__init__(*args)


class GenderBias(CognitiveBase):
    def __init__(self, *args):
        super().__init__(*args)


class SexualOverperceptionBias(CognitiveBase):
    def __init__(self, *args):
        super().__init__(*args)


class Stereotyping(CognitiveBase):
    def __init__(self, *args):
        super().__init__(*args)


