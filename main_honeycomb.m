% ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
% Matlab script to create parallelograms superimposed on honeycomb lattice
% structures. The main code is
%       construct_par(M1,M2,N1,N2),
% where, 
% with v1p and v2p being the spanning vectors of a parallelogram (par),
%   M1, M2 ~ integers ~ number of translates in v1p direction: -M1:1:M2
%   N1, N2 ~ integers ~ number of translates in v2p direction: -N1:1:N2.
% Note M1,M2,N1,N2 > 0.
% 
% Construction of lattice vectors for par will be up to user input in
% variables a1, b1, a2.
% ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
% "From paper" reference is James Lee-Thorp's PhD thesis and his
% works with Charles Fefferman and Michael I Weinstein on the
% strong-binding honeycomb.
% ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


construct_par(2,2,3,2)


function construct_par(M1,M2,N1,N2)
% ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
% Function:  
%   construct_par(M1,M2,N1,N2)
% Purpose:
%   To plot parallelograms superimposed on a graph of honeycomb vertices.
% Parameters:
%   M1, M2 ~ integers; number of translates horizontally  M1 < M2
%   N1, N2 ~ integers; number of translates vertically  N1 < N2
% Output: 
%   None. Function plots on top of an open figure.
% ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

% ~~~~~~~~~~ Code written by Michael I Weinstein ~~~~~~~~~~ %
%%% Honeycomb lattice points
%%% Given  lattice vectors v1 and kv2 general \Lambda_A, \Lambda_B and H
%
Nmax =12;Np1=Nmax+1; ax_p = 5;
figure; hold on
axis([-Np1 Np1 -Np1 Np1])
v1 = [sqrt(3)/2 1/2]'; v2 = [0 1]';v2 = [sqrt(3)/2 -1/2]';
%%% A and B points
theta=1; % deformation parameter
A  = [0 0]'; B=[1/sqrt(3) ; 0 ]; %[1/(2*sqrt(3)) 1/2]';
%%% Generate & plot triangular lattice of K-points
for j1=-Nmax:Nmax
    for l1=-Nmax:Nmax
        Anow = A+j1*v1+l1*v2;
        plot(Anow(1),Anow(2),'bo','MarkerFaceColor','b');
    end 
end
%%% Generate & plot triangular lattice of Kprime-points
for j1=-Nmax:Nmax
    for l1=-Nmax:Nmax
        Bnow = B+j1*v1+l1*v2;
        plot(Bnow(1),Bnow(2),'bo','MarkerFaceColor','r');
    end 
end
 axis([-ax_p ax_p -ax_p ax_p]) 
% ~~~~~~~~~~ Code written by Michael I Weinstein\end ~~~~~~~~~~ %

    % Construct parallelogram (par) lattice vectors.
%     a1 = input('a1 >> ');
%     b1 = input('b1 >> ');
     a1=1;b1=2;
     v1=[sqrt(3)/2;1/2];v2=[sqrt(3)/2;-1/2]; % lattice vectors from paper
     %v1 = [sqrt(3)/2 1/2]'; v2 = [0 1]';
    % k1=2*pi*[sqrt(3)/3;1];k2=2*pi*[sqrt(3)/3;-1];
    v1p = 0*v1; v2p = 0*v2;
    if iscoprime(a1,b1) == 1
        fprintf('\nInputted a1, b1 are coprime!\n');
        a2 = 0;%input('\nNow please input a2 >> '); % 1
        b2 = (1+a2*b1)/a1;
        while floor(b2)~= b2
            fprintf('\nInputted a2 is not acceptable for b2 to be an integer. \n\nPlease try again.\n');
            a2 = input(' a2 >> '); % 1
            b2 = (1+a2*b1)/a1;
        end
        %   a2 = (-1+a1*b2)b1;
        v1p = a1*v1 + b1*v2;
        v2p = a2*v1 + b2*v2;
    end
 
    % xc=0.5*[1/sqrt(3);-1]; % center from paper
    
    xc = A;
    % Get a unit triangle of A points from the origin.
    unit_tri = [xc, xc+v1, xc+v1-v2];
    scatter(unit_tri(1,:),unit_tri(2,:) ) % shouldn't see anything!

    % Obtain barycenter of the unit triangle. This will be the center for par.
    bctr = [sum(unit_tri(1,:))/3; sum(unit_tri(2,:))/3];
    scatter(bctr(1),bctr(2) ) % plots center
     
     
    % Construct unit parallelogram.
    unit_par =[ bctr,  bctr-v1p, bctr+v2p-v1p, bctr+v2p, bctr];
    
    % Create a meshgrid of translates (-M1:M2 v1p direction; -N1:N2 v2p).
    [J,K] = meshgrid(-M1:M2,-N1:N2); 
    
    % Create a vector of all combinations of -M1:M2 and -N1:N2
    temp=cat(2,J',K'); jk=reshape(temp,[],2);
  
    hold on;
    for j= 1:1%length(jk)
        par = unit_par ;%+ jk(j,1)*repmat(v1p,1,5) + jk(j,2)*repmat(v2p,1,5);
        % Draw a line between each vertex of the parallelogram.
        plot(par(1,1:2), par(2,1:2))
        plot(par(1,2:3), par(2,2:3))
        plot(par(1,3:4), par(2,3:4))
        plot(par(1,4:5), par(2,4:5))
        hold on;
    end



end


function flag = iscoprime(a,b)
% ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
% Function:  
%   iscoprime(a,b)
% Purpose:
%   To check if two integers a and b are relatively prime
% Parameters:
%   a ~ integer
%   b ~ integer
% Output: 
%   flag == 0 if NOT coprime; flag == 1 if coprime.
% ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    m = max(a,b);
    n = 1:m-1;
    ind = gcd(n,m)==1; % pick out which guys are coprime
    coprimes = n(ind);
    % return 0 if not list of coprimes; 1 otherwise.
    flag = length(coprimes(coprimes == a)); 
    
end