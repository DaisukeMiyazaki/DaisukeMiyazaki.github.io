import React from "react";
import { createRoot } from "react-dom/client";
import ImageGallery from "../../../components/photoScroll/photoScroll";
import data from "./indentations";

const container = document.getElementById("photo-scroll");
const root = createRoot(container);
root.render(<ImageGallery images={data()} />);
