close all; clear; clc;

%wczytać cameramen.tif
%odjąć 50, dodać 100, odjąć 50
a = imread('cameraman.tif');

a = a - 50;
a = a+100;
a=a-50;
a = double(a)/255;
%korekcja gamma dla [0.1 0.25 0.5 1 2 5]

gam=[0.1 0.25 0.5 1 2 5];

for k=1:6
    b=a.^gam(k);
    subplot(2,3,k), imshow(b);
    title(['\gamma = ', num2str(gam(k))]);
end

% subplot(231), imshow(a.^0.1);
% subplot(232), imshow(a.^0.25);
% subplot(233), imshow(a.^0.5);
% subplot(234), imshow(a);
% subplot(235), imshow(a.^2);
% subplot(236), imshow(a.^5);


%%
close all; clear; clc;
% a=imread('pout.tif');
a=imread('saturn.png');
a=rgb2gray(a);
subplot(221), imshow(a);
subplot(222), imhist(a, 256);
% b=imadjust(a);
% b=histeq(a, 256);
b=adapthisteq(a, 'clipLimit', 0.07, 'Distribution', 'exponential');

subplot(223), imshow(b);
subplot(224), imhist(b, 256);

%%
close all; clear; clc;
a=imread('coins.png');
imshow(a)
%imtool(a) w konsoli
bin=(a>90);
bin=medfilt2(bin, [3 3]);
subplot(121), imshow(a);
subplot(122), imshow(bin);

%%
close all; clear; clc;
%1. znaleźć fiolet
%2. kolumny min, max - 0h, 350h
%   wiersze ymin 35'000Pa
%           ymax 0Pa
%3. Pa=f(wiersz) t=f(kolumna)
%4. interp1(t, PP, 0:5:350)

a=imread('wykres.png');

%1
bin=(a(:, :, 1) == 126) & (a(:,:,2) == 47) & (a(:,:,3) == 142);

%2
xmin=343;
xmax=2375;
ymin=113;
ymax=1312;

%3
% t=(350-0)*(k-xmin)/(xmax-xmin);
% PP=3500*(ymax-w)/(ymax-ymin);

n=1;
for kx=xmin:xmax
    N=sum(bin(ymin:ymax,kx));
    if N>0
        y(n)=0;
        for ky=ymin:ymax
            if bin(ky, kx) == true
                y(n)=y(n)+ky;
            end
        end
        y(n)=y(n)/N;
        x(n)=kx;
        n=n+1;
    end
end

x=350*(x-xmin)/(xmax-xmin);
y=35000*(ymax-y)/(ymax-ymin);



subplot(121), imshow(a);
subplot(122), imshow(bin);
plot(x,y)
PP=interp1(x,y,0:5:350, 'linear');
plot(x,y,'b',0:5:350,PP,'or')

%%
close all; clear; clc;
a=imread('cameraman.tif');
% b=circshift(a,[10, 50]);
% b=imrotate(a, 30, 'bicubic', 'crop');
% b=flipud(a); %fliplr
b=padarray(a, [256, 256], 'symmetric','post');
imshow(b)

%%
close all; clc;
a=imread('cameraman.tif');
% mac=affine2d([1 0 0; 0 2 0; 0 0 1]);
% mac=projective2d([1 4 0; 3 2 0; 0 1 1]);
kat=pi/15;
b=imrotate(a,12,'loose');
% cpselect(a,b);
mac2=fitgeotrans(movingPoints, fixedPoints, 'affine');
mac2.T
[sin(kat) cos(kat)]

b=imwarp(a, mac2);
imshow(b); axis on;