import Solution.Basic

/-! Lane-3 audit, SOLUTION side: axioms of the four theorems, their exact
statements, and the definitions those statements use. Output is diffed
against AuditChallenge.lean, which prints the same items from the
challenge module. -/

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
