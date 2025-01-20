import React, { useRef } from "react";

type ImageData = {
  id: number;
  src: string;
  description: string;
};

type ImageGalleryProps = {
  images: ImageData[];
};

const ImageGallery = ({ images }: ImageGalleryProps) => {
  const imageRefs = useRef([]);

  // show an image one by one streached to the screen, and scroll to the next image when the user scrolls
  // description is displayed on the image

  // as the user scrolls, description changes
  // when the user scrolls to the next image, the description of the next image is displayed

  return (
    <>
      <div className="h-screen w-fit snap-y snap-mandatory overflow-y-scroll">
        {images.map((image, index) => (
          <div
            key={image.id}
            className="relative snap-center snap-always"
            ref={(el: HTMLDivElement | null) => (imageRefs.current[index] = el)}
            data-index={index}
          >
            <img
              src={image.src}
              alt={`Image ${image.id}`}
              className="h-screen w-full object-cover"
            />

            <div className="pointer-events-none absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2 transform whitespace-pre-wrap rounded bg-white bg-opacity-50 p-2 text-lg text-black transition-opacity duration-300">
              {image.description}
            </div>
          </div>
        ))}
      </div>
    </>
  );
};

export default ImageGallery;
