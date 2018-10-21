import numpy
import uno
import unohelper
import interval.fpu
from com.doobiecompany.examples.DoobieDoo import XDoobieDoo
from interval import interval, inf, imath
from interval.fpu import up,down
from interval.imath import *


class DoobieDooImpl( unohelper.Base, XDoobieDoo ):
	def __init__( self, ctx ):
		self.ctx = ctx

	
	def SUMItv( self, *args ):		
		from interval import interval
		somme=interval([0,0])		
		c=str(args)
		c=c.replace(",,",",")
		c=c.replace(")","")
		c=c.replace("(","")
		c=c.replace(",,",",")
		c=c.replace("'","")
		c=c.replace(" ","")
		c=c.replace("''","")
		c=c.replace(",,",",")		
		mm=c.split(",")	
		i=0					
		while (i<len(mm)): #< len(mm)					
			cour=str(mm[i])
			if cour != "None" and cour !="":
				cour=cour.replace("'","")
				cour=cour.replace(" ","")
				cour=cour.replace(",","")			
				if cour == "nan;nan":
					return "nan;nan"
				elif cour.count(";")==0:				
					b1=down(lambda: float(cour))
					b2=up(lambda: float(cour))
					from interval import interval, inf, imath
					somme=somme+interval([b1,b2])
				else:							
					a1=down(lambda:float(cour.split(";")[0]))
					a2=up(lambda:float(cour.split(";")[1]))
					#from interval import interval
					somme=somme+interval([a1,a2])
			i+=1	
		res=str(somme)		
		if res.count(",")==0:
			res1=res.split("[")[1]
			res2=res1.split("]")[0]
			return str(res2	)	
		else:		
			aa=res.split("[")[1]
			bb=aa.split(",")[0]
			cc=aa.split(" ")[1]
			dd=cc.split("]")[0]
			return bb +";"+dd	
	def DIFFItv( self, a, b ):
		if a=="nan;nan" or b=="nan;nan":
			return "nan;nan"
		else:		
			if a.count(";")==0 and b.count(";")==0:
				a1=down(lambda: float(a))
				b1=down(lambda: float(b))
				a2=up(lambda: float(a))
				b2=up(lambda: float(b))
			elif a.count(";")==0:
				a1=down(lambda: float(a))
				a2=up(lambda: float(a))		
				b1=down(lambda: float(b.split(";")[0]))
				b2=up(lambda: float(b.split(";")[1]))
			elif b.count(";")==0:
				a1=down(lambda: float(a.split(";")[0]))
				b1=down(lambda: float(b))
				a2=up(lambda: float(a.split(";")[1]))
				b2=up(lambda: float(b))
			else:
				a1=down(lambda: float(a.split(";")[0]))
				b1=down(lambda: float(b.split(";")[0]))
				a2=up(lambda: float(a.split(";")[1]))
				b2=up(lambda: float(b.split(";")[1]))
		from interval import interval
		res=str(interval([a1,a2])-interval([b1,b2]))
		if res.count(" ")==0:
			aa=res.split("[")[1]
			dd=aa.split("]")[0]
			return dd +";"+dd
		else:		
			aa=res.split("[")[1]
			bb=aa.split(",")[0]
			cc=aa.split(" ")[1]
			dd=cc.split("]")[0]
			return bb +";"+dd
	def PRODUCTItv( self, *args ):		
		from interval import interval
		somme=interval([1,1])		
		c=str(args)
		c=c.replace(",,",",")
		c=c.replace(")","")
		c=c.replace("(","")
		c=c.replace(",,",",")
		c=c.replace("'","")
		c=c.replace(" ","")
		c=c.replace("''","")
		c=c.replace(",,",",")		
		mm=c.split(",")	
		i=0					
		while (i<len(mm)): #< len(mm)					
			cour=str(mm[i])
			if cour != "None" and cour !="":
				cour=cour.replace("'","")
				cour=cour.replace(" ","")
				cour=cour.replace(",","")			
				if cour == "nan;nan":
					return "nan;nan"
				elif cour.count(";")==0:				
					b1=down(lambda: float(cour))
					b2=up(lambda: float(cour))
					from interval import interval, inf, imath
					somme=somme*interval([b1,b2])
				else:							
					a1=down(lambda:float(cour.split(";")[0]))
					a2=up(lambda:float(cour.split(";")[1]))
					#from interval import interval
					somme=somme*interval([a1,a2])
			i+=1	
		res=str(somme)		
		if res.count(",")==0:
			res1=res.split("[")[1]
			res2=res1.split("]")[0]
			return str(res2	)	
		else:		
			aa=res.split("[")[1]
			bb=aa.split(",")[0]
			cc=aa.split(" ")[1]
			dd=cc.split("]")[0]
			return bb +";"+dd
	def UNIONItv( self, *args ):
		from interval import interval
		somme=interval()		
		c=str(args)
		c=c.replace(",,",",")
		c=c.replace(")","")
		c=c.replace("(","")
		c=c.replace(",,",",")
		c=c.replace("'","")
		c=c.replace(" ","")
		c=c.replace("''","")
		c=c.replace(",,",",")		
		mm=c.split(",")	
		i=0					
		while (i<len(mm)): #< len(mm)					
			cour=str(mm[i])
			if cour != "None" and cour !="":
				cour=cour.replace("'","")
				cour=cour.replace(" ","")
				cour=cour.replace(",","")			
				if cour=="nan;nan":
					somme=somme				
				elif cour.count(";")==0:				
					b1=down(lambda: float(cour))
					b2=up(lambda: float(cour))
					from interval import interval, inf, imath
					somme=somme|interval([b1,b2])
				else:							
					a1=down(lambda:float(cour.split(";")[0]))
					a2=up(lambda:float(cour.split(";")[1]))
					#from interval import interval
					somme=somme|interval([a1,a2])
			somme=interval.hull([somme])
			i+=1	
		res=str(somme)		
		if res.count(",")==0:
			res1=res.split("[")[1]
			res2=res1.split("]")[0]
			return str(res2	)	
		else:		
			aa=res.split("[")[1]
			bb=aa.split(",")[0]
			cc=aa.split(" ")[1]
			dd=cc.split("]")[0]
			return bb +";"+dd
	def DIVItv( self, a, b ):
		if a=="nan;nan" or b=="nan;nan":
			return "nan;nan"
		else:		
			if a.count(";")==0 and b.count(";")==0:
				a1=down(lambda: float(a))
				b1=down(lambda: float(b))
				a2=up(lambda: float(a))
				b2=up(lambda: float(b))
			elif a.count(";")==0:
				a1=down(lambda: float(a))
				a2=up(lambda: float(a))		
				b1=down(lambda: float(b.split(";")[0]))
				b2=up(lambda: float(b.split(";")[1]))
			elif b.count(";")==0:
				a1=down(lambda: float(a.split(";")[0]))
				b1=down(lambda: float(b))
				a2=up(lambda: float(a.split(";")[1]))
				b2=up(lambda: float(b))
			else:
				a1=down(lambda: float(a.split(";")[0]))
				b1=down(lambda: float(b.split(";")[0]))
				a2=up(lambda: float(a.split(";")[1]))
				b2=up(lambda: float(b.split(";")[1]))
		from interval import interval
		inv=interval([b1,b2])
		invcomplet=inv.inverse()		
		res=interval([a1,a2])*invcomplet
		res1=str(interval.hull([res]))
		if res1.count(" ")==0:
			aa=res1.split("[")[1]
			dd=aa.split("]")[0]
			return dd +";"+dd
		else:
			aa=res1.split("[")[1]
			bb=aa.split(",")[0]
			cc=aa.split(" ")[1]
			dd=cc.split("]")[0]
			return bb +";"+dd
	def INTERItv( self, a, b ):
		if a.count(";")==0 and b.count(";")==0:
			a1=down(lambda: float(a))
			b1=down(lambda: float(b))
			a2=up(lambda: float(a))
			b2=up(lambda: float(b))
		elif a.count(";")==0:
			a1=down(lambda: float(a))
			a2=up(lambda: float(a))		
			b1=down(lambda: float(b.split(";")[0]))
			b2=up(lambda: float(b.split(";")[1]))
		elif b.count(";")==0:
			a1=down(lambda: float(a.split(";")[0]))
			b1=down(lambda: float(b))
			a2=up(lambda: float(a.split(";")[1]))
			b2=up(lambda: float(b))
		else:
			a1=down(lambda: float(a.split(";")[0]))
			b1=down(lambda: float(b.split(";")[0]))
			a2=up(lambda: float(a.split(";")[1]))
			b2=up(lambda: float(b.split(";")[1]))
		from interval import interval		
		p=str(interval([a1,a2]) & interval([b1,b2]))
		if (p=="interval()"):
			return "nan;nan"
		if p.count(",")==0:
			aa=p.split("[")[1]
			dd=aa.split("]")[0]
			return dd
		aa=p.split("[")[1]
		bb=aa.split(",")[0]
		cc=aa.split(" ")[1]
		dd=cc.split("]")[0]
		return bb +";"+dd
	def COMPItv( self, a, b ):
		if a==b:
			return "3"		
		elif a.count(";")==0 and b.count(";")==0:
			a1=down(lambda: float(a))
			b1=down(lambda: float(b))
			a2=up(lambda: float(a))
			b2=up(lambda: float(b))
		elif a.count(";")==0:
			a1=down(lambda: float(a))
			a2=up(lambda: float(a))		
			b1=down(lambda: float(b.split(";")[0]))
			b2=up(lambda: float(b.split(";")[1]))
		elif b.count(";")==0:
			a1=down(lambda: float(a.split(";")[0]))
			b1=down(lambda: float(b))
			a2=up(lambda: float(a.split(";")[1]))
			b2=up(lambda: float(b))
		else:
			a1=down(lambda: float(a.split(";")[0]))
			b1=down(lambda: float(b.split(";")[0]))
			a2=up(lambda: float(a.split(";")[1]))
			b2=up(lambda: float(b.split(";")[1]))
		from interval import interval

		if a1>b2:
			return "1"
		elif a1>=b1 and a1<=b2 and a2>b2:
			return "2"
		elif a1>=b1 and a1<=b2 and a2<=b2:
			return "5"
		elif a==b:
			return "3"
		elif b1>a2:
			return "4"
		elif b1>=a1 and b1<=a2 and b2>a2:
			return "5"
		elif b1>=a1 and b1<=a2 and b2<=a2:
			return "2"
	def INItv( self, a, b ):
		a1=down(lambda: float(a.split(";")[0]))
		b1=down(lambda: float(b.split(";")[0]))
		a2=up(lambda: float(a.split(";")[1]))
		b2=up(lambda: float(b.split(";")[1]))
		from interval import interval
		x=interval([a1,a2])
		y=interval([b1,b2])
		if (x.__rand__(y)==x):		
			return True
		else:		
			return False	
	def POWItv( self, a, b ):		
		aa=str(a)		
		if (aa=="nan;nan"):
			return "nan;nan"
		elif aa.count(";")==0:
			a1=down(lambda: float(aa))
			a2=up(lambda: float(aa))				
		else:
			a1=down(lambda: float(a.split(";")[0]))
			a2=up(lambda: float(a.split(";")[1]))
		c=interval([a1,a2])	
		res=c.__pow__(b)
		res1=str(interval.hull([res]))
		if res1.count(" ")==0:
			aa=res1.split("[")[1]
			dd=aa.split("]")[0]
			return dd +";"+dd
		else:
			aa=res1.split("[")[1]
			bb=aa.split(",")[0]
			cc=aa.split(" ")[1]
			dd=cc.split("]")[0]
			return bb +";"+dd	
	def ABSItv( self, a):
		aa=str(a)		
		if (aa=="nan;nan"):
			return "nan;nan"
		elif aa.count(";")==0:	
			a1=down(lambda: float(aa))
			a2=up(lambda: float(aa))
		else:			
			a1=down(lambda: float(a.split(";")[0]))
			a2=up(lambda: float(a.split(";")[1]))
		c=interval([a1,a2])	
		res=c.__abs__()
		res1=str(interval.hull([res]))
		if res1.count(" ")==0:
			aa=res1.split("[")[1]
			dd=aa.split("]")[0]
			return dd +";"+dd
		else:
			aa=res1.split("[")[1]
			bb=aa.split(",")[0]
			cc=aa.split(" ")[1]
			dd=cc.split("]")[0]
			return bb +";"+dd
	def TANItv( self, a):
		aa=str(a)		
		if (aa=="nan;nan"):
			return "nan;nan"
		elif aa.count(";")==0:
			b1=down(lambda: float(a))
			b2=up(lambda: float(a))
			res1=tan(interval([b1,b2]))
			res2=str(interval.hull([res1]))
			aa=res2.split("[")[1]
			bb=aa.split(",")[0]
			cc=aa.split(" ")[1]
			dd=cc.split("]")[0]
			return bb +";"+dd
		else:
			a1=down(lambda: float(a.split(";")[0]))
			a2=up(lambda: float(a.split(";")[1]))
			c=interval([a1,a2])	
			res=tan(c)
			res1=str(interval.hull([res]))
			aa=res1.split("[")[1]
			bb=aa.split(",")[0]
			cc=aa.split(" ")[1]
			dd=cc.split("]")[0]
			return bb +";"+dd	
	def TANHItv( self, a):
		aa=str(a)		
		if (aa=="nan;nan"):
			return "nan;nan"
		elif aa.count(";")==0:
			b1=down(lambda: float(a))
			b2=up(lambda: float(a))
			res1=tanh(interval([b1,b2]))
			res2=str(interval.hull([res1]))
			aa=res2.split("[")[1]
			bb=aa.split(",")[0]
			cc=aa.split(" ")[1]
			dd=cc.split("]")[0]
			return bb +";"+dd
		else:
			a1=down(lambda: float(a.split(";")[0]))
			a2=up(lambda: float(a.split(";")[1]))
			c=interval([a1,a2])	
			res=tanh(c)
			res1=str(interval.hull([res]))
			aa=res1.split("[")[1]
			bb=aa.split(",")[0]
			cc=aa.split(" ")[1]
			dd=cc.split("]")[0]
			return bb +";"+dd	
	def TANPIItv( self, a):
		aa=str(a)		
		if (aa=="nan;nan"):
			return "nan;nan"
		elif aa.count(";")==0:
			b1=down(lambda: float(a))
			b2=up(lambda: float(a))
			res1=tanpi(interval([b1,b2]))
			res2=str(interval.hull([res1]))
			aa=res2.split("[")[1]
			bb=aa.split(",")[0]
			cc=aa.split(" ")[1]
			dd=cc.split("]")[0]
			return bb +";"+dd
		else:
			a1=down(lambda: float(a.split(";")[0]))
			a2=up(lambda: float(a.split(";")[1]))
			c=interval([a1,a2])	
			res=tanpi(c)
			res1=str(interval.hull([res]))
			aa=res1.split("[")[1]
			bb=aa.split(",")[0]
			cc=aa.split(" ")[1]
			dd=cc.split("]")[0]
			return bb +";"+dd
	def ATANItv( self, a):
		aa=str(a)		
		if (aa=="nan;nan"):
			return "nan;nan"
		elif aa.count(";")==0:
			b1=down(lambda: float(a))
			b2=up(lambda: float(a))
			res1=atan(interval([b1,b2]))
			res2=str(interval.hull([res1]))
			aa=res2.split("[")[1]
			bb=aa.split(",")[0]
			cc=aa.split(" ")[1]
			dd=cc.split("]")[0]
			return bb +";"+dd
		else:
			a1=down(lambda: float(a.split(";")[0]))
			a2=up(lambda: float(a.split(";")[1]))
			c=interval([a1,a2])	
			res=atan(c)
			res1=str(interval.hull([res]))
			aa=res1.split("[")[1]
			bb=aa.split(",")[0]
			cc=aa.split(" ")[1]
			dd=cc.split("]")[0]
			return bb +";"+dd
	def ATANPIItv( self, a):
		aa=str(a)		
		if (aa=="nan;nan"):
			return "nan;nan"
		elif aa.count(";")==0:
			b1=down(lambda: float(a))
			b2=up(lambda: float(a))
			res1=atanpi(interval([b1,b2]))
			res2=str(interval.hull([res1]))
			aa=res2.split("[")[1]
			bb=aa.split(",")[0]
			cc=aa.split(" ")[1]
			dd=cc.split("]")[0]
			return bb +";"+dd
		else:
			a1=down(lambda: float(a.split(";")[0]))
			a2=up(lambda: float(a.split(";")[1]))
			c=interval([a1,a2])	
			res=atanpi(c)
			res1=str(interval.hull([res]))
			aa=res1.split("[")[1]
			bb=aa.split(",")[0]
			cc=aa.split(" ")[1]
			dd=cc.split("]")[0]
			return bb +";"+dd
	def COSItv( self, a):
		aa=str(a)		
		if (aa=="nan;nan"):
			return "nan;nan"
		elif aa.count(";")==0:
			b1=down(lambda: float(a))
			b2=up(lambda: float(a))
			res1=str(cos(interval([b1,b2])))
			aa=res1.split("[")[1]
			bb=aa.split(",")[0]
			cc=aa.split(" ")[1]
			dd=cc.split("]")[0]
			return bb +";"+dd
		else:
			a1=down(lambda: float(a.split(";")[0]))
			a2=up(lambda: float(a.split(";")[1]))
			c=interval([a1,a2])	
			res=cos(c)
			res1=str(interval.hull([res]))
			aa=res1.split("[")[1]
			bb=aa.split(",")[0]
			cc=aa.split(" ")[1]
			dd=cc.split("]")[0]
			return bb +";"+dd
	def COSHItv( self, a):
		aa=str(a)		
		if (aa=="nan;nan"):
			return "nan;nan"
		elif aa.count(";")==0:
			b1=down(lambda: float(a))
			b2=up(lambda: float(a))
			res1=str(cosh(interval([b1,b2])))
			aa=res1.split("[")[1]
			bb=aa.split(",")[0]
			cc=aa.split(" ")[1]
			dd=cc.split("]")[0]
			return bb +";"+dd
		else:
			a1=down(lambda: float(a.split(";")[0]))
			a2=up(lambda: float(a.split(";")[1]))
			c=interval([a1,a2])	
			res=cosh(c)
			res1=str(interval.hull([res]))
			aa=res1.split("[")[1]
			bb=aa.split(",")[0]
			cc=aa.split(" ")[1]
			dd=cc.split("]")[0]
			return bb +";"+dd
	def COSPIItv( self, a):
		aa=str(a)		
		if (aa=="nan;nan"):
			return "nan;nan"
		elif aa.count(";")==0:
			b1=down(lambda: float(a))
			b2=up(lambda: float(a))
			res1=str(cospi(interval([b1,b2])))
			aa=res1.split("[")[1]
			bb=aa.split(",")[0]
			cc=aa.split(" ")[1]
			dd=cc.split("]")[0]
			return bb +";"+dd
		else:
			a1=down(lambda: float(a.split(";")[0]))
			a2=up(lambda: float(a.split(";")[1]))
			c=interval([a1,a2])	
			res=cospi(c)
			res1=str(interval.hull([res]))
			aa=res1.split("[")[1]
			bb=aa.split(",")[0]
			cc=aa.split(" ")[1]
			dd=cc.split("]")[0]
			return bb +";"+dd
	def EXPItv( self, a):
		aa=str(a)		
		if (aa=="nan;nan"):
			return "nan;nan"
		elif aa.count(";")==0:
			b1=down(lambda: float(a))
			b2=up(lambda: float(a))
			res1=str(exp(interval([b1,b2])))
			aa=res1.split("[")[1]
			bb=aa.split(",")[0]
			cc=aa.split(" ")[1]
			dd=cc.split("]")[0]
			return bb +";"+dd
		else:
			a1=down(lambda: float(a.split(";")[0]))
			a2=up(lambda: float(a.split(";")[1]))
			c=interval([a1,a2])	
			res=exp(c)
			res1=str(interval.hull([res]))
			aa=res1.split("[")[1]
			bb=aa.split(",")[0]
			cc=aa.split(" ")[1]
			dd=cc.split("]")[0]
			return bb +";"+dd
	def EXPM1Itv( self, a):
		aa=str(a)		
		if (aa=="nan;nan"):
			return "nan;nan"
		elif aa.count(";")==0:
			b1=down(lambda: float(a))
			b2=up(lambda: float(a))
			res1=str(expm1(interval([b1,b2])))
			aa=res1.split("[")[1]
			bb=aa.split(",")[0]
			cc=aa.split(" ")[1]
			dd=cc.split("]")[0]
			return bb +";"+dd
		else:
			a1=down(lambda: float(a.split(";")[0]))
			a2=up(lambda: float(a.split(";")[1]))
			c=interval([a1,a2])	
			res=expm1(c)
			res1=str(interval.hull([res]))
			aa=res1.split("[")[1]
			bb=aa.split(",")[0]
			cc=aa.split(" ")[1]
			dd=cc.split("]")[0]
			return bb +";"+dd
	def LOGItv( self, a):
		aa=str(a)		
		if (aa=="nan;nan"):
			return "nan;nan"
		elif aa.count(";")==0:
			b1=down(lambda: float(a))
			b2=up(lambda: float(a))
			res1=str(log(interval([b1,b2])))
			aa=res1.split("[")[1]
			bb=aa.split(",")[0]
			cc=aa.split(" ")[1]
			dd=cc.split("]")[0]
			return bb +";"+dd
		else:
			a1=down(lambda: float(a.split(";")[0]))
			a2=up(lambda: float(a.split(";")[1]))
			c=interval([a1,a2])	
			res=log(c)
			res1=str(interval.hull([res]))
			aa=res1.split("[")[1]
			bb=aa.split(",")[0]
			cc=aa.split(" ")[1]
			dd=cc.split("]")[0]
			return bb +";"+dd
	def LOGDIXItv( self, a):
		aa=str(a)		
		if (aa=="nan;nan"):
			return "nan;nan"
		elif aa.count(";")==0:
			b1=down(lambda: float(a))
			b2=up(lambda: float(a))
			res1=str(log10(interval([b1,b2])))
			aa=res1.split("[")[1]
			bb=aa.split(",")[0]
			cc=aa.split(" ")[1]
			dd=cc.split("]")[0]
			return bb +";"+dd
		else:
			a1=down(lambda: float(a.split(";")[0]))
			a2=up(lambda: float(a.split(";")[1]))
			c=interval([a1,a2])	
			res=log10(c)
			res1=str(interval.hull([res]))
			aa=res1.split("[")[1]
			bb=aa.split(",")[0]
			cc=aa.split(" ")[1]
			dd=cc.split("]")[0]
			return bb +";"+dd
	def LOGUNPIItv( self, a):
		aa=str(a)		
		if (aa=="nan;nan"):
			return "nan;nan"
		elif aa.count(";")==0:
			b1=down(lambda: float(a))
			b2=up(lambda: float(a))
			res1=str(log1p(interval([b1,b2])))
			aa=res1.split("[")[1]
			bb=aa.split(",")[0]
			cc=aa.split(" ")[1]
			dd=cc.split("]")[0]
			return bb +";"+dd
		else:
			a1=down(lambda: float(a.split(";")[0]))
			a2=up(lambda: float(a.split(";")[1]))
			c=interval([a1,a2])	
			res=log1p(c)
			res1=str(interval.hull([res]))
			aa=res1.split("[")[1]
			bb=aa.split(",")[0]
			cc=aa.split(" ")[1]
			dd=cc.split("]")[0]
			return bb +";"+dd
	def LOGDEUXItv( self, a):
		aa=str(a)		
		if (aa=="nan;nan"):
			return "nan;nan"
		elif aa.count(";")==0:
			b1=down(lambda: float(a))
			b2=up(lambda: float(a))
			res1=str(log2(interval([b1,b2])))
			aa=res1.split("[")[1]
			bb=aa.split(",")[0]
			cc=aa.split(" ")[1]
			dd=cc.split("]")[0]
			return bb +";"+dd
		else:
			a1=down(lambda: float(a.split(";")[0]))
			a2=up(lambda: float(a.split(";")[1]))
			c=interval([a1,a2])	
			res=log2(c)
			res1=str(interval.hull([res]))
			aa=res1.split("[")[1]
			bb=aa.split(",")[0]
			cc=aa.split(" ")[1]
			dd=cc.split("]")[0]
			return bb +";"+dd
	def SINItv( self, a):
		aa=str(a)		
		if (aa=="nan;nan"):
			return "nan;nan"
		elif aa.count(";")==0:
			b1=down(lambda: float(a))
			b2=up(lambda: float(a))
			res1=str(sin(interval([b1,b2])))
			aa=res1.split("[")[1]
			bb=aa.split(",")[0]
			cc=aa.split(" ")[1]
			dd=cc.split("]")[0]
			return bb +";"+dd
		else:
			a1=down(lambda: float(a.split(";")[0]))
			a2=up(lambda: float(a.split(";")[1]))
			c=interval([a1,a2])	
			res=sin(c)
			res1=str(interval.hull([res]))
			aa=res1.split("[")[1]
			bb=aa.split(",")[0]
			cc=aa.split(" ")[1]
			dd=cc.split("]")[0]
			return bb +";"+dd
	def SINHItv( self, a):
		aa=str(a)		
		if (aa=="nan;nan"):
			return "nan;nan"
		elif aa.count(";")==0:
			b1=down(lambda: float(a))
			b2=up(lambda: float(a))
			res1=str(sinh(interval([b1,b2])))
			aa=res1.split("[")[1]
			bb=aa.split(",")[0]
			cc=aa.split(" ")[1]
			dd=cc.split("]")[0]
			return bb +";"+dd
		else:		
			a1=down(lambda: float(a.split(";")[0]))
			a2=up(lambda: float(a.split(";")[1]))
			c=interval([a1,a2])	
			res=sinh(c)
			res1=str(interval.hull([res]))
			aa=res1.split("[")[1]
			bb=aa.split(",")[0]
			cc=aa.split(" ")[1]
			dd=cc.split("]")[0]
			return bb +";"+dd
	def SINPIItv( self, a):
		aa=str(a)		
		if (aa=="nan;nan"):
			return "nan;nan"		
		elif aa.count(";")==0:
			b1=down(lambda: float(a))
			b2=up(lambda: float(a))
			res1=str(sin(interval([b1,b2])))
			aa=res1.split("[")[1]
			bb=aa.split(",")[0]
			cc=aa.split(" ")[1]
			dd=cc.split("]")[0]
			return bb +";"+dd
		else:
			a1=down(lambda: float(a.split(";")[0]))
			a2=up(lambda: float(a.split(";")[1]))
			c=interval([a1,a2])	
			res=sinpi(c)
			res1=str(interval.hull([res]))
			aa=res1.split("[")[1]
			bb=aa.split(",")[0]
			cc=aa.split(" ")[1]
			dd=cc.split("]")[0]
			return bb +";"+dd
	
	#ajouter les fonctions de comparaison aussi !


def createInstance( ctx ):
	return DoobieDooImpl( ctx )

g_ImplementationHelper = unohelper.ImplementationHelper()
g_ImplementationHelper.addImplementation( \
	createInstance,"com.doobiecompany.examples.DoobieDoo.python.DoobieDooImpl",
		("com.sun.star.sheet.AddIn",),)

