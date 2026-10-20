import Challenge.Basic

/-! Lane-3 audit, CHALLENGE side: the same items as AuditSolution.lean,
printed from the human-written challenge module. The axioms here are
expected to include sorryAx (the challenge bodies are `sorry` by design);
only the statements and definitions are compared. -/

set_option pp.all true
set_option maxRecDepth 8192

#print axioms positive_density_collatz_reaches_one
#print axioms positive_density_collatz_and_collatzAccel_reaches_one
#print axioms positive_density_collatz_and_collatzAccel_reaches_of_coprime_six
#print axioms positive_density_collatz_and_collatzAccel_reaches_of_not_three_dvd

#check @positive_density_collatz_reaches_one
#check @positive_density_collatz_and_collatzAccel_reaches_one
#check @positive_density_collatz_and_collatzAccel_reaches_of_coprime_six
#check @positive_density_collatz_and_collatzAccel_reaches_of_not_three_dvd

#print collatz
#print ReachWithin
#print collatzDensity
#print collatzDensityThreshold
#print collatzAccel
#print collatzDensityDep
#print collatzDensityThresholdDep
