#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Calculation of Design Moment
L=float(input("what is the unsupporteD length 'L' in meters= "))
D=int(input("what is the lateral Dimension 'D' in mm= "))
eminx=(L/500)+(D/30)          
if eminx > 20:
    eminx=eminx
if eminx < 20:
    eminx=20
B=int(input("what is the lateral Dimension 'B'= "))    
eminy=(L/500)+(B/30)  
if eminy > 20:
    eminy=eminy
if eminx < 20:
    eminy=20
pu=int(input("what is factored axial loaD 'pu'= "))
Muxl=int(input("what is Mux at top 'Muxl'= "))
Muxs=int(input("what is Mux at Bottom 'Muxs'= "))
Muyl=int(input("what is Muy at top 'Muyl'= "))
Muys=int(input("what is Muy at Bottom 'Muys'= "))
C=int(input("type 1 for column BenDing in single curvature & type 2 for column BenDing in DouBle curvature"))
if C==1:
    Mux1=(pu*eminx)/1000
    Mux2=(0.6*Muxl)+(0.4*Muxs)
    if Mux1>Mux2:
        Mux=Mux1
    else:
        Mux=Mux2
    Muy1=(pu*eminy)/1000
    Muy2=(0.6*Muyl)+(0.4*Muys)
    if Muy1>Muy2:
        Muy=Muy1
    else:
        Muy=Muy2
if C==2:
    Mux1=(pu*eminx)/1000
    Mux2=(0.6*Muxl-0.4*Muxs)
    if Mux2<0.4*Muxs:
        print("value of Mux2 is not valiD ")   
    if Mux1>Mux2:
        Mux=Mux1
    else:
        Mux=Mux2
    Muy1=(pu*eminy)/1000
    Muy2=(0.6*Muyl)+(0.4*Muys)
    if Muy2<0.4*Muys:
        print("value of Muy2 is not valiD")
    if Muy1>Muy2:
        Muy=Muy1
    else:
        Muy=Muy2
#check for long column
T=0
lex=int(input("what is length in longer Direction 'Lxeff' in mm= "))
ley=int(input("what is length in longer Direction 'Lyeff' in mm= "))
check1=lex/D
check2=ley/B
if check1>12 or check2>12:
    print("Therefore the memBer is long column")
elif check1<12 and check2<12:
    T=1
    print("Therefore the memBer is short column")
else:
    print("Therefore the memBer is Long column")
#step 3
cc=int(input("enter the value of'clear cover'= "))
p=float(input("enter %of steel to proviDe="))
fck=int(input("what is the value of 'fck'= "))
fy=int(input("what is the value of 'fy'= ")) 
F=int(input("Enter 1 if you want equal reinforcement on all four siDes and 2 for reinforcement on two opposite siDes of column"))
Max=((pu*(10**3)*D)/2000)*(lex/D)**2
May=((pu*(10**3)*B)/2000)*(ley/B)**2
ag=B*D
asc=(3/100)*ag
ac=ag-asc
puz=(0.45*fck*ac)+(0.75*fy*asc)
x=cc/D
#interpolation eq
k1=-(2.6667*x**2)+(1*x**2)-(0.3433*x)+0.234
if fy==250 and F==2:
    k2=-0.045
if fy==415 and F==2:
    k2=-(13.333*x**3)-(0.4*x**2)-(0.0133*x)+0.098
if fy==500 and F==2:
    k2=-(9.3333*x**3)-(3*x**2)-(0.1867*x)+0.231
if fy==250 and F==1:
    k2=(38.667*x**3)-(14.8*x**2)+(0.1633*x)+0.239
if fy==415 and F==1:
    k2=-(28*x**3)+(2.6*x**2)-(1.82*x)+0.512
if fy==500 and F==1:
    k2=(2.6667*x**3)-(10.6*x**2)-(0.8567*x)+0.614
pB=((k1+k2*(p/fck))*fck*B*D)*1/10**3
k=(puz-pu)/(puz-pB)
Max=(Max*k)*1/(10**6)
May=(May*k)*1/(10**6)
Fmux=Mux+Max
Fmuy=Muy+May
if T==1:
    Fmux=Mux
    Fmuy=Muy
#step 4
#Calculation of moment carrying in x and y Direction By interaction chart 
check3=cc/D
check4=cc/B
print("D'/B= %.2f"%check4)
print("D'/D=%.2f "%check3)  
check5=p/fck
print("p/fck= ",check5)
check6=(pu*1000)/(fck*B*D)
print("pu/fck.B.D=%.4f "%check6)
print("Use Charts of IS.SP16.1980")
print("see the value of x-axis at the intersection of point of intersection of pu/fck.B.D and p/fck")
mf1=float(input(" enter value of mux'/fckBDD from the chart= "))
Mux_Dash=mf1*fck*B*D*D/1e6
mf2=float(input("enter value of muy'/fckBDD from chart="))
Muy_Dash=mf2*fck*D*B*B/1e6
check7=pu/puz
if 0.2<=check7<=0.8:
    an=(1.666*check7)+ 0.666
if check7<0.2:
    an=1
else:
    an=2
check8=((Fmux/Mux_Dash)**an)+((Fmuy/Muy_Dash)**an)
if check8<=1:
    print("the Design is safe")
else:
    print("the Design is not safe,please try again By changing the value of % of steel")
#cal of Dimension of reinforcement
Dia_Bar=int(input("Enter the Diameter of longituDinal Bar you want in column in mm="))
n_olD=(asc*(4/3.14))/(Dia_Bar)**2
n=int(((n_olD//2)*2))
if n_olD%2>1:
    n=n+2
elif 0<n_olD%2<=1:
    n=n+1
else:
    n=n
#Design of link
Dia_link=(1/4)*Dia_Bar
if Dia_link<6:
    Dia_link=6
if Dia_link>6:
    Dia_link=8
if Dia_link>8:
    Dia_link=12
if Dia_link>12:
    Dia_link=16
if Dia_link>16:
    Dia_link=20
if Dia_link>20:
    Dia_link=25
PL=16*Dia_Bar
if PL<B or PL==B and B<300:
    pitch=PL
elif B<PL or B==PL and PL<300:
    pitch=B
else:
    pitch=300
# Arrangement of link for r/f on all four siDes
if F==1:
    m=int((((n-4)/4)+2)//2)*2
    if m%2>1:
        m=m+2
    elif 0<n_olD%2<=1:
        m=m+1
    else:
        m=m
    spacing=(D-cc-cc-Dia_Bar)/(m-1)
    if spacing<75 or spacing==75:
        print("simple")
        import matplotlib.pyplot as plt
        plt.figure(figsize=(5,7))
        plt.plot([0,B],[0,0],color="Blue")
        plt.plot([B,B],[0,D],color="Blue")
        plt.plot([0,B],[D,D],color="Blue")
        plt.plot([0,0],[0,D],color="Blue")
        spacing1=(B-cc-cc-Dia_Bar)/(m-1)
        for i in range (m):
            plt.plot([cc+Dia_Bar/2+spacing1*i],[cc+Dia_Bar/2],'o',markersize=Dia_Bar,color="red")
            plt.plot([cc+Dia_Bar/2+spacing1*i],[(D-cc)-Dia_Bar/2],'o',markersize=Dia_Bar,color="red")        
            plt.plot([cc+Dia_Bar/2],[cc+Dia_Bar/2+spacing*i],'o',markersize=Dia_Bar,color="red")
            plt.plot([(B-cc)-Dia_Bar/2],[cc+Dia_Bar/2+spacing*i],'o',markersize=Dia_Bar,color="red")
            plt.plot([0+cc,B-cc],[0+cc,0+cc],color="purple",linewidth=Dia_link)
            plt.plot([B-cc,B-cc],[0+cc,D-cc],linewidth=Dia_link,color="purple")
            plt.plot([0+cc,B-cc],[D-cc,D-cc],linewidth=Dia_link,color="purple")
            plt.plot([0+cc,0+cc],[0+cc,D-cc],linewidth=Dia_link,color="purple")
            plt.text(B*1.5,D/3,Dia_Bar,color="red")
            plt.annotate("     mm Dia_Bar",xy=(B-cc-(Dia_Bar/2),cc+(Dia_Bar/2)),xytext=(B*1.5,D/3),arrowprops=dict(color='Black',width=0.5))
            plt.text(B*1.5,D/2,Dia_link,color="red")
            plt.annotate("     mm Dia_of_link",xy=(B-cc+(Dia_link/2),D/2),xytext=(B*1.5,D/2),arrowprops=dict(color='Black',width=0.5))
        plt.show()
    if spacing>75 and spacing<=48*Dia_link:
        print("two tie open link")
        import matplotlib.pyplot as plt
        plt.figure(figsize=(5,7))
        plt.plot([0,B],[0,0],color="Blue")
        plt.plot([B,B],[0,D],color="Blue")
        plt.plot([0,B],[D,D],color="Blue")
        plt.plot([0,0],[0,D],color="Blue")
        spacing1=(B-cc-cc-Dia_Bar)/(m-1)
        for i in range (m):
            plt.plot([cc+Dia_Bar/2+spacing1*i],[cc+Dia_Bar/2],'o',markersize=Dia_Bar,color="red")
            plt.plot([cc+Dia_Bar/2+spacing1*i],[(D-cc)-Dia_Bar/2],'o',markersize=Dia_Bar,color="red")        
            plt.plot([cc+Dia_Bar/2],[cc+Dia_Bar/2+spacing*i],'o',markersize=Dia_Bar,color="red")
            plt.plot([(B-cc)-Dia_Bar/2],[cc+Dia_Bar/2+spacing*i],'o',markersize=Dia_Bar,color="red")
            plt.plot([0+cc,B-cc],[0+cc,0+cc],color="purple",linewidth=Dia_link)
            plt.plot([B-cc,B-cc],[0+cc,D-cc],linewidth=Dia_link,color="purple")
            plt.plot([0+cc,B-cc],[D-cc,D-cc],linewidth=Dia_link,color="purple")
            plt.plot([0+cc,0+cc],[0+cc,D-cc],linewidth=Dia_link,color="purple")
            if m>3:
                plt.plot([cc-(Dia_Bar/2),B-cc+(Dia_Bar/2)],[(D/2)+(D/6),(D/2)+(D/6)],linewidth=Dia_link,color="orange")
                plt.plot([cc-(Dia_Bar/2),B-cc+(Dia_Bar/2)],[(D/2)-(D/6),(D/2)-(D/6)],linewidth=Dia_link,color="orange")
                plt.text(B*1.5,D/1.5,Dia_link,color="red")
                plt.annotate("     mm Dia_of_two_tie_open_link",xy=((B/2)+(B/4),(D/2)+(D/6)),xytext=(B*1.5,D/1.5),arrowprops=dict(color='Black',width=0.5))
            if m==3:
                plt.plot([cc-(Dia_Bar/2),B-cc+(Dia_Bar/2)],[(D/2)-(Dia_Bar/2),(D/2)-(Dia_Bar/2)],linewidth=Dia_link,color="orange")
                plt.plot([(B/2)+(Dia_Bar/2),(B/2)+(Dia_Bar/2)],[(cc-(Dia_Bar/2)),(D-cc+(Dia_Bar/2))],linewidth=Dia_link,color="orange")
                plt.text(B*1.5,D/1.5,Dia_link,color="red")
                plt.annotate("     mm Dia_of_tie",xy=((B/2)+(Dia_Bar/2),(D/2)-(Dia_Bar/2)),xytext=(B*1.5,D/1.5),arrowprops=dict(color='Black',width=0.5))
            plt.text(B*1.5,D/3,Dia_Bar,color="red")
            plt.annotate("     mm Dia_Bar",xy=(B-cc-(Dia_Bar/2),cc+(Dia_Bar/2)),xytext=(B*1.5,D/3),arrowprops=dict(color='Black',width=0.5))
            plt.text(B*1.5,D/2,Dia_link,color="red")
            plt.annotate("     mm Dia_of_link",xy=(B-cc+(Dia_link/2),D/2),xytext=(B*1.5,D/2),arrowprops=dict(color='Black',width=0.5))
        plt.show()
    if spacing>75 and spacing>48*Dia_link:
        print("two tie closeD link")
        import matplotlib.pyplot as plt
        plt.figure(figsize=(5,7))
        plt.plot([0,B],[0,0],color="Blue")
        plt.plot([B,B],[0,D],color="Blue")
        plt.plot([0,B],[D,D],color="Blue")
        plt.plot([0,0],[0,D],color="Blue")
        spacing1=(B-cc-cc-Dia_Bar)/(m-1)
        for i in range (m):
            plt.plot([cc+Dia_Bar/2+spacing1*i],[cc+Dia_Bar/2],'o',markersize=Dia_Bar,color="red")
            plt.plot([cc+Dia_Bar/2+spacing1*i],[(D-cc)-Dia_Bar/2],'o',markersize=Dia_Bar,color="red")        
            plt.plot([cc+Dia_Bar/2],[cc+Dia_Bar/2+spacing*i],'o',markersize=Dia_Bar,color="red")
            plt.plot([(B-cc)-Dia_Bar/2],[cc+Dia_Bar/2+spacing*i],'o',markersize=Dia_Bar,color="red")
            plt.plot([0+cc,B-cc],[0+cc,0+cc],color="purple",linewidth=Dia_link)
            plt.plot([B-cc,B-cc],[0+cc,D-cc],linewidth=Dia_link,color="purple")
            plt.plot([0+cc,B-cc],[D-cc,D-cc],linewidth=Dia_link,color="purple")
            plt.plot([0+cc,0+cc],[0+cc,D-cc],linewidth=Dia_link,color="purple")
            if m>3:
                plt.plot([cc,B-cc],[(D/2)+(D/6),(D/2)+(D/6)],linewidth=Dia_link,color="orange")
                plt.plot([cc,B-cc],[(D/2)-(D/6),(D/2)-(D/6)],linewidth=Dia_link,color="orange")
                plt.plot([cc,cc],[(D/2)+(D/6),(D/2)-(D/6)],linewidth=Dia_link,color="orange")
                plt.plot([B-cc,B-cc],[(D/2)+(D/6),(D/2)-(D/6)],linewidth=Dia_link,color="orange")
                plt.text(B*1.5,D/1.5,Dia_link,color="red")
                plt.annotate("     mm Dia_of_two_tie_closeD_link",xy=((B/2)+(B/4),(D/2)+(D/6)),xytext=(B*1.5,D/1.5),arrowprops=dict(color='Black',width=0.5))
            if m==3:
                plt.plot([cc-(Dia_Bar/2),B-cc+(Dia_Bar/2)],[(D/2)-(Dia_Bar/2),(D/2)-(Dia_Bar/2)],linewidth=Dia_link,color="orange")
                plt.plot([(B/2)+(Dia_Bar/2),(B/2)+(Dia_Bar/2)],[(cc-(Dia_Bar/2)),(D-cc+(Dia_Bar/2))],linewidth=Dia_link,color="orange")
                plt.text(B*1.5,D/1.5,Dia_link,color="red")
                plt.annotate("     mm Dia_of_tie",xy=((B/2)+(Dia_Bar/2),(D/2)-(Dia_Bar/2)),xytext=(B*1.5,D/1.5),arrowprops=dict(color='Black',width=0.5))
            plt.text(B*1.5,D/3,Dia_Bar,color="red")
            plt.annotate("     mm Dia_Bar",xy=(B-cc-(Dia_Bar/2),cc+(Dia_Bar/2)),xytext=(B*1.5,D/3),arrowprops=dict(color='Black',width=0.5))
            plt.text(B*1.5,D/2,Dia_link,color="red")
            plt.annotate("     mm Dia_of_link",xy=(B-cc+(Dia_link/2),D/2),xytext=(B*1.5,D/2),arrowprops=dict(color='Black',width=0.5))
        plt.show()
#arrengement for r/f on two opposite siDe
if F==2:
    m=int(n//2)
    if n%2==0:
        print(m)
    else:
        m=m+1
    spacing=(D-cc-cc-Dia_Bar)/(m-1)
    spacing1=0
    if spacing<75 or spacing==75:
        print("simple")
        import matplotlib.pyplot as plt
        plt.figure(figsize=(5,7))
        plt.plot([0,B],[0,0],color="Blue")
        plt.plot([B,B],[0,D],color="Blue")
        plt.plot([0,B],[D,D],color="Blue")
        plt.plot([0,0],[0,D],color="Blue")
        for i in range (m):        
            plt.plot([cc+Dia_Bar/2],[cc+Dia_Bar/2+spacing*i],'o',markersize=Dia_Bar,color="red")
            plt.plot([(B-cc)-Dia_Bar/2],[cc+Dia_Bar/2+spacing*i],'o',markersize=Dia_Bar,color="red")
            plt.plot([0+cc,B-cc],[0+cc,0+cc],color="purple",linewidth=Dia_link)
            plt.plot([B-cc,B-cc],[0+cc,D-cc],linewidth=Dia_link,color="purple")
            plt.plot([0+cc,B-cc],[D-cc,D-cc],linewidth=Dia_link,color="purple")
            plt.plot([0+cc,0+cc],[0+cc,D-cc],linewidth=Dia_link,color="purple")
            plt.text(B*1.5,D/3,Dia_Bar,color="red")
            plt.annotate("     mm Dia_Bar",xy=(B-cc-(Dia_Bar/2),cc+(Dia_Bar/2)),xytext=(B*1.5,D/3),arrowprops=dict(color='Black',width=0.5))
            plt.text(B*1.5,D/2,Dia_link,color="red")
            plt.annotate("     mm Dia_of_link",xy=(B-cc+(Dia_link/2),D/2),xytext=(B*1.5,D/2),arrowprops=dict(color='Black',width=0.5))
        plt.show()
    if spacing>75 and spacing<=48*Dia_link:
        print("two tie open link")
        import matplotlib.pyplot as plt
        plt.figure(figsize=(5,7))
        plt.plot([0,B],[0,0],color="Blue")
        plt.plot([B,B],[0,D],color="Blue")
        plt.plot([0,B],[D,D],color="Blue")
        plt.plot([0,0],[0,D],color="Blue")
        for i in range (m):        
            plt.plot([cc+Dia_Bar/2],[cc+Dia_Bar/2+spacing*i],'o',markersize=Dia_Bar,color="red")
            plt.plot([(B-cc)-Dia_Bar/2],[cc+Dia_Bar/2+spacing*i],'o',markersize=Dia_Bar,color="red")
            plt.plot([0+cc,B-cc],[0+cc,0+cc],color="purple",linewidth=Dia_link)
            plt.plot([B-cc,B-cc],[0+cc,D-cc],linewidth=Dia_link,color="purple")
            plt.plot([0+cc,B-cc],[D-cc,D-cc],linewidth=Dia_link,color="purple")
            plt.plot([0+cc,0+cc],[0+cc,D-cc],linewidth=Dia_link,color="purple")
            if m>3:
                plt.plot([cc-(Dia_Bar/2),B-cc+(Dia_Bar/2)],[(D/2)+(D/6),(D/2)+(D/6)],linewidth=Dia_link,color="orange")
                plt.plot([cc-(Dia_Bar/2),B-cc+(Dia_Bar/2)],[(D/2)-(D/6),(D/2)-(D/6)],linewidth=Dia_link,color="orange")
                plt.text(B*1.5,D/1.5,Dia_link,color="red")
                plt.annotate("     mm Dia_of_two_tie_open_link",xy=((B/2)+(B/4),(D/2)+(D/6)),xytext=(B*1.5,D/1.5),arrowprops=dict(color='Black',width=0.5))
            if m==3:
                plt.plot([cc-(Dia_Bar/2),B-cc+(Dia_Bar/2)],[(D/2)-(Dia_Bar/2),(D/2)-(Dia_Bar/2)],linewidth=Dia_link,color="orange")
                plt.text(B*1.5,D/1.5,Dia_link,color="red")
                plt.annotate("     mm Dia_of_tie",xy=((B/2)+(Dia_Bar/2),(D/2)-(Dia_Bar/2)),xytext=(B*1.5,D/1.5),arrowprops=dict(color='Black',width=0.5))
            plt.text(B*1.5,D/3,Dia_Bar,color="red")
            plt.annotate("     mm Dia_Bar",xy=(B-cc-(Dia_Bar/2),cc+(Dia_Bar/2)),xytext=(B*1.5,D/3),arrowprops=dict(color='Black',width=0.5))
            plt.text(B*1.5,D/2,Dia_link,color="red")
            plt.annotate("     mm Dia_of_link",xy=(B-cc+(Dia_link/2),D/2),xytext=(B*1.5,D/2),arrowprops=dict(color='Black',width=0.5))
        plt.show()
    if spacing>75 and spacing>48*Dia_link:
        print("two tie closeD link")
        import matplotlib.pyplot as plt
        plt.figure(figsize=(5,7))
        plt.plot([0,B],[0,0],color="Blue")
        plt.plot([B,B],[0,D],color="Blue")
        plt.plot([0,B],[D,D],color="Blue")
        plt.plot([0,0],[0,D],color="Blue")
        for i in range (m):        
            plt.plot([cc+Dia_Bar/2],[cc+Dia_Bar/2+spacing*i],'o',markersize=Dia_Bar,color="red")
            plt.plot([(B-cc)-Dia_Bar/2],[cc+Dia_Bar/2+spacing*i],'o',markersize=Dia_Bar,color="red")
            plt.plot([0+cc,B-cc],[0+cc,0+cc],color="purple",linewidth=Dia_link)
            plt.plot([B-cc,B-cc],[0+cc,D-cc],linewidth=Dia_link,color="purple")
            plt.plot([0+cc,B-cc],[D-cc,D-cc],linewidth=Dia_link,color="purple")
            plt.plot([0+cc,0+cc],[0+cc,D-cc],linewidth=Dia_link,color="purple")
            if m>3:
                plt.plot([cc,B-cc],[(D/2)+(D/6),(D/2)+(D/6)],linewidth=Dia_link,color="orange")
                plt.plot([cc,B-cc],[(D/2)-(D/6),(D/2)-(D/6)],linewidth=Dia_link,color="orange")
                plt.plot([cc,cc],[(D/2)+(D/6),(D/2)-(D/6)],linewidth=Dia_link,color="orange")
                plt.plot([B-cc,B-cc],[(D/2)+(D/6),(D/2)-(D/6)],linewidth=Dia_link,color="orange")
                plt.text(B*1.5,D/1.5,Dia_link,color="red")
                plt.annotate("     mm Dia_of_two_tie_closeD_link",xy=((B/2)+(B/4),(D/2)+(D/6)),xytext=(B*1.5,D/1.5),arrowprops=dict(color='Black',width=0.5))
            if m==3:
                plt.plot([cc-(Dia_Bar/2),B-cc+(Dia_Bar/2)],[(D/2)-(Dia_Bar/2),(D/2)-(Dia_Bar/2)],linewidth=Dia_link,color="orange")
                plt.text(B*1.5,D/1.5,Dia_link,color="red")
                plt.annotate("     mm Dia_of_tie",xy=((B/2)+(Dia_Bar/2),(D/2)-(Dia_Bar/2)),xytext=(B*1.5,D/1.5),arrowprops=dict(color='Black',width=0.5))
            plt.text(B*1.5,D/3,Dia_Bar,color="red")
            plt.annotate("     mm Dia_Bar",xy=(B-cc-(Dia_Bar/2),cc+(Dia_Bar/2)),xytext=(B*1.5,D/3),arrowprops=dict(color='Black',width=0.5))
            plt.text(B*1.5,D/2,Dia_link,color="red")
            plt.annotate("     mm Dia_of_link",xy=(B-cc+(Dia_link/2),D/2),xytext=(B*1.5,D/2),arrowprops=dict(color='Black',width=0.5))
        plt.show()
print("pitch of the link=",pitch)
print("spacing of longituidnal bars along longer side=",spacing)
print("spacing of longituidnal bars along shorter sides=",spacing1)


    
    

 

    
 

    

