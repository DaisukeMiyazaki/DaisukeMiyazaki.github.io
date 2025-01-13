import React from 'react';
import { createRoot } from 'react-dom/client';
import ImageGallery from './photoScroll';

const container = document.getElementById('photo-scroll');
const root = createRoot(container); 
root.render(<ImageGallery/>);
