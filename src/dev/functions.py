f01_04 = F(g_, 4*(pi_**2)* h_ / (T_**2))
f01_07 = F(T_ , sub_0(T_) + i_* sub_0(T_)**2 / ( ta_ - i_*sub_0(T_) ))
f01_10 = F(g_, 4*pi_*pi_*h_*( 1 + 2*r_*r_/(5*h_*h_) + th_*th_/8 )/(T_*T_))
f01_11 = F(h_, _dash(h_)-d_/2)

f05_01 = F( ss('V_{R}(t)') , R_* ss('I(t)') , label='f05_01')
f05_02 = F( ss('q(t)') , C_* ss('V_{C}(t)') , label='f05_02')
f05_03 = F( ss('I(t)') , diff_('q(t)', 't') , label='f05_03')
f05_04 = F( ss('V_L(t)') , -L_*diff_('I(t)', 't') , label='f05_04')
f05_05 = F( V_-L_* diff_('I(t)', 't'), R_* ss('I(t)')+ diff_('q(t)', 't') , label='f05_05')
f05_06 = F(frac_('d^2I(t)','dt^2')+2*ga_*diff_('I(t)','t')+sub_0(om_)**2*ss('I(t)'), 0, label='f05_06')
f05_07 = F( ss('I(t)'), e_**(-ga_*t_)*(a_*sin(sub_1(om_)*t_)+ b_*cos(sub_1(om_)*t_)), label='f05_07')
f05_08 = F( ss('I(t)'), e_**(-ga_*t_)*(a_*e_**(sub_1(om_)*t_)+b_*e_**(-sub_1(om_)*t_)), label='f05_08')
f05_09 = F( ss('I(t)'), e_**(-ga_*t_)*(a_*t_+ b_ ), label='f05_09')

# f09
f09_N= F( sin(sub_m(th_)), m_*la_*N_ )
f09_01 = F( sub(E_, n_), -h_*c_*R_/(n_**2), label='f09_01' )
f09_02 = F( h_*nu_ , sub('E',sub_1(n_))-sub('E',sub_2(n_)), label='f09_02' )
f09_03 = F( 1/la_, (1/(h_*c_))*(sub('E','n')-sub_2(E_)) , label='f09_03' )
f09_04 = F( d_*sin(sub(th_,m_)),m_* la_ , label='f09_04' )
f09_05 = F( sub_m(th_), ( sub(th_, L_)- sub(th_, R_))/2 , label='f09_05' )
f09_06 = F( sub(N_, i_), sin( sub(th_,m_))/(m_* sub(la_, i_)) , label='f09_06' )
f09_07 = F( la_, sin( sub(th_,m_))/(m_*N_ ) , label='f09_07' )
f09_08 = F( Delta_(sub_i(N_))/sub_i(N_),sqrt((Delta_(th_)*cos(sub_m(th_))/sin(sub_m(th_)))**2+(Delta_(sub_i(la_))/sub_i(la_))**2), label='f09_08')
f09_09 = F( Delta_(sub_i(la_))/sub_i(la_),
 sqrt((Delta_(th_)*cos(sub_m(th_))/sin(sub_m(th_)))**2+(Delta_(sub_i(N_))/sub_i(N_))**2), label='f09_09')

# f11
f11_01 = F(m_*diff_('v', 't'), -mu_* m_* g_* cos(th_)-la_*mu_+m_*g_*sin(th_) , label='f11_01')
f11_03 = F(bar_('a') , mu_*g_*cos(th_)+(la_/m_)*v_+(ka_/m_)*v_**2-g_*sin(th_), label='f11_03')
f11_04 = F(bar_('a')/g_, mu_*cos(th_)+(la_/m_*g_)*v_+(ka_/m_*g_)*v_**2-g_*sin(th_) , label='f11_04')
f11_05 = F(bar_('a') , (la_/m_)*v_+(ka_/m_)*v_**2, label='f11_05')
f11_06 = F(bar_('a')/bar_('v'), (la_/m_)+(ka_/m_)*v_ , label='f11_06')
f11_07 = F(ep_,(_dash(v_)+_dash(d_)*(la_+ka_*_dash(v_))/m_)/(v_-d_*(la_+ka_*v_)/m_), label='f11_07')
f11_08 = F(d_, et_*S_/la_, label='f11_08')
f11_09 = F(diff_(v_, t_), -mu_* g_ , label='f11_09')
f11_11 = F(s_, ( sub_1(v_)**2- sub_2(v_)**2)/(2*mu_*g_), label='f11_11')
f11_14 = F(s_, m_*(sub_1(v_)-sub_2(v_))/la_, label='f11_14')
f11_15 = F(diff_(v_, t_), - _dash(ka_)*v_**2 , label='f11_15')
f11_16 = F(x_, (1/ _dash(ka_))*log(1+ _dash(ka_)* sub_1(v_)*t_), label='f11_16')
f11_17 = F(s_, (m_/ka_)*log( sub_1(v_)/ sub_2(v_)) , label='f11_17')
f11_18 = F(diff_(v_, t_), -( _dash(la_)*v_+ _dash(ka_)*v_**2), label='f11_18')
f11_19 = F(diff_(x_, v_), -1/( _dash(la_)+ _dash(ka_)*v_), label='f11_19')
f11_20 = F(x_, (m_/ka_)*log((_dash(la_)+_dash(ka_)*sub_1(v_))/(_dash(la_)+_dash(ka_)*v_)), label='f11_20')
f11_21 = F(s_, (m_/ka_)*log((_dash(la_)+_dash(ka_)*sub_1(v_))/(_dash(la_)+_dash(ka_)*sub_2(v_))), label='f11_21' )
f11_22 = F(para_(v_,t_),(la_*sub_1(v_))/((la_+ka_*sub_1(v_))*e_**(la_*t_/m_)-ka_*sub_1(v_)), label='f11_22')
f11_23 = F(para_(x_,t_),(m_/ka_)*log(1+(ka_*sub_1(v_)/la_)*(1-e_**(-la_*t_/m_))) , label='f11_23')
