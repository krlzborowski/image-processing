close all; clear; clc;
a=imread('cameraman.tif');

imshow(a)
b=double(a)/255;
b2=uint8(255*b);
imshow(b2)

%tryb logiczny

b2=a>80;
imshow(b2)
%%
clear; close all; clc;

a=imread('peppers.png');

subplot(224), imshow(a)
for k=1:3
    subplot(2, 2, k), imshow(a(:,:,k))
end
% 
% subplot(221), imshow(a(:,:,1))
% subplot(222), imshow(a(:,:,2))
% subplot(223), imshow(a(:,:,3))
% subplot(224), imshow(a(:,:,:))

%%
clear; close all; clc;
a=imread('peppers.png');
imshow(a)

[map,leg]=rgb2ind(a,512);
b=ind2rgb(map,leg)
subplot(121), imshow(a);
subplot(122), imshow(b);
%%
clear; close all; clc;

map=zeros(200, 300, 'uint8');
map(21:180, 26:275)=1;
map(41:160,51:250)=2;
map(61:140,76:225)=3;
leg=[1 1 1; 0 0 0; 0 1 0; 1 0 0];
imshow(map, leg)
%%
clear; close all; clc;

% b=imfinfo('camerman.tif');
a=imread('peppers.png');
% imtool(a)
% b=regionprops(a, 'all');

[Nz, Nx, K]=size(a);
subplot(121), imshow(a);
subplot(122),
b = improfile(a, [1 Nx Nx 1], [1 Nz 1 Nz]);
N=size(b,1);
plot((1:N)',b(:,1,1), 'r', (1:N), b(:,1,2), 'g');
%%
clear; close all; clc;

%interpolacja
% -metoda najbliższego sąsiada
% -metoda bilniowa
% -metoda bikubiczna


% a=checkerboard(8,4,4);
a=imread('cameraman.tif');
subplot(221), imshow(a)
skala=0.6;
b1=imresize(a,skala,'nearest');
b2=imresize(a, skala,'bilinear');
b3=imresize(a, skala, 'bicubic');

subplot(222), imshow(b1);
subplot(223), imshow(b2);
subplot(224), imshow(b3);

