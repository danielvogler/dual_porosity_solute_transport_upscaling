% daniel vogler
% AWR 2016 - anomalous dispersion
% plots the results for experiment 3

clear; close all; clc

wline = 5;
font_size = 60;
marker_size = 30;
plot_size = [3000, 2000];

%load exp3alpha0029.mat;
load exp3.mat

% times 
Dw = 3.64e-10;  % m^2/s - diffusivity in the w-phase
a = 0.0254;     % radius of spherical inclusions (m)
coeff = Dw / (a^2);

time_fl = coeff * time_fl;
time_br = coeff * time_br;
time_dns_full = coeff * time_dns_full;
time_dns_sim = coeff * time_dns_sim;
time_mva_qs = coeff * time_mva_qs;
time_mva_unc = coeff * time_mva_unc; 

%%%
%%% FIGURE 1 - REGULAR SCALE
%%%
figure(1)  % regular scale
fl = plot(time_fl, c_fl, 'o', 'color', 'r', 'markersize', marker_size', 'linewidth', wline);
hold on
br = plot(time_br, c_br, 'o', 'color', 'b', 'markersize', marker_size', 'linewidth', wline);
dnsf = plot(time_dns_full, c_dns_full, '-k', 'linewidth', wline);
dnss = plot(time_dns_sim, c_dns_sim, '--g', 'linewidth', wline);
qs = plot(time_mva_qs, c_mva_qs, '-', 'linewidth', wline);
uncoupled = plot(time_mva_unc, c_mva_unc, '-.', 'linewidth', wline);
lg = legend([fl,br,dnsf,dnss,qs,uncoupled], ' fluorescein', ' bromide', ' fully resolved DNS', ' simplified DNS', ' quasi-steady upscaled', ' uncoupled transient upscaled');
set(lg, 'location', 'northeast', 'box', 'off', 'fontsize', font_size)

% xl = xlabel('time (s)');
xl = xlabel('$t^*$');
yl = ylabel('$C/C_0$');
set(yl, 'interpreter', 'latex', 'fontsize', font_size);
set(xl, 'interpreter', 'latex', 'fontsize', font_size);
set(gca, 'fontsize', font_size)  % overrides everything el
set(gcf,'color','w'); 
set(gcf,'Position',[1 1 plot_size(1) plot_size(2)]);

% axis([1e4 5e5 1e-5 1])
axis([0 0.1 1e-5 1.2])


%%%
%%% FIGURE 2 - LOGLOG SCALE
%%%
figure(2)  
fl = loglog(time_fl, c_fl, 'o', 'color', 'r', 'markersize', marker_size, 'linewidth', wline');
hold on
br = loglog(time_br, c_br, 'o', 'color', 'b', 'markersize', marker_size, 'linewidth', wline');
dnsf = loglog(time_dns_full, c_dns_full, '-k', 'linewidth', wline);
dnss = loglog(time_dns_sim, c_dns_sim, '--g', 'linewidth', wline);
qs = loglog(time_mva_qs, c_mva_qs, '-', 'linewidth', wline);
uncoupled = loglog(time_mva_unc, c_mva_unc, '-.', 'linewidth', wline);
lg = legend([fl,br,dnsf,dnss,qs,uncoupled], ' fluorescein', ' bromide', ' fully resolved DNS', ' simplified DNS', ' quasi-steady upscaled', ' uncoupled transient upscaled');
set(lg, 'location', 'northeast', 'box', 'off')

%xl = xlabel('time (s)');
xl = xlabel('$t^*$');
yl = ylabel('$C/C_{0}$');
set(yl, 'interpreter', 'latex', 'fontsize', font_size);
set(xl, 'interpreter', 'latex', 'fontsize', font_size);
set(gca, 'fontsize', font_size)
set(gcf,'color','w'); 
set(gcf,'Position',[1 1 plot_size(1) plot_size(2)]);

%axis([1e4 1e6 1e-5 1])
axis([1e-2 1 1e-4 1])
%axis square


% arrows
%drawArrow = @(x,y) quiver( x(1),y(1),x(2)-x(1),y(2)-y(1),0,'linewidth',2 )    


points = [50000, 200000, 400000];
times = points * coeff;

ys = linspace(1e-5, 1, 100);

for i=1:length(times)
    figure(2)
    loglog(times(i), 1e-4, 'xk',  'linewidth', marker_size, 'markersize', marker_size)
end

% values = zeros(1, length(times));
% for i=1:length(values)
%     [junk, indi(i)] = min(abs(time_fl - times(i)));
%     values(i) = c_fl(indi(i));
% %     xxs = [times(i), times(i)];
% %     yys = [values(i) - 0.001, values(i)];
% %     drawArrow(xxs, yys)
%     %annotation('textarrow',[ times(i) - 0.001,times(i)],[values(i)-0.001, values(i)],'String','test ')
% 
% end




