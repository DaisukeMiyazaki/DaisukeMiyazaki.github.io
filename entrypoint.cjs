const esbuild = require("esbuild");
const babel = require("@babel/core");
const fs = require("fs");
const glob = require("glob");

const entryPoints = glob.sync(["./src/**/*.build.tsx", "./src/**/*.build.ts"], {
  ignore: ["./ts/**/*.d.ts"],
});

const isLocal = process.env.NODE_ENV === "development";

const buildOptions = {
  entryPoints: entryPoints,
  bundle: true,
  outbase: "./src",
  outdir: "./assets/js",
  tsconfig: "tsconfig.json",
  platform: "browser",
  loader: {
    ".js": "jsx",
    ".jsx": "jsx",
    ".css": "css",
  },
  plugins: [
    {
      name: "on-end",
      setup(build) {
        build.onEnd((error) => {
          if (error.errors.length > 0) {
            console.error("build error:", error);
            if (!isLocal) process.exit(1);
          } else {
            console.log("build succeeded");
          }
        });
      },
    },
    {
      name: "babel",
      setup(build) {
        build.onLoad({ filter: /\.(js|jsx)$/ }, async (args) => {
          const source = await fs.promises.readFile(args.path, "utf8");
          const result = await babel.transformAsync(source, {
            filename: args.path,
            presets: ["@babel/preset-env", "@babel/preset-react"],
          });
          return { contents: result.code, loader: "jsx" };
        });
      },
    },
  ],
};

const build = async () => {
  try {
    if (isLocal) {
      const ctx = await esbuild.context(buildOptions);
      await ctx.watch();
      console.log("watching js files...");
    } else {
      await esbuild.build(buildOptions);
    }
  } catch (error) {
    console.error("error on build:", error);
    process.exit(1);
  }
};

build();
