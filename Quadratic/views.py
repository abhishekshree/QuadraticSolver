from django.shortcuts import render, redirect
from .forms import q
import cmath
# Create your views here.
def main(request):
	an = 'a'
	bn = 'b'
	cn = 'c'
	vA, vB = 'A', 'B'
	if request.method == 'POST':
		Q = q(request.POST)

		if Q.is_valid():
			an = int(request.POST['a'])
			bn = int(request.POST['b'])
			cn = int(request.POST['c'])
			d = (bn**2) - (4*an*cn)
			vA = (-bn + cmath.sqrt(d))/(2*an)
			vB = (-bn - cmath.sqrt(d))/(2*an)
			Q = q()
	else:
		Q = q()
	context = {'q':Q,'a':an,'b':bn, 'c':cn, 'alpha':str(vA), 'beta':str(vB)}
	return render(request, 'Quadratic/index.html', context)