import FW
from flask import Flask, render_template, request, jsonify

app=Flask(__name__)

@app.route("/ComputeCollapse", methods = ["POST"])
def Collapse():
	if request.is_json:
		data = request.get_json()
		try:
			a = data['BoreholeCondition']

			a_1 = data['BreakOutAngle']
			b_1 = data['Cohesion']
			c_1 = data['FrictionAngle']
			d_1 = data['RadialRatio']
			e_1 = data['TensileStrength']

			a_4 = data['PoissonRatioInIsotropicPlane']
			b_4 = data['YoungModulusInIsotropicPlane']
			
			a_2 = data['MaxHorizontalStressAzimuth']
			b_2 = data['MaxHorizontalStressGradient']
			c_2 = data['MinHorizontalStressGradient']
			d_2 = data['OverburdenStressGradient']
			e_2 = data['PorePressureGradient']

			a_3 = data['Azimuth']
			b_3 = data['BoreholeRadius']
			c_3 = data['Inclination']
			d_3 = data['TVD']
		except:
			code=500
			reason="Key Error"
			data=[]
			return jsonify({'Code':code,'Reason':reason,'Data':data})

		criterion = 'None'
		c_4 = list()
		d_4 = list()
		try:
			c_4 = data['PoissonRatioInTransverseDirection']
			d_4 = data['YoungModulusInTransverseDirection']
			criterion = data['Criterion']
		except:
			pass

		n = len(d_3)
		if (len(a)<n or len(a_1)<n or len(a_2)<n or len(a_3)<n or len(a_4)<n or len(b_1)<n or len(b_2)<n or len(b_3)<n or len(b_4)<n 
			or len(c_1)<n or len(c_2)<n or len(c_3)<n or len(d_1)<n or len(d_2)<n or len(e_1)<n or len(e_2)<n):
			code=500
			reason="Array Error"
			data=[]
			return jsonify({'Code':code,'Reason':reason,'Data':data})
		else:
			e = FW.elasticmodel(a,a_1,b_1,c_1,d_1,e_1,a_4,b_4,c_4,d_4,a_2,b_2,c_2,d_2,e_2,a_3,b_3,c_3,d_3)
			f = FW.failurecriterion(criterion)

			if(e=="Value Error"):
				code=500
				reason="Value Error"
				data=[]
				return jsonify({'Code':code,'Reason':reason,'Data':data})

			if f==None:
				data = [float(i) for i in FW.ComputeCollapse(e,0,None,0)]
			else:
				data = [float(i) for i in FW.ComputeCollapse(e,f,None,0)]
			code=200
			reason="success"
			return jsonify({'Code':code,'Reason':reason,'Data':data})
	else:
		try:
			a = request.form['BoreholeCondition'].split(',')
			
			a_1 = [float(i) for i in request.form['BreakOutAngle'].split(',')]
			b_1 = [float(i) for i in request.form['Cohesion'].split(',')]
			c_1 = [float(i) for i in request.form['FrictionAngle'].split(',')]
			d_1 = [float(i) for i in request.form['RadialRatio'].split(',')]
			e_1 = [float(i) for i in request.form['TensileStrength'].split(',')]
			
			a_4 = [float(i) for i in request.form['PoissonRatioInIsotropicPlane'].split(',')]
			b_4 = [float(i) for i in request.form['YoungModulusInIsotropicPlane'].split(',')]
			
			a_2 = [float(i) for i in request.form['MaxHorizontalStressAzimuth'].split(',')]
			b_2 = [float(i) for i in request.form['MaxHorizontalStressGradient'].split(',')]
			c_2 = [float(i) for i in request.form['MinHorizontalStressGradient'].split(',')]
			d_2 = [float(i) for i in request.form['OverburdenStressGradient'].split(',')]
			e_2 = [float(i) for i in request.form['PorePressureGradient'].split(',')]
			
			a_3 = [float(i) for i in request.form['Azimuth'].split(',')]
			b_3 = [float(i) for i in request.form['BoreholeRadius'].split(',')]
			c_3 = [float(i) for i in request.form['Inclination'].split(',')]
			d_3 = [float(i) for i in request.form['TVD'].split(',')]
		except:
			code=500
			reason="Key Error"
			data=[]
			return jsonify({'Code':code,'Reason':reason,'Data':data})

		criterion='None'
		c_4 = list()
		d_4 = list()
		try:
			criterion = request.form['Criterion']
			c_4 = [float(i) for i in request.form['PoissonRatioInTransverseDirection'].split(',')]
			d_4 = [float(i) for i in request.form['YoungModulusInTransverseDirection'].split(',')]
		except:
			pass

		n = len(d_3)
		if (len(a)<n or len(a_1)<n or len(a_2)<n or len(a_3)<n or len(a_4)<n or len(b_1)<n or len(b_2)<n or len(b_3)<n or len(b_4)<n 
			or len(c_1)<n or len(c_2)<n or len(c_3)<n or len(d_1)<n or len(d_2)<n or len(e_1)<n or len(e_2)<n):
			code=500
			reason="Array Error"
			data=[]
			return jsonify({'Code':code,'Reason':reason,'Data':data})
		else:
			e = FW.elasticmodel(a,a_1,b_1,c_1,d_1,e_1,a_4,b_4,c_4,d_4,a_2,b_2,c_2,d_2,e_2,a_3,b_3,c_3,d_3)
			f = FW.failurecriterion(criterion)

			if(e=="Value Error"):
				code=500
				reason="Value Error"
				data=[]
				return jsonify({'Code':code,'Reason':reason,'Data':data})

			if f==None:
				result = FW.ComputeCollapse(e,0,None,0)
			else:
				result = FW.ComputeCollapse(e,f,None,0)
			
			code=200
			reason="success"
			return jsonify({'Code':code,'Reason':reason,'Data':data})

@app.route("/ComputeFracturing", methods = ["POST"])
def Fracturing():
	if request.is_json:
		data = request.get_json()
		try:
			a = data['BoreholeCondition']

			a_1 = data['BreakOutAngle']
			b_1 = data['Cohesion']
			c_1 = data['FrictionAngle']
			d_1 = data['RadialRatio']
			e_1 = data['TensileStrength']

			a_4 = data['PoissonRatioInIsotropicPlane']
			b_4 = data['YoungModulusInIsotropicPlane']

			a_2 = data['MaxHorizontalStressAzimuth']
			b_2 = data['MaxHorizontalStressGradient']
			c_2 = data['MinHorizontalStressGradient']
			d_2 = data['OverburdenStressGradient']
			e_2 = data['PorePressureGradient']

			a_3 = data['Azimuth']
			b_3 = data['BoreholeRadius']
			c_3 = data['Inclination']
			d_3 = data['TVD']
		except:
			code=500
			reason="Key Error"
			data=[]
			return jsonify({'Code':code,'Reason':reason,'Data':data})

		c_4 = list()
		d_4 = list()
		try:
			c_4 = data['PoissonRatioInTransverseDirection']
			d_4 = data['YoungModulusInTransverseDirection']
		except:
			pass

		n = len(d_3)
		if (len(a)<n or len(a_1)<n or len(a_2)<n or len(a_3)<n or len(a_4)<n or len(b_1)<n or len(b_2)<n or len(b_3)<n or len(b_4)<n 
			or len(c_1)<n or len(c_2)<n or len(c_3)<n or len(d_1)<n or len(d_2)<n or len(e_1)<n or len(e_2)<n):
			code=500
			reason="Array Error"
			data=[]
			return jsonify({'Code':code,'Reason':reason,'Data':data})
		else:
			e = FW.elasticmodel(a,a_1,b_1,c_1,d_1,e_1,a_4,b_4,c_4,d_4,a_2,b_2,c_2,d_2,e_2,a_3,b_3,c_3,d_3)

			if(e=="Value Error"):
				code=500
				reason="Value Error"
				data=[]
				return jsonify({'Code':code,'Reason':reason,'Data':data})
				
			result = [float(i) for i in FW.ComputeFracturing(e,None,0)]

			code=200
			reason="success"
			return jsonify({'Code':code,'Reason':reason,'Data':data})
	else:
		try:
			a = request.form['BoreholeCondition'].split(',')
			
			a_1 = [float(i) for i in request.form['BreakOutAngle'].split(',')]
			b_1 = [float(i) for i in request.form['Cohesion'].split(',')]
			c_1 = [float(i) for i in request.form['FrictionAngle'].split(',')]
			d_1 = [float(i) for i in request.form['RadialRatio'].split(',')]
			e_1 = [float(i) for i in request.form['TensileStrength'].split(',')]
			
			a_4 = [float(i) for i in request.form['PoissonRatioInIsotropicPlane'].split(',')]
			b_4 = [float(i) for i in request.form['YoungModulusInIsotropicPlane'].split(',')]
			
			a_2 = [float(i) for i in request.form['MaxHorizontalStressAzimuth'].split(',')]
			b_2 = [float(i) for i in request.form['MaxHorizontalStressGradient'].split(',')]
			c_2 = [float(i) for i in request.form['MinHorizontalStressGradient'].split(',')]
			d_2 = [float(i) for i in request.form['OverburdenStressGradient'].split(',')]
			e_2 = [float(i) for i in request.form['PorePressureGradient'].split(',')]
			
			a_3 = [float(i) for i in request.form['Azimuth'].split(',')]
			b_3 = [float(i) for i in request.form['BoreholeRadius'].split(',')]
			c_3 = [float(i) for i in request.form['Inclination'].split(',')]
			d_3 = [float(i) for i in request.form['TVD'].split(',')]
		except:
			code=500
			reason="Key Error"
			data=[]
			return jsonify({'Code':code,'Reason':reason,'Data':data})

		c_4 = list()
		d_4 = list()
		try:
			c_4 = [float(i) for i in request.form['PoissonRatioInTransverseDirection'].split(',')]
			d_4 = [float(i) for i in request.form['YoungModulusInTransverseDirection'].split(',')]
		except:
			pass
		
		if (len(a)<n or len(a_1)<n or len(a_2)<n or len(a_3)<n or len(a_4)<n or len(b_1)<n or len(b_2)<n or len(b_3)<n or len(b_4)<n 
			or len(c_1)<n or len(c_2)<n or len(c_3)<n or len(d_1)<n or len(d_2)<n or len(e_1)<n or len(e_2)<n):
			code=500
			reason="Array Error"
			data=[]
			return jsonify({'Code':code,'Reason':reason,'Data':data})
		else:
			e = FW.elasticmodel(a,a_1,b_1,c_1,d_1,e_1,a_4,b_4,c_4,d_4,a_2,b_2,c_2,d_2,e_2,a_3,b_3,c_3,d_3)

			if(e=="Value Error"):
				code=500
				reason="Value Error"
				data=[]
				return jsonify({'Code':code,'Reason':reason,'Data':data})
			
			result = FW.ComputeFracturing(e,None,0)
			
			code=200
			reason="success"
			return jsonify({'Code':code,'Reason':reason,'Data':data})
if __name__ == '__main__':
	app.run(debug = True, host = '0.0.0.0', threaded = True)