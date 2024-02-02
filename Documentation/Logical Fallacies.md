# Logical Fallacies

{% hint style="success" %}
Added in v.0.0.0.1
{% endhint %}

---

This module add a new 66 exceptions.

Example to use:
```python
import extraexceptions

raise extraexceptions.CherryPicking
```

or you can replace import to `from extraexceptions import ...`:
```python
from extraexceptions import logicalfallacies as lf

raise lf.CherryPicking
```

And in both cases console gave:
```commandline
Traceback (most recent call last):
  File "PATH", line 3, in <module>
    raise lf.CherryPicking
extraexceptions.logicalfallacies.CherryPicking: Except CherryPicking has been raised
```

---

With added custom text:
```python
import extraexceptions

raise extraexceptions.CherryPicking("Some text")
```

```python
from extraexceptions import logicalfallacies as lf

raise lf.CherryPicking("Some text")
```

```commandline
Traceback (most recent call last):
  File "PATH", line 3, in <module>
    raise lf.CherryPicking("Some text")
extraexceptions.logicalfallacies.CherryPicking: "CherryPicking" in "Some text" has been found
```

---

<details>

<summary>Logical Fallacies Info</summary>

## **NameOfClass - Link To The Article**

AdHominem - [Ad Hominem](https://en.wikipedia.org/wiki/Ad_hominem)

AppealToAuthority - [Appeal To Authority](https://en.wikipedia.org/wiki/Argument_from_authority)

AppealToNature - [Appeal To Nature](https://en.wikipedia.org/wiki/Appeal_to_nature)

AppealToEmotion - [Appeal To Emotion](https://en.wikipedia.org/wiki/Appeal_to_emotion)

AppealToTradition - [Appeal To Tradition](https://en.wikipedia.org/wiki/Appeal_to_tradition)

AppealToIgnorance - [Appeal To Ignorance](https://en.wikipedia.org/wiki/Argument_from_ignorance)

AppealToStone - [Appeal To Stone](https://en.wikipedia.org/wiki/Appeal_to_the_stone)

AppealToAccomplishment - [Appeal To Accomplishment](https://en.wikipedia.org/wiki/Appeal_to_accomplishment)

AppealToConsequences - [Appeal To Consequences](https://en.wikipedia.org/wiki/Appeal_to_consequences)

AppealToNovelty - [Appeal To Novelty](https://en.wikipedia.org/wiki/Appeal_to_novelty)

AffirmingTheConsequent - [Affirming The Consequent](https://en.wikipedia.org/wiki/Affirming_the_consequent)

AnecdotalFallacy - [Anecdotal Fallacy](https://en.wikipedia.org/wiki/Argument_from_anecdote)

AmbiguityFallacy - [Ambiguity Fallacy](https://en.wikipedia.org/wiki/Informal_fallacy)

AffirmingADisjunction - [Affirming A Disjunction](https://en.wikipedia.org/wiki/Affirming_a_disjunct)

AssociationFallacy - [Association Fallacy](https://en.wikipedia.org/wiki/Association_fallacy)

BurdenOfProof - [Burden Of Proof](https://en.wikipedia.org/wiki/Burden_of_proof_(law))

Bulverism - [Bulverism](https://en.wikipedia.org/wiki/Bulverism)

CircularReasoning - [Circular Reasoning](https://en.wikipedia.org/wiki/Circular_reasoning)

CompositionFallacy - [Composition Fallacy](https://en.wikipedia.org/wiki/Fallacy_of_composition)

ContinuumFallacy - [Continuum Fallacy](https://en.wikipedia.org/wiki/Sorites_paradox)

CherryPicking - [Cherry Picking](https://en.wikipedia.org/wiki/Cherry_picking)

CourtiersReply - [Courtiers Reply](https://en.wikipedia.org/wiki/Courtier%27s_reply)

ChronologicalSnobbery - [Chronological Snobbery](https://en.wikipedia.org/wiki/Chronological_snobbery)

CircumnstantialAdHominem - [Circumnstantial Ad Hominem(on finmasters.com)](https://finmasters.com/circumstantial-ad-hominem/)

DivisionFallacy - [Division Fallacy](https://en.wikipedia.org/wiki/Fallacy_of_division)

DenyingTheAntecedent - [Denying The Antecedent](https://en.wikipedia.org/wiki/Denying_the_antecedent)

DefinistFallacy - [Definist Fallacy](https://en.wikipedia.org/wiki/Definist_fallacy)

EquivocationFallacy - [Equivocation Fallacy](https://en.wikipedia.org/wiki/Equivocation)

EcologicalFallacy - [Ecological Fallacy](https://en.wikipedia.org/wiki/Ecological_fallacy)

EtymologicalFallacy - [Etymological Fallacy](https://en.wikipedia.org/wiki/Etymological_fallacy)

FalseDilemmaFallacy - [False Dilemma Fallacy](https://en.wikipedia.org/wiki/False_dilemma)

FaultyAnalogy - [Faulty Analogy](https://en.wikipedia.org/wiki/Argument_from_analogy)

FalseCause - [False Cause](https://en.wikipedia.org/wiki/Questionable_cause)

FalseEquivalence - [False Equivalence](https://en.wikipedia.org/wiki/False_equivalence)

FallacyOfSingleCause - [Fallacy Of Single Cause](https://en.wikipedia.org/wiki/Fallacy_of_the_single_cause)

GeneticFallacy - [Genetic Fallacy](https://en.wikipedia.org/wiki/Genetic_fallacy)

HastyGeneralization - [Hasty Generalization](https://en.wikipedia.org/wiki/Faulty_generalization)

RedHerring - [Red Herring](https://en.wikipedia.org/wiki/Red_herring)

TuQuoQue - [Tu QuoQue](https://en.wikipedia.org/wiki/Tu_quoque)

SlipperySlope - [Slippery Slope](https://en.wikipedia.org/wiki/Slippery_slope)

SpecialPleading - [Special Pleading](https://en.wikipedia.org/wiki/Special_pleading)

LoadedQuestion - [Loaded Question](https://en.wikipedia.org/wiki/Loaded_question)

StrawmanFallacy - [Strawman Fallacy](https://en.wikipedia.org/wiki/Straw_man)

NoTrueScotsman - [No True Scotsman](https://en.wikipedia.org/wiki/No_true_Scotsman)

TexasSharpshooter - [Texas Sharpshooter](https://en.wikipedia.org/wiki/Texas_sharpshooter_fallacy)

SuppressedCorrelative - [Suppressed Correlative](https://en.wikipedia.org/wiki/Suppressed_correlative)

PersonalIncredulity - [Personal Incredulity](https://en.wikipedia.org/wiki/Argument_from_incredulity)

MiddleGroundFallacy - [Middle Ground Fallacy](https://en.wikipedia.org/wiki/Argument_to_moderation)

SunkCostFallacy - [Sunk Cost Fallacy](https://en.wikipedia.org/wiki/Sunk_cost)

QuotingOutOfContext - [Quoting Out Of Context](https://en.wikipedia.org/wiki/Quoting_out_of_context)

HistoriansFallacy - [Historians Fallacy](https://en.wikipedia.org/wiki/Historian%27s_fallacy)

InflationOfConflict - [Inflation Of Conflict](https://en.wikipedia.org/wiki/List_of_fallacies#Inflation_of_conflict)

IncompleteComparison - [Incomplete Comparison](https://en.wikipedia.org/wiki/Incomplete_comparison)

LudicFallacy - [Ludic Fallacy](https://en.wikipedia.org/wiki/Ludic_fallacy)

MoralisticFallacy - [Moralistic Fallacy](https://en.wikipedia.org/wiki/Moralistic_fallacy)

NirvanaFallacy - [Nirvana Fallacy](https://en.wikipedia.org/wiki/Nirvana_fallacy)

ProofByAssertion - [Proof By Assertion](https://en.wikipedia.org/wiki/Proof_by_assertion)

PsychologistsFallacy - [Psychologists Fallacy](https://en.wikipedia.org/wiki/Psychologist%27s_fallacy)

ReificationFallacy - [Reification Fallacy](https://en.wikipedia.org/wiki/Reification_(fallacy))

RetrospectiveDeterminism - [Retrospective Determinism](https://en.wikipedia.org/wiki/Retrospective_determinism)

ThoughtTerminatingCliche - [Thought Terminating Cliché](https://en.wikipedia.org/wiki/Thought-terminating_clich%C3%A9)

MissingPointFallacy - [Missing Point Fallacy](https://en.wikipedia.org/wiki/Irrelevant_conclusion)

TonePolicing - [Tone Policing](https://en.wikipedia.org/wiki/Tone_policing)

ImEntitledToMyOpinion - [I'm Entitled To My Opinion](https://en.wikipedia.org/wiki/I%27m_entitled_to_my_opinion)

TwoWrongsMakeARight - [Two Wrongs Make A Right](https://en.wikipedia.org/wiki/Two_wrongs_don%27t_make_a_right)

VacuousTruth - [Vacuous Truth](https://en.wikipedia.org/wiki/Vacuous_truth)

</details>
