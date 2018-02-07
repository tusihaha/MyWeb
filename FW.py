import clr
def elasticmodel(a,a_1,b_1,c_1,d_1,e_1,a_4,b_4,c_4,d_4,a_2,b_2,c_2,d_2,e_2,a_3,b_3,c_3,d_3):
	mydll = clr.AddReference("FortranWrapper")
	import FortranWrapper
	e1 = FortranWrapper.ElasticModel()
	f1 = FortranWrapper.FailureProperties()
	m1 = FortranWrapper.MechanicalProperties()
	s1 = FortranWrapper.StressGradients()
	w1 = FortranWrapper.WellboreGeometry()
	
	b0 = FortranWrapper.BoreholeCondition.Impermeable
	b1 = FortranWrapper.BoreholeCondition.Permeable


	boreholecondition = list()
	for i in a:
		if i=='Impermeable':
			boreholecondition.append(b0)
		elif i=='Permeable':
			boreholecondition.append(b1)
		else:
			return "Value Error"
	e1.BoreholeCondition = boreholecondition
	try:
		f1.BreakOutAngle = [float(i) for i in a_1]
		f1.Cohesion = [float(i) for i in b_1]
		f1.FrictionAngle = [float(i) for i in c_1]
		f1.RadialRatio = [float(i) for i in d_1]
		f1.TensileStrength = [float(i) for i in e_1]
		e1.FailureProperties = f1

		m1.PoissonRatioInIsotropicPlane = [float(i) for i in a_4]
		m1.YoungModulusInIsotropicPlane = [float(i) for i in b_4]
		m1.PoissonRatioInTransverseDirection = [float(i) for i in c_4]
		m1.YoungModulusInTransverseDirection = [float(i) for i in d_4]
		e1.MechanicalProperties = m1

		s1.MaxHorizontalStressAzimuth = [float(i) for i in a_2]
		s1.MaxHorizontalStressGradient = [float(i) for i in b_2]
		s1.MinHorizontalStressGradient = [float(i) for i in c_2]
		s1.OverburdenStressGradient = [float(i) for i in d_2]
		s1.PorePressureGradient = [float(i) for i in e_2]
		e1.StressGradients = s1

		w1.Azimuth = [float(i) for i in a_3]
		w1.BoreholeRadius = [float(i) for i in b_3]
		w1.Inclination = [float(i) for i in c_3]
		w1.TVD = [float(i) for i in d_3]
		e1.WellboreGeometry = w1
	except:
		return "Value Error"
	return e1

def failurecriterion(criterion):
	mydll = clr.AddReference("FortranWrapper")
	import FortranWrapper
	f0=FortranWrapper.FailureCriterion.MohrCoulomb
	f1=FortranWrapper.FailureCriterion.DruckerPrager
	f2=FortranWrapper.FailureCriterion.ModifiedLade
	f3=FortranWrapper.FailureCriterion.StassidAlia
	if(criterion=="MohrCoulomb"):
		return f0
	elif(criterion=="DruckerPrager"):
		return f1
	elif(criterion=="ModifiedLade"):
		return f2
	elif(criterion=="StassidAlia"):
		return f3
		
def ComputeCollapse(a,b,c,d):
	mydll = clr.AddReference("FortranWrapper")
	import FortranWrapper
	fo = FortranWrapper.FortranDllService[FortranWrapper.ElasticModel]()
	return fo.ComputeCollapseMudWeights(a,b,c,d)

def ComputeFracturing(a,b,c):
	mydll = clr.AddReference("FortranWrapper")
	import FortranWrapper
	fo = FortranWrapper.FortranDllService[FortranWrapper.ElasticModel]()
	return fo.ComputeFracturingMudWeights(a,b,c)
