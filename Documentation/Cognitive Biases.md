# Cognitive Biases

{% hint style="success" %}
Added in v.0.0.0.2
{% endhint %}

---

This module add a new 56 exceptions.

Example to use:
```python
import extraexceptions

raise extraexceptions.BenFranklinEffect
```

or you can replace import to `from extraexceptions import ...`:
```python
from extraexceptions import cognitivebiases as cb

raise cb.BenFranklinEffect
```

And in both cases console gave:
```commandline
Traceback (most recent call last):
  File "PATH", line 3, in <module>
    raise cb.BenFranklinEffect
extraexceptions.cognitivebiases.BenFranklinEffect: Cognitive bias "BenFranklinEffect" has been raised
```

---

With added custom text:
```python
import extraexceptions

raise extraexceptions.BenFranklinEffect("Some text")
```

```python
from extraexceptions import cognitivebiases as cb

raise cb.BenFranklinEffect("Some text")
```

```commandline
Traceback (most recent call last):
  File "PATH", line 3, in <module>
    raise cb.BenFranklinEffect("Some text")
extraexceptions.cognitivebiases.BenFranklinEffect: Cognitive Bias "BenFranklinEffect" in "Some text" has been found
```

---

<details>

<summary>Cognitive Biases Info</summary>

## **NameOfClass - Link To The Article**

CommonSourceBias - [Common Source Bias](https://en.wikipedia.org/wiki/Common_source_bias)

ConservatismBias - [Conservatism Bias](https://en.wikipedia.org/wiki/Conservatism_(belief_revision))

FunctionalFixedness - [Functional Fixedness](https://en.wikipedia.org/wiki/Functional_fixedness)

LawOfInstruments - [Law Of Instruments](https://en.wikipedia.org/wiki/Law_of_the_instrument)

ClusteringIllusion - [Clustering Illusion](https://en.wikipedia.org/wiki/Clustering_illusion)

IllusoryCorrelation - [Illusory Correlation](https://en.wikipedia.org/wiki/Illusory_correlation)

Pareidolia - [Pareidolia](https://en.wikipedia.org/wiki/Pareidolia)

AnthropocentricThinking - [Anthropocentric Thinking](https://en.wikipedia.org/wiki/Anthropocentrism)

Anthropomorphism - [Anthropomorphism](https://en.wikipedia.org/wiki/Anthropomorphism)

AttentionalBias - [Attentional Bias](https://en.wikipedia.org/wiki/Attentional_bias)

FrequencyIllusion - [Frequency Illusion](https://en.wikipedia.org/wiki/Frequency_illusion)

ImplicitAssociation - [Implicit Association](https://en.wikipedia.org/wiki/Implicit-association_test)

SalienceBias - [Salience Bias](https://en.wikipedia.org/wiki/Salience_(neuroscience))

SelectionBias - [Selection Bias](https://en.wikipedia.org/wiki/Selection_bias)

Survivorship Bias - [Survivorship Bias](https://en.wikipedia.org/wiki/Survivorship_bias)

WellTravelledRoadEffect - [Well Travelled Road Effect](https://en.wikipedia.org/wiki/Well_travelled_road_effect)

NormalcyBias - [Normalcy Bias](https://en.wikipedia.org/wiki/Normalcy_bias)

EffortJustification - [Effort Justification](https://en.wikipedia.org/wiki/Effort_justification)

BenFranklinEffect - [Ben Franklin Effect](https://en.wikipedia.org/wiki/Ben_Franklin_effect)

BackfireEffect - [Backfire Effect](https://en.wikipedia.org/wiki/Belief_perseverance)

CongruenceBias - [Congruence Bias](https://en.wikipedia.org/wiki/Congruence_bias)

ExpectationBias - [Expectation Bias](https://www.thebehavioralscientist.com/glossary/expectation-bias)

ObserverExpectancyEffect - [Observer Expectancy Effect](https://en.wikipedia.org/wiki/Observer-expectancy_effect)

SelectivePerception - [Selective Perception](https://en.wikipedia.org/wiki/Selective_perception)

SemmelweisReflex - [Semmelweis Reflex](https://en.wikipedia.org/wiki/Semmelweis_reflex)

BiasBlindSpot - [Bias Blind Spot](https://en.wikipedia.org/wiki/Bias_blind_spot)

FalseConsensusEffect - [False Consensus Effect](https://en.wikipedia.org/wiki/False_consensus_effect)

FalseUniquenessBias - [False Uniqueness Bias](https://en.wikipedia.org/wiki/False-uniqueness_effect)

ForerEffect - [Forer Effect](https://en.wikipedia.org/wiki/Barnum_effect)

IllusionOfAsymmetricInsight - [Illusion Of Asymmetric Insight](https://en.wikipedia.org/wiki/Illusion_of_asymmetric_insight)

IllusionOfControl - [Illusion Of Control](https://en.wikipedia.org/wiki/Illusion_of_control)

IllusionOfTransparency - [Illusion Of Transparency](https://en.wikipedia.org/wiki/Illusion_of_transparency)

IllusionOfValidity - [Illusion Of Validity](https://en.wikipedia.org/wiki/Illusion_of_validity)

IllusorySuperiority - [Illusory Superiority](https://en.wikipedia.org/wiki/Illusory_superiority)

NaiveCynicism - [Naive Cynicism](https://en.wikipedia.org/wiki/Na%C3%AFve_cynicism)

NaiveRealism - [Naive Realism](https://en.wikipedia.org/wiki/Na%C3%AFve_realism)

OverconfidenceEffect - [Overconfidence Effect](https://en.wikipedia.org/wiki/Overconfidence_effect)

PlanningFallacy - [Planning Fallacy](https://en.wikipedia.org/wiki/Planning_fallacy)

RestraintBias - [Restraint Bias](https://en.wikipedia.org/wiki/Restraint_bias)

TraitAscriptionBias - [Trait Ascription Bias](https://en.wikipedia.org/wiki/Trait_ascription_bias)

ThirdPersonEffect - [Third Person Effect](https://en.wikipedia.org/wiki/Third-person_effect)

BaseRateFallacy - [Base Rate Fallacy](https://en.wikipedia.org/wiki/Base_rate_fallacy)

CompassionFade - [Compassion Fade](https://en.wikipedia.org/wiki/Compassion_fade)

ConjunctionFallacy - [Conjunction Fallacy](https://en.wikipedia.org/wiki/Conjunction_fallacy)

DurationNeglect - [Duration Neglect](https://en.wikipedia.org/wiki/Duration_neglect)

HyperbolicDiscounting - [Hyperbolic Discounting](https://en.wikipedia.org/wiki/Hyperbolic_discounting)

InsensitivityToSampleSize - [Insensitivity To Sample Size](https://en.wikipedia.org/wiki/Insensitivity_to_sample_size)

LessIsBetterEffect - [Less Is Better Effect](https://en.wikipedia.org/wiki/Less-is-better_effect)

NeglectOfProbability  - [Neglect Of Probability](https://en.wikipedia.org/wiki/Neglect_of_probability)

ScopeNeglect - [Scope Neglect](https://en.wikipedia.org/wiki/Scope_neglect)

ZeroRiskBias - [Zero Risk Bias](https://en.wikipedia.org/wiki/Zero-risk_bias)

AgentDetectionBias - [Agent Detection Bias](https://religions.wiki/index.php/Agent_detection_bias)

GenderBias - [Gender Bias](https://en.wikipedia.org/wiki/Gender_bias_in_medical_diagnosis)

SexualOverperceptionBias - [Sexual Overperception Bias](https://en.wikipedia.org/wiki/Error_management_theory)

Stereotyping - [Stereotyping](https://en.wikipedia.org/wiki/Stereotype)

</details>
