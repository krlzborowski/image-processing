close all; clear; clc;


% filtracja:
%  -linowa:
%   *LP
%   *HP
% -nielinowa
% 


a=imread('cameraman.tif');
a=double(a)/255;
N=5;
% LP=ones(N)/(N*N);
% LP=fspecial('gaussian', [N N], N/8);
H=[ 1 2 1 ; 0 0 0 ; -1 -2 -1];
V=[1 0 -1 ; 2 0 -2 ; 1 0 -1];
b1=imfilter(a, H, 'replicate');
b2=imfilter(a, V, 'replicate');
b=b1.^2+b2.^2;
b=sqrt(b);
% subplot(131), imshow(b1);
% subplot(132), imshow(b2);
subplot(121), imshow(a);
subplot(122), imshow(b);

% maska horyzontsalna
%  1 1 1
%  0 0 0
% -1 -1 -1

% horyzontaln analogicznie

% uint8 wartośći ujemne zamienia na 0

% maska Sobela
%  1  2  1
%  0  0  0
% -1 -2 -1

%%
clear; close all; clc;

% czarne tło 120x120, biały prostokąt 80x100 w centrum
% stworzyć procedurę filtracyjną, by zostały 4 narożniki prostokąta

% H=[ 1 1 1 ; 0 0 0 ; 1 1 1];
% V= [1 0 -1 ; 1 0 1 ; 1 0 -1];

a= zeros(120, 200);
a(21:100, 51:150)=1;

HP=[1 0 -1];
kraw=abs(imfilter(a, HP).*imfilter(a, HP'));
kraw=uint8(a+a.*kraw);
leg=[0 0 0; 1 1 1; 1 0 0];
imshow(kraw, leg)
% 
% b1=imfilter(a, H, 'replicate');
% b2=imfilter(a, V, 'replicate');


% 
% subplot(121), imshow(a);
% subplot(122), imshow(b);


% laplasjany
% -1 -1 -1
% -1 9/8 -1
% -1 -1 -1

% 0 -1 0
% -1 4/5 -1 suma 0 lub 1
% 0 -1 0

%%
close all; clear; clc;

% a=imread('cameraman.tif');
a=imread('peppers.png');

% L1=[-1 -1 -1; -1 9 -1; -1 -1 -1];
% L2=[0 -1 0; -1 4 -1; 0 -1 0];

HP=-ones(3);
HP(2,2)=8;
b1=imfilter(a, HP, 'replicate');
HP(2,2)=9;
b2=imfilter(a, HP, 'replicate');
subplot(121), imshow(b1);
subplot(122), imshow(b2);

%% 
close all; clear; clc;

% filtracja nieliniowa
% medfilt2, wiener2

a=imread('cameraman.tif');
% aszum=imnoise(a,'gaussian');
% aszum=imnoise(a, 'salt & pepper');
% aszum=imnoise(a, 'poisson');
aszum=imnoise(a, 'speckle');
N=5;

b1=medfilt2(aszum, [N N], 'symmetric');
b2=wiener2(aszum, [N N]);

LP=ones(N)/(N*N);
b3=imfilter(aszum, LP, 'replicate');
LP=fspecial('gaussian', [N N], N/8);
b4=imfilter(aszum, LP, 'replicate');

subplot(221), imshow(b1);
subplot(222), imshow(b2);
subplot(223), imshow(b3);
subplot(224), imshow(b4);

%%

% entropia
% 'canny' - bardzo moncy (wygładza, binaryzuje, odejmuje)
% sobel, prewit
close all; clear; clc;

a=imread('cameraman.tif');
% b=entropyfilt(a, ones(9));
% imagesc(b); axis image; colorbar('vertical');
b=edge(a,'sobel');
imshow(b)

% VMF - vector median flow
% -dla obrazów kolorowych
% -im mniejsza maska, tym mniejsze działanie filtru


% dekonwolucja

mask=fspecial('motion', 11, -30);
b=imfilter(a, mask, 'replicate');
c=deconvlucy(b,mask);

subplot(121), imshow(b);
subplot(122), imshow(c);



