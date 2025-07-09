import React, { useRef, useState, useEffect } from "react";

type ImageData = {
  id: number;
  src: string;
  description: string;
  link?: string;
};

type ImageGalleryProps = {
  images: ImageData[];
};

const ImageGallery = ({ images }: ImageGalleryProps) => {
  const baseURL = useRef(window.location.origin);
  const imageRefs = useRef<(HTMLDivElement | null)[]>([]);
  const [currentIndex, setCurrentIndex] = useState(0);

  useEffect(() => {
    const observer = new IntersectionObserver(
      (entries) => {
        for (const entry of entries) {
          if (entry.isIntersecting) {
            const index = parseInt(
              entry.target.getAttribute("data-index") || "0",
              10,
            );
            setCurrentIndex(index);
            break;
          }
        }
      },
      { threshold: 0.5 },
    );

    const currentImageRefs = imageRefs.current;
    currentImageRefs.forEach((ref) => {
      if (ref) observer.observe(ref);
    });

    return () => {
      currentImageRefs.forEach((ref) => {
        if (ref) observer.unobserve(ref);
      });
    };
  }, [images]);

  return (
    <>
      <div className="fixed right-4 top-1/2 z-20 flex -translate-y-1/2 transform flex-col items-center space-y-3 opacity-80">
        {images.map((_, index) => (
          <button
            key={index}
            onClick={() => {
              imageRefs.current[index]?.scrollIntoView({ behavior: "smooth" });
            }}
            className={`rounded-full transition-all duration-300 ${
              currentIndex === index ? "h-1 w-5 bg-white" : "h-1 w-1 bg-white"
            }`}
            aria-label={`Go to image ${index + 1}`}
          />
        ))}
      </div>
      <div className="mx-auto w-fit">
        {images.map((image, index) => (
          <div
            key={image.id}
            className="relative"
            ref={(el: HTMLDivElement | null) => {
              imageRefs.current[index] = el;
            }}
            data-index={index}
          >
            <img
              src={image.src}
              alt={`Image ${image.id}`}
              className="h-screen w-full object-cover"
            />

            <div
              className="pointer-events-none absolute bottom-4 right-4 whitespace-pre-wrap p-3 text-lg text-white"
              style={{ textShadow: "0 1px 3px rgba(0, 0, 0, 0.7)" }}
            >
              {image.link ? (
                <a
                  href={`${baseURL.current}${image.link}`}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="pointer-events-auto text-yellow-300 hover:text-yellow-400"
                >
                  {image.description}
                </a>
              ) : (
                image.description
              )}
            </div>
          </div>
        ))}
      </div>
    </>
  );
};

export default ImageGallery;
